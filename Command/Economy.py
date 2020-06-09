import discord

from discord.ext import commands

import random
import typing

import Functions.credito

from Functions.banco import busca_user_id,edit_user,fncooldown,fncont,fn_delete_cd
from Functions.credito import transferir,gerar_embed_credito

from importlib import reload
reload(Functions.credito)

def msg_cooldown(resultado,comando):
    if(resultado[0] == True):
        segundos = 86400-resultado[1]
        hours, r = divmod(segundos, 3600)
        hours = segundos / 3600
        minutes, seconds = divmod(r, 60)
        minutes = round(minutes,0)
        hours = int(hours)
        minutes = int(minutes)
        seconds = int(seconds)
        mensagem = 'Espere '
        if(hours > 0):
            mensagem += '{} '.format(hours)
        if(hours == 1):
            mensagem += 'hora, '
        else:
            mensagem += 'horas, '
        if(minutes > 0):
            mensagem += '{} '.format(minutes)
        if(minutes == 1):
            mensagem += 'minuto, '
        else:
            mensagem += 'minutos, '
        if(seconds > 1):
            mensagem += '{} segundos, {}'.format(seconds,comando)
        elif(seconds == 1):
            mensagem += '{} segundo, {}'.format(seconds,comando)
        else:
            mensagem += comando
        return mensagem
    else:
        return None

class Economy(commands.Cog,name="Economia"):
    """Comandos relacionados a economia do bot"""
    def __init__ (self,bot):
        self.bot = bot
        self.emoji = '💰'
        self.hidden = False
        self.admin = False

    def get_emoji(self):
        return self.emoji

    def is_hidden(self):
        return self.hidden
    
    def is_admin(self):
        return self.admin

    @commands.command(name='dia', aliases=['day'],
    usage='?dia',
    description='Pegue um valor diario de créditos de 900 a 1200 créditos.',
    brief='?dia')
    @commands.cooldown(1,10, commands.BucketType.user)
    async def dia(self,ctx):
        resultado = list()
        resultado = fncooldown(ctx.message.author.id,'dia')
        msg = msg_cooldown(resultado,'para receber os créditos diários')
        if(msg is not None):
            delt = await ctx.send(msg)
            await delt.delete(delay=3)
            await ctx.message.delete(delay=3) 
        else:
            credito = random.randint(900,1200)
            id_user = ctx.message.author.id
            user = busca_user_id(id_user)
            edit_user(id_user,user.get_qtd()+credito)
            membro = ctx.message.guild.get_member(id_user)
            nome = membro.name
            await ctx.send('Foi adicionado {} créditos a {}'.format(credito,nome))

    @commands.command(name='transferir', aliases=['depositar'],
    usage='?transferir <membro> <creditos>',
    description='Transfere uma quantia de créditos para um membro.',
    brief='?transferir @john 1000 \n?transferir john 1000 \n?transferir 534535235386192929 1000\n(Irá transferir 1000 créditos a john)')
    @commands.cooldown(1,15, commands.BucketType.channel)
    async def transfer(self,ctx, membro : commands.MemberConverter, creditos : int):
        id_user = ctx.message.author.id
        resultado = fncooldown(id_user,'transferir')
        cont = fncont(id_user,'transferir',2)
        msg = msg_cooldown(resultado,'para transferir')
        if(msg is not None and cont[0] == True):
            delt = await ctx.send(msg)
            await delt.delete(delay=3)
            await ctx.message.delete(delay=3) 
        else:
            if(not cont[1]>0):
                if(creditos <= 0):
                    delt = await ctx.send('Informe uma quantia maior que zero!')
                    await delt.delete(delay=5)
                    await ctx.message.delete(delay=5)
                    fn_delete_cd(id_user,'transferir')
                else:
                    if(membro.bot == False):
                        if(membro.id == ctx.author.id):
                            delt = await ctx.send('Você não pode transferir dinheiro para si!')
                            await delt.delete(delay=5)
                            await ctx.message.delete(delay=5)
                            fn_delete_cd(id_user,'transferir')    
                        else:
                            transferir(ctx.message.author.id,membro.id,creditos)
                            await ctx.send('Transferencia de {} realizada com sucesso para {}'.format(creditos,membro.name))
                    else:
                        delt = await ctx.send('Usuário é um bot por favor informe uma pessoa.')
                        await delt.delete(delay=5)
                        await ctx.message.delete(delay=5)
                        fn_delete_cd(id_user,'transferir')

    @commands.command(name='creditos', aliases=['balance','saldo','credito','dinheiro'],
    usage='?creditos <membro : Opcional>',
    description='Informa o números de créditos que tem.',
    brief='?creditos \n (Mostará seus créditos)\n?creditos @john \n?creditos john \n?creditos 534535235386192929 \n(Irá mostrar os créditos de john)')
    @commands.cooldown(1, 5, commands.BucketType.channel)
    async def creditos(self,ctx, membro :typing.Optional[commands.MemberConverter] = 'None'):
        if(membro == 'None'):
            membro = ctx.message.author
            emb = gerar_embed_credito(membro,True)
            await ctx.send(embed=emb)
        else: 
            if(membro.bot == False):
                emb = gerar_embed_credito(membro,False)
                await ctx.send(embed=emb)
            else:
                delt = await ctx.send('Usuário é um bot por favor informe uma pessoa')
                await delt.delete(delay=5)
                await ctx.message.delete(delay=5)

def setup(bot):
    bot.add_cog(Economy(bot))
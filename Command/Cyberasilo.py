import discord
from discord.ext import commands

import json
import random
import requests

from io import BytesIO

from Functions import Checks

from Functions.banco import busca_gostosa,update_gostosa,insert_gostosa,busca_top_gostosas
from Functions.banco import busca_burrice,update_burrice,insert_burrice,busca_top_burros

antifurro = [236844195782983680,293360838461620225,207294581266579457,281146568428486656]

def is_antifurro(ctx):
    if(ctx.author.id in antifurro):
        return True
    else:
        return False

class Cyber(commands.Cog,name= "Comandos autistas"):
    def __init__ (self,bot):
            self.bot = bot
            self.emoji = '🐮'
            self.hidden = False
            self.admin = False

    def get_emoji(self):
        return self.emoji

    def is_hidden(self):
        return self.hidden

    def is_admin(self):
        return self.admin

    @commands.Cog.listener()
    async def on_command_error(self,ctx,error):
        if(isinstance(error,commands.CommandOnCooldown)):
             if(ctx.command.name == 'burro' and ctx.guild.id == 223594824681521152):
                role = discord.utils.get(ctx.guild.roles, name="Burro")
                membros = ctx.message.guild.members
                autor = ctx.guild.get_member(ctx.message.author.id)
                if(role is not None):
                    if(role in ctx.message.author.roles):
                        mensagem = '<@{}> porra bicho você quer ser mais burro do que ja é?'.format(ctx.message.author.id)
                        await ctx.channel.send(mensagem)
                    else:
                        for m in membros:
                            if(role in m.roles):
                                await m.remove_roles(role)
                        id_burro = int(ctx.message.author.id)
                        await autor.add_roles(role)
                        mensagem = 'Burro agora é você <@{}>'.format(id_burro)
                        membro = busca_burrice(id_burro)
                        if(membro):
                            update_burrice(id_burro,membro[1]+1)
                        else:
                            insert_burrice(id_burro)
                        await ctx.channel.send(mensagem)
                        with open('Data/burros.json') as json_file:
                            burros_json = json.load(json_file)
                            burros = burros_json['burros']
                            burros.pop(0)
                            burros.append(ctx.author.id)
                        with open('Data/burros.json','w') as json_file:
                            burros_json ['burros'] = burros
                            json.dump(burros_json, json_file, indent=4)
    
    @commands.command(name='furry')
    @Checks.is_Cyber()
    @commands.cooldown(1,10, commands.BucketType.user)
    async def furry(self,ctx):
        id_user = ctx.author.id 
        if(is_antifurro(ctx) == True):
            await ctx.send('Furra vai se foder <@{}>'.format(493245195060641792))
        elif(id_user == 258070435462119425 or id_user == 194991499740577794 or id_user == 330721776403218433):
            await ctx.send('Você é furro <@{}> e vai se foder'.format(id_user))
        elif(id_user == 206108254273536000):
            await ctx.send('<@{}>, furro vai se foder <:pistoranjo_cy:591028729216761897>'.format(id_user))
        elif(id_user == 493245195060641792 or id_user == 239949378700312576):
            await ctx.send('<@{}>, furra vai se foder <:pistoranjo_cy:591028729216761897>'.format(id_user))

    @commands.command(name='burro')
    @Checks.is_Cyber()
    @commands.cooldown(1,300, commands.BucketType.guild)
    async def burro(self,ctx):
        with open('Data/burros.json') as json_file:
            burros_json = json.load(json_file)
            burros = burros_json['burros']
            membros = ctx.message.guild.members
            online = list()
            for m in membros:
                if str(m.status) != 'offline' and m.bot == False:
                    if(not m.id in burros):
                        online.append(m)
            random.shuffle(online)
            burro = random.choice(online)
            role = discord.utils.get(ctx.guild.roles, name="Burro")
            for m in role.members:
                await m.remove_roles(role)
            if(ctx.channel.id != 223594824681521152):
                await ctx.send("Burro agora é você <@{}>".format(ctx.message.author.id))
                await ctx.message.author.add_roles(role)
                burros.pop(0)
                burros.append(ctx.message.author.id)
                membro = busca_burrice(ctx.message.author.id)
                if(membro):
                    update_burrice(ctx.message.author.id,membro[1]+1)
                else:
                    insert_burrice(ctx.message.author.id)
            else:
                burros.pop(0)
                burros.append(burro.id)
                membro = busca_burrice(burro.id)
                if(membro):
                    update_burrice(burro.id,membro[1]+1)
                else:
                    insert_burrice(burro.id)
                if(burro.id == ctx.message.author.id):
                    await ctx.send('Ala ele mesmo é burro bora rir klein kekw <@{}>'.format(burro.id))
                else:
                    await ctx.send("Burro do server é <@{}>".format(burro.id))
                await burro.add_roles(role)
        with open('Data/burros.json','w') as json_file:
            burros_json ['burros'] = burros
            json.dump(burros_json, json_file, indent=4)

    @commands.command(name='topburro')
    @Checks.is_Cyber()
    @commands.cooldown(1,10, commands.BucketType.channel)
    async def topburro(self,ctx):
        try:
            lista_burros = busca_top_burros()
            if(lista_burros):
                menssagem = '```Os mais burros dos server são:\n'
                contador = 0
                for burro in lista_burros:
                    str_burro = ''
                    id_user = burro.get_id()
                    if(ctx.guild.get_member(id_user) is not None):
                        quantidade = burro.get_qtd()
                        membro = ctx.guild.get_member(id_user)
                        str_burro = '[{}] {} foi burro {} vezes'.format(contador+1,membro.name,quantidade)
                        menssagem += '{}\n'.format(str_burro)
                        contador += 1
                    if(contador == 10):
                        break
                menssagem += '\n```'
            await ctx.send(menssagem)
        except Exception as e:
            print(e)

    @commands.command(name='gostosa')
    @Checks.is_Cyber()
    @commands.cooldown(1,60, commands.BucketType.channel)
    async def gostosa(self,ctx):
        with open('Data/gostosas.json') as json_file:
            gostosa_json = json.load(json_file)
            lista_gostosa = gostosa_json['gostosas']
            role = discord.utils.get(ctx.guild.roles, name="webnamorada")
            gostosas = list()
            for m in role.members:
                if m.id != 552595247809429546 and m.id != 525447699579797505 and m.id != 238803776507478017 and m.id != 523626016145539073 and m.id != 304873309164535808:
                    if(not m.id in lista_gostosa):
                        gostosas.append(m)
            random.shuffle(gostosas)
            gostosa = random.choice(gostosas)
            lista_gostosa.pop(0)
            lista_gostosa.append(gostosa.id)
            membro = busca_gostosa(gostosa.id)
            if(membro):
                update_gostosa(gostosa.id,membro[1]+1)
            else:
                insert_gostosa(gostosa.id)
            role_burro = discord.utils.get(ctx.guild.roles, name="Burro")
            if(role_burro in gostosa.roles):
                response = requests.get('https://media.discordapp.net/attachments/223594824681521152/707385777037901944/EQH1UEyWoAEW1jn.png')
                img = BytesIO(response.content)
                file = discord.File(img,filename='burra_e_gostosa.png')
                await ctx.send(content='<@{}> gostosa'.format(gostosa.id),file=file)
            else:
                await ctx.send('<@{}> gostosa'.format(gostosa.id))
        with open('Data/gostosas.json','w') as json_file:
            gostosa_json['gostosas'] = lista_gostosa
            json.dump(gostosa_json, json_file, indent=4)

    @commands.command(name='topgostosa')
    @Checks.is_Cyber()
    @commands.cooldown(1,15, commands.BucketType.channel)
    async def toptopgostosa(self,ctx):
        try:
            lista_gostosas = busca_top_gostosas()
            if(lista_gostosas):
                menssagem = '```As mais gostosas dos server são:\n'
                contador = 0
                for gostosa in lista_gostosas:
                    str_gostosa = ''
                    id_user = gostosa.get_id()
                    if(ctx.guild.get_member(id_user) is not None):
                        quantidade = gostosa.get_qtd()
                        membro = ctx.guild.get_member(id_user)
                        str_gostosa = '[{}] {} é gostosa {} vezes'.format(contador+1,membro.name,quantidade)
                        menssagem += '{}\n'.format(str_gostosa)
                        contador += 1
                    if(contador == 10):
                        break
                menssagem += '\n```'
                await ctx.send(menssagem)
            else:
                await ctx.send('Não há registros de gostosas no server')
        except Exception as e:
            print(e)

    @commands.command(name='luacs')
    @Checks.is_Cyber()
    @commands.cooldown(1,10, commands.BucketType.user)
    async def luacs(self,ctx):
        await ctx.send("Luacs baianor <:baiano_cy:568072061034037248>")

    @commands.command(name='machista')
    @Checks.is_Cyber()
    @commands.cooldown(1,10, commands.BucketType.user)
    async def machista(self,ctx):
        if(ctx.guild.id == 223594824681521152):
            await ctx.send("<@&568591788248399884>")

def setup(bot):
    bot.add_cog(Cyber(bot))
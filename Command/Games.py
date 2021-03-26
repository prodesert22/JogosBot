import discord
from discord.ext import commands

import Functions.blackjack
import Functions.mina
import Functions.slot_machine
import Functions.Sokoban

from importlib import reload
reload(Functions.blackjack)
reload(Functions.mina)
reload(Functions.slot_machine)
reload(Functions.Sokoban)

from Functions.banco import busca_user_id
from Functions.blackjack import blackjack_game
from Functions.mina import cal_matriz, gerar_texto
from Functions.slot_machine import maquina
from Functions.Sokoban import sokoban_game

MINIMO = 50

def error_menssage(c,user):
    msg = None
    if(c > 9999999):
        msg = 'Informe um número menor que 10000000!' 
    elif(c < MINIMO):
        msg = 'A aposta mínima é de {} creditos.'.format(MINIMO)
    elif (user.get_qtd() < c):
        msg = 'Número a ser apostado é maior que o seu saldo.'
    return msg

def loot_777():
    loot = 'Valor dos prêmios:\n'
    loot += ':tangerine: :tangerine: :question: - 0.5x\n'
    loot +=':grapes: :grapes: :question: - 2x\n'
    loot +=':cherries: :cherries: :question: - 3x\n'
    loot +=':dollar: :dollar: :question: - 5x\n'
    loot +=':cherries: :cherries: :cherries: - 6x\n'
    loot +=':moneybag: :moneybag: :question: - 10x\n'
    loot +=':dollar: :dollar: :dollar: - 15x\n'
    loot +=':gem: :gem: :question: - 20x\n'
    loot +=':moneybag: :moneybag: :moneybag: - 25x\n'
    loot +=':gem: :gem: :gem: - 40x\n'
    loot +='<:sete:629450359412097024> <:sete:629450359412097024> <:sete:629450359412097024> - 100x\n'
    return loot

class Games(commands.Cog,name= "Jogos"):
    """Comandos relacionados aos jogos presentes no bot"""
    def __init__ (self,bot):
        self.bot = bot
        self.emoji = '🎮'
        self.hidden = False
        self.admin = False
        
    def get_emoji(self):
        return self.emoji

    def is_hidden(self):
        return self.hidden

    def is_admin(self):
        return self.admin

    @commands.command(name='mina', aliases=['mine'], 
    usage='?mina tamanho num_bombas',
    description='Gera um campo minado com a largura e número\n de bombas informados.',
    brief='?mina 10 50\n(Irá gera um campo minado \nde 10x10 com 50 bombas)')
    @commands.cooldown(1, 10, commands.BucketType.channel)
    async def mina(self, ctx, tamanho : int, num_bomba : int):
        try:
            tamanho = int(tamanho)
            bomba = int(num_bomba)
            if(bomba < 0 or tamanho <=0):
                delte = await ctx.send('Tamanho ou números de bombas inválido')  
                await ctx.message.delete(delay=5)
                await delte.delete(delay=5)
            elif(tamanho>13): 
                delte = await ctx.send('Tamanho inválido, excede o limite de 13')
                await ctx.message.delete(delay=5)
                await delte.delete(delay=5)
            elif(bomba>(tamanho*tamanho)):
                delte = await ctx.send('O número de bombas é maior que o tamanho. Informe um numero menor')
                await ctx.message.delete(delay=5)
                await delte.delete(delay=5)
            else:
                matrix = cal_matriz(tamanho,bomba)
                texto = gerar_texto(tamanho,matrix,bomba)
                await ctx.send(texto)
        except:
            delte = await ctx.send('Informe só numeros')
            await ctx.message.delete(delay=5)
            await delte.delete(delay=5)
    
    @commands.command(name='777',aliases=['slot','slots'],
    usage='?777 <créditos>', 
    description='Aposta uma quantia de créditos na slot machine.\n {}'.format(loot_777()), 
    brief='?777 1000\n?777 1k\n(Irá aposta 1k de créditos).')
    @commands.cooldown(1, 10, commands.BucketType.user)
    async def slotmachine(self, ctx, credito):
        try:
            id_user = ctx.message.author.id
            user = busca_user_id(id_user)
            msg = credito
            if(msg == 'all'):
                c = user.get_qtd()
                await ctx.send('Apostando all in.')  
            elif msg.count('k') == 1:
                index = msg.find('k')
                c = int(msg[:index])
                c *= 1000
                c = int(c)
            else:
                c = int(msg)
            msg = error_menssage(c,user)
            if(msg is None):
                await maquina(c,ctx.message,ctx.message.channel)
            else:
                delte = await ctx.send(msg)
                await ctx.message.delete(delay=5)
                await delte.delete(delay=5)
        except:
            delte = await ctx.send('Número inválido, infomre um número inteiro para apostar.')
            await ctx.message.delete(delay=5)
            await delte.delete(delay=5)

    @commands.command(name='blackjack', aliases=['bj','21'],
    usage='?blackjack <créditos>', 
    description='Jogue blackjack versus a maquina', 
    brief='?blackjack 1000\nApostando mil créditos\n?blackjack 2k\nApostando 2 mil créditos')
    @commands.cooldown(1,10, commands.BucketType.user)
    async def bj(self,ctx, credito):
        try:
            id_user = ctx.message.author.id
            user = busca_user_id(id_user)
            if credito.count('k') == 1:
                index = credito.find('k')
                credito = int(credito[:index])
                credito *= 1000
                credito = int(credito)
            else:
                credito = int(credito)

            msg = error_menssage(credito,user)
            if(msg is None):
                await blackjack_game(ctx,self.bot,credito)
            else:
                delte = await ctx.send(msg)
                await ctx.message.delete(delay=5)
                await delte.delete(delay=5)
        except Exception as e:
            print(e)
            delte = await ctx.send('Número inválido, número inteiro para apostar')
            await ctx.message.delete(delay=5)
            await delte.delete(delay=5)

    @commands.command(name='sokoban', aliases=['soko'],
    usage='?sokoban', 
    description='Jogue Sokoban, empurre todas as caixas nas marcoçẽos para ganhar', 
    brief='?sokoban')
    @commands.cooldown(1,30, commands.BucketType.user)
    async def soko(self,ctx):
        message = await ctx.send('Carregando o nivel <a:loading:803617428801585162>')
        level = 1
        ganhou = await sokoban_game(ctx,message,self.bot,level)
        if(ganhou is True):
            for i in range(2,5):
                await message.edit(content='Carregando novo nivel <a:loading:803617428801585162>')
                ganhou = await sokoban_game(ctx,message,self.bot,i)
                if(ganhou is False):
                    break
        
def setup(bot):
    bot.add_cog(Games(bot))

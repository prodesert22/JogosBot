import discord
from discord.ext import commands

import cairosvg
import datetime
import math
import os
import re
import requests
import unicodedata
import typing
import wand

from io import BytesIO

PATH_ABS = os.path.abspath(r"../JogosBot")
PATH_DATA = os.path.join(PATH_ABS,"Data")
PATH_svg = os.path.join(PATH_DATA,'svg')

class Utils(commands.Cog,name= "Utilidades"):
    def __init__ (self,bot):
            self.bot = bot
            self.emoji = '📋'
            self.hidden = False
            self.admin = False

    def get_emoji(self):
        return self.emoji

    def is_hidden(self):
        return self.hidden

    def is_admin(self):
        return self.admin

    @commands.command(name='ping',
    usage='?ping',
    description='Mostra a lantencia do bot.',
    brief='?ping')
    @commands.cooldown(1,20, commands.BucketType.guild)
    async def ping(self, ctx):
        tempo1 = datetime.datetime.timestamp(ctx.message.created_at)
        msg = await ctx.send('Pong!')
        tempo2 = datetime.datetime.timestamp(msg.created_at)
        ms = (tempo2-tempo1)*1000
        menssagem = 'Pong! Latência: {}ms'.format(math.trunc(ms))
        await msg.edit(content=menssagem)

    @commands.command(name='avatar', aliases=['profile'], 
    usage='?avatar <user>: Opcional',
    description='Busca a imagem do usuario.',
    brief='?avatar @john \n?avatar john \n?avatar 534535235386192929 1000')
    @commands.cooldown(1,10, commands.BucketType.user)
    async def avatar(self, ctx, Member:typing.Optional[commands.MemberConverter] = None):
        if Member:
            embed=discord.Embed(title=f"Imagem de perfil de {Member.name}.")
            embed.set_image(url=Member.avatar_url)
            await ctx.send(embed=embed)
        else:
            embed=discord.Embed(title=f"Sua imagem de perfil.")
            embed.set_image(url=ctx.author.avatar_url)
            await ctx.send(embed=embed)
    
    @commands.command(name='e', aliases=['emoji','em'], 
    usage='?e <emoji>',
    description='Busca a imagem do emoji.',
    brief='?e <emoji>')
    @commands.cooldown(1,10, commands.BucketType.user)
    async def emoji(self, ctx, emoji:str):
        emote_regex = re.compile(r'<:.*:(?P<id>\d*)>')
        match = emote_regex.match(emoji)
        if match:
            emote = 'https://cdn.discordapp.com/emojis/{}.png'.format(str(match.group('id')))
            emote_gif = 'https://cdn.discordapp.com/emojis/{}.gif'.format(str(match.group('id')))
            print(emote)
            response_png = requests.get(emote)
            response_gif = requests.get(emote_gif)
            print(type(response_png.content))
            png = BytesIO(response_png.content)
            png.seek(0)
            print(png.tell())
            file_png = discord.File(png,filename='emoji.png')
            if response_gif.status_code == 200:
                gif = BytesIO(response_gif.content)
                file_gif = discord.File(fp=gif,filename='emoji.gif')
                await ctx.send(files=[file_png,file_gif])
            else:
                await ctx.send(file=file_png)
        else:
            if(emoji.isdigit()):
                emote = 'https://cdn.discordapp.com/emojis/{}.png'.format(str(emoji))
                emote_gif = 'https://cdn.discordapp.com/emojis/{}.gif'.format(str(emoji))
                response_png = requests.get(emote)
                response_gif = requests.get(emote_gif)
                print(type(response_png.content))
                png = BytesIO(response_png.content)
                file_png = discord.File(png,filename='emoji.png')
                if response_gif.status_code == 200:
                    gif = BytesIO(response_gif.content)
                    file_gif = discord.File(fp=gif,filename='emoji.gif')
                    await ctx.send(files=[file_png,file_gif])
                else:
                    await ctx.send(file=file_png)
            else:
                cont = 1
                url = PATH_svg+"/"
                for e in emoji:
                    name = ord(e)
                    if cont == len(emoji):
                        url += f'{name:x}.svg'
                    else:
                        url += f'{name:x}-'
                    cont +=1
                if(os.path.isfile(url)):
                    t = BytesIO(cairosvg.svg2png(url=url,scale=8))
                    file = discord.File(fp=t,filename='emoji.png')
                    await ctx.send(file=file)
                else:
                    await ctx.send('Emoji não encontrado.')

def setup(bot):
    bot.add_cog(Utils(bot))
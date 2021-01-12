import discord
from discord.ext import commands

import Functions.banco
import Functions.Checks
from importlib import reload
reload(Functions.Checks)
Functions.banco.close_db()
reload(Functions.banco)

from Functions import Checks
from Functions.banco import close_db

class Owner(commands.Cog,name= "Dono"):
    """Comandos só acessados por admins"""
    def __init__ (self,bot):
        self.bot = bot
        self.emoji = '🔑'
        self.hidden = True
        self.admin = False

    def get_emoji(self):
        return self.emoji

    def is_hidden(self):
        return self.hidden

    def is_admin(self):
        return self.admin
        
    @commands.Cog.listener()
    async def on_message(self,message):
        if(message.channel.id == 749441957553504377 and message.author.id == 749441834396418158):
            text = message.content.split()
            url = text[0]
            title = text[1:]
            title = " ".join(title)
            id_video = url[17:]
            emb = discord.Embed(
                title= "Atenção, video novo do Viniccius13.",
                url= url
            )
            emb.add_field(name='Titulo: ',value=title,inline=False)
            emb.add_field(name='Link:', value=url)
            emb.set_image(url='http://i3.ytimg.com/vi/{}/hqdefault.jpg'.format(id_video))
            canal = self.bot.get_channel(635288743258882059)
            await canal.send(embed=emb)
        elif(message.channel.id == 763850761825681468 and message.author.id == 763852070540804116):
            text = message.content.split()
            url = text[0]
            title = text[1:]
            title = " ".join(title)
            id_video = url[17:]
            emb = discord.Embed(
                title= "Atenção, video novo do Danilo Amoroso.",
                url= url
            )
            emb.add_field(name='Titulo: ',value=title,inline=False)
            emb.add_field(name='Link:', value=url)
            emb.set_image(url='http://i3.ytimg.com/vi/{}/hqdefault.jpg'.format(id_video))
            canal = self.bot.get_channel(635288743258882059)
            await canal.send(embed=emb)


    @commands.command()
    @Checks.is_owner()
    async def closedb(self,ctx):
        close_db()

    @commands.command()
    @Checks.is_owner()
    async def listserver(self,ctx):
        for guild in self.bot.guilds:
            print(guild.name)

def setup(bot):
    bot.add_cog(Owner(bot))
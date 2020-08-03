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
        
    @commands.command()
    @Checks.is_owner()
    async def closedb(self,ctx):
        close_db()
    
def setup(bot):
    bot.add_cog(Owner(bot))
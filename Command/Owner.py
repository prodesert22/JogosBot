import discord
from discord.ext import commands

from Functions import Checks

from Functions.banco import reset_table_gostosa

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
    async def reset_gostosa(self,ctx):
        a = reset_table_gostosa()
        if(a == True):
            await ctx.send('Resetada a tabela')
        else:
            await ctx.send('Erro')

def setup(bot):
    bot.add_cog(Owner(bot))
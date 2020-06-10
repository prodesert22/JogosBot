import discord
from discord.ext import commands

from Functions import Checks

from Functions.banco import update_prefix

class Admin(commands.Cog,name= "Comandos para Admins"):
    """Comandos só acessados por admins"""
    def __init__ (self,bot):
        self.bot = bot
        self.emoji = '🔑'
        self.hidden = True
        self.admin = True

    def get_emoji(self):
        return self.emoji

    def is_hidden(self):
        return self.hidden

    def is_admin(self):
        return self.admin
        
    async def is_owner_server(self,ctx):
        return ctx.author.id == 236844195782983680 or ctx.guild.owner_id == ctx.author.id

    @commands.Cog.listener()
    async def on_message(self,ctx):
        m = ctx.content.lower()
        if ctx.guild == None or ctx.author.bot == True:
            pass
        else:
            if(m == '?reset_prefix' and (ctx.author.id == 236844195782983680 or ctx.guild.owner_id == ctx.author.id)):
                update_prefix(ctx.guild.id,'?')
                await ctx.send('Foi editado o prefix para `?`.')
        
    @commands.command(name="prefix", aliases=['c_prefix','change_prefix'],
    usage='?prefix <prefix>',
    description='Altere o prefix do bot neste servidor.',
    brief='?prefix !\nIrá mudar o prefix para !')
    @Checks.is_owner_server()
    @commands.cooldown(1,30, commands.BucketType.guild)
    async def change_prefix(self,ctx, prefix):
        if(len(prefix)<=3):
            update_prefix(ctx.guild.id,prefix)
            await ctx.send('Foi editado o prefix para `{}`.'.format(prefix))
        else:
            await ctx.send('Erro, exedeu o máximo de 3 caracteres permitidos.')
            ctx.command.reset_cooldown(ctx)

def setup(bot):
    bot.add_cog(Admin(bot))
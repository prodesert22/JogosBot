import discord
from discord.ext import commands

def help_command(comando,prefix):
    embed=discord.Embed(
            title='Comando: {}'.format(comando.name),
            description=comando.description)
    uso = comando.usage.replace('?',prefix[0])
    exemplos = comando.brief.replace('?',prefix[0])
    embed.add_field(name='**Uso:**',value=uso)
    embed.add_field(name='**Exemplos:**',value=exemplos)
    embed.add_field(name='\u200B',value='\u200B',inline=False)
    msg_status = lambda status:'✅ Ativado' if status == True  else '❌ Desativado'
    embed.add_field(name='Status',value=msg_status(comando.enabled))
    if(len(comando.aliases)>0):
        aliases = '' 
        for alias in comando.aliases:
            aliases +=  f"**{alias}** "
        embed.add_field(name='**Alias:**',value=aliases)
    return embed

def is_admin_ower(ctx):
    return ctx.author.id == 236844195782983680 or ctx.guild.owner_id == ctx.author.id

class Help(commands.Cog):
    def __init__ (self,bot):
        self.bot = bot
        self.emoji = '❓'
        self.hidden = True
        self.admin = False

    def get_emoji(self):
        return self.emoji

    def is_hidden(self):
        return self.hidden

    def is_admin(self):
        return self.admin

    @commands.command(name='help',aliases=['comandos'])
    @commands.cooldown(1,5, commands.BucketType.user)
    async def comandos(self,ctx, command_name):
        comando = self.bot.get_command(command_name)
        if comando is not None:
            cog = comando.cog
            if(cog is not None):
                if(cog.is_hidden() is False):
                    p = await self.bot.get_prefix(ctx.message)
                    h = help_command(comando,p)
                    await ctx.send(embed=h)
                elif(cog.is_admin() is True):
                    if(is_admin_ower(ctx) is True):
                        p = await self.bot.get_prefix(ctx.message)
                        h = help_command(comando,p)
                        await ctx.send(embed=h)
                    else:
                        msg = 'Comando não encontrado.'
                        delte = await ctx.send(msg)
                        await ctx.message.delete(delay=3)
                        await delte.delete(delay=3) 
            else:
                msg = 'Comando não encontrado.'
                delte = await ctx.send(msg)
                await ctx.message.delete(delay=3)
                await delte.delete(delay=3)
        else:
            msg = 'Comando não encontrado.'
            delte = await ctx.send(msg)
            await ctx.message.delete(delay=3)
            await delte.delete(delay=3)

    @comandos.error
    async def comandos_error(self,ctx,error):
        if isinstance(error, commands.MissingRequiredArgument):
            p = await self.bot.get_prefix(ctx.message)
            h=discord.Embed(
                title='Todos os comandos do bot por categorias.',
                description='Use `{}help <comando>` para saber mais sobre este comando'.format(p[0]))
            for nome in self.bot.cogs:
                c_ext = self.bot.cogs[nome]
                if(c_ext.is_hidden() is True):
                    if(c_ext.is_admin() is False):
                        continue
                    else:
                        if(is_admin_ower(ctx) is False):
                            continue
                comandos = ''
                for c in c_ext.walk_commands():
                    comandos += "__**{}**__ ".format(c) 
                h.add_field(name="{}**{}**".format(c_ext.get_emoji(),nome),value=comandos,inline=True)
            await ctx.send(embed=h)
        else:
            pass

def setup(bot):
    bot.add_cog(Help(bot))
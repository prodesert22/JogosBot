import discord

from discord.ext import commands

import math

from Command.Help import help_command

class No_Owner(commands.CommandError): pass
class No_Perms(commands.CommandError): pass
class No_Guild(commands.CommandError): pass
class No_Guild_Owner(commands.CommandError): pass
class No_Cyber(commands.CommandError): pass

owner_id = 236844195782983680

def is_owner():
    def predicate(ctx):
        if ctx.author.id == 236844195782983680:
            return True
        raise No_Owner()
    return commands.check(predicate)

def is_owner_server():
    def predicate(ctx):
        if ctx.author.id == ctx.guild.owner_id:
            return True
        raise No_Guild_Owner
    return commands.check(predicate)

def is_Cyber():
    def predicate(ctx):
        if ctx.guild.id == 223594824681521152:
            return True
        raise No_Cyber
    return commands.check(predicate)

def has_guild(ctx):
    def predicate(ctx):
        if ctx.guild:
            return True
        raise No_Guild
    return commands.check(predicate)

async def c_error(ctx,error):
    info = False
    mensagem = None
    delay = 5
    if isinstance(error, commands.CommandOnCooldown):
        mensagem = 'Espere {} segundos para usar esse comando novamente'.format(math.ceil(error.retry_after))
    elif isinstance(error,commands.InvalidEndOfQuotedStringError):
        mensagem = 'Erro, parametro(s) informado(s)  inválido(s).'
        delay = 4
    elif isinstance(error, commands.BadArgument):
        mensagem = error
        delay = 4
    elif isinstance(error, commands.DisabledCommand):
        mensagem = '🛠Comando desativado para manutenção'
        delay = 3
    elif isinstance(error, commands.CommandNotFound):
        pass
    elif isinstance(error, No_Guild):
        pass
    elif isinstance(error, No_Owner):
        mensagem = "Permissão negada."
        delay = 2
    elif isinstance(error, No_Guild_Owner):
        mensagem = "Permissão negada, este comando só pode ser usado pelo dono do server"
        delay = 4
    elif isinstance(error, No_Cyber):
        mensagem = "Comando só ativo no Cyber"
        delay = 3
    elif isinstance(error, commands.MissingRequiredArgument):
        info = True
        if(not ctx.command.name == 'help'):
            p = await ctx.bot.get_prefix(ctx.message)
            h = help_command(ctx.command,p)
            await ctx.send(embed=h)
    else:
        mensagem = 'Um erro inesperado acontenceu.'
        print("Erro: ",error)
        print("Tipo: ",type(error))
        print(ctx.message.content)
    if(mensagem is not None):
        delt = await ctx.channel.send(mensagem)
        if(info == False):
            await delt.delete(delay=delay)
            await ctx.message.delete(delay=delay)
            if(not isinstance(error, commands.CommandOnCooldown)):
                ctx.command.reset_cooldown(ctx)
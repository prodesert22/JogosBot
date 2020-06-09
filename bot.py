import asyncio
import discord
import math
import os

from discord.ext import commands

from Functions.banco import busca_prefix,insert_prefix
from Command.Help import help_command
from tokens import token

DEFAULT_PREFIX = '?'

async def get_prefix(bot, message):
    if(message.guild is not None):
        prefix = busca_prefix(message.guild.id)
        if(prefix is None):
            insert_prefix(message.guild.id,DEFAULT_PREFIX)
            return DEFAULT_PREFIX
        else:
            return prefix
    else:
        return DEFAULT_PREFIX

bot = commands.Bot(case_insensitive=True, command_prefix = get_prefix)
bot.remove_command('help')

@bot.check
def guild(ctx):
    return ctx.guild is not None

async def is_owner(ctx):
    return ctx.author.id == 236844195782983680

@bot.event
async def on_ready():
    print("{}, Bot online - Olá Mundo!".format(bot.user.name))
    #print(bot.guilds)
    game = discord.Game("Ativo em {} servers".format(len(bot.guilds)-2))
    await bot.change_presence(status=discord.Status.online, activity=game)
    
@bot.event
async def on_command_error(ctx,error):
    info = False
    mensagem = None
    delay = 5
    print(error)
    if isinstance(error, commands.CommandOnCooldown):
        mensagem = 'Espere {} segundos para usar esse comando novamente'.format(math.ceil(error.retry_after))
    elif isinstance(error,commands.InvalidEndOfQuotedStringError) or isinstance(error, commands.BadArgument):
        mensagem = 'Erro, parametro(s) informado inválido.'
        delay = 2
    elif isinstance(error, commands.DisabledCommand):
        mensagem = '🛠Comando desativado para manutenção'
        delay = 3
    elif isinstance(error, commands.CheckFailure):
        if(ctx.guild is not None):
            mensagem = "Permissão negada."
            delay = 2
    elif isinstance(error, commands.MissingRequiredArgument):
        info = True
        if(not ctx.command.name == 'help'):
            p = await bot.get_prefix(ctx.message)
            h = help_command(ctx.command,p)
            await ctx.send(embed=h)
    elif isinstance(error, commands.CommandNotFound):
        pass
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
            if(ctx.command):
                ctx.command.reset_cooldown(ctx)

@bot.command()
@commands.check(is_owner)
async def disable(ctx, command):
    comando = bot.get_command(command)
    if comando is not None:
        comando.update(enabled=False)
        await ctx.send('Comando {} foi desativado'.format(comando.name))
    else:
        print('Não encontrado')

@bot.command()
@commands.check(is_owner)
async def enable(ctx, command):
    comando = bot.get_command(command)
    if comando is not None:
        comando.update(enabled=True)
        await ctx.send('Comando {} foi ativado'.format(comando.name))
    else:
        print('Não encontrado')

@bot.command()
@commands.check(is_owner)
async def load(ctx, extension):
    try:
        bot.load_extension(f'Command.{extension.capitalize()}')
        await ctx.send(f'{extension.capitalize()} carregada com sucesso!')
    except Exception as e :
        print(e)
        await ctx.send(f'Erro em carregar {extension.capitalize()}.')

@bot.command()
@commands.check(is_owner)
async def unload(ctx, extension):
    try:
        bot.unload_extension(f'Command.{extension.capitalize()}')
        await ctx.send(f'{extension} descarregada com sucesso!')
    except Exception as e :
        print(e)
        await ctx.send(f'Erro em descarregar {extension.capitalize()}.')

@bot.command(name='reload')
@commands.check(is_owner)
async def reload_cog(ctx, extension):
    try:
        for _ in range(2):
            bot.unload_extension(f'Command.{extension.capitalize()}')
            bot.load_extension(f'Command.{extension.capitalize()}')
        await ctx.send(f'{extension} recarregada com sucesso!')
    except Exception as e :
        print(e)
        await ctx.send(f'Erro em recarregar {extension.capitalize()}.')

@bot.command(name='reload_all')
@commands.check(is_owner)
async def reload_cog_all(ctx):
    try:
        for filename in os.listdir('./Command'):
            if filename.endswith('.py'):
                bot.unload_extension(f'Command.{filename[:-3]}')
                bot.load_extension(f'Command.{filename[:-3]}')
        await ctx.send('Extensões carregadas com sucesso')
    except Exception as e :
        print(e)
        await ctx.send('Erro em recarregar as extensões.')

for filename in os.listdir('./Command'):
    if filename.endswith('.py'):
        bot.load_extension(f'Command.{filename[:-3]}')

bot.run(token())

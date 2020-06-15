import asyncio
import discord
import os

from discord.ext import commands

from Functions.banco import busca_prefix,insert_prefix
from Functions import Checks

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
    if ctx.guild:
        return True
    raise Checks.No_Guild

@bot.event
async def on_ready():
    print("{}, Bot online - Olá Mundo!".format(bot.user.name))
    #print(bot.guilds)
    game = discord.Game("Ativo em {} servers".format(len(bot.guilds)-2))
    await bot.change_presence(status=discord.Status.online, activity=game)
    
@bot.event
async def on_command_error(ctx,error):
    await Checks.c_error(ctx,error)

@bot.command()
@Checks.is_owner()
async def disable(ctx, command):
    comando = bot.get_command(command)
    if comando is not None:
        comando.update(enabled=False)
        await ctx.send('Comando {} foi desativado'.format(comando.name))
    else:
        print('Não encontrado')

@bot.command()
@Checks.is_owner()
async def enable(ctx, command):
    comando = bot.get_command(command)
    if comando is not None:
        comando.update(enabled=True)
        await ctx.send('Comando {} foi ativado'.format(comando.name))
    else:
        print('Não encontrado')

@bot.command()
@Checks.is_owner()
async def load(ctx, extension):
    try:
        bot.load_extension(f'Command.{extension.capitalize()}')
        await ctx.send(f'{extension.capitalize()} carregada com sucesso!')
    except Exception as e :
        print(e)
        await ctx.send(f'Erro em carregar {extension.capitalize()}.')

@bot.command()
@Checks.is_owner()
async def unload(ctx, extension):
    try:
        bot.unload_extension(f'Command.{extension.capitalize()}')
        await ctx.send(f'{extension} descarregada com sucesso!')
    except Exception as e :
        print(e)
        await ctx.send(f'Erro em descarregar {extension.capitalize()}.')

@bot.command(name='reload')
@Checks.is_owner()
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
@Checks.is_owner()
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

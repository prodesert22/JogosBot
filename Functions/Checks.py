import discord

from discord.ext import commands

import math
import re

from Command.Help import help_command

class No_Owner(commands.CommandError): pass
class No_Perms(commands.CommandError): pass
class No_Guild(commands.CommandError): pass
class No_Guild_Owner(commands.CommandError): pass
class No_Cyber(commands.CommandError): pass
class No_Guild_Owner_Bot(commands.CommandError): pass

class Membro_nao_encontrado(commands.BadArgument):
    def __init__(self, argument):
        self.argument = argument
        super().__init__(' "{}" não encontrado.'.format(argument))

class Busca_User(commands.IDConverter):

    async def query_member_named(self, guild, argument):
        #cache = guild._state.member_cache_flags.joined
        if len(argument) > 5 and argument[-5] == '#':
            username, _, discriminator = argument.rpartition('#')
            members = await guild.query_members(username, limit=100)
            return discord.utils.get(members, name=username, discriminator=discriminator)
        else:
            members = await guild.query_members(argument, limit=100)
            if members and len(members) > 0:
                return members[0]
            else:
                return None

    async def query_member_by_id(self, bot, guild, user_id):
        ws = bot._get_websocket(shard_id=guild.shard_id)
        #cache = guild._state.member_cache_flags.joined
        if ws.is_ratelimited():
            # If we're being rate limited on the WS, then fall back to using the HTTP API
            # So we don't have to wait ~60 seconds for the query to finish
            try:
                member = await guild.fetch_member(user_id)
            except discord.HTTPException:
                return None

            if cache:
                guild._add_member(member)
            return member

        # If we're not being rate limited then we can use the websocket to actually query
        members = await guild.query_members(limit=1, user_ids=[user_id])
        if not members:
            return None
        return members[0]

    async def convert(self, ctx, argument):
        bot = ctx.bot
        match = self._get_id_match(argument) or re.match(r'<@!?([0-9]+)>$', argument)
        guild = ctx.guild
        result = None
        user_id = None
        if match is None:
            # not a mention...
            result = guild.get_member_named(argument)
        else:
            user_id = int(match.group(1))
            result = guild.get_member(user_id) or discord.utils.get(ctx.message.mentions, id=user_id)
        if result is None:
            if guild is None:
                raise Membro_nao_encontrado(argument)
            if user_id is not None:
                result = await self.query_member_by_id(bot, guild, user_id)
            else:
                result = await self.query_member_named(guild, argument)

            if not result:
                raise Membro_nao_encontrado(argument)

        return result

owner_id = 236844195782983680

def is_owner():
    def predicate(ctx):
        if ctx.author.id == owner_id:
            return True
        raise No_Owner()
    return commands.check(predicate)

def is_owner_server():
    def predicate(ctx):
        if ctx.author.id == ctx.guild.owner_id:
            return True
        raise No_Guild_Owner
    return commands.check(predicate)

def is_owner_server_or_bot():
    def predicate(ctx):
        if ctx.author.id == ctx.guild.owner_id or ctx.author.id == 236844195782983680: 
            return True
        raise No_Guild_Owner_Bot
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
    elif isinstance(error, No_Owner) or isinstance(error, No_Guild_Owner_Bot) :
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
        mensagem = 'Um erro inesperado acontenceu.\n{}'.format(error)
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
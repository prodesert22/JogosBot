import discord
from discord.ext import commands

import datetime
import pycountry
from pyUFbr.baseuf import ufbr

import Functions.pesquisas
from Functions.pesquisas import dolar,euro,dolar_hoje,euro_hoje,libra,libra_hoje,corona,topcorona

from importlib import reload
reload(Functions.pesquisas)

class Apis(commands.Cog,name='Pesquisas dolar,euro,corona'):
    def __init__ (self,bot):
        self.bot = bot
        self.emoji = '🗺'
        self.hidden = False
        self.admin = False

    def get_emoji(self):
        return self.emoji

    def is_hidden(self):
        return self.hidden

    def is_admin(self):
        return self.admin

    @commands.command(name='dolar')
    @commands.cooldown(1,15, commands.BucketType.channel)
    async def contacao_dolar(self,ctx,*args):
        try:
            if(len(args) == 0):
                mensagem,data_criacao= dolar_hoje()
            else:
                data_texto = args[0]
                data_time = datetime.datetime.strptime(data_texto, '%d/%m/%Y')
                data = data_time.strftime('%m-%d-%Y')
                mensagem,data_criacao= dolar(data)
            emb = discord.Embed(
                title=':dollar: Cotação do Dólar :dollar:',
                description=mensagem,
                colour = discord.Colour.blue()
            )
            emb.set_footer(text=data_criacao)
            emb.set_author(name='{}'.format(ctx.author.name),icon_url='{}'.format(ctx.author.avatar_url))
            await ctx.send(embed=emb)
        except Exception as e:
            print(e)
            await ctx.send('A data não está no formato DD/MM/AAAA')

    @commands.command(name='euro')
    @commands.cooldown(1,15, commands.BucketType.channel)
    async def contacao_euro(self,ctx,*args):
        try:
            if(len(args) == 0):
                mensagem,data_criacao= euro_hoje()
            else:
                data_texto = args[0]
                data_time = datetime.datetime.strptime(data_texto, '%d/%m/%Y')
                data = data_time.strftime('%m-%d-%Y')
                mensagem,data_criacao= euro(data)
            emb = discord.Embed(
                title=':euro: Cotação do Euro :euro:',
                description=mensagem,
                colour = discord.Colour.blue()
            )
            emb.set_footer(text=data_criacao)
            emb.set_author(name='{}'.format(ctx.author.name),icon_url='{}'.format(ctx.author.avatar_url))
            await ctx.send(embed=emb)
        except Exception as e:
            print(e)
            await ctx.send('A data não está no formato DD/MM/AAAA')

    @commands.command(name='libra')
    @commands.cooldown(1,15, commands.BucketType.channel)
    async def contacao_libra(self,ctx,*args):
        try:
            if(len(args) == 0):
                mensagem,data_criacao= libra_hoje()
            else:
                data_texto = args[0]
                data_time = datetime.datetime.strptime(data_texto, '%d/%m/%Y')
                data = data_time.strftime('%m-%d-%Y')
                mensagem,data_criacao= libra(data)
            emb = discord.Embed(
                title=':pound: Cotação do Libra :pound:',
                description=mensagem,
                colour = discord.Colour.blue()
            )
            emb.set_footer(text=data_criacao)
            emb.set_author(name='{}'.format(ctx.author.name),icon_url='{}'.format(ctx.author.avatar_url))
            await ctx.send(embed=emb)
        except Exception as e:
            print(e)
            await ctx.send('A data não está no formato DD/MM/AAAA')

    @commands.command(name='corona')
    @commands.cooldown(3,15, commands.BucketType.channel)
    async def corona_total(self,ctx,*args):
        try:
            if(len(args) == 0):
                brasil = corona('Brazil',None,'br')
                emb = discord.Embed(
                        title='Casos do coronavírus',
                        description='{}'.format(brasil),
                        colour = discord.Colour.blue()
                    )
                emb.set_author(name='{}'.format(ctx.author.name),icon_url='{}'.format(ctx.author.avatar_url))
                emb.timestamp = datetime.datetime.utcnow()
                await ctx.send(embed=emb)
            elif(len(args) > 1):
                await ctx.send('Informe um pais ou um estado do brasil')
            else:
                if(args[0].upper() in ufbr.list_uf):
                    estado = corona(None,args[0],None)
                    emb = discord.Embed(
                        title='Casos do coronavírus',
                        description='{}'.format(estado),
                        colour = discord.Colour.blue()
                    )
                    emb.set_author(name='{}'.format(ctx.author.name),icon_url='{}'.format(ctx.author.avatar_url))
                    emb.timestamp = datetime.datetime.utcnow()
                    await ctx.send(embed=emb)
                else:
                    if(len(args[0]) != 1):
                        country = None
                        print(len(args[0]))
                        if(len(args[0]) == 2):
                            country = pycountry.countries.get(alpha_2=args[0].upper())
                        elif(len(args[0]) == 3):
                            country = pycountry.countries.get(alpha_3=args[0].upper())
                        else:
                            country = pycountry.countries.get(name=args[0].capitalize() )
                        if(country is not None):
                            pesquisado = corona(country.name,None,country.alpha_2.lower())
                            emb = discord.Embed(
                            title='Casos do coronavírus',
                            description='{}'.format(pesquisado),
                            colour = discord.Colour.blue()
                            )
                            emb.set_author(name='{}'.format(ctx.author.name),icon_url='{}'.format(ctx.author.avatar_url))
                            emb.timestamp = datetime.datetime.utcnow()
                            await ctx.send(embed=emb)
                        else:
                            await ctx.send('Pais não encontrado.')
                    else:
                        await ctx.send('Pais não encontrado.')
        except Exception as e:
            print(e)
                    
    @commands.command(name='topcorona')
    @commands.cooldown(1,15, commands.BucketType.channel)
    async def top_corona(self,ctx):
        try:
            lista = topcorona()
            emb = discord.Embed(
                title='Top paises com casos do coronavírus',
                colour = discord.Colour.blue()
            )
            emb.set_author(name='{}'.format(ctx.author.name),icon_url='{}'.format(ctx.author.avatar_url))
            for pais in lista:
                emb.add_field(name="{}".format(pais['country']),value='✅ Confirmados: {} 💀 Mortos: {}'.format(pais['confirmed'],pais['deaths']),inline=False)
            await ctx.send(embed=emb)
        except Exception as e:
            print(e)

def setup(bot):
    bot.add_cog(Apis(bot))
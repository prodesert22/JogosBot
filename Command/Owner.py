import discord
from discord.ext import commands

import Functions.banco
import Functions.Checks
from importlib import reload
reload(Functions.Checks)
Functions.banco.close_db()
reload(Functions.banco)

from Functions import Checks
from Functions.banco import close_db,busca_gostosa,update_gostosa,insert_gostosa,reset_table_gostosa,delete_gostosa
from Functions.banco import edit_user,busca_user_id,fn_insert_user

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

    @commands.command()
    @Checks.is_owner()
    async def reset_gostosa(self,ctx):
        a = reset_table_gostosa()
        if(a == True):
            await ctx.send('Resetada a tabela')
        else:
            await ctx.send('Erro')

    @commands.command()
    @Checks.is_owner()
    async def add_ponto_gostosa(self,ctx, id_user: int, pontuacao: int):
        if busca_gostosa(id_user):
            update_gostosa(id_user,pontuacao)
            await ctx.send('Adicionando')
        else:
            insert_gostosa(id_user,pontuacao)
            await ctx.send('Adicionando')

    @commands.command()
    @Checks.is_owner()
    async def remove_gostosa(self,ctx, id_user: int):
        if busca_gostosa(id_user):
            delete_gostosa(id_user)
            await ctx.send('Deletado')
        else:
            await ctx.send('Não há registro')

    @commands.command(name='editcredito', aliases=['editcreditos','editsaldo'])
    @Checks.is_owner()
    async def editcredito(self,ctx, Member: Checks.Busca_User, credito: int):
        if Member.bot == False:
            edit_user(Member.id,credito)
            await ctx.send('Editado o credito de {} para {}'.format(str(Member),credito))
        else:
            await ctx.send('O membro é um bot, por favor escolha outra pessoa')
    
    @commands.command(name='addcredito', aliases=['addcreditos','addsaldo'])
    @Checks.is_owner()
    async def addcredito(self,ctx, Member: Checks.Busca_User, credito: int):
        if Member.bot == False:
            user = busca_user_id(Member.id)
            edit_user(Member.id,user.get_qtd()+credito)
            await ctx.send('Adicionado {} creditos para {}'.format(credito,str(Member)))
        else:
            await ctx.send('O membro é um bot, por favor escolha outra pessoa')
            
def setup(bot):
    bot.add_cog(Owner(bot))
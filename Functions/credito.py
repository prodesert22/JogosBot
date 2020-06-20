import discord
import re
from Functions.banco import busca_user_id,edit_user

def gerar_embed_credito(user,autor):
      u = busca_user_id(user.id)
      if (autor == False):
            if(user.nick):
                  titulo = "Total de créditos de {}".format(user.nick)
            else:
                  titulo = "Total de créditos de {}".format(user.name)
      else:
            titulo = "Total de créditos: "
      emb = discord.Embed(
            title = titulo,
            description = ":credit_card: {} créditos".format(int(u.get_qtd())),
            colour = discord.Colour.green()
            )
      emb.set_author(name='{}'.format(user.name),icon_url='{}'.format(user.avatar_url))
      return emb

def transferir(id_user,id_user2,creditos):
    user1 = busca_user_id(id_user)
    user2 = busca_user_id(id_user2)
    edit_user(id_user,user1.get_qtd()-creditos)
    edit_user(id_user2,user2.get_qtd()+creditos)

import discord
import random 
import time
from Functions.banco import busca_user_id,edit_user

#:jack_o_lantern:
#slot = [(':jack_o_lantern:',100),(':grapes:',70),(':cherries:',50),(':dollar:',30),(':moneybag:',15),(':gem:',10),('<:sete:629450359412097024>',5)]
#slot2 = (':jack_o_lantern:',':grapes:',':cherries:',':dollar:',':moneybag:',':gem:','<:sete:629450359412097024>')

#:tangerine:
slot = [(':tangerine:',29),(':grapes:',20),(':cherries:',16),(':dollar:',13),(':moneybag:',10),(':gem:',7),('<:sete:629450359412097024>',3)]
slot2 = (':tangerine:',':grapes:',':cherries:',':dollar:',':moneybag:',':gem:','<:sete:629450359412097024>')

def valor(v,creditos):
      if (v == 0):
            creditos /= 2
            creditos = int(round(creditos,0)) 
      elif (v == 1):
            creditos *=2
      elif (v == 2):
            creditos *=3
      elif (v == 3):
            creditos *=5
      elif (v == 4):
            creditos *=10
      elif (v ==5):
            creditos *=20
      elif (v ==6):
            creditos =0
      return creditos

def gerar_valores(creditos,id_user):
      credito = creditos
      user2 = busca_user_id(id_user)
      edit_user(id_user,user2.get_qtd()-creditos)
      prize_list = [prize for prize, weight in slot for i in range(weight)]
      x1 = slot2.index(random.choice(prize_list))
      x2 = slot2.index(random.choice(prize_list))
      x3 = slot2.index(random.choice(prize_list))
      if (x1 == x2) or (x1 == x3) or (x2 == x3):
            if (x1 == x2) and (x1 == x3) and (x3 == x2):
                  if (x1==6):
                        credito *=100
                  elif (x1==0):
                        credito /= 2
                        credito = int(round(credito,0)) 
                  elif (x1==1):
                        credito *=2
                  elif (x1==2): 
                        credito *=6
                  elif (x1==3): 
                        credito *=15
                  elif (x1==4): 
                        credito *=25
                  elif (x1==5): 
                        credito *=40
                  resultado = ["",credito-creditos,x1,x2,x3]
            elif (x1 == x2): 
                  credito = valor(x1,credito)
            elif (x1 == x3):
                  credito = valor(x1,credito)
            elif (x2 == x3):
                  credito = valor(x2,credito)
            lucro = credito-creditos
            resultado = ["",lucro,x1,x2,x3]
            user2 = busca_user_id(id_user)
            edit_user(id_user,user2.get_qtd()+credito) 
      else:
            lucro = -1*creditos
            resultado = ["",lucro,x1,x2,x3]
      if (lucro <0):
            resultado[0]= "Você Perdeu"
      elif(lucro>0):
            resultado[0]= "Você Ganhou"
      else:
            resultado[0]= "Não Perdeu e nem Ganhou"

      user2 = busca_user_id(id_user)
      resultado.append(int(user2.get_qtd()))
      return resultado

async def maquina(credito,message,canal):
      id_user = message.author.id
      emb = discord.Embed(
            title = ":slot_machine: Máquina caça-níquel :slot_machine:",
            description = "",
            colour = discord.Colour.green()
      )
      emb.set_author(name='{}'.format(message.author.name),icon_url='{}'.format(message.author.avatar_url))
      texto = '--------------------- \n| <a:slots:629426697686482995> | <a:slots:629426697686482995> | <a:slots:629426697686482995> |\n---------------------'
      emb.add_field(name='RODANDO', value=texto, inline=False)
      msg = await canal.send(embed=emb)
      ###############################
      result = gerar_valores(credito,id_user)
      ###############################
      emb.set_field_at(0,name='RODANDO', value='--------------------- \n| {} | <a:slots:629426697686482995> | <a:slots:629426697686482995> |\n---------------------'.format(slot2[result[2]]), inline=False)
      time.sleep(1)
      await msg.edit(embed=emb)
      texto = '--------------------- \n| {} | {} | <a:slots:629426697686482995> |\n---------------------'.format(slot2[result[2]],slot2[result[3]]) 
      emb.set_field_at(0,name='RODANDO', value=texto, inline=False)
      time.sleep(1)
      await msg.edit(embed=emb)
      texto = '--------------------- \n| {} | {} | {} |\n---------------------'.format(slot2[result[2]],slot2[result[3]],slot2[result[4]])
      emb.set_field_at(0,name='RODANDO', value=texto, inline=False)
      time.sleep(1)
      texto = '--------------------- \n| {} | {} | {} |\n---------------------\n {}'.format(slot2[result[2]],slot2[result[3]],slot2[result[4]],result[0])
      emb.set_field_at(0,name='Resultado', value=texto, inline=False)
      if (result[1]<0):
             emb.add_field(name='Prejuízo', value='{} créditos'.format(result[1]), inline=True)
      else:
            emb.add_field(name='Lucro', value='{} créditos'.format(result[1]), inline=True)
      emb.add_field(name='Novo Saldo', value='{} créditos'.format(result[5]), inline=True)
      await msg.edit(embed=emb)
      if(result[2] == result[3] and result[4] == result[3] and result[3] == 6):
            await canal.send("temos um cagado no grupo")

def fn_gerar_embed_credito(id_user,guilda,autor):
      user = guilda.get_member(id_user)
      result = busca_user_id(id_user)
      if (autor == False):
            if(user.nick):
                  titulo = "Total de créditos de {}".format(user.nick)
            else:
                  titulo = "Total de créditos de {}".format(user.name)
      else:
            titulo = "Total de créditos: "
      emb = discord.Embed(
            title = titulo,
            description = ":credit_card: {} créditos".format(result.get_qtd()),
            colour = discord.Colour.green()
            )
      emb.set_author(name='{}'.format(user.name),icon_url='{}'.format(user.avatar_url))
      return emb

def fn_verifica_bot(id_u,guilda):
      user = guilda.get_member(id_u)
      if(user.bot == True):
            return True
      else:
            return False
import sqlite3
import datetime
import os

from .Classes import User,Galo

PATH_DB = os.path.join('Data','database.db')

try:
      db = sqlite3.connect(PATH_DB)
      print('Conectado com sucesso')
      cursor = db.cursor()
except Exception as e :
      print(e)
      print('Erro ao conectar') 

def busca_ban(id_user,guilda):
      cursor.execute('''SELECT * FROM ban WHERE id_user = ? and guilda = ? ;''',(id_user,guilda)) 
      resultado = cursor.fetchone()
      if(resultado):
            return True
      else:
            return False

def insert_ban(id_user,guilda):
      try:      
            cursor.execute('''INSERT INTO ban(id_user, guilda) VALUES (?,?)''',(id_user,guilda))
            db.commit()
      except Exception as e:
            print(e)
      
def delete_ban(id_user,guilda):
      try:      
            cursor.execute('''DELETE FROM ban WHERE id_user = ? and guilda = ?''',(id_user,guilda))
            db.commit()
      except Exception as e:
            print(e)

def busca_user_id(id_user):
      padrao = 1000
      if(id_user == 207294581266579457):
                  padrao = 2077
      resultado = []
      try:
            cursor.execute('''SELECT * FROM user WHERE id_user = ? ;''',(id_user,)) 
            resultado = cursor.fetchone()
            if(not resultado):
                  fn_insert_user(id_user)
                  resultado = [id_user,padrao]
      except Exception as e:
            print(e)
            print('Erro em selecionar')
            if(not resultado):
                  fn_insert_user(id_user)
                  resultado = [id_user,padrao]
      resultado = User(resultado[0],resultado[1])
      return resultado  

def fn_insert_user(id_user):
      padrao = 1000
      try:    
            if(id_user == 207294581266579457):
                  padrao = 2077
            cursor.execute('''INSERT INTO user(id_user, credito) VALUES (?,?)''', (id_user,padrao))
            db.commit()
      except Exception as e:
            print(e)
            print('Erro em inserir usuario')

def edit_user(id_user,creditos):
      padrao = 1000
      try:
            cursor.execute('''UPDATE user SET credito = ? WHERE id_user = ?''',(creditos,id_user))
            db.commit()
      except Exception as e:
            print(e)
            if(id_user == 207294581266579457):
                  padrao = 2077
            cursor.execute('''INSERT INTO user(id_user, credito) VALUES (?,?)''', (id_user,padrao))
            db.commit()

def fncooldown(id_user,comando):
      lista = list()
      dataatual = datetime.datetime.now()
      segundos = 0
      cursor.execute('''SELECT * FROM COOLDOWN WHERE id_user = ? and comando = ?;''', (id_user,comando))
      resultado = cursor.fetchone()
      if(not resultado):
            cursor.execute('''INSERT INTO COOLDOWN(id_user, comando, data) VALUES (?,?,?)''', (id_user,comando,dataatual))
            db.commit()
            lista=[False,0]
      else:
            time = datetime.datetime.strptime(resultado[2], '%Y-%m-%d %H:%M:%S.%f')
            segundos = dataatual.timestamp()-time.timestamp()
            segundos = int(segundos)
            if(segundos <= 86400):
                  lista=[True,segundos]
            else:
                  cursor.execute('''UPDATE COOLDOWN SET data = ? WHERE id_user = ? and comando = ?''',(dataatual,id_user,comando))
                  db.commit()
                  lista=[False,0]
      return lista

def fn_delete_cd(id_user,comando):
      try:      
            cursor.execute('''DELETE FROM COOLDOWN WHERE id_user = ? and comando = ?''',(id_user, comando))
            db.commit()
      except Exception as e:
            print(e)

def fncooldown_jb(id_user,comando,tempo):
      lista = list()
      dataatual = datetime.datetime.now()
      segundos = 0
      cursor.execute('''SELECT * FROM COOLDOWN WHERE id_user = ? and comando = ?;''', (id_user,comando))
      resultado = cursor.fetchone()
      if(not resultado):
            cursor.execute('''INSERT INTO COOLDOWN(id_user, comando, data) VALUES (?,?,?)''', (id_user,comando,dataatual))
            db.commit()
            lista=[False,0]
      else:
            time = datetime.datetime.strptime(resultado[2], '%Y-%m-%d %H:%M:%S.%f')
            segundos = dataatual.timestamp()-time.timestamp()
            segundos = int(segundos)
            if(segundos <= tempo):
                  lista=[True,segundos]
            else:
                  cursor.execute('''UPDATE COOLDOWN SET data = ? WHERE id_user = ? and comando = ?''',(dataatual,id_user,comando))
                  db.commit()
                  lista=[False,0]
      return lista

def fnselect_cd_jb(guilda):
      cursor.execute('''SELECT * FROM COOLDOWN WHERE id_user = ?;''',(guilda,))
      resultado = cursor.fetchone()
      return resultado

def fn_delete_cd_jb(guilda,comando):
      try:      
            cursor.execute('''DELETE FROM COOLDOWN WHERE id_user = ? and comando = ?''',(guilda, comando))
            db.commit()
      except Exception as e:
            print(e)

def fncont(id_user,comando,cont):
      lista = list()
      cursor.execute('''SELECT * FROM cont WHERE id_user = ? and comando = ?;''', (id_user,comando))
      resultado = cursor.fetchone()
      if(not resultado):
            cursor.execute('''INSERT INTO cont(id_user,comando,cont) VALUES (?,?,?)''', (id_user,comando,1))
            db.commit()
            lista=[False,0]
      else:
            if(resultado[1]<cont):
                  lista=[False,0]
                  cont = resultado[1]+1
                  cursor.execute('''UPDATE cont SET cont = ? WHERE id_user = ? and comando = ?''',(cont,id_user,comando))
                  db.commit()
            else:
                  lista=[True,resultado[1]]
      return lista
      
def fn_update_cont(id_user,comando):
      cursor.execute('''UPDATE cont SET cont = ? WHERE id_user = ? and comando = ?''',(1,id_user,comando))
      db.commit()


def busca_users(guilda):
      lista_user = list()
      lista_busca = list()
      try:  
            for row in cursor.execute('SELECT * FROM user ORDER BY credito DESC'):
                  lista_busca.append(User(row[0],row[1]))            
            cont_achados = 0
            for busca in lista_busca:
                  id_user = busca.get_id()
                  id_user = int(id_user)
                  if(guilda.get_member(id_user)):
                        guilda.get_member(id_user)
                        lista_user.append(User(busca.get_id(),busca.get_qtd()))
                        cont_achados +=1
                  if(cont_achados == 10):
                        break
            return lista_user
      except:
            return lista_user

def busca_top_gostosas():
      lista_gostosas = list()
      try:
            for row in cursor.execute('SELECT * FROM gostosa ORDER BY quantidade DESC'):
                  lista_gostosas.append(User(row[0],row[1]))
            return lista_gostosas
      except Exception as e:
            print(e)
            return None

def update_gostosa(id_user,quantidade):
      try:
            cursor.execute('''UPDATE gostosa SET quantidade = ? WHERE id_user = ?''',(quantidade,id_user))
            db.commit()
      except Exception as e:
            print(e)

def insert_gostosa(id_user):
      try:      
            cursor.execute('INSERT INTO gostosa(id_user, quantidade) VALUES (?,?)',(id_user,1))
            db.commit()
      except Exception as e:
            print(e)
            print('Erro em inserir gostosa')

def busca_gostosa(id_user):
      cursor.execute('SELECT * FROM gostosa WHERE id_user = ? ;',(id_user,))
      resultado = cursor.fetchone()
      if(resultado):
            return resultado
      else:
            return None

def busca_top_burros():
      lista_burros = list()
      try:
            for row in cursor.execute('SELECT * FROM burro ORDER BY quantidade DESC'):
                  lista_burros.append(User(row[0],row[1]))
            return lista_burros
      except Exception as e:
            print(e)
            return None
      
def insert_burrice(id_user):
      try:      
            cursor.execute('INSERT INTO burro(id_user, quantidade) VALUES (?,?)',(id_user,1))
            db.commit()
      except Exception as e:
            print(e)
            print('Erro em inserir galo')

def update_burrice(id_user,quantidade):
      try:
            cursor.execute('''UPDATE burro SET quantidade = ? WHERE id_user = ?''',(quantidade,id_user))
            db.commit()
      except Exception as e:
            print(e)

def busca_burrice(id_user):
      cursor.execute('SELECT * FROM burro WHERE id_user = ? ;',(id_user,))
      resultado = cursor.fetchone()
      if(resultado):
            return resultado
      else:
            return None

def busca_galos(guilda):
      lista_user = list()
      lista_busca = list()
      try:  
            for row in cursor.execute('SELECT * FROM galo ORDER BY forca DESC'):
                  lista_busca.append(Galo(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11],row[12],row[13],row[14]))            
            cont_achados = 0
            for busca in lista_busca:
                  id_user = busca.get_id()
                  id_user = int(id_user)
                  if(guilda.get_member(id_user)):
                        lista_user.append(busca)
                        cont_achados +=1
                  if(cont_achados == 10):
                        break
            return lista_user
      except:
            return lista_user

def update_galos():
      lista = list()
      try:
            for row in cursor.execute('SELECT * FROM galo ORDER BY forca DESC'):
                  lista.append(row)
            for row in lista:
                  if(row[3] is None):
                        print(row)
                        vida = row[2] *2
                        defesa = int(row[2] /10)
                        print(defesa,vida)
                        update(row[0],vida,defesa)
            db.commit()
      except Exception as e:
            print(e)

def update(id_user,vida,defesa):
      try:
            cursor.execute('''UPDATE galo SET vida = ? ,defesa = ? ,id_item1 = 0 ,id_item2 = 0 ,move1 = 1 ,move2 = 2, move3 = 3 ,move4 = 4 WHERE id_user = ?''',(vida, defesa,id_user))
      except Exception as e:
            print(e)

def fn_insert_item(id_user, id_item):
      try:      
            cursor.execute('''INSERT INTO itens_comprados(id_user, id_item) VALUES (?,?,?)''', (id_user, id_item))
            db.commit()
            #print('Novo galo, dados inseridos com sucesso.')
      except Exception as e:
            print(e)
            print('Erro em inserir galo')

def fn_busca_item(id_user, id_item):
      cursor.execute('''SELECT * FROM itens_comprados WHERE id_user = ? and id_item = ?;''', (id_user, id_item))
      resultado = cursor.fetchone()
      if(resultado):
            return True
      else:
            return False

def fn_busca_galo(id_user):
      galo = ''
      cursor.execute('''SELECT * FROM galo WHERE id_user = ?;''',(id_user,)) 
      row = cursor.fetchone()
      if(row):
            Item1 = 0
            Item2 = 0
            if(row[9] != 0):
                  Item1 = fn_busca_item_rinha(row[9])
            if(row[10] != 0):
                  Item2 = fn_busca_item_rinha(row[10])
            galo = Galo(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],Item1,Item2,row[11],row[12],row[13],row[14])
            return galo
      else:
            return None

def fn_inserir_galo(id_user, nome, img):
      try:      
            cursor.execute('''INSERT INTO galo(id_user, level, forca, img, nome, vitorias, xp, defesa, vida, move1, move2, move3, move4, id_item1, id_item2) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)''', (id_user, 1, 1, img, nome, 0, 0, 1, 10, 1, 2, 3, 4, -1, -1))
            db.commit()
      except Exception as e:
            print(e)
            print('Erro em inserir galo')

def fn_update_galo_level(level, xp, id_user):
      try:
            cursor.execute('''UPDATE galo SET level = ? ,xp = ? WHERE id_user = ?''',(level, xp, id_user))
            db.commit()
      except Exception as e:
            print(e)

def fn_update_galo_xp(xp, id_user):
      try:
            cursor.execute('''UPDATE galo SET xp = ? WHERE id_user = ?''',(xp, id_user))
            db.commit()
      except Exception as e:
            print(e)

def fn_update_galo_nome(id_user,nome):
      error = True
      try:
            cursor.execute('''UPDATE galo SET nome = ? WHERE id_user = ?''',(nome, id_user))
            db.commit()
      except Exception as e:
            print(e)
      return error

def fn_update_galo_img(img, id_user):
      try:
            cursor.execute('''UPDATE galo SET img = ? WHERE id_user = ?''',(img, id_user))
            db.commit()
      except Exception as e:
            print(e)

def fn_update_galo_vitorias(vitorias, id_user):
      try:
            cursor.execute('''UPDATE galo SET vitorias = ? WHERE id_user = ?''',(vitorias, id_user))
            db.commit()
      except Exception as e:
            print(e)

def fn_update_atributos(forca, defesa, vida, id_user):
      try:
            cursor.execute('''UPDATE galo SET forca = ?, defesa = ?, vida = ? WHERE id_user = ?''',(forca, defesa, vida, id_user))
            db.commit()
      except Exception as e:
            print(e)

def fn_update_movimento_galo(move, id_move, id_user):
      try:
            if(move == 1):
                  cursor.execute('''UPDATE galo SET move1 = ? WHERE id_user = ?;''',(id_move, id_user)) 
                  db.commit
            elif(move == 2):
                  cursor.execute('''UPDATE galo SET move2 = ? WHERE id_user = ?;''',(id_move, id_user)) 
                  db.commit
            elif(move == 2):
                  cursor.execute('''UPDATE galo SET move3 = ? WHERE id_user = ?;''',(id_move, id_user)) 
                  db.commit
            else:
                  cursor.execute('''UPDATE galo SET move4 = ? WHERE id_user = ?;''',(id_move, id_user)) 
                  db.commit
      except Exception as e:
            print(e)

def fn_update_item_equipado(id_user, item, id_item):
      try:  
            if(item == 1):
                  cursor.execute('''UPDATE galo SET id_item1 = ? WHERE id_user = ?;''',(id_item, id_user)) 
                  db.commite
            else:
                  cursor.execute('''UPDATE galo SET id_item2 = ? WHERE id_user = ?;''',(id_item, id_user)) 
                  db.commite
      except Exception as e:
            print(e)

def fn_insert_item_rinha(id_item, nome, descricao, forca, defesa, vida):
      try:      
            cursor.execute('''INSERT INTO item(id, nome, descricao, forca, defesa, vida) VALUES (?,?,?,?,?,?)''', (id_item, nome, descricao, forca, defesa, vida))
            db.commit()
      except Exception as e:
            print(e)

def fn_busca_item_rinha(id_item):
      try:
            cursor.execute('''SELECT * FROM item WHERE id_item = ?;''',(id_item,))
            row = cursor.fetchone()
            if(row):
                  Item = Item(id_item,row[1],row[2],row[3],row[4],row[5],row[6])
                  return Item
            else:
                  return None
      except Exception as e:
            print(e)

def fn_selec_movimento_rinha(id_move):
      try:
            cursor.execute('''SELECT * FROM movimentos WHERE id = ?;''',(id_move,)) 
            resultado = cursor.fetchone()
            if(resultado):
                  return resultado
            else:
                  return None
      except Exception as e:
            print(e)

def fn_busca_canal(guilda):
      try:
            cursor.execute('''SELECT * FROM canal_bicho WHERE guilda = ?;''',(guilda,)) 
            resultado = cursor.fetchone()
            if(resultado):
                  return resultado
            else:
                  return None
      except Exception as e:
            print(e)

def fn_inserir_canal(guilda_id, canal_id):
      try:      
            cursor.execute('''INSERT INTO canal_bicho(guilda, canal) VALUES (?,?)''', (guilda_id,canal_id))
            db.commit()
      except Exception as e:
            print(e)

def fn_update_canal(guilda_id, canal_id):
      try:
            cursor.execute('''UPDATE canal_bicho SET canal = ? WHERE guilda = ?''',(canal_id, guilda_id))
            db.commit()
      except Exception as e:
            print(e)

def fn_inserir_jogo(guilda_id, canal_id, message_id, inicio):
      try:      
            cursor.execute('''INSERT INTO jogo_bicho(guilda, canal, inicio, menssagem) VALUES (?,?,?,?)''', (guilda_id, canal_id, inicio, message_id))
            db.commit()
      except Exception as e:
            print(e)

def fn_busca_jogo(guilda, canal, message):
      cursor.execute('''SELECT * FROM jogo_bicho WHERE guilda = ? and canal = ? and menssagem = ?;''', (guilda,canal,message))
      resultado = cursor.fetchone()
      if(resultado):
            return resultado
      else:
            return None

def fn_busca_tem_jogo(guilda):
      cursor.execute('''SELECT * FROM jogo_bicho WHERE guilda = ?;''',(guilda,))
      resultado = cursor.fetchone()
      if(resultado):
            return resultado
      else:
            return None

def fn_delete_jogo(guilda):
      try:      
            cursor.execute('''DELETE FROM jogo_bicho WHERE guilda = ?''',(guilda,))
            db.commit()
      except Exception as e:
            print(e)

def fn_b_jogo_user(guilda,id_user):
      cursor.execute('''SELECT * FROM usuarios_jogo WHERE guilda = ? and id_user = ?;''', (guilda,id_user))
      resultado = cursor.fetchall()
      if(resultado):
            return resultado
      else:
            return None

def fn_bs_jogo_user(guilda):
      cursor.execute('''SELECT DISTINCT id_user FROM usuarios_jogo WHERE guilda = ? ;''',(guilda,))
      resultado = cursor.fetchall()
      if(resultado):
            return resultado
      else:
            return None

def fn_b_jogo_user_bicho(guilda,bicho):
      cursor.execute('''SELECT * FROM usuarios_jogo WHERE guilda = ? and bicho = ?;''',(guilda,bicho))
      resultado = cursor.fetchall()
      if(resultado):
            return resultado
      else:
            return None

def fn_i_jogo_user(guilda,id_user,bicho):
      try:      
            cursor.execute('''INSERT INTO usuarios_jogo(guilda, id_user, bicho) VALUES (?,?,?)''', (guilda, id_user, bicho))
            db.commit()
      except Exception as e:
            print(e)

def fn_u_jogo_user(guilda,id_user,bicho):
      try:      
            cursor.execute('''UPDATE usuarios_jogo SET bicho = ? WHERE guilda = ? and id_user = ?''',(bicho, guilda, id_user))
            db.commit()
      except Exception as e:
            print(e)

def fn_d_jogo_user(guilda, id_user, bicho):
      try:      
            cursor.execute('''DELETE FROM usuarios_jogo WHERE guilda = ? and id_user = ? and bicho = ?''',(guilda, id_user, bicho))
            db.commit()
      except Exception as e:
            print(e)

def fn_d_all_guild_jogo_user(guilda):
      try:
            cursor.execute('''DELETE FROM usuarios_jogo WHERE guilda = ?''',(guilda,))
            db.commit()
      except Exception as e:
            print(e)

def busca_prefix(id_guilda):
    cursor.execute('''SELECT prefix FROM Prefix WHERE id = ?;''',(id_guilda,))
    resultado = cursor.fetchone()
    if(resultado):
        return resultado
    else:
        return None

def insert_prefix(id_guilda,prefix):
      try:      
            cursor.execute('''INSERT INTO prefix(id, prefix) VALUES (?,?)''', (id_guilda, prefix))
            db.commit()
      except Exception as e:
            print(e)

def update_prefix(id_guild,prefix):
      try:      
            cursor.execute('''UPDATE Prefix SET prefix = ? WHERE id = ?''',(prefix, id_guild))
            db.commit()
      except Exception as e:
            print(e)

def delete_prefix(id_guild):
      try:      
            cursor.execute('''DELETE FROM Prefix WHERE id = ?''',(id_guild))
            db.commit()
      except Exception as e:
            print(e)
import asyncio
import copy
import discord
import numpy as np
import random

levels = dict([('1',[5,7]),('2',[7,7]),('3',[7,8]),('4',[9,9])])

#Objetos
#Parede : -1
#Vazio : 0
#Player : 1 
#Caixa : 2
#Posiçoes 3

class Pos():
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def set_x(self,x):
        self.x = x 

    def set_y(self,y):
        self.y = y

class Player(Pos):
    def __init__(self, x, y):
        super().__init__(x, y)

class Caixa(Pos):
    def __init__(self, x, y):
        super().__init__(x, y)

class Local(Pos):
    def __init__(self, x, y):
        super().__init__(x, y)

async def sokoban_game(ctx,message,bot,level):
    ganhou = False
    m, player, caixas, locais = calc_matriz(level)
    m_inicial = m.copy()
    p_inicial = copy.copy(player)
    c_inicial = caixas.copy()
    l_inicial = locais.copy()
    emb = discord.Embed(
        title = "Jogando o SokoBan:",
        description = "Reaja com:\n⬅️ ir para esquerda \n➡️ ir para direita\
        \n⬆️ ir para baixo \n⬇️ ir para baixo \n🔄 para reinicar o nivel\n🇶 Para sair",
        colour = discord.Colour.green()
    )
    movimentos = 40
    emb.add_field(name='Movimentos restantes', value=movimentos, inline=True)
    await message.add_reaction('⬅️')
    await message.add_reaction('➡️')
    await message.add_reaction('⬆️')
    await message.add_reaction('⬇️')
    await message.add_reaction('🔄')
    await message.add_reaction('🇶')
    await message.edit(content= formata_matriz(m,level),embed=emb)
    l = str(level)
    info = levels[l]
    altura = info[0]
    largura = info[1]
    while True:
        def check(reaction, user):
            return reaction.message.id == message.id and (str(reaction.emoji) == '⬅️' or str(reaction.emoji) == '➡️' or str(reaction.emoji) == '⬆️' or str(reaction.emoji) == '⬇️' or str(reaction.emoji) == '🔄' or str(reaction.emoji) == '🇶')and not user.bot == True and user.id == ctx.message.author.id
        try:
            r = await bot.wait_for('reaction_add', check=check, timeout=30)
        except asyncio.TimeoutError:
            emb = discord.Embed(
                title = "Fim de jogo",
                description = 'Tempo esgotou.',
                colour = discord.Colour.blue()
            )
            await message.clear_reactions()
            await message.edit(content=' ',embed=emb)
            break
        cima, baixo, esquerda, direita, index_c, index_b, index_e, index_d = tem_caixa_lado(player,caixas)
        local_atual, _ = find(lambda local: local.get_y() == player.get_y() and local.get_x() == player.get_x(), locais)
        if(str(r[0].emoji) == '⬅️'):
            await message.remove_reaction('⬅️',ctx.message.author)
            #verifica se tem parede
            if(player.get_x()-1 == 0):
                continue
            else:
                #verifica se tem caixa na esquerda e se ela ta colada na parede ou tem outra caixa
                if(esquerda is not None):
                    if(m[esquerda.get_y(),esquerda.get_x()-1] == 0 or m[esquerda.get_y(),esquerda.get_x()-1] == 3):
                        esquerda.set_x(esquerda.get_x()-1)
                        m[esquerda.get_y(),esquerda.get_x()] = 2
                        caixas.pop(index_e)
                        caixas.append(esquerda)
                        player.set_x(player.get_x()-1)
                        m[player.get_y(),player.get_x()] = 1
                        if(local_atual is None):
                            m[player.get_y(),player.get_x()+1] = 0
                        else:
                            m[player.get_y(),player.get_x()+1] = 3
                        texto = formata_matriz(m,level)
                        movimentos -= 1
                        emb.set_field_at(index=0,name='Movimentos restantes', value=movimentos, inline=True)
                        await message.edit(content=texto,embed=emb)
                    else:
                        continue
                else:
                    player.set_x(player.get_x()-1)
                    m[player.get_y(),player.get_x()] = 1
                    if(local_atual is None):
                        m[player.get_y(),player.get_x()+1] = 0
                    else:
                        m[player.get_y(),player.get_x()+1] = 3
                    texto = formata_matriz(m,level)
                    movimentos -= 1
                    emb.set_field_at(index=0,name='Movimentos restantes', value=movimentos, inline=True)
                    await message.edit(content=texto,embed=emb)
        elif(str(r[0].emoji) == '➡️'):
            await message.remove_reaction('➡️',ctx.message.author)
            #verifica se tem parede
            if(m[player.get_y(),player.get_x()+1] == -1):
                continue
            else:
                #verifica se tem caixa na direita e se ela ta colada na parede
                if(direita is not None):
                    if(m[direita.get_y(),direita.get_x()+1] == 0 or m[direita.get_y(),direita.get_x()+1] == 3):
                        direita.set_x(direita.get_x()+1)
                        m[direita.get_y(),direita.get_x()] = 2
                        caixas.pop(index_d)
                        caixas.append(direita)
                        player.set_x(player.get_x()+1)
                        m[player.get_y(),player.get_x()] = 1
                        if(local_atual is None):
                            m[player.get_y(),player.get_x()-1] = 0
                        else:
                            m[player.get_y(),player.get_x()-1] = 3
                        texto = formata_matriz(m,level)
                        movimentos -= 1
                        emb.set_field_at(index=0,name='Movimentos restantes', value=movimentos, inline=True)
                        await message.edit(content=texto,embed=emb)
                    else:
                        continue           
                else:
                    player.set_x(player.get_x()+1)
                    m[player.get_y(),player.get_x()] = 1
                    if(local_atual is None):
                        m[player.get_y(),player.get_x()-1] = 0
                    else:
                        m[player.get_y(),player.get_x()-1] = 3
                    texto = formata_matriz(m,level)
                    movimentos -= 1
                    emb.set_field_at(index=0,name='Movimentos restantes', value=movimentos, inline=True)
                    await message.edit(content=texto,embed=emb)
        elif(str(r[0].emoji) == '⬆️'):
            await message.remove_reaction('⬆️',ctx.message.author)
            #verifica se tem parede
            if(player.get_y()-1 == 0):
                continue
            else:
                #verifica se tem caixa em cima e se ela ta colada na parede
                if(cima is not None):
                    if(m[cima.get_y()-1,cima.get_x()] == 0 or m[cima.get_y()-1,cima.get_x()] == 3):
                        cima.set_y(cima.get_y()-1)
                        m[cima.get_y(),cima.get_x()] = 2
                        caixas.pop(index_c)
                        caixas.append(cima)
                        player.set_y(player.get_y()-1)
                        m[player.get_y(),player.get_x()] = 1
                        if(local_atual is None):
                            m[player.get_y()+1,player.get_x()] = 0
                        else:
                            m[player.get_y()+1,player.get_x()] = 3
                        texto = formata_matriz(m,level)
                        movimentos -= 1
                        emb.set_field_at(index=0,name='Movimentos restantes', value=movimentos, inline=True)
                        await message.edit(content=texto,embed=emb)
                    else:
                        continue     
                else:
                    player.set_y(player.get_y()-1)
                    m[player.get_y(),player.get_x()] = 1
                    if(local_atual is None):
                        m[player.get_y()+1,player.get_x()] = 0
                    else:
                        m[player.get_y()+1,player.get_x()] = 3
                    texto = formata_matriz(m,level)
                    movimentos -= 1
                    emb.set_field_at(index=0,name='Movimentos restantes', value=movimentos, inline=True)
                    await message.edit(content=texto,embed=emb)
        elif(str(r[0].emoji) == '⬇️'):
            await message.remove_reaction('⬇️',ctx.message.author)
            #verifica se tem parede
            if(m[player.get_y()+1,player.get_x()] == -1):
                continue  
            else:
                #verifica se tem caixa em baixo e se ela ta colada na parede
                if(baixo is not None):
                    if(m[baixo.get_y()+1,baixo.get_x()] == 0 or m[baixo.get_y()+1,baixo.get_x()] == 3):
                        baixo.set_y(baixo.get_y()+1)
                        m[baixo.get_y(),baixo.get_x()] = 2
                        caixas.pop(index_b) 
                        caixas.append(baixo)
                        player.set_y(player.get_y()+1)
                        m[player.get_y(),player.get_x()] = 1
                        if(local_atual is None):
                            m[player.get_y()-1,player.get_x()] = 0
                        else:
                            m[player.get_y()-1,player.get_x()] = 3
                        texto = formata_matriz(m,level)
                        movimentos -= 1
                        emb.set_field_at(index=0,name='Movimentos restantes', value=movimentos, inline=True)
                        await message.edit(content=texto,embed=emb)
                    else:
                        continue                 
                else:
                    player.set_y(player.get_y()+1)
                    m[player.get_y(),player.get_x()] = 1
                    if(local_atual is None):
                        m[player.get_y()-1,player.get_x()] = 0
                    else:
                        m[player.get_y()-1,player.get_x()] = 3
                    texto = formata_matriz(m,level)
                    movimentos -= 1
                    emb.set_field_at(index=0,name='Movimentos restantes', value=movimentos, inline=True)
                    await message.edit(content=texto,embed=emb)
        elif(str(r[0].emoji) == '🔄'):
            #Reinicia o level
            m = m_inicial.copy()
            caixas = c_inicial.copy()
            locais = l_inicial.copy()
            player = copy.copy(p_inicial)
            movimentos = 40
            emb.set_field_at(index=0,name='Movimentos restantes', value=movimentos, inline=True)
            await message.remove_reaction('🔄',ctx.message.author)
            await message.edit(content=formata_matriz(m_inicial,level),embed=emb)
        elif(str(r[0].emoji) == '🇶'):
            emb = discord.Embed(
                title = "Fim de jogo",
                description = 'Você saiu.',
                colour = discord.Colour.blue()
            )
            await message.clear_reactions()
            await message.edit(content=' ',embed=emb)
            break
        else:
            continue

        if(verifica_ganhou(caixas,locais,level)):
            emb = discord.Embed(
                title = "Fim de jogo",
                description = 'Você ganhou.',
                colour = discord.Colour.blue()
            )
            await message.clear_reactions()
            await message.edit(content=' ',embed=emb)
            ganhou = True
            break
        elif(movimentos == 0):
            emb = discord.Embed(
                title = "Fim de jogo",
                description = 'Você perdeu, excedeu o limite de movimentos.',
                colour = discord.Colour.blue()
            )
            await message.clear_reactions()
            await message.edit(content=' ',embed=emb)
            break
        else:
            continue
    return ganhou

def verifica_ganhou(caixas,locais,level):
    certos = 0
    for c in caixas:
        for l in locais:
            if(c.get_x() == l.get_x() and c.get_y() == l.get_y()):
                certos += 1
            else:
                continue
    return certos == level

def find(predicate,seq):
    for index, element in enumerate(seq):
        if predicate(element):
            return copy.copy(element), index
    return None,0

def tem_caixa_lado(player,caixas):
    cima = baixo = esquerda = direita = None
    index_c = index_b = index_e = index_d = 0
    esquerda, index_e = find(lambda caixa: caixa.get_y() == player.get_y() and caixa.get_x() == player.get_x()-1, caixas)
    direita, index_d = find(lambda caixa: caixa.get_y() == player.get_y() and caixa.get_x() == player.get_x()+1, caixas)
    cima, index_c = find(lambda caixa: caixa.get_y() == player.get_y()-1 and caixa.get_x() == player.get_x(), caixas)
    baixo, index_b = find(lambda caixa: caixa.get_y() == player.get_y()+1 and caixa.get_x() == player.get_x(), caixas)
    return cima, baixo, esquerda, direita, index_c, index_b, index_e, index_d

def formata_matriz(m, level):
    l = str(level)
    info = levels[l]
    altura = info[0]
    largura = info[1]
    texto = ''
    for i in range(altura):
        linha = m[i]
        for j in range(largura):
            if linha[j] == -1:
                texto += '<:stone:803630989712687105>'
            elif linha[j] == 0:
                texto += '⬛'
            elif linha[j] == 1:
                texto += '<:steve:803629871158657044>'
            elif linha[j] == 2:
                texto += '<:notebox:803628258846572575>'
            else:
                texto += '❎'
        texto += '\n' 
    return texto

def coloca_objeto(obj,b,altura,largura):
    alt = altura
    lar = largura
    o = obj
    if obj == 2:
        y = random.randint(2,alt-3)
        x = random.randint(2,lar-3)
    else:
        y = random.randint(1,alt-2)
        x = random.randint(1,lar-2)
    linha_atual = b[y]
    if not linha_atual[x] != 0:
        linha_atual[x] = obj
    else:
        y, x = coloca_objeto(o,b,alt,lar)
    return y,x

def calc_matriz(level):
        l = str(level)
        info = levels[l]
        altura = info[0]
        largura = info[1]
        matriz = np.zeros((altura,largura), dtype=np.float64)
        #parede de cima
        matriz[0,0:largura] = -1
        #parede da direita
        matriz[0:altura,0] = -1
        #parede da esquerda
        matriz[1:altura-1,largura-1] = -1
        #parede de baixo
        matriz[altura-1,1:largura] = -1
        py, px = coloca_objeto(1,matriz,altura,largura)
        player = Player(px,py)
        caixas = list()
        locais = list()
        for _ in range(level):
            cy, cx = coloca_objeto(2,matriz,altura,largura)
            caixas.append(Caixa(cx, cy))
            ly, lx = coloca_objeto(3,matriz,altura,largura)
            locais.append(Local(lx, ly))
        return matriz, player, caixas, locais
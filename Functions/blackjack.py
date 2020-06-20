import asyncio
import discord
import json
import random

from Functions.banco import busca_user_id,edit_user

def blackjack(dealer_hand, player_hand):
	lista = [False,False]
	if total(player_hand) == 21 and total(dealer_hand) == 21:
		lista = [True,True]
	elif total(player_hand) == 21:
		#print_results(dealer_hand, player_hand)
		lista = [True,False]
	elif total(dealer_hand) == 21:
		#print_results(dealer_hand, player_hand)
		lista = [False,True]	
	return lista

def hit(hand, hand_e, emojis,deck):
	card = deck.pop()
	if card == 11:card = "J"
	if card == 12:card = "Q"
	if card == 13:card = "K"
	if card == 14:card = "A"
	hand.append(card)
	hand_e,emojis = format_emoji(hand,hand_e,emojis)
	return hand,hand_e,emojis,deck

def verifica_player(player_hand):
    result = 0
    if total(player_hand) == 21:
        msg = "Você ganhou! Você tem um Blackjack!"
        result = 1
    elif total(player_hand) > 21:
        msg = "Você perdeu. Você estourou o limite máximo de 21 no total."
        result = -2
    else:
        msg = None
    return msg, result

def edit(ctx, msg, dealer, dealer_e, player, player_e, ant):
    emb = discord.Embed(
        title = "Jogando o Blackjack:",
        description = "Reaja com:\n🇭 para perdir mais cartas (Hit) \n🇸 para parar (Stand) \n🇶 Para se render (Perda só metade dos creditos)",
        colour = discord.Colour.green()
    )
    emb.set_author(name='{}'.format(ctx.message.author.name),icon_url='{}'.format(ctx.message.author.avatar_url))
    if(ant == 'Stand'):
        emb.add_field(name='Decisão anterior:', value='Você parou.', inline=False)
    elif(ant == 'Hit'):
        emb.add_field(name='Decisão anterior:', value='Você pediu mais cartas.', inline=False)
    if(msg is None):
        emb.add_field(name='Mão do dealer:', value='{} {} com uma carta virada'.format(dealer_e[0],dealer[0]), inline=True)
    else:
        emb.add_field(name='Mão do dealer:', value=' {} {} \nScore total de {}'.format(format_l_to_s(dealer_e),format_l_to_s(dealer),total(dealer)), inline=True)
    emb.add_field(name='Sua mão:', value='{} {} \nScore de {}'.format(format_l_to_s(player_e),format_l_to_s(player),total(player)), inline=True)
    if(msg is None):
        emb.set_footer(text='Você tem 15 segundos para responder.')
    else:
        emb.add_field(name='Resultado', value=msg, inline=False)
    return emb

def round1(deck):
	hand = []
	for i in range(2):
	    card = deck.pop()
	    if card == 11:card = "J"
	    if card == 12:card = "Q"
	    if card == 13:card = "K"
	    if card == 14:card = "A"
	    hand.append(card)
	i = i 
	return hand, deck

def total_a(total, hand):
	conta = 0
	for card in hand:
		if card == "A":
			if(hand.count("A") > 1):
				conta  = hand.count("A")
				break
			if(total>=11):
				conta+=1
			else:
				conta+=11
	return conta

def total(hand):
	total = 0
	for card in hand:
		if card == "J" or card == "Q" or card == "K":
			total += 10
		elif not card == 'A':
			total += card
	total += total_a(total,hand)
	return total

def add_emoji_card(card, emoji_hand, emojis):
    index = 'card_{}'.format(card) 
    c = emojis[index]
    random.shuffle(c)
    emoji_choice = c.pop()
    emojis[index] = c
    emoji_hand.append(emoji_choice)
    return emoji_hand, emojis

def score(dealer_hand, player_hand):
	msg = ""
	resultado = 0
	if total(player_hand) == 21 and total(dealer_hand) == 21:
		msg = "Empate! Você e o Dealer tem um blackjack."
	elif total(player_hand) == 21:
		msg = "Você ganhou! Você tem um Blackjack!"
		resultado = 1
	elif total(dealer_hand) == 21:
		msg = "Você perdeu. O dealer tem um Blackjack!"
		resultado = -2
	elif total(player_hand) > 21:
		msg = "Você perdeu. Você estourou o limite máximo de 21 no total."
		resultado = -2
	elif total(dealer_hand) > 21:
		msg = "Você ganhou! O dealer estourou o limite máximo de 21 no total."			   
		resultado = 1
	elif total(player_hand) < total(dealer_hand):
		msg = "Você perdeu. O dealer tem o score maior que o seu."
		resultado = -2
	elif total(player_hand) > total(dealer_hand):
		msg = "Você ganhou! Você tem o score maior que o do dealer."
		resultado = 1
	else:
		msg = "Empate! Você e o Dealer tem o mesmo score." 	
	return msg , resultado

def format_emoji(hand, hand_e, emojis):
    if(hand_e is None):
        emoji_hand = list()
        for card in hand:
            emoji_hand, emojis = add_emoji_card(card,emoji_hand,emojis)
            # index = 'card_{}'.format(card) 
            # c = emojis[index]
            # random.shuffle(c)
            # emoji_choice = c.pop()
            # emojis[index] = c
            # emoji_hand.append(emoji_choice)
    else:
        emoji_hand = hand_e
        if(isinstance(hand[len(hand_e):],int)):
            emoji_hand, emojis = add_emoji_card(card,emoji_hand,emojis)
        else:
            for card in hand[len(hand_e):]:
                emoji_hand, emojis = add_emoji_card(card,emoji_hand,emojis)
                # index = 'card_{}'.format(card) 
                # c = emojis[index]
                # random.shuffle(c)
                # emoji_choice = c.pop()
                # emojis[index] = c
                # emoji_hand.append(emoji_choice)
    return emoji_hand, emojis

def format_l_to_s(l):
    string = ''
    cont = 0
    for s in l:
        if(cont == len(l)-1):
            string += '{} '.format(s)
        else:
            string += '{}, '.format(s)
        cont +=1
    return string

def bj_quit(ctx,descricao):
    emb = discord.Embed(
        title = "Fim de o jogo",
        description = descricao,
        colour = discord.Colour.blue()
    )
    emb.set_author(name='{}'.format(ctx.message.author.name),icon_url='{}'.format(ctx.message.author.avatar_url))
    return emb

def saldo(result,id_user,credito):
    user = busca_user_id(id_user)
    if(result == -2):
        cor = discord.Colour.red()
        edit_user(id_user,user.get_qtd()-credito)
    elif(result == -1):
        cor = discord.Colour.orange()
        credito /= 2 
        credito = int(round(credito,0))
        edit_user(id_user,user.get_qtd()-credito)
    elif(result == 0):
        cor = discord.Colour.blue()
    else:
        cor = discord.Colour.green()
        edit_user(id_user,user.get_qtd()+credito)
    user = busca_user_id(id_user)
    emb = discord.Embed(
        title = "Seu novo saldo",
        description = ":credit_card: {} créditos".format(int(user.get_qtd())),
        colour = cor
    )
    return emb

async def blackjack_game(ctx,bot,credito):
    deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]*4
    random.shuffle(deck)
    with open('Data/emojis_cards.json') as json_file:
        emojis = json.load(json_file)
    dealer_hand, deck = round1(deck)
    player_hand, deck = round1(deck)
    print('dealer',dealer_hand)
    print('player',player_hand)
    dealer_hand_e, emojis = format_emoji(dealer_hand,None,emojis)
    player_hand_e, emojis = format_emoji(player_hand,None,emojis)
    lista = blackjack(dealer_hand,player_hand)
    if(lista[0] == True and lista[1] == True):
        msg = "Empate! Você e o Dealer tem um blackjack."
        emb = edit(ctx,msg,dealer_hand,dealer_hand_e,player_hand,player_hand_e,'')
        emb2 = saldo(0,ctx.message.author.id,credito)
        await ctx.send(embed=emb)
        await ctx.send(embed=emb2)
    elif(lista[0] == True):
        msg = 'Parabéns você ganhou! Você tem um Blackjack'
        emb = edit(ctx,msg,dealer_hand,dealer_hand_e,player_hand,player_hand_e,'')
        emb2 = saldo(1,ctx.message.author.id,credito)
        await ctx.send(embed=emb)
        await ctx.send(embed=emb2)
    elif(lista[1] == True):
        msg = 'Você perdeu! O dealer tem um Blackjack'
        emb = edit(ctx,msg,dealer_hand,dealer_hand_e,player_hand,player_hand_e,'')
        emb2 = saldo(-2,ctx.message.author.id,credito)
        await ctx.send(embed=emb)
        await ctx.send(embed=emb2)
    else:
        emb = discord.Embed(
            title = "Bem vindo o Blackjack:",
            description = "Reaja com:\n🇭 para perdir mais cartas (Hit) \n🇸 para parar (Stand) \n🇶 Para se render (Perda só metade dos creditos)",
            colour = discord.Colour.blue()
        )
        emb.add_field(name='Mão do dealer:', value='{} {} com uma carta virada'.format(dealer_hand_e[0],dealer_hand[0]), inline=True)
        emb.add_field(name='Sua mão:', value='{} {} com total de {}'.format(format_l_to_s(player_hand_e),format_l_to_s(player_hand),total(player_hand)), inline=True)
        emb.set_footer(text='Você tem 10 segundos para responder.')
        message = await ctx.send(embed=emb)
        await message.add_reaction('🇭')
        await message.add_reaction('🇸')
        await message.add_reaction('🇶')
        while True:
            def check(reaction, user):
                return reaction.message.id == message.id and (str(reaction.emoji) == '🇭' or str(reaction.emoji) == '🇸' or str(reaction.emoji) == '🇶') and not user.bot == True
            try:
                r = await bot.wait_for('reaction_add', check=check, timeout=10)
            except asyncio.TimeoutError:
                emb = bj_quit(ctx,'O tempo de escolha esgotou')
                emb2 = saldo(-1,ctx.message.author.id,credito)
                await message.clear_reactions()
                await message.edit(embed=emb)
                await ctx.send(embed=emb2)
                break
            if(str(r[0].emoji) == '🇭'):
                player_hand,player_hand_e,emojis,deck = hit(player_hand,player_hand_e,emojis,deck)
                msg, result = verifica_player(player_hand)
                if(msg is None):
                    emb = edit(ctx,msg,dealer_hand,dealer_hand_e,player_hand,player_hand_e,'Hit')
                    await message.remove_reaction('🇭',ctx.message.author)
                    await message.edit(embed=emb)
                else:
                    emb = edit(ctx,msg,dealer_hand,dealer_hand_e,player_hand,player_hand_e,'Hit')
                    await message.remove_reaction('🇭',ctx.message.author)
                    emb2 = saldo(result,ctx.message.author.id,credito)
                    await message.edit(embed=emb)
                    await ctx.send(embed=emb2)
                    break
            elif(str(r[0].emoji) == '🇸'):
                if(total(dealer_hand) <= total(player_hand)):
                    while(total(dealer_hand) <=17 and len(dealer_hand) <6):
                        dealer_hand,dealer_hand_e,emojis,deck = hit(dealer_hand,dealer_hand_e,emojis,deck)
                msg,result = score(dealer_hand, player_hand)
                emb = edit(ctx,msg,dealer_hand,dealer_hand_e,player_hand,player_hand_e,'Stand')
                await message.clear_reactions()
                emb2 = saldo(result,ctx.message.author.id,credito)
                await message.edit(embed=emb)
                await ctx.send(embed=emb2)
                break
            elif(str(r[0].emoji) == '🇶'):
                emb = bj_quit(ctx,'Você se rendeu!')
                emb2 = saldo(-1,ctx.message.author.id,credito)
                await message.clear_reactions()
                await message.edit(embed=emb)
                await ctx.send(embed=emb2)
                break
            else:
                print('outro')

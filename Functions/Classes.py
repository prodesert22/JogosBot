class User:
      def __init__(self, id_user, credito):
            self.id_user = id_user
            self.credito = credito

      def get_id(self):
            return self.id_user

      def get_qtd(self):
            return self.credito

class Galo: 
    def __init__(self, id_user, level, forca, defesa, vida, img, nome, vitorias, xp, Item1, Item2, move1 , move2, move3, move4):
        self.id_user = id_user
        self.level = level
        self.forca = forca
        self.img = img
        self.nome = nome
        self.vitorias = vitorias
        self.xp = xp
        self.defesa = defesa
        self.vida = vida
        self.esquiva = 10
        self.move1 = Movimento(move1,'teste1',20,5)
        self.move2 = Movimento(move2,'teste2',20,5)
        self.move3 = Movimento(move3,'teste3',20,5)
        self.move4 = Movimento(move3,'teste4',20,5)
        self.Item1 = Item1
        self.Item2 = Item2
        if(self.Item1 != 0):
            self.forca = self.forca + (self.forca *self.Item1.get_forca/100)
            self.vida = self.vida  + (self.vida * self.Item1.get_vida/100)
            self.defesa = self.defesa + (self.defesa * self.Item1.get_defesa/100)
            self.esquiva = self.esquiva + (self.esquiva * self.Item1.get_esquiva/100)
        if(self.Item2 != 0):
            self.forca = self.forca + (self.forca *self.Item2.get_forca/100)
            self.vida = self.vida  + (self.vida * self.Item2.get_vida/100)
            self.defesa = self.defesa + (self.defesa * self.Item2.get_defesa/100)
            self.esquiva = self.esquiva + (self.esquiva * self.Item2.get_esquiva/100)

    @property    
    def get_id(self):
        return self.id_user

    @property    
    def get_level(self):
        return self.level
    
    @property    
    def get_forca(self):
        return self.forca
    
    @property    
    def get_img(self):
        return self.img

    @property    
    def get_nome(self):
        return self.nome

    @property    
    def get_vitorias(self):
        return self.vitorias     

    @property    
    def get_xp(self):
        return self.xp

    @property    
    def get_defesa(self):
        return self.defesa

    @property    
    def get_esquiva(self):
        return self.esquiva
    
    @property    
    def get_Item1(self):
        return self.Item1

    @property    
    def get_Item2(self):
        return self.Item2

    @property    
    def get_move1(self):
        return self.move1
        
    @property    
    def get_move2(self):
        return self.move2
    
    @property    
    def get_move3(self):
        return self.move3

    @property    
    def get_move4(self):
        return self.move4

    @property    
    def get_lista_moves(self):
        listamoves =[self.move1,self.move2,self.move3,self.move4]
        return listamoves

    @property    
    def get_vida(self):
        return self.vida

    def set_vida(self,vida):
        self.vida = vida

class Movimento:
    def __init__(self, id_move, nome, ataque, critico):
        self.id_move = id_move
        self.nome = nome
        self.ataque = ataque
        self.critico = critico

    @property 
    def get_id(self):
        return self.id_move

    @property 
    def get_nome(self):
        return self.nome

    @property 
    def get_ataque(self):
        return self.ataque

    @property 
    def get_critico(self):
        return self.critico

class Item: 
    def __init__(self, id_item, nome, descricao, forca, defesa, esquiva, vida):
        self.id_item = id_item
        self.forca = forca
        self.defesa = defesa
        self.esquiva = esquiva
        self.vida = vida
        self.nome = nome
        self.descricao = descricao

    @property 
    def get_id(self):
        return self.id_item
    
    @property 
    def get_forca(self):
        return self.forca

    @property 
    def get_defesa(self):
        return self.defesa
    
    @property 
    def get_esquiva(self):
        return self.esquiva
    
    @property 
    def get_vida(self):
        return self.vida

    @property 
    def get_nome(self):
        return self.nome

class Crypto():
    def __init__(self, nome, simbolo, logo, site, preco):
        self.nome = nome
        self.simbolo = simbolo
        self.logo = logo
        self.site = site
        self.preco = preco

    @property 
    def get_nome(self):
        return self.nome
    
    @property   
    def get_simbolo(self):
        return self.simbolo
    
    @property 
    def get_logo(self):
        return self.logo
    
    @property 
    def get_site(self):
        return self.site
    
    @property 
    def get_preco(self):
        return self.preco
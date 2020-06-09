import numpy as np
import random 

numeros = ('zero','one','two','three','four','five','six','seven','eight','nine')

def cal_matriz(tamanho,bomba):
      tama=tamanho
      matriz = np.zeros((tamanho,tamanho), dtype=np.float64)

      for n in range(bomba):
            colocarbomba(matriz,tama)
      
      for i in range(tama): 
            for j in range(tama):
                  valor = matriz[i,j]
                  if valor == -1:
                        carregarnumeros(i,j,matriz,tama)


      print('matriz')           
      for i in range(tamanho):
            for j in range(tamanho):
                  print(f'[{matriz[i,j]}]',end='')
            print('\n')
      return matriz
 
def colocarbomba(b,tamanho):
      t = tamanho
      l = random.randint(0,t-1)
      c = random.randint(0,t-1)
      linha_atual = b[l]
      if not linha_atual[c] == -1:
            linha_atual[c] = -1
      else:
            colocarbomba(b,t)
      
def carregarnumeros(linha_N,coluna,matriz,tamanho):
      t = tamanho-1
      #linha de cima
      if(linha_N-1>-1):
            linha = matriz[linha_N-1]
            if coluna-1 > -1:
                  if not linha[coluna-1] == -1:
                        linha[coluna-1] += 1
            if not linha[coluna] == -1:
                  linha[coluna] += 1
            if t >= coluna+1:
                  if not linha[coluna+1] == -1:
                        linha[coluna+1] += 1

      #mesma linha
      linha = matriz[linha_N]
      if(coluna-1 > -1):
            if(not linha[coluna-1] == -1):
                  linha[coluna-1] += 1
      if(coluna+1 <= t):
            if(not linha[coluna+1] == -1):
                  linha[coluna+1] += 1
      
      #linha de baixo
      if t >= linha_N+1:
            linha = matriz[linha_N+1]

            if coluna-1 > -1:
                  if not linha[coluna-1] == -1:
                        linha[coluna-1] += 1

            if not linha[coluna] == -1:
                  linha[coluna] += 1

            if t >= coluna+1:
                  if not linha[coluna+1] == -1:
                        linha[coluna+1] += 1

def gerar_texto(tamanho,matriz,bomba):
      texto = '**Campo minado** ({} x {} com {} bombas) \n'.format(tamanho,tamanho,bomba)
      for i in range(tamanho):
            for j in range(tamanho):
                  if matriz[i,j] == -1:
                        texto += '||:boom:||'
                  else:
                        pos = int(matriz[i,j])
                        texto += '||:'+numeros[pos]+':||'
            texto += '\n'
      return texto
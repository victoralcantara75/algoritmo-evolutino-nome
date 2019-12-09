#ALGORITMO EVOLUTIVO
import random
import time

def gerarInicial(tamanho_nome, num_individuos=6):

	individuos = list([] for i in range(num_individuos))

	for j in range (0, num_individuos):
		for i in range (0,tamanho_nome):
			num = random.randrange(2)
			individuos[j].append(num)

	return individuos

def avaliacao(individuos, letra,tamanho_nome):

	aptidoes = []
	maximo = False
	idx = -1

	for individuo in individuos:
		aptidao = 0
		for pos_individuo, pos_letra in zip(individuo, letra):
			if pos_individuo == pos_letra:
				aptidao = aptidao + 1
		aptidoes.append(aptidao)		

	if tamanho_nome in aptidoes:
		maximo = True
		idx = aptidoes.index(tamanho_nome)

	return aptidoes, maximo, idx

def selecao(individuos, aptidoes):

	melhores = []

	for i in range (0, 4):
		#acho o melhor individuo
		melhor = max(aptidoes)
		#salvo o index desse individuo
		idx = aptidoes.index(melhor)
		#inserir esse individuo numa lista de melhores
		melhores.append(individuos[idx])
		#retiro ele das listas  para refazer a busca
		aptidoes.remove(melhor)
		individuos.pop(idx)
	
	return melhores

def cruzamento(melhores, taxa_mutacao, tamanho_nome):

	nova_populacao = []

	while (len(melhores) != 0):
		tam = len(melhores)
		idx_c1 = random.randrange(tam)
		c1 = melhores[idx_c1]
		melhores.remove(c1)

		tam = len(melhores)
		idx_c2 = random.randrange(tam)
		c2 = melhores[idx_c2]
		melhores.remove(c2)

		nova_populacao.append(c1)
		nova_populacao.append(c2)

		c3 = c1[:]
		c4 = c2[:]

		posicao = random.randrange(tamanho_nome)

		temp = c3[posicao]
		c3[posicao] = c4[posicao]
		c4[posicao] = temp

		mutacao = random.random()
		if mutacao < taxa_mutacao:
			posicao = random.randrange(tamanho_nome)
			num = random.randrange(2)
			c3[posicao] = num

		mutacao = random.random()
		if mutacao < taxa_mutacao:
			posicao = random.randrange(tamanho_nome)
			num = random.randrange(2)
			c4[posicao] = num

		nova_populacao.append(c3)
		nova_populacao.append(c4)

	return nova_populacao

def printarNome(nome):

	d = ""
	cont = 0;
	letras = []
	for i in nome:
		d = "" + d + str(i)
		cont = cont +1
		if cont == 5:
			letras.append(alfabeto2[d])
			cont = 0
			d = ""
	
	print(letras)
	time.sleep(0.1)


if __name__ == '__main__':

	alfabeto = {
		"A":'00000', "B":'00001',"C":'00010',"D": '00011',"E": '00100',"F": '00101',"G": '00110',"H": '00111',"I": '01000',"J": '01001',"K": '01010',"L": '01011' ,"M": '01100',"N": '01101',"O": '01110',"P": '01111',"Q": '10000',"R": '10001',"S": '10010',"T": '10011',"U": '10100',"V": '10101',"W": '10110',"X": '10111',"Y": '11000',"Z": '11001'	
	}
	alfabeto2 = {
		"00000":"A", "00001":"B", "00010":"C", "00011":"D", "00100":"E", "00101":"F", "00110":"G", "00111":"H", "01000":"I","01001":"J", "01010":"K", "01011":"L", "01100":"M", "01101":"N", "01110":"O", "01111":"P", "10000":"Q", "10001":"R", "10010":"S", "10011":"T", "10100":"U", "10101":"V", "10110":"W", "10111":"X", "11000":"Y", "11001":"Z" , "11010": "-", "11011": "-", "11100": "-", "11101":"-", "11110": "-", "11111":"-" 
	}

	nome_entrada = input("Digite o nome (maiusculo): ")
	nome = []

	for i in nome_entrada:
		valor = alfabeto[i]
		for j in valor:
			nome.append(int(j))
		

	printarNome(nome)
	
	taxa_mutacao = 0.4
	aptidoes = []
	melhores = []

	tamanho_nome = len(nome)

	individuos = gerarInicial(tamanho_nome, 6)

	while True:
		aptidoes, maximo, idx = avaliacao(individuos, nome, tamanho_nome)
		if maximo == True:
			melhor_individuo = individuos[idx]
			break
		#print('APTIDOES: ', aptidoes)

		melhores = selecao(individuos, aptidoes)
		#print('MELHOR: ', melhores[0])
		printarNome(melhores[0])

		individuos = cruzamento(melhores, taxa_mutacao, tamanho_nome)

	printarNome(melhor_individuo)
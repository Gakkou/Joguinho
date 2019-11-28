#coding=UTF-8
'''
	Joguinho:
	Lucas S. Avila 111136
'''

from graphics import *
import random
import time

resolu1 = 700
resolu2 = 700

# Janela Principal
def win_principal(resolu1, resolu2):
	wingame = GraphWin("Joguinho", resolu1, resolu2)
	# Imagem de fundo
	fundo_inst = Image(Point(resolu1/2,resolu2/2), "resources/sea.png")
	fundo_inst.draw(wingame)
	return (wingame)

# Instruções
def instru(wingame, resolu1, resolu2):
	# Lendo do arquivo
	objinstrucoes = open("instr.txt", 'r')
	instrucoes = objinstrucoes.read()
	objinstrucoes.close()
	# Escrevendo na janela
	textoinstru = Text(Point(resolu1/2, resolu2/2), instrucoes)
	textoinstru.setStyle("bold")
	textoinstru.setSize(15)
	textoinstru.setFill("White")
	textoinstru.draw(wingame)
	# Desenhando botão
	botaop1 = Rectangle(Point(resolu1/2 - 50, resolu2 - 105), Point(resolu1/2 + 50, resolu2 - 80))
	botaop1.setFill("White")
	botaop1.draw(wingame)
	botaop2 = Text(botaop1.getCenter(), "Ok!")
	botaop2.draw(wingame)
	# Checando o click
	click = wingame.getMouse()
	while(click.getX() < botaop1.getP1().getX() or click.getX() > botaop1.getP2().getX() or click.getY() < botaop1.getP1().getY() or click.getY() > botaop1.getP2().getY()):
		click = wingame.getMouse()
	textoinstru.undraw()
	botaop1.undraw()
	botaop2.undraw()

# Contador
def contador(nivel, wingame, resolu1, resolu2):
	# Desenhando o tempo do contador
	cont = 3
	contador = Text(Point((resolu1/2) + 50, resolu2/2), str(cont))
	contador.setSize(25)
	contador.setFill("White")
	contador.setStyle("bold")
	contador.draw(wingame)
	# Testa o nivel
	if(nivel == 1):
		texto = "O jogo vai começar em: "
	else:
		texto = "O nível " + str(nivel) + " começa em: "
	# Desenha o texto
	textoqualquer = Text(Point((resolu1/4) + 20, resolu2/2), texto)
	textoqualquer.setSize(25)
	textoqualquer.setFill("White")
	textoqualquer.setStyle("bold")
	textoqualquer.draw(wingame)
	# Conta o tempo
	while(cont > 0):
		time.sleep(1)
		cont = cont - 1
		contador.setText(str(cont))
	contador.undraw()
	textoqualquer.undraw()

def drawLife(vida):
	textoqualquer = Text(Point(600, 650), "Vida: " + str(vida))
	textoqualquer.setSize(25)
	textoqualquer.setFill("White")
	textoqualquer.setStyle("bold")
	return textoqualquer

def drawTime(time):
	textoqualquer = Text(Point(100, 650), "Tempo: " + str(time))
	textoqualquer.setSize(25)
	textoqualquer.setFill("White")
	textoqualquer.setStyle("bold")
	return textoqualquer
	
# Criando inimigos e suas características únicas
def criarini(nivel, wingame, resolu1, resolu2):
	# Características de cada
	iniimg = ["resources/trash1.png", "resources/trash2.png", "resources/trash3.png", "resources/trash4.png"]
	mexer = [nivel, random.randint(1+(2*nivel)/3, 2+nivel), random.randint(nivel, 1+(3*nivel)/2), random.randint(nivel, 1+(4*nivel)/3)]
	vida = [random.randint(1, 2+nivel/4), random.randint(1+nivel/4, 2+nivel/2), random.randint(1+nivel/2, 2+nivel), random.randint(nivel, 4*nivel/3)]
	# Desenhando no jogo
	global nini
	global initela
	global imginitela
	global vidainitela
	global mexerinitela
	global celas
	initela = []		# Área de detecção
	imginitela = []		# A imagem
	vidainitela = []	# A vida
	mexerinitela = []	# A movimentação
	celas = []
	nini = random.randint(1+nivel/4, 4+nivel/4)
	cont = 0
	while(cont < nini):
		pontoa = Point(random.randint(0, resolu1-200), random.randint(0, resolu2-200))
		pontob = Point(pontoa.getX()+200, pontoa.getY()+200)
		initela.append(Rectangle(pontoa, pontob))
		#initela[cont].draw(wingame)		# Temporário
		img = random.choice(iniimg)
		imginitela.append(Image(initela[cont].getCenter(), img))
		imginitela[cont].draw(wingame)
		cont1 = iniimg.index(img)
		vidainitela.append(vida[cont1])
		mexerinitela.append(mexer[cont1])
		celas.append(Image(initela[cont].getCenter(), "cela.png"))
		cont += 1

# Menu do jogo
def Menu():
	wingame = win_principal(resolu1, resolu2)
	teste = 1
	desenho_io = 0
	while(teste == 1):
		if(desenho_io == 0):
			# Botão iniciar
			A1 = Point(resolu1/2 - 40, resolu2/2 - 80)
			A2 = Point(resolu1/2 + 40, resolu2/2 - 55)
			iniciarretan = Rectangle(A1, A2)
			iniciarretan.setFill("White")
			iniciarretan.draw(wingame)
			iniciartexto = Text(iniciarretan.getCenter(), "Iniciar!")
			iniciartexto.draw(wingame)
			# Botão instru
			B1 = Point(resolu1/2 - 40, resolu2/2 - 35)
			B2 = Point(resolu1/2 + 40, resolu2/2 - 10)
			instruretan = Rectangle(B1, B2)
			instruretan.setFill("White")
			instruretan.draw(wingame)
			instrutexto = Text(instruretan.getCenter(), "Instruções")
			instrutexto.draw(wingame)
			# Botão placar
			C1 = Point(resolu1/2 - 40, resolu2/2 + 10)
			C2 = Point(resolu1/2 + 40, resolu2/2 + 35)
			placarretan = Rectangle(C1, C2)
			placarretan.setFill("white")
			placarretan.draw(wingame)
			placartexto = Text(placarretan.getCenter(), "Placar")
			placartexto.draw(wingame)
			# Botão sair
			D1 = Point(resolu1/2 - 40, resolu2/2 + 55)
			D2 = Point(resolu1/2 + 40, resolu2/2 + 80)
			sairretan = Rectangle(D1, D2)
			sairretan.setFill("white")
			sairretan.draw(wingame)
			sairtexto = Text(sairretan.getCenter(), "Sair")
			sairtexto.draw(wingame)
			desenho_io = 1
		click = wingame.getMouse()
		if(click.getX() >= A1.getX() and click.getX() <= A2.getX() and click.getY() >= A1.getY() and click.getY() <= A2.getY()):
			# Botão iniciar
			iniciarretan.undraw()
			iniciartexto.undraw()
			instruretan.undraw()
			instrutexto.undraw()
			placarretan.undraw()
			placartexto.undraw()
			sairretan.undraw()
			sairtexto.undraw()
			desenho_io = 0
			Jogo(wingame)
			parabains()
			registroscore()
		elif(click.getX() >= B1.getX() and click.getX() <= B2.getX() and click.getY() >= B1.getY() and click.getY() <= B2.getY()):
			# Botão instruções
			iniciarretan.undraw()
			iniciartexto.undraw()
			instruretan.undraw()
			instrutexto.undraw()
			placarretan.undraw()
			placartexto.undraw()
			sairretan.undraw()
			sairtexto.undraw()
			desenho_io = 0
			instru(wingame, resolu1, resolu2)
		elif(click.getX() >= C1.getX() and click.getX() <= C2.getX() and click.getY() >= C1.getY() and click.getY() <= C2.getY()):
			# Botão placar
			teladescore()
		elif(click.getX() >= D1.getX() and click.getX() <= D2.getX() and click.getY() >= D1.getY() and click.getY() <= D2.getY()):
			# Botão sair
			teste = 0

# Rodando o jogo
def Jogo(wingame):
	global score
	nivel = 1
	score = 0		# Pontuação
	vida = 3		# Vida do jogador
	while(vida > 0):
		ninitela = 1
		tempo = 0.0
		contador(nivel, wingame, resolu1, resolu2)
		criarini(nivel, wingame, resolu1, resolu2)
		ninitela = nini
		textoVida = drawLife(vida)
		textoVida.draw(wingame)
		tempoRestante = int(9.0 - nivel/4 - tempo)
		textoTempo = drawTime(tempoRestante)
		textoTempo.draw(wingame)
		while(vida > 0  and tempo < 9.0 - nivel/4 and ninitela > 0):
			if tempoRestante != int(9.0 - nivel/4 - tempo):
				tempoRestante = int(9.0 - nivel/4 - tempo)
				textoTempo.undraw()
				textoTempo = drawTime(tempoRestante)
				textoTempo.draw(wingame)
			click = wingame.checkMouse()
			cont = 0
			while(cont < nini and cont != -1):
				if(click != None):	
					pontoa = initela[cont].getP1()
					pontob = initela[cont].getP2()
					if(click.getX() >= pontoa.getX() and click.getX() <= pontob.getX() and click.getY() >= pontoa.getY() and click.getY() <= pontob.getY()):
						if(vidainitela[cont] != 0):
							score += 100
							vidainitela[cont] += -1
							if(vidainitela[cont] == 0):
								initela[cont].undraw()
								ninitela += -1
							cont = -1
						else:
							cont += 1
					else:
						cont += 1
				else:
					cont = -1
			cont = 0
			while(cont < nini):
				if(vidainitela[cont] > 0):
					moverx = mexerinitela[cont]*random.randint(-1,1)
					movery = mexerinitela[cont]*random.randint(-1,1)
					initela[cont].move(moverx, movery)
					imginitela[cont].move(moverx, movery)
					celas[cont].move(moverx, movery)
				cont += 1
			time.sleep(0.01)
			tempo += 0.01
		cont = 0
		while(cont < nini):
			if(vidainitela[cont] > 0):
				#initela[cont].undraw()
				imginitela[cont].undraw()
				vida += -1
			else:
				imginitela[cont].undraw()
				celas[cont].undraw()
			cont += 1
		nivel += 1
		score +=10*(9.0 - nivel/4 - tempo) + 1000
		textoTempo.undraw()
		textoVida.undraw()
	
# Tela de parabéns
def parabains():
	wincongrats = GraphWin("Parabéns", 300, 200)
	texto = Text(Point(150, 100), "Parabéns!!!\n\nSua pontuação foi de " + str(score) + " pontos.")
	texto.draw(wincongrats)
	wincongrats.getMouse()
	wincongrats.close()

# Registro de Score
def registroscore():
	winscore = GraphWin("Registro", 500, 600)
	entrada = Entry(Point(250, 300), 10)
	entrada.setText("Usuario")
	entrada.draw(winscore)
	texto = Text(Point(250, 200), "Digite o seu nome (SEM ACENTOS):")
	texto.draw(winscore)
	botaop1 = Rectangle(Point(225, 550), Point(275, 575))
	botaop1.setFill("White")
	botaop1.draw(winscore)
	botaop2 = Text(botaop1.getCenter(), "Ok!")
	botaop2.draw(winscore)
	click = winscore.getMouse()
	while(click.getX() < botaop1.getP1().getX() or click.getX() > botaop1.getP2().getX() or click.getY() < botaop1.getP1().getY() or click.getY() > botaop1.getP2().getY()):
		click = winscore.getMouse()
	nomeplayer = entrada.getText()
	entrada.undraw()
	texto.undraw()
	botaop1.undraw()
	botaop2.undraw()
	arqplacar = open("placar.txt", 'r')
	texto = arqplacar.readlines()
	verif = 0
	for elem in texto:
		cont = -2
		scoret = ''
		while(cont != 0):
			if(elem[cont] == ' '):
				cont = 0
			else:
				scoret = elem[cont] + scoret
				cont+= -1 
		scoret = eval(scoret)*1.0
		if(score > scoret):
			lugar = texto.index(elem)
			break
	cont1 = len(texto)
	ultimalinha = texto[-1]
	texto.append(ultimalinha)
	while(cont1 > lugar):
		texto[cont1-1] = texto[cont1-2]
		cont1 += -1
	texto[lugar] = nomeplayer + " -- " + str(score) + "\n"
	arqplacar = open("placar.txt", 'w')
	arqplacar.writelines(texto)
	arqplacar.close()
	winscore.close()
	teladescore()
	
# Tela de Score
def teladescore():
	winscore = GraphWin("Placar", 500, 600)
	arqplacar = open("placar.txt", 'r')
	texto = arqplacar.read()
	arqplacar.close()
	textotela = Text(Point(250, 300), texto)
	textotela.draw(winscore)
	winscore.getMouse()
	winscore.close()

Menu()

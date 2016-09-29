#coding=UTF-8
'''
	Joguinho:
	Lucas S. Avila 111136
	Gabriela R. Suita
'''

from graphics import *
import random
import time

# Janela de configuração
def resolu_config():
	# Resolução padrão
	global resolu1 
	global resolu2
	resolu1 = 1280
	resolu2 = 720
	winresolu = GraphWin("Configuração", 500, 500)
	# Imagem de fundo
	fundo_config = Image(Point(250,250), "fundo1.png")
	fundo_config.draw(winresolu)
	# Textos
	presolucao = Text(Point(250, 150), "Digite a resolução:")
	presolucao.setStyle("bold")
	presolucao.setSize(20)
	presolucao.draw(winresolu)
	textox = Text(Point(250, 250), "x")
	textox.setStyle("bold")
	textox.setSize(20)
	textox.draw(winresolu)
	# Entradas
	entrada1 = Entry(Point(150, 250), 10)
	entrada1.setFill("White")
	entrada2 = Entry(Point(350, 250), 10)
	entrada2.setFill("White")
	entrada1.draw(winresolu)
	entrada2.draw(winresolu)
	# Desenhando botão
	pontob1 = Point(225, 400)
	pontob2 = Point(275, 425)
	botaop1 = Rectangle(pontob1, pontob2)
	botaop1.setFill("White")
	botaop1.draw(winresolu)
	botaop2 = Text(botaop1.getCenter(), "Ok!")
	botaop2.draw(winresolu)
	# Checando o click
	click = winresolu.getMouse()
	while(click.getX() < pontob1.getX() or click.getX() > pontob2.getX() or click.getY() < pontob1.getY() or click.getY() > pontob2.getY()):
		click = winresolu.getMouse()
	winresolu.close()
	# Checando resolução (minimo:700x700)
	if (eval(entrada1.getText())<700):
		resolu1=700
	else:
		resolu1 = eval(entrada1.getText())

	if (eval(entrada2.getText())<700):
		resolu2=700
	else:
		resolu2 = eval(entrada2.getText())

# Janela Principal
def win_principal(resolu1, resolu2):
	wingame = GraphWin("Joguinho", resolu1, resolu2)
	return (wingame)

# Instruções
def instru(wingame, resolu1, resolu2):
	# Lendo do arquivo
	objinstrucoes = open("instr.txt", 'r')
	instrucoes = objinstrucoes.read()
	objinstrucoes.close()
	# Imagem de fundo
	fundo_inst = Image(Point(resolu1/2,resolu2/2), "fundo.png")
	fundo_inst.draw(wingame)
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
	botaop2 = Text(botaop1.getCenter(), "Começar!")
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
	
# Criando inimigos e suas características únicas
def criarini(nivel, wingame, resolu1, resolu2):
	# Características de cada
	iniimg = ["fabiob2.png", "dirceu1.png", "maranhao2.png", "renanc2.png", "aecio.png", "feliciano2.png", "cunha1.png", "bolsonaropai2.png", "temer1.png"]
	mexer = [0, 0, 0, 0, 0, nivel, random.randint(1+(2*nivel)/3, 2+nivel), random.randint(nivel, 1+(3*nivel)/2), random.randint(nivel, 1+(4*nivel)/3)]
	vida = [random.randint(1, 2+nivel/4), random.randint(1+nivel/4, 2+nivel/2), random.randint(1+nivel/2, 2+nivel), random.randint(nivel, 4*nivel/3), random.randint(4*nivel/3, 3*nivel/2), random.randint(1, 2+nivel/4), random.randint(1+nivel/4, 2+nivel/2), random.randint(1+nivel/2, 2+nivel), random.randint(nivel, 4*nivel/3)]
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

# Rodando o jogo
def Jogo():
	resolu_config()						# Chama a janela de configuração
	wingame = win_principal(resolu1, resolu2)		# Cria a Janela Principal
	instru(wingame, resolu1, resolu2)			# Mostra as instruções
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
		while(vida > 0  and tempo < 9.0 - nivel/4 and ninitela > 0):
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
								#initela[cont].undraw() #temporário
								celas[cont].draw(wingame)
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
	wingame.close()
	
# Tela de parabéns
def parabains():
	wincongrats = GraphWin("Parabéns", 300, 200)
	texto = Text(Point(150, 100), "Primeiramente FORA TEMER!!!\n\nSua pontuação foi de " + str(score) + " pontos.")
	texto.draw(wincongrats)
	wincongrats.getMouse()
	wincongrats.close()

# Tela de score
def telascore():
	winscore = GraphWin("Placar", 500, 600)
	entrada = Entry(Point(250, 300), 10)
	entrada.setText("Usuario")
	entrada.draw(winscore)
	texto = Text(Point(250, 200), "Digite a o seu nome:")
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
	arqplacar = open("placar.txt", 'r')
	texto = arqplacar.read()
	arqplacar.close()
	textotela = Text(Point(250, 300), texto)
	textotela.draw(winscore)
	winscore.getMouse()

Jogo()
parabains()
telascore()

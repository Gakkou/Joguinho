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
	# Textos
	presolucao = Text(Point(250, 150), "Digite a resolução desejada:")
	presolucao.draw(winresolu)
	textox = Text(Point(250, 250), "x")
	textox.draw(winresolu)
	# Entradas
	entrada1 = Entry(Point(150, 250), 10)
	entrada2 = Entry(Point(350, 250), 10)
	entrada1.draw(winresolu)
	entrada2.draw(winresolu)
	# Desenhando botão
	pontob1 = Point(225, 400)
	pontob2 = Point(275, 425)
	botaop1 = Rectangle(pontob1, pontob2)
	botaop1.draw(winresolu)
	botaop2 = Text(botaop1.getCenter(), "Ok!")
	botaop2.draw(winresolu)
	# Checando o click
	click = winresolu.getMouse()
	while(click.getX() < pontob1.getX() or click.getX() > pontob2.getX() or click.getY() < pontob1.getY() or click.getY() > pontob2.getY()):
		click = winresolu.getMouse()
	winresolu.close()
	# Resolução
	resolu1 = eval(entrada1.getText())
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
	# Escrevendo na janela
	textoinstru = Text(Point(resolu1/2, resolu2/2), instrucoes)
	textoinstru.draw(wingame)
	# Desenhando botão
	botaop1 = Rectangle(Point(resolu1/2 - 50, resolu2 - 105), Point(resolu1/2 + 50, resolu2 - 80))
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
	contador = Text(Point(resolu1/2, resolu2/2), str(cont))
	contador.setSize(36)
	contador.draw(wingame)
	# Testa o nivel
	if(nivel == 1):
		texto = "O jogo começa em: "
	else:
		texto = "O nivel " + str(nivel) + " começa em: "
	# Desenha o texto
	textoqualquer = Text(Point(resolu1/4, resolu2/2), texto)
	textoqualquer.setSize(36)
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
	# Criar o desenho das imagens!!!!
	
	# Respawn
	iniimg = ["fabio", "dirceu", "maranhão", "renan", "aecio", "feliciano", "cunha", "bolsonaro", "temer"] # Vão ser imagens!!!!
	mexer = [0, 0, 0, 0, 0, nivel, random.randint(nivel, 2*nivel), random.randint(nivel, 3*nivel), random.randint(nivel, 4*nivel)]
	vida = [random.randint(1, 2+nivel/4), random.randint(1+nivel/4, 2+nivel/2), random.randint(1+nivel/2, 2+nivel), random.randint(nivel, 4*nivel/3), random.randint(4*nivel/3, 3*nivel/2), random.randint(1, 2+nivel/4), random.randint(nivel/4, 2+nivel/2), random.randint(nivel/2, 2+nivel), random.randint(nivel, 4*nivel/3)]
	# Desenhando no jogo
	global nini
	global initela
	global imginitela
	global vidainitela
	global mexerinitela
	initela = []
	imginitela = []
	vidainitela = []
	mexerinitela = []
	nini = random.randint(1+nivel/4, 4+nivel/4)
	cont = 0
	while(cont < nini):
		pontoa = Point(random.randint(0, resolu1-200), random.randint(0, resolu2-200))
		pontob = Point(pontoa.getX()+200, pontoa.getY()+200)
		initela.append(Rectangle(pontoa, pontob))
		initela[cont].draw(wingame)		# Temporário
		imginitela.append(random.choice(iniimg))  
		#imginitela[cont].draw(wingame)	# Quando juntar com as imagens
		cont1 = iniimg.index(imginitela[cont])
		vidainitela.append(vida[cont1])
		mexerinitela.append(mexer[cont1])
		cont += 1

# Rodando o jogo
def Jogo():
	resolu_config()								# Chama a janela de configuração
	wingame = win_principal(resolu1, resolu2)	# Cria a Janela Principal
	instru(wingame, resolu1, resolu2)			# Mostra as instruções
	nivel = 1
	vida = 3		#vida do jogador
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
							vidainitela[cont] += -1
							if(vidainitela[cont] == 0):
								initela[cont].undraw() #temporário
								#imginitela
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
				initela[cont].move(mexerinitela[cont]*random.randint(-1,1),mexerinitela[cont]*random.randint(-1,1))
				cont += 1
			time.sleep(0.01)
			tempo += 0.01
		nivel += 1

Jogo()

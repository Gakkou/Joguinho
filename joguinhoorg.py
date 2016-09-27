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
def criarini(nivel):
	# Respawn
	global ini
	global mexer
	global vida
	iniimg = ["fabio", "dirceu", "maranhão", "renan", "aecio", "feliciano", "cunha", "bolsonaro", "temer"]
	mexer = [0, 0, 0, 0, 0, nivel, random.randint(nivel, 2*nivel), random.randint(nivel, 3*nivel), random.randint(nivel, 4*nivel)]
	vida = [random.randint(1, 1+nivel/4), random.randint(1+nivel/4, 1+nivel/2), random.randint(1+nivel/2, nivel), random.randint(nivel, 4*nivel/3), random.randint(4*nivel/3, 3*nivel/2), random.randint(1, nivel/4), random.randint(nivel/4, nivel/2), random.randint(nivel/2, nivel), random.randint(nivel, 4*nivel/3)]
	# Desenhando no jogo
	global nini
	global initela
	global vidainitela
	initela = []
	vidainitela = []
	nini = random.randint(1+nivel/4, 4+nivel/4)
	cont = 0
	while(cont < nini):
		pontoa = Point(random.randint(0, resolu1-200), random.randint(0, resolu2-200))
		pontob = Point(pontoa.getX()+200, pontoa.getY()+200)
		initela.append(Rectangle(pontoa, pontob))
		initela[cont].draw(wingame)
		
		cont += 1

# Rodando o jogo
def Jogo():
	resolu_config()								# Chama a janela de configuração
	wingame = win_principal(resolu1, resolu2)	# Cria a Janela Principal
	instru(wingame, resolu1, resolu2)			# Mostra as instruções
	nivel = 1
	vida = 3		#vida do jogador
	while(vida > 0):
		contador(nivel, wingame, resolu1, resolu2)
			
Jogo()

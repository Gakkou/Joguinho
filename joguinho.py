#coding=UTF-8

'''
Joguinho:
Lucas S. Avila
Gabriela Suita
'''
from graphics import *
import random
import time


# Janela de configuração da resolução do jogo
winresolu = GraphWin("Configuração", 500, 500)
presolucao = Text(Point(250, 150), "Digite a resolução desejada:")
presolucao.draw(winresolu)
textox = Text(Point(250, 250), "x")
textox.draw(winresolu)
entrada1 = Entry(Point(150, 250), 10)
entrada2 = Entry(Point(350, 250), 10)
entrada1.draw(winresolu)
entrada2.draw(winresolu)
pontob1 = Point(225, 400)
pontob2 = Point(275, 425)
botaop1 = Rectangle(pontob1, pontob2)
botaop1.draw(winresolu)
botaop2 = Text(botaop1.getCenter(), "Ok!")
botaop2.draw(winresolu)
click = winresolu.getMouse()
while(click.getX() < pontob1.getX() or click.getX() > pontob2.getX() or click.getY() < pontob1.getY() or click.getY() > pontob2.getY()):
	click = winresolu.getMouse()
winresolu.close()

resolu1 = eval(entrada1.getText())
resolu2 = eval(entrada2.getText())

# Arquivo de instruções
objinstrucoes = open("instr.txt", 'r')
instrucoes = objinstrucoes.read()

# Janela principal
wingame = GraphWin("Joguinho", resolu1, resolu2)
textoinstru = Text(Point(resolu1/2, resolu2/2), instrucoes)
textoinstru.draw(wingame)
pontob1 = Point(resolu1/2 - 50, resolu2 - 105)
pontob2 = Point(resolu1/2 + 50, resolu2 - 80)
botaop1 = Rectangle(pontob1, pontob2)
botaop1.draw(wingame)
botaop2 = Text(botaop1.getCenter(), "Começar!")
botaop2.draw(wingame)
click = wingame.getMouse()
while(click.getX() < pontob1.getX() or click.getX() > pontob2.getX() or click.getY() < pontob1.getY() or click.getY() > pontob2.getY()):
	click = wingame.getMouse()
textoinstru.undraw()
botaop1.undraw()
botaop2.undraw()

# Contador 
cont = 3
contador = Text(Point(resolu1/2, resolu2/2), str(cont))
contador.setSize(36)
contador.draw(wingame)
textoqualquer = Text(Point(resolu1/4, resolu2/2), "O jogo vai começar em:")
textoqualquer.setSize(36)
textoqualquer.draw(wingame)
while(cont > 0):
	time.sleep(1)
	cont = cont - 1
	contador.setText(str(cont))
#wingame.close()

#Waves
nivel = 1
while(nivel <= 20 and nivel != -1):
	if(nivel % 5 == 0):
		#Wave com chefe
		
	else:
		#Wave sem chefe
		segundo = 0
		while (segundo < random.randint(, )):
			
	nivel += 1
if(nivel == -1):
	#perdeu
	
else:
	#ganhou
	

'''
	- PNG com a caras dos inimigos;
	- Fazer lista de objetos GraphWin, reutilizar;
	- inimigos por wave min: 3, max: 9;
	- Tempos dos corruptos max: 8s, min: 3s;
	- Chefes no levels 5, 10, 15, 20. 20 é o "primeiramente";
	- Janelas tem vidas que dimínuem com o número de clicks;
	- Janela com o tempo(Retangulo que diminui conforme o tempo que passa);
	- Tempo com contadores;
	- O lugar onde as janelas aparecem deve ser aleatório também!!
	- Arrumar as janelas auxiliares;
	- Arrumar o cursor;
	- Pegar fotos de x políticos;
	- Transformar as fotos em ppm ou gif; 
	- Recortar os rostos;
	- Diminuir as resoluções;
'''

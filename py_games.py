"""Este archivo fue creado con la finalidad de recopilar todos los juegos basicos que he hecho
y que estoy por hacer, para agregarle su posterior capa UI e incorporarlos a Android mediante
Flutter.
El tiempo esperado de finalizacion de este proyecto no debe de ser mayor a una semana
Dia de inicio: 21/03/23 11:27
"""
import random

exit_menu = 1
selecc_game = 0

class GatoGame:
    def __init__(self):
        self.tablero = [[1, 2, 3],[4, 5, 6],[7, 8, 9]]
        self.jugador = "O"
        self.maquina = "X"
        self.tablero_completo = False
        self.game_over = False
    def game(self):
        while not self.game_over:
            print(self.game_over)
            self.setup()
            self.ai_turn()
            self.setup()
            if self.checking(self.maquina):
                self.game_over = True
                break
            self.game_over = self.checking(self.maquina)
            self.player_turn()
            self.game_over = self.checking(self.jugador) or self.game_over
        self.cleanup()
    def setup(self):
        print("+-------+-------+-------+", "\n|\t|\t|\t|","\n|  ", self.tablero[0][0], "  |  ", self.tablero[0][1], "  |  ", self.tablero[0][2],"  |", "\n|\t|\t|\t|\n","+-------+-------+-------+", "\n|\t|\t|\t|","\n|  ", self.tablero[1][0], "  |  ", self.tablero[1][1], "  |  ", self.tablero[1][2],"  |", "\n|\t|\t|\t|\n","+-------+-------+-------+", "\n|\t|\t|\t|","\n|  ", self.tablero[2][0], "  |  ", self.tablero[2][1], "  |  ", self.tablero[2][2],"  |", "\n|\t|\t|\t|\n","+-------+-------+-------+")  
    def ai_turn(self):
        z = random.randint(0,2)
        y = random.randint(0,2)
        if type(self.tablero[z][y]) == int:
            self.tablero[z][y] = self.maquina
        else:
            self.ai_turn()
    def player_turn(self):
        z = int(input("Ingrese el eje x: "))
        y = int(input("Ingrese el eje y: "))
        if type(self.tablero[y][z]) == int:
            self.tablero[y][z] = self.jugador
        else:
            self.player_turn()
    def checking(self, marcador):
        if self.tablero[0][0] == self.tablero[0][1] == self.tablero[0][2] == marcador or self.tablero[1][0] == self.tablero[1][1] == self.tablero[1][2] == marcador or self.tablero[2][0] == self.tablero[2][1] == self.tablero[2][2] == marcador or self.tablero[0][0] == self.tablero[1][0] == self.tablero[2][0] == marcador or self.tablero[0][1] == self.tablero[1][1] == self.tablero[2][1] == marcador or self.tablero[0][2] == self.tablero[1][2] == self.tablero[2][2] == marcador or self.tablero[0][0] == self.tablero[1][1] == self.tablero[2][2] == marcador or self.tablero[0][2] == self.tablero[1][1] == self.tablero[2][0] == marcador:
            print(marcador, "ha ganado",self.tablero,self.tablero_completo)
            return True
        else:
            return False
    def cleanup(self):
        self.tablero = [[1, 2, 3],[4, 5, 6],[7, 8, 9]]
        self.tablero_completo = False

class RandNum:
    def __init__(self):
        self.user_num = 0
        self.ran_num = 10
    def game(self):
        self.set_user_num()
        self.set_random_int()
        self.compare_num()
    def set_user_num(self):
        self.user_num = int(input("Ingrese un numero del 1 al 5\n"))
    def set_random_int(self):
        self.ran_num = random.randint(1,5)
        return self.ran_num
    def compare_num(self):
        if self.ran_num == self.user_num:
            print("Correcto")
        else:
            print("Incorrecto")
    def reset(self):
        self.user_num, self.ran_num = 0, 10

class ai_guess:
    def __init__(self):
        self.user_num = 0
        self.ran_num = []
        self.num_real = 0
    def game(self):
        self.user_number()
        self.ai_guesser()
        while self.user_num != self.num_real:
            for i in self.ran_num:
                if i == self.num_real:
                    break
                else:
                    self.ran_num.append(random.randint(1,5))
            self.ai_guesser()
        else:
            print("Ya se que tu numero es", self.num_real)
            self.cleanup()
    def user_number(self):
        self.user_num = int(input("Ingrese el numero a adivinar (1-5)\n"))
    def ai_guesser(self):
        self.num_real = random.randint(1,5)
    def cleanup(self):
        self.user_num, self.num_real = 0, 0
        self.ran_num.clear()

class PiePapTij:
    def __init__(self):
        self.options = ['piedra', 'papel', 'tijeras']
        self.user_answer = ''
        self.ai_answer = 10
        self.ciclico = 1
    def game(self):
        print("Este es el juego de piedra, papel o tijeras")
        while self.ciclico == 1:
            self.userinput()
            self.aiinput()
            print("\n")
            self.logic()
            self.cleanup()
            self.ciclico = int(input("Desea volver a jugar? (1.Si /Else.No)"))
    def logic(self):
        if self.user_answer == self.options[self.ai_answer]:
            print("U Draw")
        elif self.user_answer == self.options[0] and self.ai_answer == 1:
            print("U Lose")
        elif self.user_answer == self.options[0] and self.ai_answer == 2:
            print("U Win")
        elif self.user_answer == self.options[1] and self.ai_answer == 0:
            print("U Win")
        elif self.user_answer == self.options[1] and self.ai_answer == 2:
            print("U Lose")
        elif self.user_answer == self.options[2] and self.ai_answer == 0:
            print("U Lose")
        elif self.user_answer == self.options[2] and self.ai_answer == 1:
            print("U Win")
    def userinput(self):
        self.user_answer = str(input("Ingrese su eleccion\n"))
        self.user_answer = self.user_answer.lower()
    def aiinput(self):
        self.ai_answer = random.randint(0,2)
    def cleanup(self):
        self.user_answer = ''
        self.ai_answer = 10

class MineSweeper:
    def  __init__(self):
        self.bombs = []
        self.map = []
        self.map = []
        self.game_over = False
    def game(self):
        self.usersetting()
        self.setmap()
        self.setdifficulty()
        self.generatebombs()
        while not self.game_over:
            self.print_board()
            y = int(input("Ingrese el eje x:\n")) #por comodidad visual x horizontal
            x = int(input("Ingrese el eje y:\n")) #por comodidad visual y vertical
            if not self.reveal(x,y):
                print("Activaste una mina, el juego ha terminado")
                self.game_over = True
                break
            if all(self.revealed[i][j] or (i,j) in self.bombs for i in range(len(self.map)) for j in range(len(self.map[0]))):
                print("Ganaste")
                break
    def usersetting(self):
        size = int(input("Ingrese el mapa que quiere: (1.Chico/2.Grande)"))
        difficulty = int(input("Ingrese la dificultad: (1.Facil/2.Dificil)"))
        self.mode = difficulty
        self.size = size
    def setmap(self):
        if self.size == 1:
            self.map = [["O" for _ in range(5)]for _ in range(5)]
            self.num_cells = 25
            self.revealed = [[False for _ in range(5)] for _ in range(5)]
        elif self.size == 2:
            self.map = [["O" for _ in range(6)]for _ in range(8)]
            self.num_cells = 48
            self.revealed = [[False for _ in range(6)] for _ in range(8)]
        else:
            print("Mapa invalido")
    def setdifficulty(self):
        if self. mode == 1:
            self.bomb_count = int(self.num_cells/7)
        elif self.mode == 2:
            self.bomb_count = int(self.num_cells/4)
    def generatebombs(self):
        self.bombs = random.sample([(x,y)for x in range(len(self.map))for y in range(len(self.map[0]))], self.bomb_count)
    def reveal(self, x, y):
        bombs_around = 0
        if (x, y) in self.bombs:
            self.revealed[x][y] = True
            return False
        elif self.map[x][y] == 0:
            self.revealed[x][y] = True
            for dx in [-1,0, 1]:
                for dy in [-1,0, 1]:
                    if (dx,dy) == (0, 0):
                        continue
                    if 0 <= x+dx < len(self.map[0]) and 0 <= y+dx < len(self.map) and not self.revealed[x+dx][y+dy]:
                        self.reveal(x+dx, y+dy)
            return True
        else:
            self.revealed[x][y] = True
            for dx in [-1,0, 1]:
                for dy in [-1,0, 1]:
                    if (dx,dy) == (0, 0):
                        continue
                    if (x+dx, y+dy) in self.bombs:
                        bombs_around += 1
            self.map[x][y] = bombs_around
            return True
    def print_board(self):
        for row in self.map:
            print("\n")
            for element in row:
                print(' '.join(str(element)), end = " ")
        print("\n")

class Ahorcado:
    def __init__(self):
        self.palabras = ["aire", "ojos", "piel", "anteojos", "joven", "viejo", "alto", "bajo", "pequeño", "gordo", "delgado", "bella", "azul", "verde", "negro", "sombrero", "guantes", "corbata", "gemelos", "paraguas", "plata", "oro", "perla", "diamante", "esmeralda", "anillo", "pulsera", "reloj", "elegante", "sencillo", "chaqueta", "traje", "camisa", "zapatos", "pelo", "maquillaje", "peine", "dedo", "hueso", "cara", "ojo", "calor", "ambulancia", "enfermera", "farmacia", "vitaminas", "pastillas", "dentista", "ciego", "correr", "caminar", "regresar", "saltar", "fin", "cerrar", "nombre", "mujer", "hombre", "soltero", "novio", "nacer", "vivir", "edad", "anciana","trabajar", "cobrar", "azafata", "artista", "panadero", "carpintero", "cocinero", "maestro", "bombero", "juez", "modelo", "monje", "pintor", "piloto", "secretaria", "taxista", "escritor", "jefe", "aprendiz", "jubilado", "empleo", "industria", "taller", "tienda", "vacaciones", "sueldo", "impuesto", "huelga", "obedecer", "locura", "humor", "inteligencia", "orgullo", "timidez", "valiente", "aburrido", "loco", "divertido", "bueno", "feliz", "amable", "pobre", "serio", "extraño", "gritar", "llorar", "suspirar", "preocupado", "risa", "amor", "suerte", "enamorado", "ver", "apagar", "luz", "color", "lupa", "microscopio", "claro", "cantar", "silbar", "voz", "eco", "trueno", "altavoz", "radio", "auricular", "liso", "comer", "dulce", "salado", "perfume", "despertarse", "vestirse", "desayunar", "leer", "dormirse", "toalla", "cobija", "almuerzo", "sopa", "agua", "leche", "jugo", "sal", "pimienta", "vinagre", "ajo", "perejil", "menta", "canela", "mayonesa", "pan", "mantequilla", "miel", "manzana", "pera", "durazno", "cereza", "papa", "lechuga", "arroz", "pollo", "pavo", "hamburguesa", "camarones", "tortilla", "espagueti", "sopa", "helado", "chocolate", "galletas", "bombones", "limpiar", "cortar", "hervir", "planchar", "aspiradora", "plancha", "horno", "abrelatas", "vajilla", "vaso", "cafetera", "azucarera", "comprar", "gastar", "vender", "barato", "caro", "gratis", "cliente", "bolsa", "precio", "recibo", "ascensor", "esquiar", "ciclismo", "golf", "pelota", "tenis", "bicicleta", "estadio", "gol", "torneo", "leer", "dibujar", "cantar", "bailar", "libro", "revista", "clavo", "cine", "pala", "cocina", "hielo", "coro", "piano", "cartas", "pesca", "radio", "noticias", "televisor", "documental", "anuncio", "aplaudir", "teatro", "circo", "mago", "disco", "portero", "propina", "regalo", "fiesta", "vela", "alfombra", "puerta", "ventana", "cortina", "escritorio", "cuadro", "juguete", "alquiler", "mudanza", "casa", "pared", "chimenea", "comedor", "plaza", "calle", "estacionamiento", "parque", "puente", "puerto", "edificio", "escuela", "museo", "estatua", "fuente", "turista", "mendigo", "manejar", "acelerar", "frenar", "cruzar", "reparar", "conductor", "multa", "atasco", "carretera", "peaje", "curva", "florecer", "campo", "bosque", "huerto", "selva", "tronco", "rama", "flor", "hoja", "musgo", "cedro", "roble", "pino", "nogal", "naranjo", "tallo", "clavel", "margarita", "amapola", "rosa", "girasol", "violeta", "gato", "perro", "vaca", "pato", "oveja", "conejo", "pez", "oso", "jirafa", "erizo", "mariposa", "foca", "tigre", "cobra", "almeja", "paloma", "cisne", "mosquito", "hormiga", "llover", "nevar", "nublado", "soleado", "clima", "rayo", "nieve", "sol", "viento", "padre", "madre", "hijo", "abuela", "estudioso", "aula", "tiza", "regla", "computadora", "diccionario"]
        self.aiword = 0
        self.guesslen = 0
        self.string = []
        self.usercompleteword = ''
        self.userletra = ''
        self.counterplace = 0
        self.lives = 7
        self.numtries = 0
    def game(self):
        self.ai_choose()
        while self.lives != 0 and self.palabras[self.aiword] != self.usercompleteword:
            print(self.string)
            self.usercompleteword = ''
            self.userguess()
            self.logic()
            self.userletra = ''
        if self.lives == 0:
            print("Perdiste")
        else:
            print("Correcto la palabra es", self.usercompleteword, self.palabras[self.aiword])
        self.cleanup()
    def logic(self):
        found = False
        for i in range(self.guesslen):
            if self.palabras[self.aiword][i] == self.userletra:
                self.string[i] = self.userletra
                found = True
        if not found:
            self.lives -= 1
    def userguess(self):
        self.userletra = input("Ingresa la letra que cree\n")
        self.userletra = self.userletra.lower()
    def ai_choose(self):
        self.aiword = random.randint(0,len(self.palabras)-1)
        self.guesslen = len(self.palabras[self.aiword])
        for i in range(self.guesslen):
            self.string.append('_ ')
    def cleanup(self):
                self.aiword = 0
                self.guesslen = 0
                self.string = []
                self.userletra = ''
                self.counterplace = 0
                self.lives = 7


while exit_menu == 1:
    print("Este es el menu de seleccion de juego")
    selecc_game = int(input("Que juego desea jugar?\n1.TicTacToe\n2.Numero al azar\n3.Adivino tu numero\n4.Piedra, Papel o Tijera\n5.Buscaminas\n6.Ahorcado\n"))
    if selecc_game == 1:
        GatoGame().game()
    elif selecc_game == 2:
        RandNum().game()
    elif selecc_game == 3:
        ai_guess().game()
    elif selecc_game == 4:
        PiePapTij().game()
    elif selecc_game == 5:
        MineSweeper().game()
    elif selecc_game == 6:
        Ahorcado().game()
    exit_menu = int(input("Desea seguir jugando? (1.Si / Else. No)"))

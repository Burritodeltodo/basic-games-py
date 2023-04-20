
from PIL import Image
import random
x , res, avi_sel, lis_com = 0,  0, 0, 0 #x=loop de codigo, res=eleccion de usuario para comparar con avi_sel, #avi_sel=avion seleccionado, lis_com=comparara el numero con lis_elec
lis_av = { 1:"Airbus A380" , 2:"Airbus A350" , 3:"Airbus A330" , 4:"Boeing 777" , 5:"Boeing 787" , 6:"Boeing 747"}
lis_elec = [] #Lista que se mostrara al usuario
resize=(1024,576)
img_a332 = Image.open("F:/PY/Aircraft_Game/A332.jpg")
img_a350 = Image.open("F:/PY/Aircraft_Game/A350.jpg")
img_a380 = Image.open("F:/PY/Aircraft_Game/A380.jpg")
img_b747 = Image.open("F:/PY/Aircraft_Game/B747.jpg")
img_b777 = Image.open("F:/PY/Aircraft_Game/B777.jpg")
img_b787 = Image.open("F:/PY/Aircraft_Game/B787.jpg")
img_a332 = img_a332.resize(resize)
img_a350 = img_a350.resize(resize)
img_a380 = img_a380.resize(resize)
img_b747 = img_b747.resize(resize)
img_b777 = img_b777.resize(resize)
img_b787 = img_b787.resize(resize)
def para_juego(lis_av): #inicia el juego tomando 4 aviones al azar, seleccionando 1 como su avion y retornar valores lis_elec & avi_sel
    lis_elec.append("void") #Se agrega un valor vacio por el ciclo for que se encuentra en el codigo principal (line 20) y asi escriba del 1-4 y tome valores de la lista al mismo tiempo
    while len(lis_elec) <5:
        lis_com = random.randint(1, 6)
        if lis_com not in lis_elec:
            lis_elec.append(lis_com)
    avi_sel = random.choices(lis_elec,weights=[0,1,1,1,1],k=1)
    return (lis_elec, avi_sel)

while x == 0:
    (selec_avi, avi_real) = para_juego(lis_av)
    print(avi_real)
    for i in range (1, 5):
        print(i, lis_av[lis_elec[i]])
    if avi_real == 1:
        img_a332.show()
    elif avi_real == 2:
        img_a350.show()
    elif avi_real == 3:
        img_a380.show()
    elif avi_real == 4:
        img_b747.show()
    elif avi_real == 5:
        img_b777.show()
    elif avi_real == 6:
        img_b787.show()
    res = int(input("¿Que avion es el de la imagen? "))
    lis_elec.clear()
    x=int(input("Desea seguir? (1=No//0=Si)"))
tamaño = int(input("INGRESE EL TAMAÑO DEL LADO: "))
lado =int(input("INGRESE EL NUMERO DE  LADOS: "))
import turtle
t = turtle.Pen()

def dibujo():
	for x in range(0,lado):
		t.forward(tamaño)
		t.left(360/lado)

dibujo()
turtle.getscreen()._root.mainloop()
import turtle
t = turtle.Pen()
lado = int(input("INGRESE NUMEOR DE LADOS: "))

for x in range(0,lado):
	t.forward(50)
	t.left(360/lado)
turtle.getscreen()._root.mainloop()
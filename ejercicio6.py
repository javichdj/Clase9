import turtle
t = turtle.Pen()
lado = int(input("INGRESE NUMEOR DE LADOS: "))

for x in range(1,5):
	t.forward(lado)
	t.left(90)


turtle.getscreen()._root.mainloop()
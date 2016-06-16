import turtle
t = turtle.Pen()
lado = int(input("INGRESE NUMERO DE LADOS: "))

t.reset()
for x in range(0,lado):
	t.forward(100)
	t.left(144)
turtle.getscreen()._root.mainloop()
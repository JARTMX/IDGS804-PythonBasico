dato1="hola"
dato2="mundo"

saludo=dato1+ " "+ dato2
print(saludo)

print("el saludo es %s %s" % (dato1,dato2))

saludoFinal="saludo {} {}".format(dato1,dato2)
print(saludoFinal)

saludoFinal="saludo {a} {b}".format(a=dato1,b=dato2)
print(saludoFinal)
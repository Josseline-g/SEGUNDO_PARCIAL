#Calcular la superficie de un rectangulo
#y cargar los datos de dos rectangulo y mostrar cual es el mayor

#Datos del primer rectangulo
base=int(input("Ingrese la base del rectangulo:"));
altura=int(input("Ingrese la altura del rectangulo:"));
superficie= (base*altura)
print ("La superficie es de:", superficie)

#Datos del segundo rectangulo
base2=int(input("Ingrese la base del segundo rectangulo:"));
altura2=int(input("Ingrese la altura del segundo rectangulo:"));
superficie2= (base2*altura2)
print ("La superficie es de:", superficie2)

#Rectangulo con mayor superficie

def mostrar_superficie_mayor (superficie,superficie2):
    print ("La superficie mayor es")
    if superficie>superficie2:
        print (superficie)
    else:
        superficie2>ssuperficie
        print (superficie2)

mostrar_superficie_mayor(superficie,superficie2)

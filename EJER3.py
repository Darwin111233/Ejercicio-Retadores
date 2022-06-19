#Nombre: Darwin Rafael Castro Garcia
#Grupo: 7
Kg_c_cemnt = 0
Kg_c_yes = 0
peso = 0
limite_Max = 3254
limite = 3254
Costal_cemento=int(input("Numero de costales de cemento: "))

Costal_yeso = int(input("Numero de costales de yeso: "))

Kg_c_cemnt += Costal_cemento*40
Kg_c_yes += Costal_yeso*30

peso += Kg_c_cemnt + Kg_c_yes 

Envio = peso >= limite_Max/2 and peso < limite



print("El peso total en (kg): ",peso)
print("¿Se puede realizar el envio? ",Envio)


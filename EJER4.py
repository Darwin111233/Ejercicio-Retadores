#Nombre: Darwin Rafael Castro Garcia
#Grupo: 7

N_cajas_Ven= int(input("Numero de cajas a vender: "))

Id_producto = int(input("Ingrese el Id del producto de las cajas: "))

if(Id_producto==1 ):
  productos =["Maiz"]
  print ("El producto es: ",productos[0])
  if(N_cajas_Ven<=100):
    Resultado_M = N_cajas_Ven * 285.55 + 1500
    print("El costo total a pagar es: ",Resultado_M)
  else:
    Resulta_M100_ =N_cajas_Ven * 285.55
    print("El costo total a pagar es: ",Resulta_M100_)

if(Id_producto==2):
  productos =["Pepino"]
  print ("El producto es: ",productos[0])
  if(N_cajas_Ven<=100):
    Resultado_P= N_cajas_Ven * 334.72 + 1500
    print("El costo total a pagar es: ",Resultado_P)
  else:
    Resultado_P100=N_cajas_Ven * 334.72
    print("El costo total a pagar es: ",Resultado_P100)
    if(Id_producto==3):
      productos =["Tomate_v"]
      print("El producto es: ",productos[0])
      if(N_cajas_Ven<=100):
        Resultado_Tv= N_cajas_Ven * 129.00 + 1500
        print("El costo total a pagar es: ",Resultado_Tv)
      else:
        Resultado_Tv100= N_cajas_Ven * 129.00
        print("El costo total a pagar es: ",Resultado_Tv100 )
        
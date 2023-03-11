opcion= 1

empanadas=[]

while opcion !=1:
    print("****Empanadas*****")
    print("opcion 1= Ingresar una empanada")
    print("opcion 2= Mostrar todas las empanadas")
    print("opcion 3= Buscar empanada por id")
    print("opcion 4= Editar empanada")
    print("opcion 5= Eliminar empanada")
    print("Preciona 0 para salir ")

    opcion=int(input("Ingresa la opcion: "))

    if(opcion==1):
        empanada={}
        empanada['id']=int(input("Digite el id de la empanada"))
        empanada['nombre']=int(input("Digite el nombre de la empanada"))
        empanada['precio']=float(input("Digite el precio de la empanada"))
        empanada['popularidad']=int(input("Digite la popularidad de la empanada"))
        empanada['fecha de vc']=input("Digite la fecha de vc de la empanada")
        empanadas.append(empanada)
        print("Empanadas registradas")
        
    elif(opcion==2):
        for empanada in empanadas:
            print(empanada)
    elif(opcion==3):
        buscarempa=int(input("ingrese el id de la empanada buscada: "))
        for empanada in empanadas:
            if( empanada['id']!=buscarempa):
                print("empanada no existe")
            else:
                print(f'Id Encontrado{empanada}')
                
    elif(opcion==4):
        buscarempa=int(input("ingrese el id de la empanada buscada: "))
        for empanada in empanadas:
            if( empanada['id']!=buscarempa):
                print("empanada no existe")
            else:
                print(f"el precio actual empanda es:{empanada ['precio']}")
                precioNuevo=float(input("Ingrese el nuevo precio: "))
                empanada["precio"]=precioNuevo
    elif(opcion==5):
        pass
    elif(opcion==0):
        pass
  
    else:
        print("opcion invalida")

  
    


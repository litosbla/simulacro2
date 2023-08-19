import json
def error(msg):
    print("\r!!!!!! Error: ",msg.upper())
    input("\t Digite cualquier tecla para continuar")

def leer_nombre(msg):
    while True: # numero de horas 
        try:
            nombre_agregar= input(msg)
            if  nombre_agregar.isalpha():
                return nombre_agregar
            error("Valor invalido")
            continue
        except ValueError:
            error("Valor invalido")
            continue
def leer_id(msg):
    while True: # id
        try:
            id_agregar=int(input(msg))
            if id_agregar>0:
                return id_agregar
                
            error("Valor negativo")
            continue
                    
        except ValueError:
            error("Valor invalido")
            continue
def leer_documento(msg):
    while True: # id
        try:
            id_agregar=int(input(msg))
            if id_agregar>0:
                return id_agregar
                
            error("Valor negativo")
            continue
                    
        except ValueError:
            error("Valor invalido")
            continue

def leer_nota(msg):
    while True: # numero de horas 
        try:
            nota_agregar= float(input(msg))
            if  nota_agregar>0 and nota_agregar<= 5:
                return nota_agregar
            error("Valor invalido")
            continue
        except ValueError:
            error("valor invalido")
            continue
def validar_otro_ciclo(msg):
    while True:
        try:
            y=input(msg)
            if y.lower() == "si":
                return True
            if y.lower() == "no":
                return False
            print("!@ valor invalido")
        except ValueError:
            print("!@ valor invalido")
            continue
def menu():
    while True:
        try:
            print("="*30)
            print("\tMENU")
            print("\t1- Mostrar en pantalla todas las mascotas\n\t2- Crear nueva mascota con multiples servicios\n\t3- Mostrar los datos de mascotas por tipo elegido(raza,precio y servicios)\n\t4- Actualizar los datos de una mascota consultada por indice\n\t5- Eliminar una mascota de la tienda por indice\n\t6- Salir")
            print("="*30)
            op=int(input("\t>> escoja una opción (1-6)"))
            
            if op <1 or op >8:
                error("!@ Valor invalido")
                continue
            return op
        except ValueError:
            error("!@ Valor invalido")
            continue
def services():
    lista=[]
    while True:
        try:
            servicio=input("\tDigite un servicio: ")
            if servicio.isalpha() and servicio not in lista:
                lista.append(servicio)
                if validar_otro_ciclo("\t@Desea ingresar otro servicio ? (si|no) "):
                    continue
                return lista
            error("valor invalido o repetido")
        except ValueError:
            error("valor invalido.")
            continue
                
def ingresar_datos():
    mascotas=leer_json()
    
    while True:  
        nom=len(mascotas["pets"])+1
        print(" "*15,f"\n\tDigite para la mascota #{nom}\n"," "*15)

        tipo=leer_nombre(f"\tDigite el tipo: ")
        # if True in [True for x in range(len(mascotas)) if mascotas[x]["codigo"]==documento]:
        #     error("Codigo repetido")
        #     continue
        
        raza=leer_nombre(f"\tDigite la raza: ")
        talla=leer_talla(f"\tDigite la talla: ")
        precio=leer_documento(f"\tDigite el precio: ")
        servicios=services()
        #definitiva= (nota1+nota2+nota3)/3
        datos={
                "tipo":tipo,
                "raza":raza,
                "talla":talla,
                "precio":precio,
                "servicios":servicios
                
            }
        mascotas["pets"].append(datos)
        

        
        
        if validar_otro_ciclo("\t@¿Quiere seguir agregando mascotas? (si|no) "):
            continue
        subir_json(mascotas)

        break
def validar_entero_string(key,value):
    if type(value) is int:
        print(f"\t{key} --->${value:,.0f}")
    
    else:
        print(f"\t{key} --->{value}")
def mostrar(dic_persona,i):
    print(" "*15,f"\n  Mascota {i+1} \n"," "*15)
    [[print(f"\tservicio {i+1} ---> {value[i]}") for i in range(len(value))] if type(value) is list else validar_entero_string(key,value) for key,value in dic_persona.items()]
    #[ ( [print(f"nota {i+1} ---> {value[i]}") for i in range(len(value))] if type(value) is list else print(key," ---> ",value)) for key,value in dic_persona.items() ]

def buscar_tipo():
    mascotas=leer_json()
    print(" "*15,f"\n Mostrar por tipo \n"," "*15)
    while True:
        codigo = leer_nombre("\tDigite el tipo de mascota que quiere buscar: ")
        if True in [True for x in range(len(mascotas["pets"])) if mascotas["pets"][x]["tipo"]==codigo]:
            [mostrar(mascotas["pets"][i],i) for i in range(len(mascotas["pets"])) if mascotas["pets"][i]["tipo"]==codigo]
            if validar_otro_ciclo("\t¿Desea buscar otro tipo? (si|no)"):
                continue
            break
        error("Codigo repetido")
        continue

def leer_talla(msg):
    lista=["pequeño","pequeña","mediano","mediana","grande"]
    while True:
        talla=leer_nombre(msg)
        if talla in lista:
            return talla
        error("talla incorrecta")
        continue
def Actualizar():

    tipo=leer_nombre(f"\tDigite el tipo: ")
    raza=leer_nombre(f"\tDigite la raza: ")
    talla=leer_talla(f"\tDigite la talla: ")
    precio=leer_documento(f"\tDigite el precio: ")
    servicios=services()

    datos={
            "tipo":tipo,
            "raza":raza,
            "talla":talla,
            "precio":precio,
            "servicios":servicios
            
        }
    
    return datos
    
def modificar_datos():
    mascotas=leer_json()
    while True:
        mostrar_todos()
        codigo=leer_id("Digite el numero de la mascota que quiere actualizar: ")-1
        if codigo < 0 or codigo >len(mascotas["pets"]):
            error("Mascota inexistente")
            continue

        datos_agregar=Actualizar()
        mascotas["pets"][codigo]=datos_agregar
        
        
        if validar_otro_ciclo("\t@Desea modificar otra mascota? (si|no) "):
            continue
        subir_json(mascotas)
        break
        
def borrar_datos():
    mascotas=leer_json()
    while True:
        mostrar_todos()
        codigo=leer_id("\tDigite el numero de la mascota que quiere borrar ")-1
        if codigo < 0 or codigo >len(mascotas["pets"]):
            error("Mascota inexistente")
            continue

        #datos_agregar=Actualizar()
        
        mascotas["pets"].pop(codigo)
        print("se ha borrado")
        
        
        if validar_otro_ciclo("\t@Desea eliminar otra mascota? (si|no)"):
            continue
        subir_json(mascotas)
        break
        
            
def mostrar_todos():
    mascotas=leer_json()
    [mostrar(mascotas["pets"][i],i) for i in range(len(mascotas["pets"]))]
    
# def borrar_datos_2(personas):
#     while True:
#         codigo=leer_id("Digite el codigo del estudiante que quiere borrar ")
#         if True in [True for x in range(len(personas)) if personas[x]["codigo"]==codigo]:
#             personas=[  personas[x] for x in range(len(personas))  if personas[x]["codigo"]!=codigo  ]
#             print("datos borrados")
#             if validar_otro_ciclo("Desea borrar otro estudiante?(si|no)"):
#                 continue
#             return personas
#         error("codigo no existe")
#         if validar_otro_ciclo("Desea borrar otro estudiante?(si|no)"):
#                 continue
#         return personas
# def defini(dic):
#     dic["definitiva"]=sum(dic["tres_notas"])/len(dic["tres_notas"])
#     return dic
# def calcular_definitiva(personas):
#     personas=[defini(personas[i]) for i in range(len(personas))]
#     return personas
# def mostrar_tipo(mascotas):
#     tipo=leer_nombre("Digite el tipo que quiere buscar")

def leer_json():
    with open("mascotas.json","r") as file:
        data=json.load(file)
    return data
def subir_json(data):
    with open("mascotas.json","w") as file:
        json.dump(data,file,indent=4)
    
def inicializar_json():
    with open("mascotas.json","w") as file:
        mascotas={}
        mascotas["pets"]=[]
        json.dump(mascotas,file,indent=4)

#1. Listar todas las ciudades, sin clasificar por departamento.
# 2. Adicionar una nueva ciudad en un departamento existente.
# 3. Eliminar una ciudad de un departamento
# 4. Crear un Departamento.
# 5. Eliminar un Departamento
# 6. Listar todos los Departamentos
def main():
    #inicializar_json()
    while True:
        op=menu()
        if op ==1:
            mostrar_todos()## mostrar 
        elif op==2:
            ingresar_datos()
        elif op==3:
            buscar_tipo()
        elif op==4:
            modificar_datos()
        elif op==5:
            borrar_datos()
        elif op==6:
            print("hasta luego")
            break
        
        
main()  
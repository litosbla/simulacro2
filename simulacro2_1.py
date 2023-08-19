import json

def leer_json():
    with open("paiscidudad.json","r") as file:
        data=json.load(file)
    return data
def subir_json(data):
    with open("paiscidudad.json","w") as file:
        json.dump(data,file,indent=4,ensure_ascii="utf-8")
def error(msg):
    print(f"\t@ error {msg.upper()}")
    input("\tDigite cualquier tecla para continuar")
def leer_string(msg):
    while True:
        try:
            caracter=input(msg)
            if caracter !="":
                return caracter
            error("caracter invalido")
            continue
        except ValueError:
            error("caracter invalido")
            continue
def leer_numero(msg):
    while True:
        try:
            caracter=int(input(msg))
            if caracter >0:
                return caracter
            error("valor invalido")
            continue
        except ValueError:
            error("valor invalido")
            continue
def leer_rango(msg,min,max):
    print(min,max)
    while True:
        try:
            caracter=leer_numero(msg)
            if caracter > min and caracter< max:
                return caracter
            error(f"caracter invalido, tiene que estar entre {min} y {max}")
            continue
        except ValueError:
            error(f"caracter invalido")
            continue
def menu():
# 1. Listar todas las ciudades, sin clasificar por departamento.
# 2. Adicionar una nueva ciudad en un departamento existente.
# 3. Eliminar una ciudad de un departamento
# 4. Crear un Departamento.
# 5. Eliminar un Departamento
# 6. Listar todos los Departamentos
    print("="*35,"\n\t Menú Paises y Departamentos \n","="*35)
    print("\t1. Listar todas las ciudades, sin clasificar por departamento.\n\t2. Adicionar una nueva ciudad en un departamento existente\n\t3. Eliminar una ciudad de un departamento\n\t4. Crear un Departamento.\n\t5. Eliminar un Departamento\n\t6. Listar todos los Departamentos\n\t7. salir")
    print("="*35)
    op =leer_rango("Digite la opcion que quiere ejecutar",0,8)
    return op
def mostrar_ciudad(ciudades_por_departamento):
     # parto de dic_ciudad.items()
    [[print(f"\t{key} ---- > {value}") if key != "coordenadas" else [print(f"\t{key_1} ---- > {value_1}")for key_1,value_1 in value.items()] for key, value in ciudades_por_departamento[i].items()]for i in range(len(ciudades_por_departamento))]

def listar_ciudades():
    pais=leer_json()
    #parto de pais["departamentos"][i]["ciudades"]
    [mostrar_ciudad(pais["Departamentos"][i]["Ciudades"])for i in range(len(pais["Departamentos"]))]
def leer_num_dif_lista(msg,msgerror,lista):
    while True:
        num=leer_numero(msg)
        if num not in lista:
            return num
        error(msgerror)
        continue
def leer_string_dif_lista(msg,msgerror,lista):
    while True:
        caracter=leer_string(msg).capitalize()
        if caracter not in lista:
            return caracter
        error(msgerror)
        continue
def valida_nom_ciudad_en_departamento(lista):
    while True:
        nombre=leer_string("Digite el nombre de la ciudad")
        if nombre not in lista:
            return nombre
        error("Ciudad existente en el departamento")
        continue
def validar_otro_ciclo(msg):
    while True:
        try:
            answer=input(msg)
            if answer.lower()=="si":
                return True
            if answer.lower()=="no":
                return False
            error("Valor invalido, debe ser -->(si/noo)")
            continue
        except ValueError:
            error("Valor invalido, debe ser -->(si/noo)")
            continue

def crea_lista_ciudades(lista_ids):
    ids_ciudades=lista_ids
    listaCiudad_en_dept=[]
    ciudades=[]
    while True:
        
        idCiudad=leer_num_dif_lista("Digite el id de la ciudad","id de ciudad existente",ids_ciudades)
        ids_ciudades.append(idCiudad)
        nomCiudad=valida_nom_ciudad_en_departamento(listaCiudad_en_dept)
        listaCiudad_en_dept.append(nomCiudad)
        imagen=nomCiudad.lower()+".jpg"
        coordenadas={"lat":23,"lon":72}
        datos={
            "idCiudad":idCiudad,
            "nomCiudad":nomCiudad,
            "imagen":imagen,
            "cordenadas":coordenadas
        }
        ciudades.append(datos)

        if validar_otro_ciclo("Desea seguir ingresando ciudades (si/no)"):
            continue
        return ciudades
def adicionar_ciudad():
    pais=leer_json()
    while True:
        ids_departamentos,nombres_departamentos,ids_ciudades=calcular_de_limitantes(pais)
        [print(i," --- > ",departamento)for i,departamento in enumerate(nombres_departamentos)]
        i=leer_rango("\tDigite el indice del departamento al que quiere agregar otra ciudad",0,len(nombres_departamentos)+1)
        while True:
            
        ciudades=crea_lista_ciudades(ids_ciudades)
        pais["Departamentos"][i]["Ciudades"].extend(ciudades)
        if validar_otro_ciclo("Desea agregar otra ")


def calcular_de_limitantes(pais):
    ids_departamentos=[dept["idDep"] for dept in pais["Departamentos"]]
    nombres_departamentos=[dept["nomDepartamento"] for dept in pais["Departamentos"]]
    ids_ciudades=[]  
    [ids_ciudades.extend([ciudad["idCiudad"] for ciudad in departamento["Ciudades"]]) for departamento in pais["Departamentos"]]
    return ids_departamentos,nombres_departamentos,ids_ciudades

def adicionar_departamentos():
    pais=leer_json()
    while True:
        ids_departamentos,nombres_departamentos,ids_ciudades=calcular_de_limitantes(pais)
        idDep=leer_num_dif_lista("Digite el id del departamento","Id existente",ids_departamentos)
        nomDepartamento=leer_string_dif_lista("Digite el nombre del departamento","Nombre existente",nombres_departamentos)
        Ciudades=crea_lista_ciudades(ids_ciudades)

        departamento={
            "idDep":idDep,
            "nomDepartamento":nomDepartamento,
            "Ciudades":Ciudades
        }
        pais["Departamentos"].append(departamento)
        if validar_otro_ciclo("Desea agregar otro departamento?"):
            continue
        break

    subir_json(pais)

def main():
    while True:
        op=menu()
        if op == 1:
            listar_ciudades()
        elif op == 2:
            adicionar_ciudad()
        elif op == 3:
            eliminar_ciudad_vs_departamento()
        elif op == 4:
            adicionar_departamentos()
        elif op == 5:
            eliminar_departamento()
        elif op == 6:
            listar_departamento()
        elif op == 7:
            salir()
        
main()
    

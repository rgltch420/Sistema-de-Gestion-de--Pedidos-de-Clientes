import re
client = {}

def is_valid_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(pattern, email)

def createClients():
    tries = 0
    id_client = 0
    while(True):
        try:
            tries_users = input("Cuantos usarios deseas ingresar: ").strip()
            tries_user_converted = int(tries_users)
            if tries_user_converted < 1:
                print("debe ser al menos 1")
                continue
            break
        except (ValueError,UnboundLocalError):
            print("Ingresa unicamente numeros positivos mayor a cero")   
        
    while tries_user_converted > tries :
        tries += 1 
        try:
            id_clients = input("Ingrese el ID del cliente: ").strip()
        except ValueError:
            print("Por favor ingresa un numero positivo mayor a 0")    
        name_client = input("Ingresa el nombre del cliente: ").strip()
        email_client = input("Ingresa el email del cliente: ").strip()
        id_client= int(id_clients)
        if id_client < 1: 
            print("Ingresa unicamente numeros positivos mayores a 1")
            tries -= 1
            id_client -= 1
            continue
        if not (name_client and id_client):
            print("No dejar campos vacios o espacios vacios")
            tries -= 1
            id_client -= 1
            continue
        if not is_valid_email(email_client):
            print("Ingresa un email válido (ej: xxxxx@xxxx.com)")
            tries -= 1
            id_client -= 1
            continue     
        client[id_client]={
        "Name": name_client,
        "Email": email_client
    }
        print(f"Cliente {client[id_client]['Name']} fue creado exitosamente con su mail {client[id_client]['Email']}")
        
        return id_client
        
       
    else:
        print("Ingresaste correctamente todos los usuarios")
        
           
  
createClients()  
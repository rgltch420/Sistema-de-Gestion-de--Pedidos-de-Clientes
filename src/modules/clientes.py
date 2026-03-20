import re
client = {}

def is_valid_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(pattern, email)

def createClients():
   

    while(True):
        try:
            tries_user_converted = int(input("Cuantos usarios deseas ingresar: ").strip())
            if tries_user_converted < 1:
                print("debe ser al menos 1")
                continue
            break
        except ValueError:
            print("Ingresa unicamente numeros validos")   
        
    tries = 0

    while tries_user_converted > tries :

        try:
            id_client= int(input("Ingrese el ID del cliente: ").strip())
            if id_client < 1: 
                print("El ID debe ser mayor a 0")
                continue
            
        except ValueError:
            print("ID invalido")
            continue    
        
      
        if id_client in client:
            print("Ese id ya existe")
            continue

        name_client = input("Ingresa el nombre del cliente: ").strip()    
        if not name_client:
            print("El nombre no puede estar vacio")
            continue

        email_client = input("Ingresa el email del cliente: ").strip()
        if not is_valid_email(email_client):
            print("Ingresa un email válido (ej: xxxxx@xxxx.com)")
            continue 

        client[id_client]={
        "Name": name_client,
        "Email": email_client
    }
        print(f"Cliente {client[id_client]['Name']} fue creado exitosamente con su mail {client[id_client]['Email']}")    
        tries += 1 
    return client
        
       
    
        
           
  
def get_client(id_client):
    return client.get(id_client)
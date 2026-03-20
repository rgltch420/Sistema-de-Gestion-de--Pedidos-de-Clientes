import re

client = {}

def is_valid_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return bool(re.match(pattern, email))


def create_clients():

    while True:
        try:
            total_users = int(input("How many users do you want to register?: ").strip())
            if total_users < 1:
                print("You must register at least 1 user")
                continue
            break
        except ValueError:
            print("Enter only valid numbers")

    count = 0

    while count < total_users:

        try:
            id_client = int(input("Enter client ID: ").strip())
            if id_client < 1:
                print("ID must be greater than 0")
                continue

        except ValueError:
            print("Invalid ID")
            continue

        if id_client in client:
            print("This ID already exists")
            continue

        name_client = input("Enter client name: ").strip()
        if not name_client:
            print("Name cannot be empty")
            continue

        email_client = input("Enter client email: ").strip()
        if not is_valid_email(email_client):
            print("Enter a valid email (e.g: example@mail.com)")
            continue

        client[id_client] = {
            "Name": name_client,
            "Email": email_client
        }

        print(f"Client {name_client} was successfully created with email {email_client}")
        count += 1

    return client


def get_client(id_client):
    return client.get(id_client)
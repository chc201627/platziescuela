import sys

clients  = [
    {
        'name' : 'Camilo',
        'company' : 'Google',
        'email' : 'camilo@google.com',
        'position' : 'Software engineer',
    },
    {
        'name' : 'Ricardo',
        'company' : 'Facebook',
        'email' : 'ricado@facebook.com',
        'position' : 'Data engineer',
    }


]

def create_client(client):
    global clients
    if client not in clients:
        clients.append(client)
     
    else:
        print("Client alreade is in the client\'s list")

def ingress_client_data():
    client= {
            'name' : _get_client_field('name'),
            'company': _get_client_field('company'),
            'email' : _get_client_field('email'),
            'position'  : _get_client_field('position'),
        }
    
    return client
            

def list_clients():
    for idx, client in enumerate(clients):
        print(" {uid} | {name} | {company} | {email} | {position}".format(
        uid=idx,
        name = client['name'],
        company= client['company'],
        email = client['email'],
        position = client['position']
        ))

def update_client(client_id, update_client_name):
    global clients
    
    if len(clients) -1 >= client_id :
         clients[client_id] = update_client_name
    else:
        _print_client_not_list()

def delete_client(client_id):
    global clients
    for idx, client in enumerate(clients):
        if idx == client_id:
            del clients[idx]
            break
    
  

def search_client(client_name):
    global clients  
    for client in clients:
        if client['name'] != client_name:
            continue
        else:
            return True



def _print_welcome():
    print('WELCOME TO PLATZI VENTAS')
    print ('*'*50)
    print ('what would you like to do today ? ')
    print ('[C]reate clients')
    print ('[L]ist clients ')
    print ('[U]pdate clients')
    print ('[D]elate clients')
    print ('[S]earch clients')

def _get_client_field(field_name):
        field = None
        
        while not field:
            field = input("What is the client {}?".format(field_name))
        
        return field

def get_client_name():
    client_name = None

    while not client_name:
        client_name = input ('What is the client name?')
    
        
        if client_name == 'exit' or client_name == 'EXIT':
            client_name = None
            break
    
    if not client_name:
        sys.exit()

    return client_name

def _print_client_not_list():
    return   print('Client is not in client list')

i

if __name__ == '__main__':
    _print_welcome()

    command = input()
    command = command.upper()

    if command == 'C':
        client = ingress_client_data()

        create_client(client)
        list_clients()
    elif command == 'L':
        list_clients()
    elif command == 'U':
        client_id = int(_get_client_field('id'))
        updated_client = ingress_client_data()

        update_client(client_id, updated_client)
        list_clients()
    elif command == 'D':
        client_id = int(_get_client_field('id'))

        delete_client(client_id)
        list_clients()
    elif command == 'S':
        client_name = _get_client_field('name')
        found = search_client(client_name)
        
        if found:
            print('The client is in the client\'s list')
        else:
            print('The client: {} is not in our client\'s list'.format(client_name))
    else:
        print('Invalid command')
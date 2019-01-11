import sys

clients  = ['Camilo','Ernesto','Juan']

def create_client(client_name):
    global clients
    if client_name not in clients:
        clients.append(client_name)
     
    else:
        print('Client alreade is in the client\'s list')
        

def list_clients():
    for idx, client in enumerate(clients):
        print("{}:{}".format(idx, client))

def update_client(client_name, update_client_name):
    global clients
    if client_name in clients:
        index = clients.index(client_name)
        clients[index] = update_client_name
    else:
        _print_client_not_list()

def delete_client(client_name):
    global clients
    if client_name in clients:
        clients.remove(client_name)
    else:
       _print_client_not_list()

def search_client(client_name):
    global clients  
    for client in clients:
        if client != client_name:
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

if __name__ == "__main__":

    _print_welcome()

    command = input()
    command = command.upper()


    if command == 'C':
        client_name = get_client_name()
        create_client(client_name)
        list_clients()
    elif command == 'L':
        list_clients()
    elif command =='D':
        client_name = get_client_name()
        delete_client(client_name)
        list_clients()
    elif command == 'U':
        client_name = get_client_name()
        update_client_name=input('What is the updated client name? ')
        update_client(client_name, update_client_name)
        list_clients()
    elif command =='S':
        client_name = get_client_name()
        found  = search_client(client_name)

        if found:
            print("The client is in the client' list")
        else:
            print ("The cliente: {} is not in our client's list".format(client_name))
    else:
        print('Invalid command')

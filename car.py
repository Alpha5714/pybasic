

command =""
while command != "quit":


    command = input('enter your command')
    if command.lower()=="start":
        print('STARTED LETS GOO')
        
    elif command.lower()=="stop":
        print("The car has stopped")
    elif command.lower() == 'help':
        print('start- to start the car'
              'stop- to stop the car'
              'quit to quit the game')
    elif command.lower() == 'quit':
        break
    else:
        print('I am working on that')
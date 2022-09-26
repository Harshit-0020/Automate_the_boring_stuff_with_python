list_of_commands = '''start - to start the car
stop - to stop the car
quit - to exit '''
help_command = "HELP"
start_command = "START"
quit_command = "QUIT"
stop_command = "STOP"
command = ""
car_started = False
while True:
    command = input("> ").upper()
    if command == help_command:
        print(list_of_commands)
    elif command == quit_command:
        break
    elif command == start_command:
        if car_started:
            print("Car is already started !!!")
        else:
            car_started = True
            print("Car started...Ready to go")
    elif command == stop_command:
        if not car_started:
            print("Car is already stopped.")
        else:
            car_started = False
            print("Car stopped.")

from parking import Parking
import sys

p = None

def process_command(command) :
    global p
    command = [ x for x in command.split(' ') if len(x) > 0 ]
    if len(command) == 0 : 
        return
    if command[0] == "create_parking_lot" :
        p = Parking(command[1])
        print("\n")
    
    if command[0] == 'park' :
        p.park(command[1],command[2])
        print("\n")
    elif command[0] == 'leave' :
        p.leave(command[1])
        print("\n")
    elif command[0] == 'status' :
        p.status()
        print("\n")
    elif command[0] == 'registration_numbers_for_cars_with_colour' :
        p.registation_number_of_cars_with_colour(command[1])
        print("\n")
    elif command[0] == 'slot_number_for_registration_number':
        p.slot_number_for_registration_number(command[1])
        print("\n")
    elif command[0] == 'exit' :
        sys.exit(0)


if __name__ == '__main__' :
    if len(sys.argv) > 1 :
        file_name = sys.argv[1]
        for line in open(file_name,'r') :
            process_command(line.strip())

    else :
        while True :
            line = raw_input()
            process_command(line.strip())

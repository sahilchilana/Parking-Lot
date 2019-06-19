# Parking-Lot
Code for creating a simple parking lot  
1. Runner file run.py  
2. car.py handles information about the car example registration number and colour  
3. lot.py handles information regarding the slot for one instance  
4. parking.py corresponds to slot allocation and other commands  
5. To run using input file:
  `python run.py files_input.txt`  
6. Commands for running from command line  
    * create_parking_lot number  : creates a parking lot of specified number  
    * park reg_no color : parks the car in the nearest slot
    * leave slot_no : removes the car from the slot no provided
    * status  : gives the status of the parking lot
    * registration_numbers_for_cars_with_colour color : gets the registration number corresponding to the color of the car
    * slot_number_for_registration_number reg_no : gets the slot number for the car with the registration number provided
    * exit : exits the program

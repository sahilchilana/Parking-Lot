from car import Car
from lot import PSlot

class Parking():

    def __init__(self, no_of_slots):
        self._slots_ = []
        self._no_of_occupied_slots_ = 0
        try :
            no_of_slots = int(no_of_slots)
        except Exception as e :
            raise Exception("No of slots should be of type int")

        if no_of_slots <= 0 :
            raise Exception("Invalid no of slots.")

        for i in range(no_of_slots):
                self._slots_.append(PSlot(slot_no=i,
                                    available=True))
        
        print("Created a parking lot with %s slots" %no_of_slots)

    def get_nearest_available_slot(self):

        if self._no_of_occupied_slots_ == len(self._slots_) :
            return -1

        for slot in self._slots_ :
            if slot.get_available() :
                return slot.get_slot_no()

    def park(self, reg_no, colour):

        available_slot = self.get_nearest_available_slot()
        if available_slot != -1:
            car = Car(reg_no=reg_no,colour=colour)
            self._slots_[available_slot].set_car(car)
            self._slots_[available_slot].set_available(False)
            self._no_of_occupied_slots_ += 1
            print("Allocated slot number: %s" % (available_slot+1))
        else:
            print("Sorry, parking lot is full.")

    def leave(self, slot_no):

        try :
            slot_no = int(slot_no)
        except Exception as e :
            raise Exception("Slot no should be of type int")

        if (slot_no-1) >= len(self._slots_) :
            raise Exception("Invalid slot no")

        
        if self._slots_[(slot_no-1)].get_available() :
            print("No car was parked at this slot")
            return

        self._slots_[(slot_no-1)].set_available(True)
        self._no_of_occupied_slots_ -= 1
        print("Car was removed from slot number: %s" %slot_no)

    def status(self):

        if self._no_of_occupied_slots_ == 0 :
            print("No car parked")
            return
        print("Slot No\tRegistration No\tColour")
        for i in self._slots_ :
            if not i.get_available() :
                car = i.get_car()
                print("%s\t%s\t\t%s" % ((i.get_slot_no()+1), car.get_reg_no(), car.get_colour()))


    def slot_number_for_registration_number(self, reg_no):

        for lot in self._slots_ :
            if not lot.get_available() :
                car = lot.get_car()
                if car.get_reg_no() == reg_no :
                    print("Car is parked at lot number :%s" %(lot.get_slot_no()+1))
                    return lot.get_slot_no()

        print("Car with given registration number not found")
        return -1

    def registation_number_of_cars_with_colour(self,colour) :
        cnt = 0
        reg_no = []
        for lot in self._slots_ :
            if not lot.get_available() :
                car = lot.get_car()
                if car.get_colour() == colour :
                    reg_no.append(car.get_reg_no())
                    cnt += 1
        
        if cnt == 0 :
            print("No car of the given colour found")
        else:
            print(', '.join(reg_no))
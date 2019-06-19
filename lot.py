from car import Car
class PSlot(object):

    def __init__(self, slot_no=None, available=None):
        self._car_ = None
        self._slot_no_ = slot_no
        self._available_ = available

    def get_car(self):
        if not self._car_ :
            raise Exception("No car was present in the lot")
        return self._car_

    def set_car(self, value):
        if type(value) != type(Car()) :
            raise Exception("Value of type Car expected")
        self._car_ = value

    def get_slot_no(self):
        return self._slot_no_

    def get_available(self):
        return self._available_

    def set_available(self, value):
        self._available_ = value




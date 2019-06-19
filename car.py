
class Car:

    def __init__(self,reg_no=None,colour=None):
        self._reg_no_ = reg_no
        self._colour_ = colour

    def get_reg_no(self):
        if not self._reg_no_ :
            raise Exception("Registration Number not assigned")
        return self._reg_no_

    def set_reg_no(self, value):
        self._reg_no_ = value

    def get_colour(self):
        if not self._colour_ :
            raise Exception("Colout of Car Not assigned")
        return self._colour_

    def set_colour(self, value):
        self._colour_ = value


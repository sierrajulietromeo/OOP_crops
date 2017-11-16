#http://pythonschool.net/oop/adding-methods-to-our-class/
class Crop:
    """A generic good crop"""

    #constructor
    def __init__(self, growth_rate, light_need, water_need):
        #set the attributes with an initial

        self._growth = 0
        self._days_growing = 0
        self._growth_rate = growth_rate
        self._light_need = light_need
        self._water_need = water_need
        self._status = "Seed"
        self._type = "Generic"

        #above attribibutes are prefixed with an underscore to indicate
        #that they should not be accessed outside the class.

        #when you create any method, you must pass self as a parameter
    def needs(self):
        #return a dictionary containing the light and water needs.
        return {"light need":self._light_need,"water need":self._water_need}

        #method to report
    def report(self):
        #return a dictionary containing the type, status, growth and days growing.
        return {"type":self._type,"status":self._status,"growth":self._growth, "days growing":self._days_growing }


def main ():
    #instantiate an object of the class.
    new_crop = Crop(1,4,3)
    #test
    print(new_crop.needs())
    print(new_crop.report())


if __name__ == "__main__":
    main()

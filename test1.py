



class a(object):
    """docstring for a"""
    def __init__(self, arg = 0):
        super(a, self).__init__()
        self.__arg = arg

    @property
    def arg(self):
        return self.__arg

    @arg.setter
    def arg(self, args):
        if args < 10:
            self.__arg = args
        else:
            print("Bad input")


x = a()
print(x._a__arg)

x.arg = 11
print(x.arg)

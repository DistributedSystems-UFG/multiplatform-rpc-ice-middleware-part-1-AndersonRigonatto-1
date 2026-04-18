import sys, Ice
import Demo

class PrinterI(Demo.Printer):
    def printString(self, s, current=None):
        print(s)
        return s + "*"

    def sum(self, a, b, current=None):
        print(f"sum({a}, {b})")
        return a + b

    def average(self, values, current=None):
        print(f"average({list(values)})")
        if not values:
            return 0.0
        return sum(values) / len(values)

    def reverseString(self, s, current=None):
        print(f"reverseString({s!r})")
        return s[::-1]

communicator = Ice.initialize(sys.argv)

adapter = communicator.createObjectAdapterWithEndpoints("SimpleAdapter", "default -p 11000")
object = PrinterI()
adapter.add(object, communicator.stringToIdentity("SimplePrinter"))
adapter.activate()

communicator.waitForShutdown()

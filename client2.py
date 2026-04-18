import sys, Ice
import Demo

communicator = Ice.initialize(sys.argv)

base1 = communicator.stringToProxy("SimplePrinter1:tcp -h 98.90.53.6 -p 11000")
base2 = communicator.stringToProxy("SimplePrinter2:tcp -h 98.90.53.6 -p 11000")
printer1 = Demo.PrinterPrx.checkedCast(base1)
printer2 = Demo.PrinterPrx.checkedCast(base2)
if (not printer1) or (not printer2):
    raise RuntimeError("Invalid proxy")

print(printer1.printString("Hello World from printer1!"))
print(printer2.printString("Hello World from printer2!"))

print("printer1.sum(10, 20) =", printer1.sum(10, 20))
print("printer2.sum(100, 250) =", printer2.sum(100, 250))

print("printer1.average([10.0, 20.0, 30.0]) =", printer1.average([10.0, 20.0, 30.0]))
print("printer2.average([2.5, 7.5]) =", printer2.average([2.5, 7.5]))

print("printer1.reverseString('distributed') =", printer1.reverseString("distributed"))
print("printer2.reverseString('systems') =", printer2.reverseString("systems"))

communicator.waitForShutdown()

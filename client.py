import sys, Ice
import Demo

communicator = Ice.initialize(sys.argv)

base = communicator.stringToProxy("SimplePrinter:tcp -h 98.90.53.6 -p 11000")
printer = Demo.PrinterPrx.checkedCast(base)
if not printer:
    raise RuntimeError("Invalid proxy")

print(printer.printString("Hello World!"))
print("sum(7, 35) =", printer.sum(7, 35))
print("average([1.0, 2.0, 3.0, 4.0]) =", printer.average([1.0, 2.0, 3.0, 4.0]))
print("reverseString('Hello World!') =", printer.reverseString("Hello World!"))

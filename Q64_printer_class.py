
# Q64: Printer Class and Three Objects

class Printer:

    def __init__(self, print_capacity, color_mode, printer_type):

        self.print_capacity = print_capacity
        self.color_mode = color_mode
        self.printer_type = printer_type

    def display(self):

        print("Print Capacity:", self.print_capacity, "pages per minute")
        print("Color Mode:", self.color_mode)
        print("Printer Type:", self.printer_type)


# Create three printer objects
printer1 = Printer(30, "Color", "Inkjet")
printer2 = Printer(40, "Monochrome", "Laser")
printer3 = Printer(25, "Color", "Laser")

# Display printer details and object identities
print("Printer 1")
printer1.display()
print("Object Identity:", id(printer1))

print("\nPrinter 2")
printer2.display()
print("Object Identity:", id(printer2))

print("\nPrinter 3")
printer3.display()
print("Object Identity:", id(printer3))

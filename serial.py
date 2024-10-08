"""Python serial number generator."""

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """

    '''Initializes self and start. Sets self.start and self.next to the start value'''
    def __init__(self, start):
        self.start = self.next = start

    '''Returns start value, everytime fx is called, returns next sequential number'''
    def generate(self):
        self.next += 1
        return self.next - 1 
    
    '''Resets current value(self.next) to the original start value(self.start)'''
    def reset(self):
        self.next = self.start
        

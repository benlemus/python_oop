from random import choice

"""Word Finder: finds random words from a dictionary."""
class WordFinder:
    '''Initializes attributes. Opens file, calls to parse file into a list and displays the amount of words read.'''
    def __init__(self, file):
        file = open(file)

        self.words = self.parse(file) 
        print(f'{len(self.words)} words read')
    
    '''Represents what WordFinder does. Shows example of what should be the output'''
    def __repr__(self):
        return f'<SerialGenerator start={self.start} next={self.start + 1}'

    '''Returns a list of parsed words stripped of whitespace'''
    def parse(self, file):
        return [word.strip() for word in file]
    
    '''Returns a random word from parsed list'''
    def random(self):
        return choice(self.words)
    
'''Special Word Finder: finds a random word from a file but does not include comments.'''
class SpecialWordFinder(WordFinder):

    '''Returns a parsed list from file of words all stripped of whitespace and does not include comments'''
    def parse(self, file):
        return [word.strip() for word in file if word.strip() and not word.startswith('#')]


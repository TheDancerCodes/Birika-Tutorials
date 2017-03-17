# Open Python Shell

# >>> from post_mortem_pdb import *
# >>> add_one_hundred()
# Enter a number between 1 and 10: test

#NB: Python provided us with a traceback, which is really just the details 
# about what happened when it encountered the error.
# Most of the time, the error messages associated with a traceback are very helpful.

def add_one_hundred():
    again = 'yes'
    while again == 'yes':
        number = raw_input('Enter a number between 1 and 10: ')
        new_number = (int(number) + 100)
        print '{} plus 100 is {}!'.format(number, new_number)
        again = raw_input('Another round, my friend? (`yes` or `no`) ')
    print "Goodbye!"

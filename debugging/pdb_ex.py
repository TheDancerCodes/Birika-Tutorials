# Ultimately, the program was generating new numbers for comparison within the elif
# causing the user input to be wrong each time.

# Additionally, in the comparison -  elif answer == num1 * num2 - the answer is a
# string while num1 and num2 are integers.

# To fix this, you just need to caste the answer to an integer.

import sys
# import pdb
from random import choice

random1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
random2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

while True:
    print "To exit this game type 'exit'"
    num1 = choice(random2)
    num2 = choice(random1)
    answer = int(raw_input("What is {} times {}?".format(num1, num2)))

    # pdb.set_trace()

    # answer = raw_input("What is {} times {}? ".format(choice(random2), choice(random1)))

    # exit
    if answer == "exit":
        print "Now exiting game!"
        sys.exit()

    # determine if number is correct
    elif answer == num1 * num2:
        print "Correct!"
        break
    else:
        print "Wrong!"


    # test = int(choice(random2))*int(choice(random1))

    # determine if number is correct
    # elif answer == choice(random2) * choice(random1):
    #     print "Correct!"
    # else:
    #     print "Wrong!"

# Example: setting breakpoints, which allow you to pause code execution at a certain line


# Here, we started the debugger on line 11, then set a breakpoint on line 5.
# We continued the program until it hit that breakpoint.
# Then we checked the value of num- 0.
#
# We set another break at line 12, then continued again and
# said that the result was 1 - result = 0 + 1 - which is what we expected.
# Then we did the same process again and found that the next result was 2 based
# on the value of num - result = 1 + 1.


# Workflow

# > /debugging/pdb_ex2.py(11)main()
# -> for num in xrange(0, 10):
# (Pdb) b 5
# Breakpoint 1 at /debugging/pdb_ex2.py:5
# (Pdb) c
# > /debugging/pdb_ex2.py(5)add_one()
# -> result = num + 1
# (Pdb) args
# num = 0
# (Pdb) b 12
# Breakpoint 2 at /debugging/pdb_ex2.py:12
# (Pdb) c
# 1
# > /debugging/pdb_ex2.py(12)main()
# -> add_one(num)
# (Pdb) b 5
# Breakpoint 3 at /debugging/pdb_ex2.py:5
# (Pdb) c
# > /debugging/pdb_ex2.py(5)add_one()
# -> result = num + 1
# (Pdb) args
# num = 1
# (Pdb) c
# 2
# > /debugging/pdb_ex2.py(12)main()
# -> add_one(num)

import pdb


def add_one(num):
    result = num + 1
    print result
    return result

def main():
    pdb.set_trace()
    for num in xrange(0, 10):
        add_one(num)


if __name__ == "__main__":
    main()

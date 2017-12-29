'''
@author: Nick DeMasi

Code to complete Day 7 of 2017 Advent of
Code using Python 3

'''


import os


ABS_PATH = 'C://Users/ldema/Coding/python_projects/adventofcode2017'


class Register(object):
    def __init__(self):
        self.variables = {}

    def find_max(self):
        '''Finds largest variable in register'''
        max_val = 0
        max_var = ''
        for var in self.variables.keys():
            if self.variables[var] > max_val:
                max_val = self.variables[var]
                max_var = var

        return max_var

    def read_instruction(self, instruction):
        '''Make changes to register according to instruction'''

        # split instruction into parts
        i_split = instruction.split(" ")

        # store each part of the instruction
        var = i_split[0]
        mod = i_split[1]
        val = int(i_split[2])
        d_var = i_split[4]
        conditional = i_split[5]
        mod_val = int(i_split[6])

        # if var not yet encountered, initialize at 0
        if var not in self.variables.keys():
            self.variables[var] = 0

        # if dependednt var not yet encountered, initialize at 0
        if d_var not in self.variables.keys():
            self.variables[d_var] = 0

        # generate function
        function = self.__generate_function(mod, conditional)

        # check that function exists
        if function == None:
            raise ValueError("Unable to generate function")

        # carry out instruction
        function(self.variables[var], val, self.variables[d_var], mod_val)

    def __generate_function(self, mod, conditional):
        '''Function generation engine'''
        if conditional == '==' and mod == 'inc':
            def f(var, val, d_var, mod_val):
                if d_var == val:
                    var += mod_val
        elif conditional == '==' and mod == 'dec':
            def f(var, val, d_var, mod_val):
                if d_var == val:
                    var -= mod_val
        elif conditional == '!=' and mod == 'inc':
            def f(var, val, d_var, mod_val):
                if d_var != val:
                    var += mod_val
        elif conditional == '!=' and mod == 'dec':
            def f(var, val, d_var, mod_val):
                if d_var != val:
                    var -= mod_val
        elif conditional == '>=' and mod == 'inc':
            def f(var, val, d_var, mod_val):
                if d_var >= val:
                    var += mod_val
        elif conditional == '>=' and mod == 'dec':
            def f(var, val, d_var, mod_val):
                if d_var >= val:
                    var -= mod_val
        elif conditional == '<=' and mod == 'inc':
            def f(var, val, d_var, mod_val):
                if d_var <= val:
                    var += mod_val
        elif conditional == '<=' and mod == 'dec':
            def f(var, val, d_var, mod_val):
                if d_var <= val:
                    var -= mod_val
        elif conditional == '>' and mod == 'inc':
            def f(var, val, d_var, mod_val):
                if d_var > val:
                    var += mod_val
        elif conditional == '>' and mod == 'dec':
            def f(var, val, d_var, mod_val):
                if d_var > val:
                    var -= mod_val
        elif conditional == '<' and mod == 'inc':
            def f(var, val, d_var, mod_val):
                if d_var < val:
                    var += mod_val
        elif conditional == '<' and mod == 'dec':
            def f(var, val, d_var, mod_val):
                if d_var < val:
                    var -= mod_val
        else:
            return None

        return f


if __name__ == '__main__':
    path = os.path.join(ABS_PATH, 'input/day8.txt')
    file = open(path, 'r')
    instructions = file.read().split('\n')

    register = Register()
    for i in instructions[:-1]:
        register.read_instruction(i)

    print("Part 1:        ", max(register.variables.values()))

'''
Created on Jul 8, 2018

@author: Syed Faizan
'''
import config
import sys

class ArithmetricExpression(object):
    '''
    classdocs
    '''

    express = 'cat'
    def __init__(self, statement):
        '''
        Constructor
        '''
        self.statement = statement
        
    def getExpression(self):
        # Sets arithExpress to anything after the equal sign
        arithExpress = self.statement[self.statement.find('=') + 1::].rstrip()
        # If the Key isn't found in the dictionary throw an error
        try:
            # Replaces all the variables in the string so that eval() can handle the arithmetic properly
            for i in range(0,len(arithExpress)):
                # If part of the arithmetic expression is a variable replace it with the variable value
                if arithExpress[i].isalpha():
                    arithExpress = arithExpress.replace(arithExpress[i],str(config.variables[arithExpress[i]]))
            # returns the result of the arithmetic expression
            return  int(eval(arithExpress))
        except KeyError:
            sys.stderr.write('Undeclared Variable in line : '+ self.statement)
            sys.exit()

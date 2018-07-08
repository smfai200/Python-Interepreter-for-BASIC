
import config
class BooleanExpression(object):
    '''
    classdocs
    '''


    def __init__(self,booleanStatement):
        '''
        Constructor
        '''
        self.booleanStatement = booleanStatement
        
    def compare(self):
        expression = self.booleanStatement[self.booleanStatement.find('IF') + 3:self.booleanStatement.find('GOTO')].rstrip()
        expression = BooleanExpression.replaceVar(self,expression)
        splitExpression = expression.split()
        result = False
        if '<=' in expression:
            if int(splitExpression[0]) <= int(splitExpression[2]):
                result = True
        elif '=' in expression:
            if int(splitExpression[0]) == int(splitExpression[2]):
                result = True
        elif '>=' in expression:
            if int(splitExpression[0]) >= int(splitExpression[2]):
                result = True
        elif '<>' in expression:
            if int(splitExpression[0]) != int(splitExpression[2]):
                result = True
        elif '<' in expression:
            if int(splitExpression[0]) < int(splitExpression[2]):
                result = True
        elif '>' in expression:
            if int(splitExpression[0]) > int(splitExpression[2]):
                result = True
        return result
    
    def replaceVar(self,statement):
        for i in range(0,len(statement)):
            if statement[i].isalpha():
                statement = statement.replace(statement[i],str(config.variables[statement[i]]))
        return statement
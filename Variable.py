import config

class Variable(object):
    '''
    classdocs
    '''

    
    def __init__(self,statement):
        '''
        Constructor
        '''
        self.statement = statement
        
    def getVariable(self):
        return
    
    def setVariable(self,expression):
        varStatement = self.statement.split()
        config.variables[varStatement[2]] = expression    

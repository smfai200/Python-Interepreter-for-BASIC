from Statement import Statement
import config
import sys
class PrintStatement(Statement):
    '''
    classdocs
    '''


    def __init__(self, statementLine):
        super (PrintStatement, self).__init__(statementLine)
        self.statement = statementLine
        
    def execute (self):
        
        printStatement = self.statement.split()
        try:
            return print(config.variables[printStatement[2]])
        except  KeyError:
            sys.stderr.write('Undeclared Variable ine line : '+ self.statement)
            sys.exit()
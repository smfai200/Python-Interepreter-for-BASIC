from Statement import Statement
import sys
class StopStatement(Statement):
    '''
    classdocs
    '''


    def __init__(self, statementLine):
        super (StopStatement, self).__init__(statementLine)
        self.statement = statementLine
        
    def execute (self):
        sys.exit()
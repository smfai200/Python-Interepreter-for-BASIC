
from Statement import Statement
import config

class GotoStatement(Statement):
    '''
    classdocs
    '''

    def __init__(self, statementLine):
        super (GotoStatement, self).__init__(statementLine)
        self.statement = statementLine
        
    def execute (self):
        # goToStatement is a string that gets everything after the GOTO part of the string
        goToStatement = self.statement[self.statement.find('GOTO') + 4::].rstrip()
        # Change the loop index to the new line number - 1 so that it process the
        # line number next
        config.index = int(goToStatement) -1

from Statement import Statement
from BooleanExpression import BooleanExpression
from GotoStatement import GotoStatement
class IfStatement(Statement):
    '''
    classdocs
    '''


    def __init__(self, statementLine):
        super (IfStatement, self).__init__(statementLine)
        self.statement = statementLine
        
    def execute (self):  
        # If the boolean Expression is true then create a Goto Statement and execute it
        if BooleanExpression(self.statement).compare():
            GotoStatement(self.statement).execute()
        
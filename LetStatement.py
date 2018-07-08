
from Statement import Statement
from ArithmetricExpression import ArithmetricExpression
from Variable import Variable

class LetStatement(Statement):
    '''
    classdocs
    '''


    def __init__(self, statementLine):
        super (LetStatement, self).__init__(statementLine)
        self.statement = statementLine
        
    def execute (self):
        # Sets a variable the result of an Arithmetic Expression
        Variable.setVariable(self,ArithmetricExpression(self.statement).getExpression())

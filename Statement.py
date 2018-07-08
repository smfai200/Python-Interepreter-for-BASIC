import abc

class Statement(object):
    '''
    classdocs
    '''
    @abc.abstractmethod
    def execute (self):
        return   

    def __init__(self,statementLine):
        '''
        Constructor
        '''
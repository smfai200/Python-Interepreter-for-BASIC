

import IfStatement
import GotoStatement
import LetStatement
import PrintStatement
import StopStatement
import config
import Statement
import re
import sys

def main():   
    lineNumber = []
    # Fill the statement list with null statements
    for i in range(995):
        config.statements.append(Statement.Statement("null"))  
    #Opens the file to read it
    f = open('test1.bas', 'rU')
    #For every line in the file check to see if its a statement
    
    for line in f:
        #Splits the line up so that I can grab the line number from the statement
        lineList = line.split()
        #checks the syntax
        SytaxCheck(line)
        
        if lineList[0] in lineNumber:
            sys.stderr.write('Double line number detected in line : ' + lineList)
            sys.exit()
        else:
            lineNumber.append(lineList[0])
            
        #If it has and IF in it then its an If statement
        if "IF" in line:
            config.statements.insert(int(lineList[0]), IfStatement.IfStatement(line))
            # If it has a goto into then it's a GOTO Statement
        elif "GOTO" in line:
            config.statements.insert(int(lineList[0]), GotoStatement.GotoStatement(line))
            # If it has a Let in it then it's a LET statement
        elif "LET" in line:
            config.statements.insert(int(lineList[0]), LetStatement.LetStatement(line))
            # If it has a Print in it then it's a PRINT statement
        elif "PRINT" in line:
            config.statements.insert(int(lineList[0]), PrintStatement.PrintStatement(line))
            # If it has a Stop in it then it's a STOP statement
        elif "STOP" in line:
            config.statements.insert(int(lineList[0]), StopStatement.StopStatement(line))
    # close the file
    f.close()
    #print("Hello Faizan")
	
    # while the count does no reach the end of the statement then execute each statement
    #try:
    while config.index <= len(config.statements):
        config.statements[config.index].execute()
        config.index += 1
    #except:
      #pass
def SytaxCheck(line):
    #makes sure that they syntax is right in the statement
    lineList = line.split()
    regex = re.compile("^([A-Z]|[0-9]+|LET|GOTO|STOP|IF|PRINT|=|<>|<|>|<=|>=|\+|-|/|\*)$")
    for a in lineList:
        if not re.search(regex, a):
            sys.stderr.write('Invalid Syntax in line : ' + line)
            sys.exit()
if __name__ == '__main__':
    main()
    
    

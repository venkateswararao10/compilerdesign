from sly import Parser
from callexer import callexer
import re
class calparser(Parser):
        tokens=callexer.tokens
        literals=callexer.literals
        precedence=(('left','+','-'),('left','*','/'),('nonassoc','(',')'))
        @_('expr')
        def L(self,value):
                print(value[0])
        @_('L NEWLINE expr')
        def L(self,value):
                print(value[2])
        @_('expr "+" expr')
        def expr(self,value):
                return value[0]+value[2]
        @_('expr "-" expr')
        def expr(self,value):
                return value[0]-value[2]
        @_('expr "*" expr')
        def expr(self,value):
                return value[0]*value[2]
        @_('expr "/" expr')
        def expr(self,value):
                return value[0]/value[2]
        @_('"(" expr ")"')
        def expr(self,value):
                return value[1]
        @_('INTEGER','ID')
        def expr(self,value):
                return value[0]
lexer=callexer()
parser=calparser()
expression='''2-(4+9)+d-a
3+4
4+5'''
parser.parse(lexer.tokenize(expression))


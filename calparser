from sly import Parser
from callexer import callexer
class calparser(Parser):
        tokens=callexer.tokens
        literals=callexer.literals
        precedence=(('left','+','-'),('left','*','/'),('nonassoc','(',')'))
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
        @_('INTEGER')
        def expr(self,value):
                return value[0]
lexer=callexer()
parser=calparser()
expression='2-(4+9)'
result=parser.parse(lexer.tokenize(expression))
print(result)

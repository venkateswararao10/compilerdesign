from LexicalAnalyzerForTinyC import lexer
from sly import Lexer
from sly import Parser
import argparse
apr=argparse.ArgumentParser()
apr.add_argument("inputfile")
apr.add_argument('-o',nargs=1)
args=apr.parse_args()
class parser(Parser):
        def __init__(self):
                self.memory={}
        tokens=lexer.tokens
        literals=lexer.literals
        precedence=(('left','+','-'),('left','*','/'))
        @_('TYPE ID "(" ")" "{" Statements "}"')
        def Program(self,t):
                pass
        @_('Statement ";" Statements')
        def Statements(self,t):
                pass
        @_('TYPE Variables')
        def Statement(self,t):
                pass
        @_('ID "," Variables')
        def Variables(self,t):
                self.memory[t.ID]=0
        @_('ID')
        def Variables(self,t):
                pass
        @_('ID "=" Expr')
        def Statement(self,t):
                self.memory[t.ID]=t.Expr
        @_('PRINT Expr')
        def Statement(self,t):
                print(t.Expr)
        @_('Statement ";"')
        def Statements(self,t):
                pass
        @_('Expr "+" Expr')
        def Expr(self,t):
                return t.Expr0+t.Expr1
        @_('Expr "-" Expr')
        def Expr(self,t):
                return t.Expr0-t.Expr1
        @_('Expr "*" Expr')
        def Expr(self,t):
                return t.Expr0*t.Expr1
        @_('Expr "/" Expr')
        def Expr(self,t):
                return t.Expr0/t.Expr1
        @_('INTEGER')
        def Expr(self,t):
                return t.INTEGER
        @_('ID')
        def Expr(self,t):
                return self.memory[t.ID]
input=open(args.inputfile,'r')
l=lexer()
p=parser()

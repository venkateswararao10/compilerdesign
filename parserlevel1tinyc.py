from sly import Parser
from lexicallevel1tinyc import level1
import argparse
class parser(Parser):
        tokens=level1.tokens
        literals=level1.literals
        memory={}
        @_('return_type ID "(" ")" "{" statements "}"')
        def program(self,value):
                        pass
        @_('INT')
        def return_type(self,value):
                        pass
        @_('statement ";" statements')
        def statements(self,value):
                        pass
        @_('statement ";"')
        def statements(self,value):
                        pass
        @_('declaration_stmt')
        def statement(self,value):
                        pass
        @_('assisgnment_stmt')
        def statement(self,value):
                        pass
        @_('type list_of_variables')
        def declaration_stmt(self,value):
                        pass
        @_('ID "," list_of_variables')
        def list_of_variables(self,value):
                        pass
        @_('ID')
        def list_of_variables(self,value):
                 self.memory[value.ID]=0
        @_('ID "=" ID')
        def assisgnment_stmt(self,value):
                        self.memory[value.ID0]=self.memory[value.ID1]
        @_('ID "=" CONST')
        def assisgnment_stmt(self,value):
                        self.memory[value.ID]=value.CONST
        @_('print_stmt')
        def statement(self,value):
                        pass
        @_('PRINT ID')
        def print_stmt(self,value):
                        print(self.memory[value.ID])
                        print(type(self.memory[value.ID]))
        @_('INT')
        def type(self,value):
                pass
lex=level1()
par=parser()
a=argparse.ArgumentParser()
a.add_argument("inputfile")
a.add_argument("-p",nargs=1)
args=a.parse_args()
expression='''int main(){
int a;
a=30;
b=a;
print a;
print b; }
'''
with open(args.inputfile,'r') as f:
        if args.p is None:
                        par.parse(lex.tokenize(f.read()))
        else:
                with open(args.p[0],'a') as g:
                                g.write(f"{par.parse(lex.tokenize(f.read()))}")

 python3 parserlevel1tinyc.py inputcode.TINYC -p output.txt
30
<class 'int'>
30
<class 'int'>

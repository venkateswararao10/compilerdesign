from sly import Lexer
class callexer(Lexer):
        literals={'+','-','/','*','(',')'}
        tokens={INTEGER,NEWLINE,ID}
        ignore=' '
        NEWLINE=r'\n'
        INTEGER=r'[0-9]+'
        ID=r'[a-zA-Z][a-zA-Z0-9]*'
        def INTEGER(self,t):
                t.value=int(t.value)
                return t
        def ID(self,t):
                t.value=int(input(f'enter the {t.value}'))
                return t



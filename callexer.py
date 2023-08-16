from sly import Lexer
class callexer(Lexer):
        literals={'+','-','/','*','(',')'}
        tokens={INTEGER}
        INTEGER=r'[0-9]+'
        def INTEGER(self,t):
                t.value=int(t.value)
                return t

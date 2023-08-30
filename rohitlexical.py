from sly import Lexer
class lexer(Lexer):
        #declaring tokens and literals
        tokens={ID,TYPE,PRINT,INTEGER}
        literals={'(',')','{','}',';','=',',','+','-','*','/'}
        #giving ignore statements
        ignore=r' \t'
        ignore_comments='\#.*'
        ignore_newline=r'\n+'
        #giving regular expressions of identifiers and integer constants along with some keywords
        ID=r'[a-zA-Z_][a-zA-Z0-9_]*'
        INTEGER=r'\d+'
        ID['print']=PRINT
        ID['int']=TYPE
        @_('\d+')
        def INTEGER(self,t):
                t.value=int(t.value)
                return t


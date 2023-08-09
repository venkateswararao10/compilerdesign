from sly import Lexer
class callexer(Lexer):
        literals={'{','(','}',')',';'}
        tokens={ID,INTEGER,INT,MAIN,IF,ELSE,WHILE,ASSIGN,PLUS,MINUS,MUL,DIVIDE,PRINT}
        # String containing ignored characters (between tokens)
        ignore = ' \t' #r'[ ]+'
        # Other ignored patterns
        ignore_comment = r'\#.*'
        ignore_newline = r'\n+'
        ID=r'[a-zA-z][a-zA-z0-9]*'
        ID['if']=IF
        ID['else']=ELSE
        ID['while']=WHILE
        ID['main']=MAIN
        ID['int']=INT
        ID['print']=PRINT
        ASSIGN=r'='
        INTEGER=r'[0-9]+'
        PLUS=r'\+'
        MINUS=r'-'
        MUL=r'\*'
        DIVIDE=r'/'
lexer=callexer()
f=open('level1.tinyc','r')
expression=f.read()
for token in  lexer.tokenize(expression):
        print(f'type->{token.type} value->{token.value}')

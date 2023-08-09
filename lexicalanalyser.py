from sly import Lexer
class callexer(Lexer):
        literals={'{','(','}',')',';'}
        tokens={ID,INTEGER,INT,MAIN,IF,ELSE,WHILE,ASSIGN,PLUS,MINUS,MUL,DIVIDE,PRINT}
        # String containing ignored characters (between tokens)
        ignore = ' \t' #r'[ ]+'
        # Other ignored patterns
        ignore_comment = r'\#.*' #r'[#]+' #r'[#]'
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




21VV1A0559@admincse-610-1110in:~/Compilerdesign/9aug2023$ python3 lexicalanalysis.py
type->INT value->int
type->MAIN value->main
type->( value->(
type->) value->)
type->{ value->{
type->INT value->int
type->ID value->a
type->; value->;
type->ID value->a
type->ASSIGN value->=
type->ID value->b
type->MUL value->*
type->ID value->c
type->DIVIDE value->/
type->INTEGER value->8
type->; value->;
type->PRINT value->print
type->ID value->a
type->; value->;
type->} value->}

from sly import Lexer
class level1(Lexer):
        literals={":",";","=","==","+","-","*","/","(",")","{","}",".",",",".","\n","!","%","[","]"}
        tokens={CONST,ID,INT,PRINT}
        ignore=' \t'
        ignore_comment=r"\#.*"
        ignore_newline=r"\n+"
        ID=r'[a-zA-Z][a-zA-z0-9]*'
        ID['int']=INT
        ID['print']=PRINT
        CONST=r'\d+'
        #@_('\d+')
        def CONST(self,t):
                t.value=int(t.value)
                return t
if __name__=='__main__':
        tinyc=level1()
        expression='''int main(){
        int a=30;
        print a;
        }'''
        for token in tinyc.tokenize(expression):
                print(f"type->{token.type} value->{token.value}")


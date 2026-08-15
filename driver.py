from antlr4 import *
from OrkaLexer import OrkaLexer
from OrkaParser import OrkaParser
import sys
from ListenerInterp import ListenerInterp

#input_text = "program epsilon var x, y, z: integer; begin read(x, y); x := x; while x > 0 do begin write(x); x := x - 1; end; end"
#lexer = OrkaLexer(InputStream(input_text))
#stream = CommonTokenStream(lexer)
#parser = OrkaParser(stream)

#tree = parser.program()

#print(tree.toStringTree(recog=parser))

def main(argv):
    input_stream = FileStream(argv[1])
    lexer = OrkaLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = OrkaParser(stream)
    tree = parser.program()
    if parser.getNumberOfSyntaxErrors() > 0:
        print("syntax errors")
    else:
        linterp = ListenerInterp()
        walker = ParseTreeWalker()
        walker.walk(linterp, tree)
    #print(tree.toStringTree(recog=parser))    

if __name__ == '__main__':
    main(sys.argv)
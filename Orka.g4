grammar Orka;

program : 'program' Ident  decl runsection;

Ident : [a-z]+;

decl : 'var' declarlist?;

declarlist: (identlist ':' (type) ';')*;

identlist : Ident (',' Ident)*;

type : 'integer' | 'real' | 'boolean';

runsection: 'begin' actionsequence 'end';
actionsequence : (command ';')*;

command : input | output | assign | ifstatement | switchstatement | whilestatement | forstatement;

input : 'read(' identlist ')';
output : 'write(' identlist ')'| 'write(' const ')';

const : intnumb | realnumb | boolconst;

boolconst : 'true' | 'false';
intnumb : sign? Numb;
realnumb: sign? (| Numb '.' Numb | Numb'.' | '.'Numb);
Numb : [0-9]+; 
sign : '+'| '-';

assign : Ident ':=' (arithmexpr | boolconst);
expression :   boolexpr | arithmexpr; 

arithmexpr : term (('+'| '-') term)*;

term : factor (('*'| '/') factor)*;

factor : sign? (base ('^' factor)?) | '('arithmexpr')';
base : Ident | intnumb | realnumb;

boolexpr : boolconst | logicalexpr;

logicalexpr : logicalterm ('or' logicalterm)*;

logicalterm : logicalmultiplier ('and' logicalmultiplier)*;

logicalmultiplier : logicalrel| 'not' logicalmultiplier | '(' logicalexpr ')';

logicalrel : arithmexpr relop arithmexpr | Ident relop boolexpr;

ifstatement : 'if' boolexpr 'then' doblock ('else' doblock)?;
doblock : 'begin' actionsequence 'end';

// Цикл while
whilestatement : 'while' boolexpr 'do' doblock;

// Цикл for
forstatement : 'for' Ident ':=' arithmexpr ('to' | 'downto') arithmexpr 'do' doblock;

switchstatement : 'case' expression 'of' caselist ('default' ':' doblock)? 'end';
caselist : const ':' doblock (const ':' doblock);

relop : '='| '<=' | '<'| '>'| '>='|'<>';
WS : [ \t\r\n]+ -> skip;

Comment: '#' ~[\r\n]* -> skip;
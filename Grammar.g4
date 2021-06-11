grammar Grammar;

DOT : '.';
COMMA : ',';
SEMICOLON : ';';
APOSTROPHE :  '\'';
QUOTE : '"';
COLON : ':';
DOUBLE_COLON : '::';
HASH : '#';
LEFT_BRACKET : '(';
RIGHT_BRACKET : ')';
SQR_LEFT_BRACKET : '[';
SQR_RIGHT_BRACKET : ']';
CURLY_LEFT_BRACKET : '{';
CURLY_RIGHT_BRACKET : '}';
LE : '<';
GE : '>';
LEQ : '<=';
GEQ : '>=';
PLUS : '+';
MINUS : '-';
MUL : '*';
DIV : '/';
MOD : '%';
ASSIGN : '=';
AND : '&&';
OR : '||';
NOT : '!';
NOT_EQ : '!=';
EQ : '==';
PP : '++';
MM : '--';
PEQ : '+=';
MINEQ : '-=';
MULEQ : '*=';
DIVEQ : '/=';
DARRL: '<<';
DARRR: '>>';
NUMBER : MINUS? (NATURAL | (NATURAL DOT NATURAL));
INT : 'int';
FLOAT : 'float';
DOUBLE : 'double';
LONG : 'long';
CHAR : 'char';
STRING : 'string';
BOOL : 'bool';
VOID : 'void';
IF : 'if';
ELSE : 'else';
ELSE_IF : 'else if';
WHILE : 'while';
FOR : 'for';
BREAK : 'break';
CONTINUE : 'continue';
RETURN : 'return';
MAIN : 'main';
TRUE : 'true';
FALSE : 'false';
COUT: 'cout';
CIN: 'cin';
BOOLS : TRUE | FALSE;
ENDL: 'endl';
DIGIT : [0-9];
NATURAL : '0' | ([1-9][0-9]*);
ID : NONDIGIT CHARACTER*;
NONDIGIT: [a-zA-Z_];
CHARACTER : DIGIT|NONDIGIT;
TEXT : CHARACTER+;
INCLUDE : '#include<iostream>';
STD : 'using namespace std;';
WS : [ \t\r\n]+ -> skip ;
COMM : '//' ~ [\r\n]*;

program
: INCLUDE STD funcDec* varDec* mainFunc EOF;

mainFunc
: INT MAIN LEFT_BRACKET VOID? RIGHT_BRACKET block;

block
: CURLY_LEFT_BRACKET blockElement* CURLY_RIGHT_BRACKET;

blockElement
: exp SEMICOLON 
| statement
| declaration
| assignment
| coutExp
| cinExp
| COMM;

expOrEndl
: (DARRL exp | DARRL ENDL);

coutExp
: COUT expOrEndl+ SEMICOLON;

cinExp
: CIN DARRR ID SEMICOLON;

exp
: exp expOp exp
| NUMBER
| ID
| func
| LEFT_BRACKET exp RIGHT_BRACKET
| singleExp
| APOSTROPHE CHARACTER APOSTROPHE
| QUOTE TEXT QUOTE
| BOOLS;

expOp
: PLUS
| MINUS
| MUL
| DIV
| MOD
| AND
| OR
| LE
| GE
| LEQ
| GEQ
| NOT_EQ
| EQ;

incOp
: PP
| MM;

singleExp
: NOT ID
| incOp ID
| ID incOp;

bracketsExp
: LEFT_BRACKET exp RIGHT_BRACKET;

statement
: ifSt
| forSt
| whileSt
| returnSt
| BREAK SEMICOLON
| CONTINUE SEMICOLON
| block;

ifSt
: IF bracketsExp block (ELSE_IF bracketsExp block)* (ELSE block)?;

whileSt
: WHILE bracketsExp block;

forSt
: FOR LEFT_BRACKET (varDec|varAssignment|exp)? SEMICOLON exp? SEMICOLON exp? RIGHT_BRACKET block;

returnSt
: RETURN exp SEMICOLON;

identifierType
: INT 
| LONG
| FLOAT
| DOUBLE
| CHAR
| STRING
| BOOL;

funcType
: identifierType
| VOID;

funcDec
: funcType ID LEFT_BRACKET params? RIGHT_BRACKET block;

func
: ID LEFT_BRACKET exp (COMMA exp)* RIGHT_BRACKET;

assignment
: varAssignment
| arrayAssignment
| singleExp
| varOpVar;

declaration
: varDec
| arrayDec;

varDec
: identifierType ID (ASSIGN exp)? SEMICOLON;

varAssignment
: ID ASSIGN exp SEMICOLON;

varOp
: PEQ
| MINEQ
| MULEQ
| DIVEQ;

varOpVar
: ID varOp ID SEMICOLON;

arrayDec
: identifierType ID SQR_LEFT_BRACKET NATURAL? SQR_RIGHT_BRACKET (ASSIGN arrayInit)? SEMICOLON;

arrayInit
: CURLY_LEFT_BRACKET exp (COMMA exp)* CURLY_RIGHT_BRACKET;

arrayAssignment
: ID SQR_LEFT_BRACKET NATURAL SQR_RIGHT_BRACKET ASSIGN exp;

params
: identifierType ID (COMMA identifierType ID)*;

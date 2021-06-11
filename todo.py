# program
# : INCLUDE STD funcDec* varDec* mainFunc EOF;

# mainFunc
# : INT MAIN LEFT_BRACKET VOID? RIGHT_BRACKET block;

# block
# : CURLY_LEFT_BRACKET blockElement* CURLY_RIGHT_BRACKET;

# blockElement
# : exp SEMICOLON
# | statement
# | declaration
# | assignment
# | coutExp
# | cinExp;

# expOrEndl
# : (DARRL exp | DARRL ENDL);

# coutExp
# : COUT exp expOrEndl* SEMICOLON;

# cinExp
# : CIN ID SEMICOLON;

exp
# : exp expOp exp
| NUMBER
| ID
| func
# | LEFT_BRACKET exp RIGHT_BRACKET
| singleExp
| APOSTROPHE CHARACTER APOSTROPHE
| QUOTE TEXT QUOTE
| BOOLS;

# expOp
# : PLUS
# | MINUS
# | MUL
# | DIV
# | MOD
# | AND
# | OR
# | LE
# | GE
# | LEQ
# | GEQ
# | NOT_EQ
# | EQ;

singleExp
: NOT ID
| (PP|MM) ID
| ID (PP|MM);

# bracketsExp
# : LEFT_BRACKET exp RIGHT_BRACKET;

statement
# : ifSt
| forSt
# | whileSt
# | returnSt
| BREAK SEMICOLON
| CONTINUE SEMICOLON
| block;

# ifSt
# : IF bracketsExp block (ELSE_IF bracketsExp block)* (ELSE block)?;

# whileSt
# : WHILE bracketsExp block;

forSt
: FOR LEFT_BRACKET (varDec|varAssignment|exp)? SEMICOLON exp? SEMICOLON exp? RIGHT_BRACKET block;

# returnSt
# : RETURN exp SEMICOLON;

# identifierType
# : INT
# | LONG
# | FLOAT
# | DOUBLE
# | CHAR
# | STRING
# | BOOL;
#
# funcType
# : identifierType
# | VOID;

# funcDec
# : funcType ID LEFT_BRACKET params? RIGHT_BRACKET block;

func
: ID LEFT_BRACKET exp (COMMA exp)* RIGHT_BRACKET;

assignment
: varAssignment
| arrayAssignment
| singleExp
# | varOpVar;

declaration
# : varDec
| arrayDec;

# varDec
# : identifierType ID (ASSIGN exp)? SEMICOLON;

varAssignment
: ID ASSIGN exp;

# varOp
# : PEQ
# | MINEQ
# | MULEQ
# | DIVEQ;

# varOpVar
# : ID varOp ID SEMICOLON;

arrayDec
: identifierType ID SQR_LEFT_BRACKET NATURAL? SQR_RIGHT_BRACKET (ASSIGN arrayInit)? SEMICOLON;

arrayInit
: CURLY_LEFT_BRACKET exp (COMMA exp)* CURLY_RIGHT_BRACKET;

arrayAssignment
: ID SQR_LEFT_BRACKET NATURAL SQR_RIGHT_BRACKET ASSIGN exp;

# params
# : identifierType ID (COMMA identifierType ID)*;

NA NUDE:
func - parseFunc

grammar simple;

options{
	language=Python;
	output=AST;
	ASTLabelType=CommonTree;
	backtrack=true;
}
/* Arithmetic operators, in order of precedence. */
MULT	:	'*';
PLUS	:	'+';
MINUS	:	'-';

/* Boolean operators, in order of precedence. */
NOT	 :	'not';
AND	:	'&';
OR	:	'|';
RELOP	:	('=' | '<' | '<=' | '>' | '>=');

/* If / else. */
IF	:	'if';
THEN	:	'then';
ELSE	:	'else';
ENDIF	:	'fi';
SKIP	:	'skip';

/* Do while. */
WHILE	:	'while';
DO	:	'do';
ENDWHILE	:	'od';

/* Misc. */
GETS	:	':=';
SEMI	:	';';
LPAREN	:	'(';
RPAREN	:	')';
BLOCK	:	'block';
UNARY	:	'unary';

/* Atoms. */
BOOLEAN	:	('true' | 'false');
IDENT	:	('a'..'z' | 'A'..'Z')('a'..'z' | 'A'..'Z' | '0'..'9')*;
INTEGER	:	('0'..'9')+;

/* Ignore whitespace. */
WS	:	(' ' | '\t' | '\n' | '\r' | '\f')+ {$channel = HIDDEN;};


program
 	:	block
 	;

block
	:	statement+
		-> ^(BLOCK statement+)
	;

/* Arithmetic expressions - craziness due to precendence! */
arith_expr
	:	add_expr
	;
add_expr
	:	sub_expr (PLUS^ sub_expr)*
	;
sub_expr 
	:	mult_expr (MINUS^ mult_expr)*
	;
mult_expr 
	:	unary_expr (MULT^ unary_expr)*
	;
unary_expr
	:	MINUS arith_atom
		-> ^(UNARY MINUS arith_atom)
	|	PLUS arith_atom
		-> ^(UNARY PLUS arith_atom)
	|	arith_atom
	;
arith_atom
	:	(IDENT | INTEGER)
	|	LPAREN! arith_expr RPAREN!
	;

/* Boolean expressions - craziness due to precedence! */
bool_expr 
	:	or_expr
	;
or_expr 
 	:	and_expr (AND^ and_expr)*
 	;
and_expr
 	:	bool_atom (OR^ bool_atom)*
 	;
bool_atom
 	:	BOOLEAN
	|	NOT^ bool_atom
	|	LPAREN! bool_expr RPAREN!
	|	arith_expr RELOP^ arith_expr
	;

statement
    :   IDENT GETS^ arith_expr SEMI!
    |   SKIP SEMI!
    |   IF^ bool_expr THEN! block ELSE! block ENDIF! SEMI!
    |   WHILE^ bool_expr DO! block ENDWHILE! SEMI!
    ;
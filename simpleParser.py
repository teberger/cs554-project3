# $ANTLR 3.1.3 Mar 18, 2009 10:09:25 simple.g 2014-12-03 02:38:12

import sys
from antlr3 import *
from antlr3.compat import set, frozenset

from antlr3.tree import *



# for convenience in actions
HIDDEN = BaseRecognizer.HIDDEN

# token types
SEMI=20
DO=17
MINUS=6
MULT=4
ELSE=13
SKIP=15
WS=28
EOF=-1
IF=11
UNARY=24
INTEGER=27
OR=9
ENDIF=14
LPAREN=21
BLOCK=23
RPAREN=22
BOOLEAN=25
NOT=7
IDENT=26
AND=8
THEN=12
WHILE=16
ENDWHILE=18
GETS=19
RELOP=10
PLUS=5

# token names
tokenNames = [
    "<invalid>", "<EOR>", "<DOWN>", "<UP>", 
    "MULT", "PLUS", "MINUS", "NOT", "AND", "OR", "RELOP", "IF", "THEN", 
    "ELSE", "ENDIF", "SKIP", "WHILE", "DO", "ENDWHILE", "GETS", "SEMI", 
    "LPAREN", "RPAREN", "BLOCK", "UNARY", "BOOLEAN", "IDENT", "INTEGER", 
    "WS"
]




class simpleParser(Parser):
    grammarFileName = "simple.g"
    antlr_version = version_str_to_tuple("3.1.3 Mar 18, 2009 10:09:25")
    antlr_version_str = "3.1.3 Mar 18, 2009 10:09:25"
    tokenNames = tokenNames

    def __init__(self, input, state=None, *args, **kwargs):
        if state is None:
            state = RecognizerSharedState()

        super(simpleParser, self).__init__(input, state, *args, **kwargs)






        self._adaptor = None
        self.adaptor = CommonTreeAdaptor()
                


        
    def getTreeAdaptor(self):
        return self._adaptor

    def setTreeAdaptor(self, adaptor):
        self._adaptor = adaptor

    adaptor = property(getTreeAdaptor, setTreeAdaptor)


    class program_return(ParserRuleReturnScope):
        def __init__(self):
            super(simpleParser.program_return, self).__init__()

            self.tree = None




    # $ANTLR start "program"
    # simple.g:49:1: program : block ;
    def program(self, ):

        retval = self.program_return()
        retval.start = self.input.LT(1)

        root_0 = None

        block1 = None



        try:
            try:
                # simple.g:50:3: ( block )
                # simple.g:50:5: block
                pass 
                root_0 = self._adaptor.nil()

                self._state.following.append(self.FOLLOW_block_in_program316)
                block1 = self.block()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, block1.tree)



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "program"

    class block_return(ParserRuleReturnScope):
        def __init__(self):
            super(simpleParser.block_return, self).__init__()

            self.tree = None




    # $ANTLR start "block"
    # simple.g:53:1: block : ( statement )+ -> ^( BLOCK ( statement )+ ) ;
    def block(self, ):

        retval = self.block_return()
        retval.start = self.input.LT(1)

        root_0 = None

        statement2 = None


        stream_statement = RewriteRuleSubtreeStream(self._adaptor, "rule statement")
        try:
            try:
                # simple.g:54:2: ( ( statement )+ -> ^( BLOCK ( statement )+ ) )
                # simple.g:54:4: ( statement )+
                pass 
                # simple.g:54:4: ( statement )+
                cnt1 = 0
                while True: #loop1
                    alt1 = 2
                    LA1_0 = self.input.LA(1)

                    if (LA1_0 == IF or (SKIP <= LA1_0 <= WHILE) or LA1_0 == IDENT) :
                        alt1 = 1


                    if alt1 == 1:
                        # simple.g:0:0: statement
                        pass 
                        self._state.following.append(self.FOLLOW_statement_in_block328)
                        statement2 = self.statement()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            stream_statement.add(statement2.tree)


                    else:
                        if cnt1 >= 1:
                            break #loop1

                        if self._state.backtracking > 0:
                            raise BacktrackingFailed

                        eee = EarlyExitException(1, self.input)
                        raise eee

                    cnt1 += 1

                # AST Rewrite
                # elements: statement
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                if self._state.backtracking == 0:

                    retval.tree = root_0

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 55:3: -> ^( BLOCK ( statement )+ )
                    # simple.g:55:6: ^( BLOCK ( statement )+ )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(BLOCK, "BLOCK"), root_1)

                    # simple.g:55:14: ( statement )+
                    if not (stream_statement.hasNext()):
                        raise RewriteEarlyExitException()

                    while stream_statement.hasNext():
                        self._adaptor.addChild(root_1, stream_statement.nextTree())


                    stream_statement.reset()

                    self._adaptor.addChild(root_0, root_1)



                    retval.tree = root_0



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "block"

    class arith_expr_return(ParserRuleReturnScope):
        def __init__(self):
            super(simpleParser.arith_expr_return, self).__init__()

            self.tree = None




    # $ANTLR start "arith_expr"
    # simple.g:59:1: arith_expr : add_expr ;
    def arith_expr(self, ):

        retval = self.arith_expr_return()
        retval.start = self.input.LT(1)

        root_0 = None

        add_expr3 = None



        try:
            try:
                # simple.g:60:2: ( add_expr )
                # simple.g:60:4: add_expr
                pass 
                root_0 = self._adaptor.nil()

                self._state.following.append(self.FOLLOW_add_expr_in_arith_expr353)
                add_expr3 = self.add_expr()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, add_expr3.tree)



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "arith_expr"

    class add_expr_return(ParserRuleReturnScope):
        def __init__(self):
            super(simpleParser.add_expr_return, self).__init__()

            self.tree = None




    # $ANTLR start "add_expr"
    # simple.g:62:1: add_expr : sub_expr ( PLUS sub_expr )* ;
    def add_expr(self, ):

        retval = self.add_expr_return()
        retval.start = self.input.LT(1)

        root_0 = None

        PLUS5 = None
        sub_expr4 = None

        sub_expr6 = None


        PLUS5_tree = None

        try:
            try:
                # simple.g:63:2: ( sub_expr ( PLUS sub_expr )* )
                # simple.g:63:4: sub_expr ( PLUS sub_expr )*
                pass 
                root_0 = self._adaptor.nil()

                self._state.following.append(self.FOLLOW_sub_expr_in_add_expr363)
                sub_expr4 = self.sub_expr()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, sub_expr4.tree)
                # simple.g:63:13: ( PLUS sub_expr )*
                while True: #loop2
                    alt2 = 2
                    LA2_0 = self.input.LA(1)

                    if (LA2_0 == PLUS) :
                        alt2 = 1


                    if alt2 == 1:
                        # simple.g:63:14: PLUS sub_expr
                        pass 
                        PLUS5=self.match(self.input, PLUS, self.FOLLOW_PLUS_in_add_expr366)
                        if self._state.backtracking == 0:

                            PLUS5_tree = self._adaptor.createWithPayload(PLUS5)
                            root_0 = self._adaptor.becomeRoot(PLUS5_tree, root_0)

                        self._state.following.append(self.FOLLOW_sub_expr_in_add_expr369)
                        sub_expr6 = self.sub_expr()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, sub_expr6.tree)


                    else:
                        break #loop2



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "add_expr"

    class sub_expr_return(ParserRuleReturnScope):
        def __init__(self):
            super(simpleParser.sub_expr_return, self).__init__()

            self.tree = None




    # $ANTLR start "sub_expr"
    # simple.g:65:1: sub_expr : mult_expr ( MINUS mult_expr )* ;
    def sub_expr(self, ):

        retval = self.sub_expr_return()
        retval.start = self.input.LT(1)

        root_0 = None

        MINUS8 = None
        mult_expr7 = None

        mult_expr9 = None


        MINUS8_tree = None

        try:
            try:
                # simple.g:66:2: ( mult_expr ( MINUS mult_expr )* )
                # simple.g:66:4: mult_expr ( MINUS mult_expr )*
                pass 
                root_0 = self._adaptor.nil()

                self._state.following.append(self.FOLLOW_mult_expr_in_sub_expr382)
                mult_expr7 = self.mult_expr()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, mult_expr7.tree)
                # simple.g:66:14: ( MINUS mult_expr )*
                while True: #loop3
                    alt3 = 2
                    LA3_0 = self.input.LA(1)

                    if (LA3_0 == MINUS) :
                        alt3 = 1


                    if alt3 == 1:
                        # simple.g:66:15: MINUS mult_expr
                        pass 
                        MINUS8=self.match(self.input, MINUS, self.FOLLOW_MINUS_in_sub_expr385)
                        if self._state.backtracking == 0:

                            MINUS8_tree = self._adaptor.createWithPayload(MINUS8)
                            root_0 = self._adaptor.becomeRoot(MINUS8_tree, root_0)

                        self._state.following.append(self.FOLLOW_mult_expr_in_sub_expr388)
                        mult_expr9 = self.mult_expr()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, mult_expr9.tree)


                    else:
                        break #loop3



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "sub_expr"

    class mult_expr_return(ParserRuleReturnScope):
        def __init__(self):
            super(simpleParser.mult_expr_return, self).__init__()

            self.tree = None




    # $ANTLR start "mult_expr"
    # simple.g:68:1: mult_expr : unary_expr ( MULT unary_expr )* ;
    def mult_expr(self, ):

        retval = self.mult_expr_return()
        retval.start = self.input.LT(1)

        root_0 = None

        MULT11 = None
        unary_expr10 = None

        unary_expr12 = None


        MULT11_tree = None

        try:
            try:
                # simple.g:69:2: ( unary_expr ( MULT unary_expr )* )
                # simple.g:69:4: unary_expr ( MULT unary_expr )*
                pass 
                root_0 = self._adaptor.nil()

                self._state.following.append(self.FOLLOW_unary_expr_in_mult_expr401)
                unary_expr10 = self.unary_expr()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, unary_expr10.tree)
                # simple.g:69:15: ( MULT unary_expr )*
                while True: #loop4
                    alt4 = 2
                    LA4_0 = self.input.LA(1)

                    if (LA4_0 == MULT) :
                        alt4 = 1


                    if alt4 == 1:
                        # simple.g:69:16: MULT unary_expr
                        pass 
                        MULT11=self.match(self.input, MULT, self.FOLLOW_MULT_in_mult_expr404)
                        if self._state.backtracking == 0:

                            MULT11_tree = self._adaptor.createWithPayload(MULT11)
                            root_0 = self._adaptor.becomeRoot(MULT11_tree, root_0)

                        self._state.following.append(self.FOLLOW_unary_expr_in_mult_expr407)
                        unary_expr12 = self.unary_expr()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, unary_expr12.tree)


                    else:
                        break #loop4



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "mult_expr"

    class unary_expr_return(ParserRuleReturnScope):
        def __init__(self):
            super(simpleParser.unary_expr_return, self).__init__()

            self.tree = None




    # $ANTLR start "unary_expr"
    # simple.g:71:1: unary_expr : ( MINUS arith_atom -> ^( UNARY MINUS arith_atom ) | PLUS arith_atom -> ^( UNARY PLUS arith_atom ) | arith_atom );
    def unary_expr(self, ):

        retval = self.unary_expr_return()
        retval.start = self.input.LT(1)

        root_0 = None

        MINUS13 = None
        PLUS15 = None
        arith_atom14 = None

        arith_atom16 = None

        arith_atom17 = None


        MINUS13_tree = None
        PLUS15_tree = None
        stream_MINUS = RewriteRuleTokenStream(self._adaptor, "token MINUS")
        stream_PLUS = RewriteRuleTokenStream(self._adaptor, "token PLUS")
        stream_arith_atom = RewriteRuleSubtreeStream(self._adaptor, "rule arith_atom")
        try:
            try:
                # simple.g:72:2: ( MINUS arith_atom -> ^( UNARY MINUS arith_atom ) | PLUS arith_atom -> ^( UNARY PLUS arith_atom ) | arith_atom )
                alt5 = 3
                LA5 = self.input.LA(1)
                if LA5 == MINUS:
                    alt5 = 1
                elif LA5 == PLUS:
                    alt5 = 2
                elif LA5 == LPAREN or LA5 == IDENT or LA5 == INTEGER:
                    alt5 = 3
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 5, 0, self.input)

                    raise nvae

                if alt5 == 1:
                    # simple.g:72:4: MINUS arith_atom
                    pass 
                    MINUS13=self.match(self.input, MINUS, self.FOLLOW_MINUS_in_unary_expr419) 
                    if self._state.backtracking == 0:
                        stream_MINUS.add(MINUS13)
                    self._state.following.append(self.FOLLOW_arith_atom_in_unary_expr421)
                    arith_atom14 = self.arith_atom()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_arith_atom.add(arith_atom14.tree)

                    # AST Rewrite
                    # elements: MINUS, arith_atom
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 
                    if self._state.backtracking == 0:

                        retval.tree = root_0

                        if retval is not None:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                        else:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                        root_0 = self._adaptor.nil()
                        # 73:3: -> ^( UNARY MINUS arith_atom )
                        # simple.g:73:6: ^( UNARY MINUS arith_atom )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(UNARY, "UNARY"), root_1)

                        self._adaptor.addChild(root_1, stream_MINUS.nextNode())
                        self._adaptor.addChild(root_1, stream_arith_atom.nextTree())

                        self._adaptor.addChild(root_0, root_1)



                        retval.tree = root_0


                elif alt5 == 2:
                    # simple.g:74:4: PLUS arith_atom
                    pass 
                    PLUS15=self.match(self.input, PLUS, self.FOLLOW_PLUS_in_unary_expr438) 
                    if self._state.backtracking == 0:
                        stream_PLUS.add(PLUS15)
                    self._state.following.append(self.FOLLOW_arith_atom_in_unary_expr440)
                    arith_atom16 = self.arith_atom()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_arith_atom.add(arith_atom16.tree)

                    # AST Rewrite
                    # elements: PLUS, arith_atom
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 
                    if self._state.backtracking == 0:

                        retval.tree = root_0

                        if retval is not None:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                        else:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                        root_0 = self._adaptor.nil()
                        # 75:3: -> ^( UNARY PLUS arith_atom )
                        # simple.g:75:6: ^( UNARY PLUS arith_atom )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(UNARY, "UNARY"), root_1)

                        self._adaptor.addChild(root_1, stream_PLUS.nextNode())
                        self._adaptor.addChild(root_1, stream_arith_atom.nextTree())

                        self._adaptor.addChild(root_0, root_1)



                        retval.tree = root_0


                elif alt5 == 3:
                    # simple.g:76:4: arith_atom
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_arith_atom_in_unary_expr457)
                    arith_atom17 = self.arith_atom()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, arith_atom17.tree)


                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "unary_expr"

    class arith_atom_return(ParserRuleReturnScope):
        def __init__(self):
            super(simpleParser.arith_atom_return, self).__init__()

            self.tree = None




    # $ANTLR start "arith_atom"
    # simple.g:78:1: arith_atom : ( ( IDENT | INTEGER ) | LPAREN arith_expr RPAREN );
    def arith_atom(self, ):

        retval = self.arith_atom_return()
        retval.start = self.input.LT(1)

        root_0 = None

        set18 = None
        LPAREN19 = None
        RPAREN21 = None
        arith_expr20 = None


        set18_tree = None
        LPAREN19_tree = None
        RPAREN21_tree = None

        try:
            try:
                # simple.g:79:2: ( ( IDENT | INTEGER ) | LPAREN arith_expr RPAREN )
                alt6 = 2
                LA6_0 = self.input.LA(1)

                if ((IDENT <= LA6_0 <= INTEGER)) :
                    alt6 = 1
                elif (LA6_0 == LPAREN) :
                    alt6 = 2
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 6, 0, self.input)

                    raise nvae

                if alt6 == 1:
                    # simple.g:79:4: ( IDENT | INTEGER )
                    pass 
                    root_0 = self._adaptor.nil()

                    set18 = self.input.LT(1)
                    if (IDENT <= self.input.LA(1) <= INTEGER):
                        self.input.consume()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, self._adaptor.createWithPayload(set18))
                        self._state.errorRecovery = False

                    else:
                        if self._state.backtracking > 0:
                            raise BacktrackingFailed

                        mse = MismatchedSetException(None, self.input)
                        raise mse




                elif alt6 == 2:
                    # simple.g:80:4: LPAREN arith_expr RPAREN
                    pass 
                    root_0 = self._adaptor.nil()

                    LPAREN19=self.match(self.input, LPAREN, self.FOLLOW_LPAREN_in_arith_atom478)
                    self._state.following.append(self.FOLLOW_arith_expr_in_arith_atom481)
                    arith_expr20 = self.arith_expr()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, arith_expr20.tree)
                    RPAREN21=self.match(self.input, RPAREN, self.FOLLOW_RPAREN_in_arith_atom483)


                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "arith_atom"

    class bool_expr_return(ParserRuleReturnScope):
        def __init__(self):
            super(simpleParser.bool_expr_return, self).__init__()

            self.tree = None




    # $ANTLR start "bool_expr"
    # simple.g:84:1: bool_expr : or_expr ;
    def bool_expr(self, ):

        retval = self.bool_expr_return()
        retval.start = self.input.LT(1)

        root_0 = None

        or_expr22 = None



        try:
            try:
                # simple.g:85:2: ( or_expr )
                # simple.g:85:4: or_expr
                pass 
                root_0 = self._adaptor.nil()

                self._state.following.append(self.FOLLOW_or_expr_in_bool_expr498)
                or_expr22 = self.or_expr()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, or_expr22.tree)



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "bool_expr"

    class or_expr_return(ParserRuleReturnScope):
        def __init__(self):
            super(simpleParser.or_expr_return, self).__init__()

            self.tree = None




    # $ANTLR start "or_expr"
    # simple.g:87:1: or_expr : and_expr ( AND and_expr )* ;
    def or_expr(self, ):

        retval = self.or_expr_return()
        retval.start = self.input.LT(1)

        root_0 = None

        AND24 = None
        and_expr23 = None

        and_expr25 = None


        AND24_tree = None

        try:
            try:
                # simple.g:88:3: ( and_expr ( AND and_expr )* )
                # simple.g:88:5: and_expr ( AND and_expr )*
                pass 
                root_0 = self._adaptor.nil()

                self._state.following.append(self.FOLLOW_and_expr_in_or_expr510)
                and_expr23 = self.and_expr()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, and_expr23.tree)
                # simple.g:88:14: ( AND and_expr )*
                while True: #loop7
                    alt7 = 2
                    LA7_0 = self.input.LA(1)

                    if (LA7_0 == AND) :
                        alt7 = 1


                    if alt7 == 1:
                        # simple.g:88:15: AND and_expr
                        pass 
                        AND24=self.match(self.input, AND, self.FOLLOW_AND_in_or_expr513)
                        if self._state.backtracking == 0:

                            AND24_tree = self._adaptor.createWithPayload(AND24)
                            root_0 = self._adaptor.becomeRoot(AND24_tree, root_0)

                        self._state.following.append(self.FOLLOW_and_expr_in_or_expr516)
                        and_expr25 = self.and_expr()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, and_expr25.tree)


                    else:
                        break #loop7



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "or_expr"

    class and_expr_return(ParserRuleReturnScope):
        def __init__(self):
            super(simpleParser.and_expr_return, self).__init__()

            self.tree = None




    # $ANTLR start "and_expr"
    # simple.g:90:1: and_expr : bool_atom ( OR bool_atom )* ;
    def and_expr(self, ):

        retval = self.and_expr_return()
        retval.start = self.input.LT(1)

        root_0 = None

        OR27 = None
        bool_atom26 = None

        bool_atom28 = None


        OR27_tree = None

        try:
            try:
                # simple.g:91:3: ( bool_atom ( OR bool_atom )* )
                # simple.g:91:5: bool_atom ( OR bool_atom )*
                pass 
                root_0 = self._adaptor.nil()

                self._state.following.append(self.FOLLOW_bool_atom_in_and_expr530)
                bool_atom26 = self.bool_atom()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, bool_atom26.tree)
                # simple.g:91:15: ( OR bool_atom )*
                while True: #loop8
                    alt8 = 2
                    LA8_0 = self.input.LA(1)

                    if (LA8_0 == OR) :
                        alt8 = 1


                    if alt8 == 1:
                        # simple.g:91:16: OR bool_atom
                        pass 
                        OR27=self.match(self.input, OR, self.FOLLOW_OR_in_and_expr533)
                        if self._state.backtracking == 0:

                            OR27_tree = self._adaptor.createWithPayload(OR27)
                            root_0 = self._adaptor.becomeRoot(OR27_tree, root_0)

                        self._state.following.append(self.FOLLOW_bool_atom_in_and_expr536)
                        bool_atom28 = self.bool_atom()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, bool_atom28.tree)


                    else:
                        break #loop8



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "and_expr"

    class bool_atom_return(ParserRuleReturnScope):
        def __init__(self):
            super(simpleParser.bool_atom_return, self).__init__()

            self.tree = None




    # $ANTLR start "bool_atom"
    # simple.g:93:1: bool_atom : ( BOOLEAN | NOT bool_atom | LPAREN bool_expr RPAREN | arith_expr RELOP arith_expr );
    def bool_atom(self, ):

        retval = self.bool_atom_return()
        retval.start = self.input.LT(1)

        root_0 = None

        BOOLEAN29 = None
        NOT30 = None
        LPAREN32 = None
        RPAREN34 = None
        RELOP36 = None
        bool_atom31 = None

        bool_expr33 = None

        arith_expr35 = None

        arith_expr37 = None


        BOOLEAN29_tree = None
        NOT30_tree = None
        LPAREN32_tree = None
        RPAREN34_tree = None
        RELOP36_tree = None

        try:
            try:
                # simple.g:94:3: ( BOOLEAN | NOT bool_atom | LPAREN bool_expr RPAREN | arith_expr RELOP arith_expr )
                alt9 = 4
                LA9 = self.input.LA(1)
                if LA9 == BOOLEAN:
                    alt9 = 1
                elif LA9 == NOT:
                    alt9 = 2
                elif LA9 == LPAREN:
                    LA9_3 = self.input.LA(2)

                    if (self.synpred13_simple()) :
                        alt9 = 3
                    elif (True) :
                        alt9 = 4
                    else:
                        if self._state.backtracking > 0:
                            raise BacktrackingFailed

                        nvae = NoViableAltException("", 9, 3, self.input)

                        raise nvae

                elif LA9 == PLUS or LA9 == MINUS or LA9 == IDENT or LA9 == INTEGER:
                    alt9 = 4
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 9, 0, self.input)

                    raise nvae

                if alt9 == 1:
                    # simple.g:94:5: BOOLEAN
                    pass 
                    root_0 = self._adaptor.nil()

                    BOOLEAN29=self.match(self.input, BOOLEAN, self.FOLLOW_BOOLEAN_in_bool_atom550)
                    if self._state.backtracking == 0:

                        BOOLEAN29_tree = self._adaptor.createWithPayload(BOOLEAN29)
                        self._adaptor.addChild(root_0, BOOLEAN29_tree)



                elif alt9 == 2:
                    # simple.g:95:4: NOT bool_atom
                    pass 
                    root_0 = self._adaptor.nil()

                    NOT30=self.match(self.input, NOT, self.FOLLOW_NOT_in_bool_atom555)
                    if self._state.backtracking == 0:

                        NOT30_tree = self._adaptor.createWithPayload(NOT30)
                        root_0 = self._adaptor.becomeRoot(NOT30_tree, root_0)

                    self._state.following.append(self.FOLLOW_bool_atom_in_bool_atom558)
                    bool_atom31 = self.bool_atom()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, bool_atom31.tree)


                elif alt9 == 3:
                    # simple.g:96:4: LPAREN bool_expr RPAREN
                    pass 
                    root_0 = self._adaptor.nil()

                    LPAREN32=self.match(self.input, LPAREN, self.FOLLOW_LPAREN_in_bool_atom563)
                    self._state.following.append(self.FOLLOW_bool_expr_in_bool_atom566)
                    bool_expr33 = self.bool_expr()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, bool_expr33.tree)
                    RPAREN34=self.match(self.input, RPAREN, self.FOLLOW_RPAREN_in_bool_atom568)


                elif alt9 == 4:
                    # simple.g:97:4: arith_expr RELOP arith_expr
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_arith_expr_in_bool_atom574)
                    arith_expr35 = self.arith_expr()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, arith_expr35.tree)
                    RELOP36=self.match(self.input, RELOP, self.FOLLOW_RELOP_in_bool_atom576)
                    if self._state.backtracking == 0:

                        RELOP36_tree = self._adaptor.createWithPayload(RELOP36)
                        root_0 = self._adaptor.becomeRoot(RELOP36_tree, root_0)

                    self._state.following.append(self.FOLLOW_arith_expr_in_bool_atom579)
                    arith_expr37 = self.arith_expr()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, arith_expr37.tree)


                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "bool_atom"

    class statement_return(ParserRuleReturnScope):
        def __init__(self):
            super(simpleParser.statement_return, self).__init__()

            self.tree = None




    # $ANTLR start "statement"
    # simple.g:100:1: statement : ( IDENT GETS arith_expr SEMI | SKIP SEMI | IF bool_expr THEN block ELSE block ENDIF SEMI | WHILE bool_expr DO block ENDWHILE SEMI );
    def statement(self, ):

        retval = self.statement_return()
        retval.start = self.input.LT(1)

        root_0 = None

        IDENT38 = None
        GETS39 = None
        SEMI41 = None
        SKIP42 = None
        SEMI43 = None
        IF44 = None
        THEN46 = None
        ELSE48 = None
        ENDIF50 = None
        SEMI51 = None
        WHILE52 = None
        DO54 = None
        ENDWHILE56 = None
        SEMI57 = None
        arith_expr40 = None

        bool_expr45 = None

        block47 = None

        block49 = None

        bool_expr53 = None

        block55 = None


        IDENT38_tree = None
        GETS39_tree = None
        SEMI41_tree = None
        SKIP42_tree = None
        SEMI43_tree = None
        IF44_tree = None
        THEN46_tree = None
        ELSE48_tree = None
        ENDIF50_tree = None
        SEMI51_tree = None
        WHILE52_tree = None
        DO54_tree = None
        ENDWHILE56_tree = None
        SEMI57_tree = None

        try:
            try:
                # simple.g:101:5: ( IDENT GETS arith_expr SEMI | SKIP SEMI | IF bool_expr THEN block ELSE block ENDIF SEMI | WHILE bool_expr DO block ENDWHILE SEMI )
                alt10 = 4
                LA10 = self.input.LA(1)
                if LA10 == IDENT:
                    alt10 = 1
                elif LA10 == SKIP:
                    alt10 = 2
                elif LA10 == IF:
                    alt10 = 3
                elif LA10 == WHILE:
                    alt10 = 4
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 10, 0, self.input)

                    raise nvae

                if alt10 == 1:
                    # simple.g:101:9: IDENT GETS arith_expr SEMI
                    pass 
                    root_0 = self._adaptor.nil()

                    IDENT38=self.match(self.input, IDENT, self.FOLLOW_IDENT_in_statement595)
                    if self._state.backtracking == 0:

                        IDENT38_tree = self._adaptor.createWithPayload(IDENT38)
                        self._adaptor.addChild(root_0, IDENT38_tree)

                    GETS39=self.match(self.input, GETS, self.FOLLOW_GETS_in_statement597)
                    if self._state.backtracking == 0:

                        GETS39_tree = self._adaptor.createWithPayload(GETS39)
                        root_0 = self._adaptor.becomeRoot(GETS39_tree, root_0)

                    self._state.following.append(self.FOLLOW_arith_expr_in_statement600)
                    arith_expr40 = self.arith_expr()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, arith_expr40.tree)
                    SEMI41=self.match(self.input, SEMI, self.FOLLOW_SEMI_in_statement602)


                elif alt10 == 2:
                    # simple.g:102:9: SKIP SEMI
                    pass 
                    root_0 = self._adaptor.nil()

                    SKIP42=self.match(self.input, SKIP, self.FOLLOW_SKIP_in_statement613)
                    if self._state.backtracking == 0:

                        SKIP42_tree = self._adaptor.createWithPayload(SKIP42)
                        self._adaptor.addChild(root_0, SKIP42_tree)

                    SEMI43=self.match(self.input, SEMI, self.FOLLOW_SEMI_in_statement615)


                elif alt10 == 3:
                    # simple.g:103:9: IF bool_expr THEN block ELSE block ENDIF SEMI
                    pass 
                    root_0 = self._adaptor.nil()

                    IF44=self.match(self.input, IF, self.FOLLOW_IF_in_statement626)
                    if self._state.backtracking == 0:

                        IF44_tree = self._adaptor.createWithPayload(IF44)
                        root_0 = self._adaptor.becomeRoot(IF44_tree, root_0)

                    self._state.following.append(self.FOLLOW_bool_expr_in_statement629)
                    bool_expr45 = self.bool_expr()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, bool_expr45.tree)
                    THEN46=self.match(self.input, THEN, self.FOLLOW_THEN_in_statement631)
                    self._state.following.append(self.FOLLOW_block_in_statement634)
                    block47 = self.block()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, block47.tree)
                    ELSE48=self.match(self.input, ELSE, self.FOLLOW_ELSE_in_statement636)
                    self._state.following.append(self.FOLLOW_block_in_statement639)
                    block49 = self.block()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, block49.tree)
                    ENDIF50=self.match(self.input, ENDIF, self.FOLLOW_ENDIF_in_statement641)
                    SEMI51=self.match(self.input, SEMI, self.FOLLOW_SEMI_in_statement644)


                elif alt10 == 4:
                    # simple.g:104:9: WHILE bool_expr DO block ENDWHILE SEMI
                    pass 
                    root_0 = self._adaptor.nil()

                    WHILE52=self.match(self.input, WHILE, self.FOLLOW_WHILE_in_statement655)
                    if self._state.backtracking == 0:

                        WHILE52_tree = self._adaptor.createWithPayload(WHILE52)
                        root_0 = self._adaptor.becomeRoot(WHILE52_tree, root_0)

                    self._state.following.append(self.FOLLOW_bool_expr_in_statement658)
                    bool_expr53 = self.bool_expr()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, bool_expr53.tree)
                    DO54=self.match(self.input, DO, self.FOLLOW_DO_in_statement660)
                    self._state.following.append(self.FOLLOW_block_in_statement663)
                    block55 = self.block()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, block55.tree)
                    ENDWHILE56=self.match(self.input, ENDWHILE, self.FOLLOW_ENDWHILE_in_statement665)
                    SEMI57=self.match(self.input, SEMI, self.FOLLOW_SEMI_in_statement668)


                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "statement"

    # $ANTLR start "synpred13_simple"
    def synpred13_simple_fragment(self, ):
        # simple.g:96:4: ( LPAREN bool_expr RPAREN )
        # simple.g:96:4: LPAREN bool_expr RPAREN
        pass 
        self.match(self.input, LPAREN, self.FOLLOW_LPAREN_in_synpred13_simple563)
        self._state.following.append(self.FOLLOW_bool_expr_in_synpred13_simple566)
        self.bool_expr()

        self._state.following.pop()
        self.match(self.input, RPAREN, self.FOLLOW_RPAREN_in_synpred13_simple568)


    # $ANTLR end "synpred13_simple"




    # Delegated rules

    def synpred13_simple(self):
        self._state.backtracking += 1
        start = self.input.mark()
        try:
            self.synpred13_simple_fragment()
        except BacktrackingFailed:
            success = False
        else:
            success = True
        self.input.rewind(start)
        self._state.backtracking -= 1
        return success



 

    FOLLOW_block_in_program316 = frozenset([1])
    FOLLOW_statement_in_block328 = frozenset([1, 11, 15, 16, 26])
    FOLLOW_add_expr_in_arith_expr353 = frozenset([1])
    FOLLOW_sub_expr_in_add_expr363 = frozenset([1, 5])
    FOLLOW_PLUS_in_add_expr366 = frozenset([5, 6, 21, 26, 27])
    FOLLOW_sub_expr_in_add_expr369 = frozenset([1, 5])
    FOLLOW_mult_expr_in_sub_expr382 = frozenset([1, 6])
    FOLLOW_MINUS_in_sub_expr385 = frozenset([5, 6, 21, 26, 27])
    FOLLOW_mult_expr_in_sub_expr388 = frozenset([1, 6])
    FOLLOW_unary_expr_in_mult_expr401 = frozenset([1, 4])
    FOLLOW_MULT_in_mult_expr404 = frozenset([5, 6, 21, 26, 27])
    FOLLOW_unary_expr_in_mult_expr407 = frozenset([1, 4])
    FOLLOW_MINUS_in_unary_expr419 = frozenset([5, 6, 21, 26, 27])
    FOLLOW_arith_atom_in_unary_expr421 = frozenset([1])
    FOLLOW_PLUS_in_unary_expr438 = frozenset([5, 6, 21, 26, 27])
    FOLLOW_arith_atom_in_unary_expr440 = frozenset([1])
    FOLLOW_arith_atom_in_unary_expr457 = frozenset([1])
    FOLLOW_set_in_arith_atom467 = frozenset([1])
    FOLLOW_LPAREN_in_arith_atom478 = frozenset([5, 6, 21, 26, 27])
    FOLLOW_arith_expr_in_arith_atom481 = frozenset([22])
    FOLLOW_RPAREN_in_arith_atom483 = frozenset([1])
    FOLLOW_or_expr_in_bool_expr498 = frozenset([1])
    FOLLOW_and_expr_in_or_expr510 = frozenset([1, 8])
    FOLLOW_AND_in_or_expr513 = frozenset([5, 6, 7, 21, 25, 26, 27])
    FOLLOW_and_expr_in_or_expr516 = frozenset([1, 8])
    FOLLOW_bool_atom_in_and_expr530 = frozenset([1, 9])
    FOLLOW_OR_in_and_expr533 = frozenset([5, 6, 7, 21, 25, 26, 27])
    FOLLOW_bool_atom_in_and_expr536 = frozenset([1, 9])
    FOLLOW_BOOLEAN_in_bool_atom550 = frozenset([1])
    FOLLOW_NOT_in_bool_atom555 = frozenset([5, 6, 7, 21, 25, 26, 27])
    FOLLOW_bool_atom_in_bool_atom558 = frozenset([1])
    FOLLOW_LPAREN_in_bool_atom563 = frozenset([5, 6, 7, 21, 25, 26, 27])
    FOLLOW_bool_expr_in_bool_atom566 = frozenset([22])
    FOLLOW_RPAREN_in_bool_atom568 = frozenset([1])
    FOLLOW_arith_expr_in_bool_atom574 = frozenset([10])
    FOLLOW_RELOP_in_bool_atom576 = frozenset([5, 6, 21, 26, 27])
    FOLLOW_arith_expr_in_bool_atom579 = frozenset([1])
    FOLLOW_IDENT_in_statement595 = frozenset([19])
    FOLLOW_GETS_in_statement597 = frozenset([5, 6, 21, 26, 27])
    FOLLOW_arith_expr_in_statement600 = frozenset([20])
    FOLLOW_SEMI_in_statement602 = frozenset([1])
    FOLLOW_SKIP_in_statement613 = frozenset([20])
    FOLLOW_SEMI_in_statement615 = frozenset([1])
    FOLLOW_IF_in_statement626 = frozenset([5, 6, 7, 21, 25, 26, 27])
    FOLLOW_bool_expr_in_statement629 = frozenset([12])
    FOLLOW_THEN_in_statement631 = frozenset([11, 15, 16, 26])
    FOLLOW_block_in_statement634 = frozenset([13])
    FOLLOW_ELSE_in_statement636 = frozenset([11, 15, 16, 26])
    FOLLOW_block_in_statement639 = frozenset([14])
    FOLLOW_ENDIF_in_statement641 = frozenset([20])
    FOLLOW_SEMI_in_statement644 = frozenset([1])
    FOLLOW_WHILE_in_statement655 = frozenset([5, 6, 7, 21, 25, 26, 27])
    FOLLOW_bool_expr_in_statement658 = frozenset([17])
    FOLLOW_DO_in_statement660 = frozenset([11, 15, 16, 26])
    FOLLOW_block_in_statement663 = frozenset([18])
    FOLLOW_ENDWHILE_in_statement665 = frozenset([20])
    FOLLOW_SEMI_in_statement668 = frozenset([1])
    FOLLOW_LPAREN_in_synpred13_simple563 = frozenset([5, 6, 7, 21, 25, 26, 27])
    FOLLOW_bool_expr_in_synpred13_simple566 = frozenset([22])
    FOLLOW_RPAREN_in_synpred13_simple568 = frozenset([1])



def main(argv, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr):
    from antlr3.main import ParserMain
    main = ParserMain("simpleLexer", simpleParser)
    main.stdin = stdin
    main.stdout = stdout
    main.stderr = stderr
    main.execute(argv)


if __name__ == '__main__':
    main(sys.argv)

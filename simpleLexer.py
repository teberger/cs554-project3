# $ANTLR 3.1.3 Mar 18, 2009 10:09:25 simple.g 2014-12-03 02:38:12

import sys
from antlr3 import *
from antlr3.compat import set, frozenset


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


class simpleLexer(Lexer):

    grammarFileName = "simple.g"
    antlr_version = version_str_to_tuple("3.1.3 Mar 18, 2009 10:09:25")
    antlr_version_str = "3.1.3 Mar 18, 2009 10:09:25"

    def __init__(self, input=None, state=None):
        if state is None:
            state = RecognizerSharedState()
        super(simpleLexer, self).__init__(input, state)


        self.dfa6 = self.DFA6(
            self, 6,
            eot = self.DFA6_eot,
            eof = self.DFA6_eof,
            min = self.DFA6_min,
            max = self.DFA6_max,
            accept = self.DFA6_accept,
            special = self.DFA6_special,
            transition = self.DFA6_transition
            )






    # $ANTLR start "MULT"
    def mMULT(self, ):

        try:
            _type = MULT
            _channel = DEFAULT_CHANNEL

            # simple.g:10:6: ( '*' )
            # simple.g:10:8: '*'
            pass 
            self.match(42)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "MULT"



    # $ANTLR start "PLUS"
    def mPLUS(self, ):

        try:
            _type = PLUS
            _channel = DEFAULT_CHANNEL

            # simple.g:11:6: ( '+' )
            # simple.g:11:8: '+'
            pass 
            self.match(43)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "PLUS"



    # $ANTLR start "MINUS"
    def mMINUS(self, ):

        try:
            _type = MINUS
            _channel = DEFAULT_CHANNEL

            # simple.g:12:7: ( '-' )
            # simple.g:12:9: '-'
            pass 
            self.match(45)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "MINUS"



    # $ANTLR start "NOT"
    def mNOT(self, ):

        try:
            _type = NOT
            _channel = DEFAULT_CHANNEL

            # simple.g:15:6: ( 'not' )
            # simple.g:15:8: 'not'
            pass 
            self.match("not")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "NOT"



    # $ANTLR start "AND"
    def mAND(self, ):

        try:
            _type = AND
            _channel = DEFAULT_CHANNEL

            # simple.g:16:5: ( '&' )
            # simple.g:16:7: '&'
            pass 
            self.match(38)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "AND"



    # $ANTLR start "OR"
    def mOR(self, ):

        try:
            _type = OR
            _channel = DEFAULT_CHANNEL

            # simple.g:17:4: ( '|' )
            # simple.g:17:6: '|'
            pass 
            self.match(124)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "OR"



    # $ANTLR start "RELOP"
    def mRELOP(self, ):

        try:
            _type = RELOP
            _channel = DEFAULT_CHANNEL

            # simple.g:18:7: ( ( '=' | '<' | '<=' | '>' | '>=' ) )
            # simple.g:18:9: ( '=' | '<' | '<=' | '>' | '>=' )
            pass 
            # simple.g:18:9: ( '=' | '<' | '<=' | '>' | '>=' )
            alt1 = 5
            LA1 = self.input.LA(1)
            if LA1 == 61:
                alt1 = 1
            elif LA1 == 60:
                LA1_2 = self.input.LA(2)

                if (LA1_2 == 61) :
                    alt1 = 3
                else:
                    alt1 = 2
            elif LA1 == 62:
                LA1_3 = self.input.LA(2)

                if (LA1_3 == 61) :
                    alt1 = 5
                else:
                    alt1 = 4
            else:
                nvae = NoViableAltException("", 1, 0, self.input)

                raise nvae

            if alt1 == 1:
                # simple.g:18:10: '='
                pass 
                self.match(61)


            elif alt1 == 2:
                # simple.g:18:16: '<'
                pass 
                self.match(60)


            elif alt1 == 3:
                # simple.g:18:22: '<='
                pass 
                self.match("<=")


            elif alt1 == 4:
                # simple.g:18:29: '>'
                pass 
                self.match(62)


            elif alt1 == 5:
                # simple.g:18:35: '>='
                pass 
                self.match(">=")






            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "RELOP"



    # $ANTLR start "IF"
    def mIF(self, ):

        try:
            _type = IF
            _channel = DEFAULT_CHANNEL

            # simple.g:21:4: ( 'if' )
            # simple.g:21:6: 'if'
            pass 
            self.match("if")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "IF"



    # $ANTLR start "THEN"
    def mTHEN(self, ):

        try:
            _type = THEN
            _channel = DEFAULT_CHANNEL

            # simple.g:22:6: ( 'then' )
            # simple.g:22:8: 'then'
            pass 
            self.match("then")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "THEN"



    # $ANTLR start "ELSE"
    def mELSE(self, ):

        try:
            _type = ELSE
            _channel = DEFAULT_CHANNEL

            # simple.g:23:6: ( 'else' )
            # simple.g:23:8: 'else'
            pass 
            self.match("else")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "ELSE"



    # $ANTLR start "ENDIF"
    def mENDIF(self, ):

        try:
            _type = ENDIF
            _channel = DEFAULT_CHANNEL

            # simple.g:24:7: ( 'fi' )
            # simple.g:24:9: 'fi'
            pass 
            self.match("fi")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "ENDIF"



    # $ANTLR start "SKIP"
    def mSKIP(self, ):

        try:
            _type = SKIP
            _channel = DEFAULT_CHANNEL

            # simple.g:25:6: ( 'skip' )
            # simple.g:25:8: 'skip'
            pass 
            self.match("skip")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "SKIP"



    # $ANTLR start "WHILE"
    def mWHILE(self, ):

        try:
            _type = WHILE
            _channel = DEFAULT_CHANNEL

            # simple.g:28:7: ( 'while' )
            # simple.g:28:9: 'while'
            pass 
            self.match("while")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "WHILE"



    # $ANTLR start "DO"
    def mDO(self, ):

        try:
            _type = DO
            _channel = DEFAULT_CHANNEL

            # simple.g:29:4: ( 'do' )
            # simple.g:29:6: 'do'
            pass 
            self.match("do")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "DO"



    # $ANTLR start "ENDWHILE"
    def mENDWHILE(self, ):

        try:
            _type = ENDWHILE
            _channel = DEFAULT_CHANNEL

            # simple.g:30:10: ( 'od' )
            # simple.g:30:12: 'od'
            pass 
            self.match("od")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "ENDWHILE"



    # $ANTLR start "GETS"
    def mGETS(self, ):

        try:
            _type = GETS
            _channel = DEFAULT_CHANNEL

            # simple.g:33:6: ( ':=' )
            # simple.g:33:8: ':='
            pass 
            self.match(":=")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "GETS"



    # $ANTLR start "SEMI"
    def mSEMI(self, ):

        try:
            _type = SEMI
            _channel = DEFAULT_CHANNEL

            # simple.g:34:6: ( ';' )
            # simple.g:34:8: ';'
            pass 
            self.match(59)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "SEMI"



    # $ANTLR start "LPAREN"
    def mLPAREN(self, ):

        try:
            _type = LPAREN
            _channel = DEFAULT_CHANNEL

            # simple.g:35:8: ( '(' )
            # simple.g:35:10: '('
            pass 
            self.match(40)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "LPAREN"



    # $ANTLR start "RPAREN"
    def mRPAREN(self, ):

        try:
            _type = RPAREN
            _channel = DEFAULT_CHANNEL

            # simple.g:36:8: ( ')' )
            # simple.g:36:10: ')'
            pass 
            self.match(41)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "RPAREN"



    # $ANTLR start "BLOCK"
    def mBLOCK(self, ):

        try:
            _type = BLOCK
            _channel = DEFAULT_CHANNEL

            # simple.g:37:7: ( 'block' )
            # simple.g:37:9: 'block'
            pass 
            self.match("block")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "BLOCK"



    # $ANTLR start "UNARY"
    def mUNARY(self, ):

        try:
            _type = UNARY
            _channel = DEFAULT_CHANNEL

            # simple.g:38:7: ( 'unary' )
            # simple.g:38:9: 'unary'
            pass 
            self.match("unary")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "UNARY"



    # $ANTLR start "BOOLEAN"
    def mBOOLEAN(self, ):

        try:
            _type = BOOLEAN
            _channel = DEFAULT_CHANNEL

            # simple.g:41:9: ( ( 'true' | 'false' ) )
            # simple.g:41:11: ( 'true' | 'false' )
            pass 
            # simple.g:41:11: ( 'true' | 'false' )
            alt2 = 2
            LA2_0 = self.input.LA(1)

            if (LA2_0 == 116) :
                alt2 = 1
            elif (LA2_0 == 102) :
                alt2 = 2
            else:
                nvae = NoViableAltException("", 2, 0, self.input)

                raise nvae

            if alt2 == 1:
                # simple.g:41:12: 'true'
                pass 
                self.match("true")


            elif alt2 == 2:
                # simple.g:41:21: 'false'
                pass 
                self.match("false")






            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "BOOLEAN"



    # $ANTLR start "IDENT"
    def mIDENT(self, ):

        try:
            _type = IDENT
            _channel = DEFAULT_CHANNEL

            # simple.g:42:7: ( ( 'a' .. 'z' | 'A' .. 'Z' ) ( 'a' .. 'z' | 'A' .. 'Z' | '0' .. '9' )* )
            # simple.g:42:9: ( 'a' .. 'z' | 'A' .. 'Z' ) ( 'a' .. 'z' | 'A' .. 'Z' | '0' .. '9' )*
            pass 
            if (65 <= self.input.LA(1) <= 90) or (97 <= self.input.LA(1) <= 122):
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse

            # simple.g:42:30: ( 'a' .. 'z' | 'A' .. 'Z' | '0' .. '9' )*
            while True: #loop3
                alt3 = 2
                LA3_0 = self.input.LA(1)

                if ((48 <= LA3_0 <= 57) or (65 <= LA3_0 <= 90) or (97 <= LA3_0 <= 122)) :
                    alt3 = 1


                if alt3 == 1:
                    # simple.g:
                    pass 
                    if (48 <= self.input.LA(1) <= 57) or (65 <= self.input.LA(1) <= 90) or (97 <= self.input.LA(1) <= 122):
                        self.input.consume()
                    else:
                        mse = MismatchedSetException(None, self.input)
                        self.recover(mse)
                        raise mse



                else:
                    break #loop3



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "IDENT"



    # $ANTLR start "INTEGER"
    def mINTEGER(self, ):

        try:
            _type = INTEGER
            _channel = DEFAULT_CHANNEL

            # simple.g:43:9: ( ( '0' .. '9' )+ )
            # simple.g:43:11: ( '0' .. '9' )+
            pass 
            # simple.g:43:11: ( '0' .. '9' )+
            cnt4 = 0
            while True: #loop4
                alt4 = 2
                LA4_0 = self.input.LA(1)

                if ((48 <= LA4_0 <= 57)) :
                    alt4 = 1


                if alt4 == 1:
                    # simple.g:43:12: '0' .. '9'
                    pass 
                    self.matchRange(48, 57)


                else:
                    if cnt4 >= 1:
                        break #loop4

                    eee = EarlyExitException(4, self.input)
                    raise eee

                cnt4 += 1



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "INTEGER"



    # $ANTLR start "WS"
    def mWS(self, ):

        try:
            _type = WS
            _channel = DEFAULT_CHANNEL

            # simple.g:46:4: ( ( ' ' | '\\t' | '\\n' | '\\r' | '\\f' )+ )
            # simple.g:46:6: ( ' ' | '\\t' | '\\n' | '\\r' | '\\f' )+
            pass 
            # simple.g:46:6: ( ' ' | '\\t' | '\\n' | '\\r' | '\\f' )+
            cnt5 = 0
            while True: #loop5
                alt5 = 2
                LA5_0 = self.input.LA(1)

                if ((9 <= LA5_0 <= 10) or (12 <= LA5_0 <= 13) or LA5_0 == 32) :
                    alt5 = 1


                if alt5 == 1:
                    # simple.g:
                    pass 
                    if (9 <= self.input.LA(1) <= 10) or (12 <= self.input.LA(1) <= 13) or self.input.LA(1) == 32:
                        self.input.consume()
                    else:
                        mse = MismatchedSetException(None, self.input)
                        self.recover(mse)
                        raise mse



                else:
                    if cnt5 >= 1:
                        break #loop5

                    eee = EarlyExitException(5, self.input)
                    raise eee

                cnt5 += 1
            #action start
            _channel = HIDDEN;
            #action end



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "WS"



    def mTokens(self):
        # simple.g:1:8: ( MULT | PLUS | MINUS | NOT | AND | OR | RELOP | IF | THEN | ELSE | ENDIF | SKIP | WHILE | DO | ENDWHILE | GETS | SEMI | LPAREN | RPAREN | BLOCK | UNARY | BOOLEAN | IDENT | INTEGER | WS )
        alt6 = 25
        alt6 = self.dfa6.predict(self.input)
        if alt6 == 1:
            # simple.g:1:10: MULT
            pass 
            self.mMULT()


        elif alt6 == 2:
            # simple.g:1:15: PLUS
            pass 
            self.mPLUS()


        elif alt6 == 3:
            # simple.g:1:20: MINUS
            pass 
            self.mMINUS()


        elif alt6 == 4:
            # simple.g:1:26: NOT
            pass 
            self.mNOT()


        elif alt6 == 5:
            # simple.g:1:30: AND
            pass 
            self.mAND()


        elif alt6 == 6:
            # simple.g:1:34: OR
            pass 
            self.mOR()


        elif alt6 == 7:
            # simple.g:1:37: RELOP
            pass 
            self.mRELOP()


        elif alt6 == 8:
            # simple.g:1:43: IF
            pass 
            self.mIF()


        elif alt6 == 9:
            # simple.g:1:46: THEN
            pass 
            self.mTHEN()


        elif alt6 == 10:
            # simple.g:1:51: ELSE
            pass 
            self.mELSE()


        elif alt6 == 11:
            # simple.g:1:56: ENDIF
            pass 
            self.mENDIF()


        elif alt6 == 12:
            # simple.g:1:62: SKIP
            pass 
            self.mSKIP()


        elif alt6 == 13:
            # simple.g:1:67: WHILE
            pass 
            self.mWHILE()


        elif alt6 == 14:
            # simple.g:1:73: DO
            pass 
            self.mDO()


        elif alt6 == 15:
            # simple.g:1:76: ENDWHILE
            pass 
            self.mENDWHILE()


        elif alt6 == 16:
            # simple.g:1:85: GETS
            pass 
            self.mGETS()


        elif alt6 == 17:
            # simple.g:1:90: SEMI
            pass 
            self.mSEMI()


        elif alt6 == 18:
            # simple.g:1:95: LPAREN
            pass 
            self.mLPAREN()


        elif alt6 == 19:
            # simple.g:1:102: RPAREN
            pass 
            self.mRPAREN()


        elif alt6 == 20:
            # simple.g:1:109: BLOCK
            pass 
            self.mBLOCK()


        elif alt6 == 21:
            # simple.g:1:115: UNARY
            pass 
            self.mUNARY()


        elif alt6 == 22:
            # simple.g:1:121: BOOLEAN
            pass 
            self.mBOOLEAN()


        elif alt6 == 23:
            # simple.g:1:129: IDENT
            pass 
            self.mIDENT()


        elif alt6 == 24:
            # simple.g:1:135: INTEGER
            pass 
            self.mINTEGER()


        elif alt6 == 25:
            # simple.g:1:143: WS
            pass 
            self.mWS()







    # lookup tables for DFA #6

    DFA6_eot = DFA.unpack(
        u"\4\uffff\1\26\3\uffff\10\26\4\uffff\2\26\3\uffff\1\26\1\47\3\26"
        u"\1\53\3\26\1\57\1\60\2\26\1\63\1\uffff\3\26\1\uffff\3\26\2\uffff"
        u"\2\26\1\uffff\1\74\1\75\1\76\1\26\1\100\3\26\3\uffff\1\75\1\uffff"
        u"\1\104\1\105\1\106\3\uffff"
        )

    DFA6_eof = DFA.unpack(
        u"\107\uffff"
        )

    DFA6_min = DFA.unpack(
        u"\1\11\3\uffff\1\157\3\uffff\1\146\1\150\1\154\1\141\1\153\1\150"
        u"\1\157\1\144\4\uffff\1\154\1\156\3\uffff\1\164\1\60\1\145\1\165"
        u"\1\163\1\60\1\154\2\151\2\60\1\157\1\141\1\60\1\uffff\1\156\2\145"
        u"\1\uffff\1\163\1\160\1\154\2\uffff\1\143\1\162\1\uffff\3\60\1\145"
        u"\1\60\1\145\1\153\1\171\3\uffff\1\60\1\uffff\3\60\3\uffff"
        )

    DFA6_max = DFA.unpack(
        u"\1\174\3\uffff\1\157\3\uffff\1\146\1\162\1\154\1\151\1\153\1\150"
        u"\1\157\1\144\4\uffff\1\154\1\156\3\uffff\1\164\1\172\1\145\1\165"
        u"\1\163\1\172\1\154\2\151\2\172\1\157\1\141\1\172\1\uffff\1\156"
        u"\2\145\1\uffff\1\163\1\160\1\154\2\uffff\1\143\1\162\1\uffff\3"
        u"\172\1\145\1\172\1\145\1\153\1\171\3\uffff\1\172\1\uffff\3\172"
        u"\3\uffff"
        )

    DFA6_accept = DFA.unpack(
        u"\1\uffff\1\1\1\2\1\3\1\uffff\1\5\1\6\1\7\10\uffff\1\20\1\21\1\22"
        u"\1\23\2\uffff\1\27\1\30\1\31\16\uffff\1\10\3\uffff\1\13\3\uffff"
        u"\1\16\1\17\2\uffff\1\4\10\uffff\1\11\1\26\1\12\1\uffff\1\14\3\uffff"
        u"\1\15\1\24\1\25"
        )

    DFA6_special = DFA.unpack(
        u"\107\uffff"
        )

            
    DFA6_transition = [
        DFA.unpack(u"\2\30\1\uffff\2\30\22\uffff\1\30\5\uffff\1\5\1\uffff"
        u"\1\22\1\23\1\1\1\2\1\uffff\1\3\2\uffff\12\27\1\20\1\21\3\7\2\uffff"
        u"\32\26\6\uffff\1\26\1\24\1\26\1\16\1\12\1\13\2\26\1\10\4\26\1\4"
        u"\1\17\3\26\1\14\1\11\1\25\1\26\1\15\3\26\1\uffff\1\6"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\31"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\32"),
        DFA.unpack(u"\1\33\11\uffff\1\34"),
        DFA.unpack(u"\1\35"),
        DFA.unpack(u"\1\37\7\uffff\1\36"),
        DFA.unpack(u"\1\40"),
        DFA.unpack(u"\1\41"),
        DFA.unpack(u"\1\42"),
        DFA.unpack(u"\1\43"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\44"),
        DFA.unpack(u"\1\45"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\46"),
        DFA.unpack(u"\12\26\7\uffff\32\26\6\uffff\32\26"),
        DFA.unpack(u"\1\50"),
        DFA.unpack(u"\1\51"),
        DFA.unpack(u"\1\52"),
        DFA.unpack(u"\12\26\7\uffff\32\26\6\uffff\32\26"),
        DFA.unpack(u"\1\54"),
        DFA.unpack(u"\1\55"),
        DFA.unpack(u"\1\56"),
        DFA.unpack(u"\12\26\7\uffff\32\26\6\uffff\32\26"),
        DFA.unpack(u"\12\26\7\uffff\32\26\6\uffff\32\26"),
        DFA.unpack(u"\1\61"),
        DFA.unpack(u"\1\62"),
        DFA.unpack(u"\12\26\7\uffff\32\26\6\uffff\32\26"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\64"),
        DFA.unpack(u"\1\65"),
        DFA.unpack(u"\1\66"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\67"),
        DFA.unpack(u"\1\70"),
        DFA.unpack(u"\1\71"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\72"),
        DFA.unpack(u"\1\73"),
        DFA.unpack(u""),
        DFA.unpack(u"\12\26\7\uffff\32\26\6\uffff\32\26"),
        DFA.unpack(u"\12\26\7\uffff\32\26\6\uffff\32\26"),
        DFA.unpack(u"\12\26\7\uffff\32\26\6\uffff\32\26"),
        DFA.unpack(u"\1\77"),
        DFA.unpack(u"\12\26\7\uffff\32\26\6\uffff\32\26"),
        DFA.unpack(u"\1\101"),
        DFA.unpack(u"\1\102"),
        DFA.unpack(u"\1\103"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\12\26\7\uffff\32\26\6\uffff\32\26"),
        DFA.unpack(u""),
        DFA.unpack(u"\12\26\7\uffff\32\26\6\uffff\32\26"),
        DFA.unpack(u"\12\26\7\uffff\32\26\6\uffff\32\26"),
        DFA.unpack(u"\12\26\7\uffff\32\26\6\uffff\32\26"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"")
    ]

    # class definition for DFA #6

    class DFA6(DFA):
        pass


 



def main(argv, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr):
    from antlr3.main import LexerMain
    main = LexerMain(simpleLexer)
    main.stdin = stdin
    main.stdout = stdout
    main.stderr = stderr
    main.execute(argv)


if __name__ == '__main__':
    main(sys.argv)

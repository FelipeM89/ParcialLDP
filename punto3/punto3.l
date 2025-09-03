%{
#include "punto3.tab.h"
%}

DIGIT   [0-9]
REAL    {DIGIT}+(\.{DIGIT}+)?

%%

"sqrt"          { return SQRT; }
{REAL}          { yylval.num = atof(yytext); return NUM; }
[ \t]           ;
\n              { return '\n'; }
.               { return yytext[0]; }

%%

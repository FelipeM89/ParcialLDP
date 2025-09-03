%{
#include <stdio.h>
#include <stdlib.h>
#include <math.h>

void yyerror(const char *s);
int yylex(void);
%}

%union {
    double num;
}

%token <num> NUM
%token SQRT
%left '+' '-'
%left '*' '/'
%type <num> expr

%%

input:
    | input expr '\n'   { printf("Resultado: %f\n", $2); }
    ;

expr:
      NUM                { $$ = $1; }
    | SQRT '(' expr ')'  { $$ = sqrt($3); }
    | expr '+' expr      { $$ = $1 + $3; }
    | expr '-' expr      { $$ = $1 - $3; }
    | expr '*' expr      { $$ = $1 * $3; }
    | expr '/' expr      { $$ = $1 / $3; }
    | '(' expr ')'       { $$ = $2; }
    ;

%%

void yyerror(const char *s) {
    fprintf(stderr, "Error: %s\n", s);
}

#include<stdio.h>
#define MAX 10
typedef struct stack{
   int top;
   int capacity;
   char *s;
}STACK;

STACK *createStack(){
    STACK *s = (STACK *)malloc(sizeof(STACK));
    s->top = -1;
    s->capacity = MAX;
    s->s = (char *)malloc(sizeof(char)*MAX);
    return s;
}

void push(STACK *s,char c)
{
    if(s->top == MAX-1)
        printf("Stack overflow");
    else{
        s->s[++s->top] = c;
    }
}

char pop(STACK *s)
{
    if(s->top == -1){
        printf("Stack underflow");
        return '\0';
    }
    else{
        s->top--;
        return s->s[s->top+1];
    }
}

char opposite(char c){
   switch(c){
   case ')':
          return '(';
   case '}':
          return '{';
   case ']':
          return '[';

   }

}

void main()
{
    char exp[10];
    printf("Enter Expression");
    scanf("%s",exp);
    STACK *s = createStack();
    for(int i=0;exp[i];i++){
        if(exp[i] == '(' || exp[i] == '{' || exp[i] == '[')
            push(s,exp[i]);
        else if(exp[i] == ')' || exp[i] == '}' || exp[i] == ']'){
            char c = pop(s);
            if(c != opposite(exp[i]) || c == '\0'){
                printf("Invalid Expression");
                return;
            }
        }
    }
    if(s->top != -1){
        printf("Invalid Expression");
    }
    else
        printf("Valid Expression");
}

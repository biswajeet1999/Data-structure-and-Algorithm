#include<stdio.h>
#include<stdlib.h>
#define capacity 100
typedef struct Stack
{
    int top;
    char *array;
}STACK;
STACK *createstack()
{
    STACK *stack;
    stack=(STACK *)malloc(sizeof(STACK));
    stack->top=-1;
    stack->array=(char *)malloc(capacity);
    return stack;
}
int isfull(STACK *stack)
{
    if(stack->top==capacity-1)
        return 1;
    else
        return 0;
}
int isempty(STACK *stack)
{
    if(stack->top==-1)
        return 1;
    else
        return 0;
}
void push(STACK *stack,char item)
{
    if(!isfull(stack)){
        stack->array[++stack->top]=item;
    }
}
char pop(STACK *stack)
{
    if(!isempty(stack)){
        char item;
        item=stack->array[stack->top];
        stack->top--;
        return item;
    }
}
void main()
{
    STACK *stack;
    stack=createstack();
    int i,j;// i for infix matrix and j for postfix matrix
    char infix[capacity],postfix[capacity];
    printf("Enter expression\n");
    gets(infix);
    for(i=0;infix[i]!='\0';i++);
    infix[i]=')';
    i++;
    infix[i]='\0';
    push(stack,'(');
    i=0,j=0;
    while(!isempty(stack))
    {
        if(infix[i]=='('){
            push(stack,'(');
            i++;
        }
        else if(infix[i]>='a' && infix[i]<='z' || infix[i]>='A' && infix[i]<='Z'){
            postfix[j]=infix[i];
            i++;j++;
        }
        else if(infix[i]==')'){
            while(stack->array[stack->top]!='('){
                    postfix[j]=pop(stack);
                    j++;
            }
            if(stack->array[stack->top]=='('){
                pop(stack);
                i++;
            }
        }
        else if(infix[i]=='^'){
            if(stack->array[stack->top]=='^'){
                postfix[j]=pop(stack);
                j++;
            }
            push(stack,'^');
            i++;
        }
        else if(infix[i]=='*' || infix[i]=='/'){
            while(stack->array[stack->top]=='*' || stack->array[stack->top]=='/' || stack->array[stack->top]=='^'){
                    postfix[j]=pop(stack);
                    j++;
            }
            push(stack,infix[i]);
            i++;
        }
        else if(infix[i]=='-' || infix[i]=='+'){
            while(stack->array[stack->top]=='*' || stack->array[stack->top]=='/' || stack->array[stack->top]=='^' || stack->array[stack->top]=='+' || stack->array[stack->top]=='-'){
                    postfix[j]=pop(stack);
                    j++;
            }
            push(stack,infix[i]);
            i++;
        }
    }
    puts(postfix);
}

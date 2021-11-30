#include<stdio.h>
#include<stdlib.h>
typedef struct Stack
{
    int top;
    int capacity;
    char *array;
}STACK;
STACK *createstack()
{
    STACK *stack;
    stack=(STACK *)malloc(sizeof(STACK));
    printf("Enter string size\n");
    scanf("%d",&stack->capacity);
    stack->top=-1;
    stack->array=(char *)malloc(stack->capacity);
    return stack;
}
void push(STACK *stack,char item)
{
    stack->array[++(stack->top)]=item;
}
char pop(STACK *stack)
{
    char item;
    item=stack->array[stack->top];
    stack->top--;
    return item;
}
void main()
{
    STACK *stack;
    stack=createstack();
    char c;
    printf("Enter string\n");
    while((c=getche())!=13){
        push(stack,c);
    }
    printf("\n");
    while(stack->top!=-1)
        printf("%c",pop(stack));
}

#include<stdio.h>
#include<stdlib.h>
typedef struct Stack
{
    int top;
    int capacity;
    int *array;
}STACK;
STACK *createstack()
{
    STACK *stack;
    stack=(STACK *)malloc(sizeof(STACK));
    printf("Enter capacity\n");
    scanf("%d",&stack->capacity);
    stack->top=-1;
    stack->array=(int *)malloc(stack->capacity*sizeof(int));
    return stack;
}
int isfull(STACK *stack)
{
    if(stack->top==stack->capacity-1){
        printf("Stack is FULL\n");
        return 1;
    }
    else
        return 0;
}
int isempty(STACK *stack)
{
    if(stack->top==-1){
        printf("Stack is EMPTY\n");
        return 1;
    }
    else
        return 0;
}
void push(STACK *stack)
{
    if(!isfull(stack)){
        int item;
        printf("Enter the item\n");
        scanf("%d",&item);
        stack->array[++stack->top]=item;
    }
}
int pop(STACK *stack)
{
    if(!isempty(stack)){
        int item;
        item=stack->array[stack->top];
        printf("You have removed %d\n",item);
        stack->top--;
    }
}
void main()
{
    STACK *stack;
    stack=createstack();
        while(1)
    {
        int item,choice;
        printf("CHOICE :\n1.push\t2.pop\t3.peek\t4.exit\n");
        printf("Enter your choice\n");
        scanf("%d",&choice);
        switch(choice)
        {
         case 1:
             push(stack);
             break;
         case 2:
             item=pop(stack);
             break;
         case 3:
            printf("You peeked %d\n",stack->array[stack->top]);
            break;
         case 4:
            exit(1);
         default:
             printf("Invallid choice\n");
        }
        getch();
        system("cls");
    }
}

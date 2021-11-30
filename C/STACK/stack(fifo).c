#include<stdio.h>
#include<stdlib.h>
typedef struct Stack
{
    int top;
    int capacity;
    int *array;
}STACK;
STACK *stack1;
STACK *createstack(int cap)
{
    STACK *stack;
    stack=(STACK *)malloc(sizeof(STACK));
    stack->top=-1;
    stack->capacity=cap;
    stack->array=(int *)malloc(stack->capacity);
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
void push(STACK *stack,int item)
{
    if(!isfull(stack)){
        stack->array[++stack->top]=item;
    }
}
int pop(STACK *stack)
{
    if(!isempty(stack)){
        int item;
        item=stack->array[stack->top];
        stack->top--;
        return item;
    }
}
static int popfo(STACK *stack)
{
    static int index;
    int item=NULL;
    if(!isempty(stack)){
         if(stack->top>=index){
              while(stack->top>index)
              {
                push(stack1,pop(stack));
              }
             item=stack->array[stack->top];
             index++;
        }
        while(stack1->top>-1)
        {
            push(stack,pop(stack1));
        }
      return item;
    }
}
void main()
{
    STACK *stack;
    int capacity;
    printf("Enter capacity\n");
    scanf("%d",&capacity);
    stack=createstack(capacity);
    stack1=createstack(capacity);
        while(1)
    {
        int item,choice;
        printf("CHOICE :\n1.push\t2.pop\t3.peek\t4.exit\n");
        printf("Enter your choice\n");
        scanf("%d",&choice);
        switch(choice)
        {
         case 1:
             printf("Enter the item\n");
             scanf("%d",&item);
             push(stack,item);
             break;
         case 2:
             item=popfo(stack);
             if(item==NULL)
                printf("Empty\n");
             else
                printf("you removed %d",item);
             break;
         case 3:
            printf("You peeked %d\n",stack->array[stack->top]);
            break;
         case 4:
            exit(1);
         default:
             printf("Invallid choice\n");
        }
        printf("\n");
    }
}

#include<stdio.h>
#include<stdlib.h>
int cap;
int isempty(int *top)
{
    if(*top==-1){
        printf("Stack is EMPTY\n");
        return 1;
    }
    else
        return 0;
}
int isfull(int *top)
{
    if(*top==cap-1){
        printf("Stack is FULL\n");
        return 1;
    }
    else
        return 0;
}
void push(int *a,int *top)
{
    if(!isfull(top)){
        (*top)++;
        int item;
        printf("Enter the item\n");
        scanf("%d",&item);
        *(a+(*top))=item;
    }
}
int pop(int *a,int *top)
{
    if(!isempty(top)){
        int item;
        item=a[*top];
        printf("You have removed %d\n",a[*top]);
        (*top)--;
        return item;
    }
}
void main()
{
    printf("Enter the capacity\n");
    scanf("%d",&cap);
    int a[cap],top=-1,choice,item;
    while(1)
    {
         printf("CHOICE :\n1.push\t2.pop\t3.peek\t4.exit\n");
        printf("Enter your choice\n");
        scanf("%d",&choice);
        switch(choice)
        {
         case 1:
             push(a,&top);
             break;
         case 2:
             item=pop(a,&top);
             break;
         case 3:
            printf("%d\n",a[top]);
            break;
         case 4:
            exit(1);
         default:
             printf("Invallid choice\n");
        }
        system("cls");
    }
}

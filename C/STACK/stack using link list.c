#include<stdio.h>
typedef struct node
{
    int data;
    struct node *next;
}NODE;
NODE *START=NULL;
void push(int data)
{
    NODE *temp,t;
    temp=(NODE *)malloc(sizeof(NODE));
    temp->data=data;
    temp->next=START;
    START=temp;
}
void pop()
{
    NODE *temp;
    if(START==NULL)
        printf("STACK IS EMPTY\n");
    else{
        temp=START;
        START=START->next;
        printf("You removed %d\n",temp->data);
        free(temp);
    }
}
void peek()
{
    if(START==NULL)
        printf("STACK IS EMPTY\n");
    else
        printf("Last time you entered %d \n",START->data);
}
void main()
{
    int x,data;
    while(1)
    {
        printf("1-insert\n2-delete\n3-peek\n4-exit\n");
        scanf("%d",&x);
        switch(x)
        {
        case 1:
            printf("Enter the data\n");
            scanf("%d",&data);
            push(data);
            break;
        case 2:
            pop();
            break;
        case 3:
            peek();
            break;
        case 4:
            exit(0);
        }
    }
}


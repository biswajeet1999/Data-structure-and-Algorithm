#include<stdio.h>
struct Node
{
    int data;
    struct Node *next;
};
void push(struct Node **head,int data)
{
    struct Node *temp=(struct Node *)malloc(sizeof(struct Node));
    temp->data=data;
    temp->next=NULL;
    if((*head)==NULL)
        (*head)=temp;
    else{
        struct Node *t=(*head);
        while(t->next!=NULL)
           t=t->next;
        t->next=temp;
    }
}
void pairWiseSwap(struct Node **head)
{
    struct Node *t=(*head);
    int data;
    while(t->next!=NULL){
        data=t->data;
        t->data=t->next->data;
        t->next->data=data;
        if(t->next->next !=NULL)
           t=t->next->next;
        else
            break;
    }
}
void printList(struct Node **head)
{
    struct Node *t=(*head);
    while(t!=NULL){
        printf("%d ",t->data);
        t=t->next;
    }
}
void main()
{
    struct Node *head=NULL;
    push(&head,1);
    push(&head,2);
    push(&head,3);
    push(&head,4);
    push(&head,5);
    push(&head,6);
    pairWiseSwap(&head);
    printList(&head);
}

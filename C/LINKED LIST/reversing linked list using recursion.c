#include<stdio.h>
#include<stdlib.h>
typedef struct Node
{
    int data;
    struct Node *next;
}Node;
Node *head=NULL;
Node *insert(Node *h,int data) /// insert at first
{
    Node *temp=(Node *)malloc(sizeof(Node));
    temp->data=data;
    temp->next=NULL;
    temp->next=h;
    h=temp;
    return h;
}
void display(Node *head)
{
    while(head){
        printf("%d  ",head->data);
        head=head->next;
    }
}
void *reverse(Node *h)
{
    if(h->next){
        reverse(h->next);
        h->next->next=h;
        h->next=NULL;
    }
    else{
        head =h;
    }
}
void main()
{
    head=insert(head,50);
    head=insert(head,40);
    head=insert(head,30);
    head=insert(head,20);
    head=insert(head,10);
    display(head);
    reverse(head);
    printf("\nAfter reverse\n");
    display(head);
}

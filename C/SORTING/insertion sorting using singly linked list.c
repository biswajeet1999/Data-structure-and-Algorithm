#include<stdio.h>
typedef struct node
{
    int data;
    struct node *next;
}Node;
Node *insert(Node *head,int data)
{
    Node *temp=(Node *)malloc(sizeof(Node));
    temp->data=data;
    temp->next=NULL;
    if(head==NULL)                // if list is empty
        head=temp;
    else if(head->data > data){   // if the data is insert at first
        temp->next=head;
        head=temp;
    }else{                        // if data insert at last or middle
        Node *t=head;
        while(t->next!=NULL){
            if(t->data < data && t->next->data > data)
                break;
            else t=t->next;
        }
        temp->next=t->next;
        t->next=temp;
    }
    return head;
}
void display(Node *head)
{
    while(head != NULL){
        printf("%d",head->data);
        if(head->next)
            printf(" -> ");
        head=head->next;
    }
}
void main()
{
    Node *head=NULL;
    int choise=1,data;
    while(choise){
        printf("Enter data\n");
        scanf("%d",&data);
        head=insert(head,data);
        printf("Enter: 1.insert  0.exit\n");
        scanf("%d",&choise);
    }
    display(head);
}

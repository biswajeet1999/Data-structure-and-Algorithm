#include<stdio.h>
#include<stdlib.h>
typedef struct node
{
    struct node *prev;
    struct node *next;
    int data;
}NODE;
void traverse(NODE **s)
{
    if(*s==NULL)
        printf("List is empty\n");
    else{
        NODE *temp;
        temp=*s;
        while(temp!=NULL){
            printf("%d\t",temp->data);
            temp=temp->next;
        }
    }
}
NODE *find(NODE **s,int data)
{
    NODE *temp;
    temp=*s;
    while(temp!=NULL){
       if(temp->data==data)
           return temp;
        temp=temp->next;
    }
    return NULL;
}
void insertFIRST(NODE **s,int data)
{
    NODE *temp;
    temp=(NODE *)malloc(sizeof(NODE));
    temp->data=data;
    temp->prev=NULL;
    if(*s==NULL){
        *s=temp;
        temp->next=NULL;
    }
    else{
        (*s)->prev=temp;
        temp->next=*s;
        *s=temp;
    }
}
void insertLAST(NODE **s,int data)
{
    NODE *temp=(NODE *)malloc(sizeof(NODE));
    temp->data=data;
    temp->next=NULL;
    if(*s==NULL){
        *s=temp;
        temp->prev=NULL;
    }
    else{
        NODE *t=*s;
        while(t->next!=NULL){
            t=t->next;
        }
        t->next=temp;
        temp->prev=t->next;
    }
}
void insertAFTERNODE(NODE **s,int data,int pos)
{
    NODE *position,*temp;
    temp=(NODE *)malloc(sizeof(NODE));
    temp->data=data;
    position=find(s,pos);
    if(position==NULL)
        printf("Invalid Position\n");
    else if(position->next==NULL){
        position->next=temp;
        temp->prev=position;
        temp->next=NULL;
    }
    else{
        temp->next=position->next;
        position->next->prev=temp;
        position->next=temp;
        temp->prev=position;
    }
}
void deletFIRST(NODE **s)
{
    if(*s==NULL)
        printf("List is empty\n");
    else{
        NODE *temp=*s;
        *s=temp->next;
        (*s)->prev=NULL;
        free(temp);
    }
}
void deletLAST(NODE **s)
{
    NODE *temp=*s;
    while(temp->next!=NULL){
        temp=temp->next;
    }
    temp->prev->next=NULL;
    free(temp);
}
void deletNODE(NODE **s,int pos)
{
    NODE *position=find(s,pos);
    if(position==NULL)
        printf("\nInvalid number\n");
    else if(position->prev==NULL){  //first node
        *s=position->next;
        (*s)->prev=NULL;
    }
    else if(position->next==NULL)   //last node
        position->prev->next=NULL;
    else{
        position->prev->next=position->next;
        position->next->prev=position->prev;
    }
    free(position);
}
void main()
{
    NODE *start=NULL;
    insertFIRST(&start,5);
    insertLAST(&start,10);
    insertFIRST(&start,3);
    insertAFTERNODE(&start,7,10);
    traverse(&start);
    deletNODE(&start,7);
    printf("\n");
    traverse(&start);
}

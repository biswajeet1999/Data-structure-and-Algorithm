#include<stdio.h>
#include<stdlib.h>
typedef struct node
{
    int data;
    struct node *next;
}NODE;
void traverse(NODE **l)
{
    if((*l)==NULL)
        printf("List is empty\n");
    else{
        NODE *temp=(*l)->next;
        do{
            printf("%d\t",temp->data);
            temp=temp->next;
        }while(temp!=(*l)->next);
    }
}
NODE *find(NODE **l,int data)
{
    if(*l==NULL)
        return NULL;
    else{
        NODE *temp=(*l)->next;
        do{
            if(temp->data==data){
                return temp;
            }
            temp=temp->next;
        }while(temp!=(*l)->next);
        return NULL;
    }
}
void insertFIRST(NODE **l,int data)
{
    NODE *temp=(NODE *)malloc(sizeof(NODE));
    temp->data=data;
    if(*l==NULL){
        *l=temp;
        temp->next=temp;
    }else{
        temp->next=(*l)->next;
         (*l)->next=temp;
    }
}
void insertLAST(NODE **l,int data)
{
    NODE *temp=(NODE *)malloc(sizeof(NODE));
    temp->data=data;
    if(*l==NULL){
        *l=temp;
        temp->next=temp;
    }else{
        temp->next=(*l)->next;
        (*l)->next=temp;
        *l=temp;
    }
}
void insertAFTERNODE(NODE **l,int data,int pos)
{
    NODE *position=find(l,pos);
    if(position==NULL)
        printf("data not found\n");
    else{
        NODE *temp=(NODE *)malloc(sizeof(NODE));
        temp->data=data;
        temp->next=position->next;
        position->next=temp;
        if(position==*l)
            *l=position->next;
    }
}
void deleteFIRST(NODE **l)
{
    if(*l==NULL)
        printf("List is empty\n");
    else if((*l)->next==*l){
        free(*l);
        *l=NULL;
    }
    else{
        NODE *temp=(*l)->next;
        (*l)->next=temp->next;
        free(temp);
    }
}
void deleteLAST(NODE **l)
{
    if(*l==NULL)
        printf("List is empty\n");
    else if((*l)->next==*l){
        free(*l);
        *l=NULL;
    }
    else{
        NODE *temp=(*l);
        while(temp->next!=*l){
            temp=temp->next;
        }
        temp->next=(*l)->next;
        free(*l);
        *l=temp;
    }
}
void deleteNODE(NODE **l,int pos)
{
    NODE *position=find(l,pos);
    if(position==NULL)
        printf("Data not found\n");
    else{
        if(position==(*l)->next)
            (*l)->next=position->next;
        else{
            NODE *temp=(*l)->next;
            do{
                temp=temp->next;
            }while(temp->next!=position);
            temp->next=position->next;
            if(position==*l)
                *l=temp;
        }
        free(position);
    }
}
void main()
{
    NODE *LAST=NULL;
    insertFIRST(&LAST,20);
    insertLAST(&LAST,40);
    insertFIRST(&LAST,10);
    insertLAST(&LAST,30);
    insertAFTERNODE(&LAST,50,30);
    //deleteFIRST(&LAST);
    //deleteLAST(&LAST);
    //deleteLAST(&LAST);
    //deleteLAST(&LAST);
    deleteNODE(&LAST,5);
    traverse(&LAST);
}

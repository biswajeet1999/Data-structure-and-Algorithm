#include<stdio.h>
#include<stdlib.h>
typedef struct node
{
    int data;
    struct node *next;
}NODE;
void insert(NODE **s,int data)
{
    NODE *temp=(NODE *)malloc(sizeof(NODE));
    temp->data=data;
    temp->next=NULL;
    if(*s==NULL)
        (*s)=temp;
    else{
       if((*s)->next==NULL){
          if(data<=(*s)->data){
              temp->next=(*s);
              (*s)=temp;
          }else
              (*s)->next=temp;
       }else{
          if((*s)->data > data){
            temp->next=*s;
            *s=temp;
          }else{
          NODE *t=(*s);
          while(t->next!=NULL){
            if(t->next->data < data)
               t=t->next;
            else
                break;
          }
          temp->next=t->next;
          t->next=temp;
          return;
          }
       }
    }
}
void delet(NODE **s)
{
    if(*s==NULL)
        printf("List is empty\n");
    else{
        NODE *temp=*s;
        *s=temp->next;
        free(temp);
    }

}
void display(NODE **s)
{
    if(*s==NULL)
        printf("List is empty\n");
    else{
        NODE *temp=*s;
        while(temp!=NULL){
            printf("%d ",temp->data);
            temp=temp->next;
        }
    }
}
void main()
{
    NODE *START=NULL;
    int c;
    while(1){
        printf("\n1.insert\n2.delete\n3.display\n4.exit\n");
        scanf("%d",&c);
        switch(c){
        case 1:
            printf("Enter item  ");
            scanf("%d",&c);
            insert(&START,c);
            break;
        case 2:
            delet(&START);
            break;
        case 3:
            display(&START);
            break;
        case 4:
            exit(1);
        }
    }

}

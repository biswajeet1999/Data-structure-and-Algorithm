#include<stdio.h>
#include<stdlib.h>
typedef struct node
{
    int data;
    struct node *link;
}NODE;
NODE *START=NULL;
NODE *search(int data)
{
    NODE *temp;
        temp=START;
            while(temp->link!=NULL)
            {
                if(temp->data==data)
                    return temp;
                else
                    temp=temp->link;
            }
            if(temp->data==data)
                return temp;
            else
                return NULL;
}
NODE *createnode()
{
    NODE *temp;
    temp=(NODE *)malloc(sizeof(NODE));
    return temp;
}
void insertFIRST(int info)
{
    NODE *temp;
    temp=createnode();
    temp->data=info;
    if(START==NULL){
        START=temp;
        START->link=NULL;
    }
    else{
        temp->link=START;
        START=temp;
    }
}
void insertLAST(int info)
{
    NODE *temp;
    temp=createnode();
    temp->data=info;
    if(START==NULL){
        START=temp;
        START->link=NULL;
    }
    else{
        NODE *t;
        t=START;
        while(t->link!=NULL)
            t=t->link;
        t->link=temp;
        temp->link=NULL;
    }
}
void insertAFTERNODE(int data,int info)
{
    NODE *temp,*find;
    temp=createnode();
    temp->data=info;
    if(START==NULL)
        printf("List is empty\n");
    else{
        find=search(data);
        if(find==NULL)
            printf("Data does not exist\n");
        else{
            temp->link=find->link;
            find->link=temp;
        }
  }
}
void deletenodeFIRST()
{
    if(START==NULL){
        printf("Linked list is empty\n");
    }
    else{
        NODE *temp;
        temp=START->link;
        free(START);
        START=temp;
    }
}
void deleteLAST()
{
    NODE *temp;
    if(START==NULL)
        printf("List is empty\n");
    else{
        temp=START;
        while(temp->link->link!=NULL)
             temp=temp->link;
        temp=temp->link;
        free(temp->link);
        temp->link=NULL;
    }
}
void deletAFTERNODE(int data)
{
    NODE *find,*temp;
    temp=START;
    if(START==NULL)
        printf("List is empty\n");
    else{
        find=search(data);
        if(find==NULL)
            printf("Data does not exist\n");
        else if(temp->link==NULL && temp->data==data)
        {
            free(START);
            START=NULL;
        }
        else if(temp->data==data){
            START=START->link;
            //free(find);
            free(temp);
        }
        else{
            while(temp->link->data!=find->data)
                temp=temp->link;
            temp->link=find->link;
            free(find);
        }
    }
}
void display()
{
    NODE *temp;
    temp=START;
    if(START==NULL)
        printf("List is empty\n");
    else{
        while(temp->link!=NULL){
            printf("%d\t",temp->data);
            temp=temp->link;
        }
        printf("%d\n",temp->data);
    }
}
void reverselist()
{
    if(START==NULL)
        printf("List is empty\n");
    else{
        NODE *t1,*t2;
        t1=t2=NULL;
        while(START!=NULL){
           t2=START->link;
           START->link=t1;
           t1=START;
           START=t2;
        }
        START=t1;
    }
}
void main()
{
    int choise,data,find;
    while(1){
        printf("\n1.insert first\t2.insert last\t3.insert after node\n4.delete first\t5.delete last\t6.delete after node\n7.display\t8.reverse\n9.exit\n");
        scanf("%d",&choise);
        switch(choise)
        {
        case 1:
            printf("Enter data\n");
            scanf("%d",&data);
            insertFIRST(data);
            break;
        case 2:
            printf("Enter data\n");
            scanf("%d",&data);
            insertLAST(data);
            break;
        case 3:
            printf("Enter data\n");
            scanf("%d",&data);
            printf("Enter data after you add\n");
            scanf("%d",&find);
            insertAFTERNODE(find,data);
            break;
        case 4:
            deletenodeFIRST();
            break;
        case 5:
            deleteLAST();
            break;
        case 6:
            printf("Enter data you delete\n");
            scanf("%d",&find);
            deletAFTERNODE(find);
            break;
        case 7:
            display();
            break;
        case 8:
            reverselist();
            display();
            break;
        case 9:
            exit(0);
        }
   }

}

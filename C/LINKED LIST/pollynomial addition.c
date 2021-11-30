#include<stdio.h>
#include<stdlib.h>
typedef struct node
{
    int coff,exp;
    struct node *next;
}NODE;
NODE *createpolly()
{
    NODE *head=NULL;
    int option=1;
    while(option==1){
        NODE *temp=(NODE *)malloc(sizeof(NODE));
        temp->next=NULL;
        printf("Enter coefficient and exponent: ");
        scanf("%dx^%d",&temp->coff,&temp->exp);
        temp->next=head;
        head=temp;
        printf("1.enter   2.exit: ");
        scanf("%d",&option);
    }
    return head;
}
NODE *sequencepolly(NODE *head)
{
    NODE *headtemp=NULL,*temp=NULL;
    while(head){
        temp=head;             // this step extract 1st element from non-sequence list and hold in temp  and update the old list
        head=temp->next;
        if(headtemp==NULL || headtemp->exp < temp->exp){  // this check if temporary head is empty or not and the temp will insert
            temp->next=headtemp;                          // at first or not
            headtemp=temp;
        }
        else{
            NODE *q=headtemp;
            while(q->next != NULL){                       // this will check temp will insert in the middle  or at last
                if(q->exp > temp->exp && q->next->exp < temp->exp)
                    break;
                else
                    q=q->next;
            }
            temp->next=q->next;
            q->next=temp;
        }

    }
    return headtemp;   // return the sequence list
}
NODE *addpolly(NODE *head1,NODE *head2)
{
    NODE *head3=NULL;
    while(head1 && head2){
        NODE *temp=(NODE *)malloc(sizeof(NODE));
        temp->next=NULL;
        if(head1->exp == head2->exp){   //  if  node of head1 and head2 are same
            temp->exp=head1->exp;
            temp->coff=head1->coff + head2->coff;
            head1=head1->next;head2=head2->next;
        }else if(head1->exp > head2->exp){  // if  node of head1 greater then node head 2
            temp->coff=head1->coff; temp->exp=head1->exp;
            head1=head1->next;
        }else{    // if node of head2 greater then node of head1
            temp->coff=head2->coff; temp->exp=head2->exp;
            head2=head2->next;
        }
        temp->next=head3;   // 3rd list will be update
        head3=temp;
    }
    while(head1!=NULL){  //if head1 have remaining nodes
        NODE *t=head1,*temp=(NODE *)malloc(sizeof(NODE));
        temp->exp=t->exp; temp->coff=t->coff;
        temp->next=head3;
        head3=temp;
        head1=head1->next;
    }
    while(head2!=NULL){   //if head2 have remaining nodes
        NODE *t=head2,*temp=(NODE *)malloc(sizeof(NODE));
        temp->exp=t->exp; temp->coff=t->coff;
        temp->next=head3;
        head3=temp;
        head2=head2->next;
    }
    return head3;
}
void display(NODE *head)
{
    while(head!=NULL){
        printf("%dx^%d",head->coff,head->exp);
        if(head->next){
            if(head->next->coff > 0)
                printf(" + ");
        }
        head=head->next;
    }
    printf("\n");
}
void main()
{
    NODE *head1=NULL,*head2=NULL,*head3=NULL;
    printf("Create first polynomial\n");
    head1=createpolly();
    head1=sequencepolly(head1);
    printf("Create second polynomial\n");
    head2=createpolly();
    head2=sequencepolly(head2);
    printf("first polynomial:  ");
    display(head1);
    printf("second polynomial:  ");
    display(head2);
    head3=addpolly(head1,head2);
    head3=sequencepolly(head3);
    display(head3);
}

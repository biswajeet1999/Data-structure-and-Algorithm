#include<stdio.h>
#include<stdlib.h>
#include<string.h>
typedef struct node
{
  long rollno;
  int sem;
  char a[20];
  struct node *next;
}NODE;
NODE *push(NODE *head,long rollno,int sem,char a[])
{
  NODE *temp=(NODE *)malloc(sizeof(NODE));
  temp->rollno=rollno;
  temp->sem=sem;
  strcpy(temp->a,a);
  temp->next=NULL;
  if(head==NULL)
    head=temp;
  else{
    NODE *t=head;
    while(t->next != NULL)
      t=t->next;
    t->next=temp;
  }
  return head;
}
NODE *pop(NODE *head)
{
  if(head==NULL)
    printf("List is EMPTY\n");
  else if(head->next==NULL){
    printf("you removed:\n");
    printf("%s",head->a);
    printf("\n%ld",head->rollno);
    printf("\n%d",head->sem);
    free(head);
    head=NULL;
  }
  else{
    NODE *temp=head;
    while(temp->next->next != NULL)
      temp=temp->next;
    printf("you removed:\n");
    printf("%s",temp->next->a);
    printf("\n%ld",temp->next->rollno);
    printf("\n%d",temp->next->sem);
    free(temp->next);
    temp->next=NULL;
  }
  return head;
}
void main()
{
  NODE *head=NULL;
  int option,sem;
  long rollno;
  char a[20],c;
  while(1){
    printf("\n1.push  2.pop  3.exit\n");
    printf("Enter: ");
    scanf("%d",&option);
    switch(option){
      case 1:
        printf("Enter student name rollno semistar\n");
        scanf("%s",a);
        scanf("%c",&c);
        scanf("%ld%d",&rollno,&sem);
        head=push(head,rollno,sem,a);
        break;
      case 2:
        head=pop(head);
        break;
      case 3:
        exit(1);
    }
  }
}

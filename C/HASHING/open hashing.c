#include<stdio.h>
#include<stdlib.h>
typedef struct hash
{
    long int rollno;
    int cgpa;
    char name[20];
    struct hash *next;
}HASH;
int HASH_FUN(long int key,int n)
{
    int sum=0,r;
    while(key >= n && key >9){   // why i take key > 9 , you can illustrate by taking example key= 12 and n= 2. here 1+2=3 but 3>2 sot it became an infinite loop
        while(key){
            r=r%10;
            sum+=r;
            key/=10;
        }
        key=sum;
    }
    if(key < n)              //  why i take this condition ,you can illustrate by taking above example
        return key;
    else
        return (n-1);
}
void insert(HASH *s,HASH t,int n)
{
    int key=HASH_FUN(t.rollno,n);
    if(s[key].rollno == 0)
        s[key]=t;
    else{
        HASH *temp=&s[key];
        while(temp->next != NULL)
            temp=temp->next;
        HASH *p=(HASH *)malloc(sizeof(HASH));
        *p=t;
        p->next=NULL;
        temp->next=p;
    }
}
void search(HASH *s,long int rollno,int n)
{
    int key=HASH_FUN(rollno,n);
    printf("Searching....................\n");
    if(s[key].rollno==rollno){
        printf("Searching successful\n");
        puts(s[key].name);
        printf("rollno: %ld",s[key].rollno);
        printf("cgpa: %d",s[key].cgpa);
    }
    else{
        HASH *t=s[key].next;
        while(t){
            if(t->rollno == rollno){
                printf("Searching successful\n");
                puts(t->name);
                printf("rollno: %ld",t->rollno);
                printf("\ncgpa: %d",t->cgpa);
                break;
            }
            else
                t=t->next;
        }
        if(t==NULL)
            printf("Searching unsuccessful\nData not found");
    }
}
void display(HASH *s,int n)
{
    system("cls");
    int i;
    HASH *t=NULL;
    for(i=0;i<n;i++){
        if(s[i].rollno){
            puts(s[i].name);
            printf("rollno: %ld",s[i].rollno);
            printf("\ncgpa: %d",s[i].cgpa);
            if(s[i].next){
                t=s[i].next;
                while(t){
                    printf("\n    ||   \n");
                    puts(t->name);
                    printf("rollno: %ld",t->rollno);
                    printf("\ncgpa: %d",t->cgpa);
                    t=t->next;
                }
            }
        }
        printf("\n\n");
    }
}
void main()
{
    int n,i,option;
    long int rollno;
    printf("Enter no of rows for hash table: ");
    scanf("%d",&n);
    HASH s[n],t;
    for(i=0;i<n;i++){  // here i assign all rollno to 0 to make it easy while inserting
        s[i].rollno=0;
        s[i].next=NULL;
    }
    i=0;
    while(1){
        printf("\n1. insert   2. search   3. display   4. exit\n");
        scanf("%d",&option);
        switch(option){
          case 1:
              t.next=NULL;
              printf("Enter name: ");
              fflush(stdin);
              gets(t.name);
              printf("enter rollno and cgpa\n");
              scanf("%ld%d",&t.rollno,&t.cgpa);
              insert(s,t,n);
              break;
          case 2:
              printf("Enter rollno: ");
              scanf("%ld",&rollno);
              search(s,rollno,n);
              break;
          case 3:
              display(s,n);
              break;
          case 4:
              exit(1);
        }
    }
}

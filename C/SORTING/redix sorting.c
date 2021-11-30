#include<stdio.h>

typedef struct node
{
    int data;
    struct node *next;
}Node;

Node *create_node(int data)
{
    Node *temp=(Node *)malloc(sizeof(Node));
    temp->data=data;
    temp->next=NULL;
    return temp;
}

int find_max_len(int *a,int n)
{
    int i,max=a[0],count=0;
    for(i=1;i<n;i++){
        if(a[i]>max)
            max=a[i];

    }
    while(max){
        count++;
        max/=10;
    }
    return count;
}

void main()
{
    int n;
    printf("enter no. of elements: ");
    scanf("%d",&n);
    int a[n],i,j,mod=10,div=1,temp,swap,len=0,k;
    for(i=0;i<n;i++)
    {
        scanf("%d",&a[i]);
    }
    Node *b[10],*t;
    len=find_max_len(a,n);
  for(k=1;k<=len;k++){
     for(i=0;i<10;i++)  // initialize all elements of array of pointers with null
     {
        b[i]=NULL;
     }
    for(i=0;i<n;i++)             // it will attach data in the array of pointers as per digit
    {
        temp=(a[i]%mod)/div;
        Node *temp_node=create_node(a[i]);
        if(b[temp]==NULL) b[temp]= temp_node;
        else{
          t=b[temp];
          while(t->next)
               t=t->next;
          t->next=temp_node;
        }
    }
   for(i=0;i<10;i++)               // sort data in each bucket
    {
      if(b[i] != NULL){
        t=b[i];
        while(t->next){
            if(t->data > t->next->data){
                swap=t->data;
                t->data=t->next->data;
                t->next->data=swap;
            }
            t=t->next;
        }
      }
    }
    for(i=0,j=0;i<10;i++)   // store all the data from bucket to array
    {
        t=b[i];
        while(t){
            a[j]=t->data;
            t=t->next;
            j++;
        }
    }
    mod*=10;
    div*=10;
  }
  for(i=0;i<n;i++){
    printf("%d  ",a[i]);
  }
}

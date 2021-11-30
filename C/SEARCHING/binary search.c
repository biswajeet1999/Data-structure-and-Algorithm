#include<stdio.h>
void bubblesort(int *a,int max)
{
    int i,n,temp;
    for(n=0;n<=max;n++){
      for(i=0;i<max-n;i++)
      {
          if(a[i]>a[i+1]){
              temp=a[i];
              a[i]=a[i+1];
              a[i+1]=temp;
          }
      }
    }
    printf("After sort\n");
    for(i=0;i<=max;i++)
       printf("%d\n",a[i]);
}
int binsearch(int *p,int max,int search)
{
    int min=0,mid;
    while(min<=max)
    {
        mid=(max+min)/2;
        if(p[mid]==search)
            return mid+1;
        else if(search<p[mid])
            max=mid-1;
        else
            min=mid+1;
    }
    return -1;
}
void main()
{
    int max,search,i,r;
    printf("Enter the max capacity\n");
    scanf("%d",&max);
    int a[max];
    printf("Enter the nos.\n");
    for(i=0;i<max;i++)
      scanf("%d",&a[i]);
    printf("Enter the element to search\n");
    scanf("%d",&search);
    bubblesort(a,max-1);
    r=binsearch(a,max-1,search);
    if(r==-1)
        printf("Not found");
    else
        printf("line %d",r);
}

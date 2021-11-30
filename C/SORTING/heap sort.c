#include<stdio.h>
void heapify(int *a,int i)
{
    int temp;
    while(a[i] > a[(i-1)/2]){
        temp=a[i];
        a[i]=a[(i-1)/2];
        a[(i-1)/2]=temp;
        i=(i-1)/2;
    }
}
void setposition(int *a,int j)
{
    int i=0,l,r,max,temp;
    while(i<j){
        l=2*i+1;
        r=2*i+2;
        if(l<=j && r<=j){   //if both child in the range
           if(a[l]>a[r])
              max=l;
           else
              max=r;
           temp=a[i];
           a[i]=a[max];
           a[max]=temp;
           i=max;
        }
        else if(l<=j){     //if only left child exist in the range
            if(a[l]>a[i]){
                temp=a[i];
                a[i]=a[l];
                a[l]=temp;
            }
            i=l;
        }
        else              // if no child present i.e the node in right position
            break;
    }
}
void heapsort(int a[],int n)
{
    int i=0,j=n-1,temp;
    if(i<j){
        temp=a[i];
        a[i]=a[j];
        a[j]=temp;
        setposition(a,j-1);
        heapsort(a,j);
    }
}
void display(int *a,int n)
{
    int i;
    for(i=0;i<n;i++)
        printf("%d ",a[i]);
}
void main()
{
    int a[10],i;
    printf("Enter the elements to heap\n");
    for(i=0;i<10;i++){
        scanf("%d",&a[i]);
        heapify(a,i);
    }
    printf("Before heap sort\n");
    display(a,10);
    heapsort(a,10);
    printf("\nafter heap sort\n");
    display(a,10);
}

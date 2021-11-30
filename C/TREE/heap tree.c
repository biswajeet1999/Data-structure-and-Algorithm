#include<stdio.h>
void insertheap(int a[],int j)
{
    int temp;
    int parent=(j-1)/2;
    while(a[j]>a[parent]){
        temp=a[j];
        a[j]=a[parent];
        a[parent]=temp;
        j=(j-1)/2;
        parent=(j-1)/2;
    }
}
int delet(int a[],int i)  //in heap data is always deleted from top
{
    int j=0,l,r;
    int temp,max;
    a[0]=a[i];  // i contains the index of last data
    i--;
    while(j<=i){
       l=(j*2)+1;
       r=(j*2)+2;
       if(l<=i && r<=i){   // two child are in range
            if(a[l]>a[r])
                max=l;
            else
                max=r;
            temp=a[j]; a[j]=a[max]; a[max]=temp;
            j=max;
       }
       else if(l<=r){    // left child exist and in range
            if(a[l]>a[j]){
                temp=a[l]; a[l]=a[j]; a[j]=temp;
            }
            j=l;
       }
       else   // no child and placed in right position but tree have more level then current node level
         break;
    }
    return i;
}
void display(int a[],int i)
{
    int j;
    printf("After heapify\n");
    for(j=0;j<i;j++)
        printf("%d  ",a[j]);
}
void main()
{
    int n,i=0,choise;
    printf("No of elements want to store\n");
    scanf("%d",&n);
    int a[n];
    while(1){
        printf("\n1. insert\n2.delete\n3.display\n4.exit\n");
        scanf("%d",&choise);
        switch(choise){
        case 1:
            if(i<n){
              printf("Enter data\n");
              scanf("%d",&a[i]);
              insertheap(a,i);
              i++;
            }else printf("Heap is full\n");
            break;
        case 2:
            i=delet(a,i);
            break;
        case 3:
            display(a,i);
            break;
        case 4:
            exit(0);
        default:
            printf("invalid choice");
        }
    }
}

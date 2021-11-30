#include<stdio.h>
#include<math.h>
void quick_sort(int a[],int f,int l)
{
    int i,first=f,temp;          // f = index of first element  l = index of last element  first contains the index of pivot element
    if(f > l)                         // if we put (f == l) then it will not work because when f == l the fun terminates
        return;                       // and the in previous fun from where it called, there right fun will call and there value
    else{                             // of f > l and the control enters the else condition of that function which gives
        for(i=f+1;i<=l;i++){          // segmentation fault
            if(a[i] < a[first]){
                if(abs(first-i) > 1){   // if the smaller element placed after some element then bring it just after the pivot element
                    temp=a[first+1];    //  after that
                    a[first+1]=a[i];
                    a[i]=temp;
                }
                temp=a[first];          // it will swap with the pivot element
                a[first]=a[first+1];
                a[first+1]=temp;
                first=first+1;
            }
        }
    }
    quick_sort(a,f,first-1);    // sort left part of the pivot value
    quick_sort(a,first+1,l);    // sort right part of the pivot value
}
void display(int a[],int n)
{
    int i;
    for(i=0;i<n;i++)
        printf("%d ",a[i]);
}
void main()
{
    int a[10],i;
    printf("Enter 10 elements\n");
    for(i=0;i<10;i++)
        scanf("%d",&a[i]);
    quick_sort(a,0,9);
    display(a,10);
}

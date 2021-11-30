#include<stdio.h>
void mergearray(int *a,int f,int p,int l)
{
    int temp[l-f+1],i,j,k=0;
    for(i=f,j=p+1;i<=p && j<=l;){
        if(a[i]>=a[j]){
            temp[k]=a[j]; k++;j++;
        }
        else{
            temp[k]=a[i]; k++;i++;
        }
    }
        for(j;j<=l;j++,k++){
            temp[k]=a[j];
        }
        for(i;i<=p;i++,k++){
            temp[k]=a[i];
        }
    j=f;
    for(i=0;i<l-f+1;i++,j++)
        a[j]=temp[i];
}
void mergesort(int *a,int f,int l)
{
    if(f==l)
        return;
    int p=(l+f)/2;
    mergesort(a,f,p);
    mergesort(a,p+1,l);
    mergearray(a,f,p,l);
}
void display(int *a,int n)
{
    int i;
    for(i=0;i<n;i++)
        printf("%d",a[i]);
}
void main()
{
    int n;
    printf("No of elements: ");
    scanf("%d",&n);
    int a[n],i,l,f;
    for(i=0;i<n;i++)
        scanf("%d",&a[i]);
    l=n-1;
    f=0;
    mergesort(a,f,l);
    display(a,n);
}

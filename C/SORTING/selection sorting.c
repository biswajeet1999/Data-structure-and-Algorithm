#include<stdio.h>
void main()
{
    int a[10],i,j,min,t;
    printf("Enter elements\n");
    for(i=0;i<10;i++)
        scanf("%d",&a[i]);
    for(i=0;i<9;i++){
        min=i;
        for(j=i+1;j<10;j++){
            if(a[j]<a[min])
               min=j;
        }
        t=a[i];
        a[i]=a[min];
        a[min]=t;
    }
    for(i=0;i<10;i++)
        printf("%d  ",a[i]);
}

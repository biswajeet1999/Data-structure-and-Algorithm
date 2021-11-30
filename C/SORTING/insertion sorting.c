#include<stdio.h>
void main()
{
    int a[10],i,j,temp;
    printf("Enter nos.\n");
    for(i=0;i<10;i++)
        scanf("%d",&a[i]);
    for(i=1;i<10;i++){
        for(j=i;j>0;j--){
            if(a[j]<a[j-1]){
                temp=a[j];
                a[j]=a[j-1];
                a[j-1]=temp;
            }
        }
    }
    for(i=0;i<10;i++)
        printf("%d  ",a[i]);
}

#include<stdio.h>
void main()
{
    int n;
    printf("Enter no of elements: ");
    scanf("%d",&n);
    int a[n],i,key,flag=0;
    printf("Enter elements to array\n");
    for(i=0;i<n;i++)
        scanf("%d",&a[i]);
    printf("Enter the value to search: ");
    scanf("%d",&key);
    for(i=0;i<n;i++){
      if(a[i]==key){
          flag=1;
          break;
      }
    }
    if(flag==1)
        printf("index=%d",i+1);
    else
        printf("Data not found");
}

#include<stdio.h>
void main()
{
    int r,c;
    printf("Enter no of rows and columns\n");
    scanf("%d%d",&r,&c);
    int a[r][c],i,j,count=0;  // count will count no. of non zero elements
    printf("Enter values for matrix\n");
    for(i=0;i<r;i++){
        for(j=0;j<c;j++){
            scanf("%d",&a[i][j]);
            if(a[i][j])
                count+=1;
        }
    }
    printf("Original Matrix\n");
    for(i=0;i<r;i++){
        for(j=0;j<c;j++)
            printf("%d ",a[i][j]);
        printf("\n");
    }
    count++;
    int spar[count][3],k;
    spar[0][0]=r;spar[0][1]=c;spar[0][2]=count-1;
    for(i=0,k=1;i<r;i++){
        for(j=0;j<c;j++){
            if(a[i][j]){
                spar[k][0]=i;spar[k][1]=j;spar[k][2]=a[i][j];
                k++;
            }
        }
    }
    printf("3 Tuple matrix:\n");
    for(i=0;i<count;i++){
        for(j=0;j<3;j++)
            printf("%d ",spar[i][j]);
        printf("\n");
    }
}

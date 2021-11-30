#include<stdio.h>
int size;
int count = 0;
void printKBIT(char *s,int n){
    int i;
    if(n == 0){
        for(int j=0;j<size;j++)
            printf("%c",s[j]);
        printf("\n");
        count++;
        return;
    }
    for(i=1;i<=n;i++){
        s[n-1] = i+48;
        printKBIT(s,n-1);
    }
}

int main()
{
    int n;
    printf("Enter k size: ");
    scanf("%d",&n);
    char s[n];
    size = n;
    printKBIT(s,n);
    printf("Possible combination: %d",count);
    return 0;
}

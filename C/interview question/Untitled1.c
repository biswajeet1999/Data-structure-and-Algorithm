#include<stdio.h>

void main()
{
    int a[9] = {-1,3,5,-2,7,-1,6,7,1};
    int m[9];
    m[0] = a[0];
    m[1] = (a[0]>a[1] ? a[0]:a[1]);
    for(int i=2;i<9;i++){
        m[i] = a[i-1]>m[i-2]+a[i]?a[i-1]:m[i-2]+a[i];
    }
    printf("%d",m[8]);
}

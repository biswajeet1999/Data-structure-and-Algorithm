#include<stdio.h>
#include<string.h>
#define MAX 20

int noOfDigits(int n)
{
    int count = 0;
    while(n > 0){
        count++;
        n/=10;
    }
    return count;
}

int power(int x, int n)
{
    int sum = 1;
    for(int i=1;i<=n;i++)
        sum*=10;
    return sum;
}

int hash(char *s, int n)
{
    int sum = 0;
    for(int i=0; i<n; i++){
        sum = (sum*power(10, noOfDigits(s[i]))) + s[i];
    }
    return sum;
}

int rabin_krap(char *s, int n, char *p, int m)
{
    int pattern_hash = hash(p ,m);
    int string_hash = hash(s, m);
    for(int i=0; i<= n-m; i++){
        if(i > 0)
            string_hash = (string_hash - s[i-1]*power(10, noOfDigits(string_hash)-noOfDigits(s[i-1])))*power(10, noOfDigits(s[i+m-1])) + s[i+m-1];
        if( pattern_hash == string_hash ){
            return i;
        }
    }
    return -1;
}

void main()
{
    char string[MAX], pattern[MAX];
    printf("Enter String: ");
    scanf("%s", string);
    printf("Enter pattern: ");
    scanf("%s", pattern);

    printf("Index: %d", rabin_krap(string, strlen(string), pattern, strlen(pattern)));
}

#include<stdio.h>
#include<string.h>
#include<stdlib.h>
#define TRUE 1
#define FALSE 0

int *preprocess(char *p, int len) {
    /* It will find logest common prefix from start that is suffix at ith position of pattern */
    int *preprocessedArray = (int *)calloc(len, sizeof(int));
    int j = 0;
    for(int i = 1; i < len; i++) {
        if(p[j] == p[i]) {
            preprocessedArray[i] = j + 1;
            j++;
        } else {
            preprocessedArray[i] = 0;
            j = 0;
        }
    }
    return preprocessedArray;
}

int KMP(char *s, char *p) {
    int n = strlen(s);
    int m = strlen(p);
    int *preprocessed = preprocess(p, m);
    int j = 0; // keep track of pattern
    int index = -1;
    for(int i = 0; i < n; i++) {
        if(s[i] == p[j]) {
            j++;
        } else {
            j = preprocessed[j-1];
        }
        if(j == m) { // substring found
            return (i-m+1);
        }
    }
    return FALSE;
}

int main() {
    char s[20], p[20];
    printf("Enter String: ");
    scanf("%s", s);
    printf("Enter Pattern: ");
    scanf("%s", p);
    printf("Found at: %d", KMP(s, p));
    return 0;
}
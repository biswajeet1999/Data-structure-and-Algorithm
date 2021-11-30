#include<stdio.h>
#include<limits.h>


void print_parenthization(int n, int s[n][n], int i, int j) {
  if (i == j) {
    printf("A%d ", i);
    return;
  }
  printf("(");
  print_parenthization(n, s, i, s[i][j]);
  print_parenthization(n, s, s[i][j]+1, j);
  printf(")");
}

void MCM(int *p, int n) {
  int m[n][n], s[n][n];
  for (int i = 0; i < n; i++) {
    m[i][0] = m[0][i] = m[i][i] = 0;
  }
  for (int dist = 2; dist <= n-1; dist++) {
    for (int i = 1; i <= n-dist; i++) {
      int j = i + dist - 1;
      m[i][j] = INT_MAX;
      for (int k = i; k < j; k++) {
        int q = m[i][k] + m[k+1][j] + p[i-1] * p[k] * p[j];
        if (q < m[i][j]) {
          m[i][j] = q;
          s[i][j] = k;
        }
      }
    }
  }
  print_parenthization(n, s, 1, n-1);
}

int main() {
  int n;
  printf("Enter no of matrices: ");
  scanf("%d", &n);
  int p[n+1];
  printf("Enter dimensions:\n");
  for (int i = 0; i <= n; i++) {
    scanf("%d", &p[i]);
  }
  MCM(p, n+1);
}
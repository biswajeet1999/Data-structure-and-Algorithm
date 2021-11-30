// N_Queen problem using 1D array
// Author:- Biswajeet padhi
// Date:- 6/2/2019
// 4th sem

#include<stdio.h>

int check(int board[], int n, int row) {
  // check same column
  int i, j;
  for (i = row-1; i >= 0; i--) {
    // two queen have same column
    if (board[i] == board[row]) {   
      return 0;
    }
  }
  // check left diagonal
  for (i = row-1, j = board[row]-1; i >= 0 && j >= 0; i--,j-- ) {
    if (board[i] == j) {
      return 0;
    }
  }
  // check right diagonal
  for (i = row-1, j = board[row]+1; i >= 0, j < n; i--,j++ ) {
    if (board[i] == j) {
      return 0;
    }
  }
}

int N_Queen(int board[], int n, int row) {
  // base condition when row no is equal to n
  if (row == n) {
    return 1;
  }
  
  int res = 0;
  
  for (int col = 0; col < n; col++) {
    // return 1 if position is correct else return 0
    board[row] = col;
    if (check(board, n, row)) {      
      res = N_Queen(board, n, row+1);
      if (res) {
        return 1;
      }
    }
  }
  return 0;
}

int main() {
  int n;
  printf("Enter no of queen: ");
  scanf("%d",&n);
  int board[n];
  N_Queen(board, n, 0);
  for (int i = 0; i < n; i++)
  {
    printf("%d  ", board[i]);
  }
  
  return 0;
}
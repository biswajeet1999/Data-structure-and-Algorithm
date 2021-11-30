#include<iostream>
using namespace std;
#define SIZE 500000

void factorial(int n, signed short int *fact) {
   fact[0] = 1;
   int carry = 0;
   for(int i = 2; i <= n; i++) {
      carry = 0;
      for(int j = 0; j < SIZE; j++) {
         int mul = (fact[j] * i ) + carry;
         fact[j] = (mul % 10);
         carry = mul / 10;
      }
   }
}

void print(signed short int fact[]) {
   int j = SIZE - 1;
   for(; fact[j] == 0; j--);
   while(j >= 0) {
      cout << fact[j];
      j--;
   }
   cout << endl;      
}

int main() {
   signed short int fact[SIZE] = {0};
   int n;
   cout << "Enter n: ";
   cin >> n;

   factorial(n, fact);
   print(fact);
   return 0;
}
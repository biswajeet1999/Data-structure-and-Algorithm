#include<iostream>
using namespace std;

inline int max(int num1, int num2) {
    return (num1 > num2) ? num1 : num2;
}

inline int min(int num1, int num2) {
    return (num1 < num2) ? num1 : num2;
}

// player 1 = 0, player 2 = 1
// array length should be power of 2 
int maxProfit(int *coins, int l, int r, int playerId) {
    if(l > r) {
        return 0;
    } else if(l == r) {
        
        if(playerId == 1) 
            return 0;
        return coins[l];

    } else if(l == r-1) {
        
        if(playerId == 1) 
            return min(coins[l], coins[r]);
        return max(coins[l], coins[r]);

    } else {
        if(playerId == 1) {
            if(coins[l] > coins[r])
                return maxProfit(coins, l + 1, r, 1 - playerId);
            return maxProfit(coins, l, r - 1, 1 - playerId);
        }
            
        return max( coins[l] + maxProfit(coins, l + 1, r, 1 - playerId), maxProfit(coins, l, r-1, 1 - playerId) + coins[r]  );
    }
}

int main () {

    int coins[] = {3, 9, 1, 2};
    int n = sizeof(coins) / sizeof(coins[0]);
    cout << maxProfit(coins, 0, n - 1, 0);
    return 0;
}
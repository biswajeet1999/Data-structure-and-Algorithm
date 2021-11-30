#include <iostream>
#include <string>
using namespace std;

void reset(char *arr, int len)
{
    for (int i = 0; i < len; i++)
    {
        arr[i] = '\0';
    }
}

void print(string str, char *temp, int len)
{
    int strCur = 0;
    for (int i = 0; i < len; i++)
    {
        if (temp[i])
        {
            cout << temp[i];
        }
        else
        {
            cout << str[strCur];
            strCur++;
        }
    }
    cout << endl;
}

void interleaving(string str1, string str2, char *temp, int len, int curPosition, int curCharIndex)
{
    // base case
    if (curCharIndex == str1.size())
    {
        print(str2, temp, len);
        return;
    }
    if (curPosition >= len)
        return;
    if (curCharIndex > str1.size())
        return;

    for (int i = curPosition; i < len; i++)
    {
        temp[i] = str1[curCharIndex];
        interleaving(str1, str2, temp, len, i + 1, curCharIndex + 1);
        temp[i] = '\0';
    }
}

int main()
{
    string str1, str2;
    cout << "Input string1: ";
    cin >> str1;
    cout << "Enter string2: ";
    cin >> str2;
    int n = str1.size() + str2.size();
    char temp[n];
    reset(temp, n);
    interleaving(str1, str2, temp, n, 0, 0);
    return 0;
}
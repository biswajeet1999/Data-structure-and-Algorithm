#include<stdio.h>
#include<malloc.h>
#include<string.h>

typedef struct Node {
    struct Node *left;
    char data;
    struct Node *right;
}Node;

Node *createNode(char data) {
    Node *n = (Node *)malloc(sizeof(Node));
    n->left = n->right = NULL;
    n->data = data;
    return n;
}

int getIndex(char *in, int start, int end, char ch) {
    for(int i = start ; i <= end; i++) {
        if(in[i] == ch) {
            return i;
        }
    }
}

Node *buildTree(char *pre, char *in, int inStart, int inEnd) {
    static int preCur = -1; // for each time it will increament by 1
    
    // Base Cases
    if(preCur >= (int)strlen(pre)) { // strlen return type is unsigned Int so it is imp to typecast it
        printf("Hello %d", preCur);
        return NULL;
    }
    if(strcmp(pre, "") == 0 || strcmp(in, "") == 0) {
        return NULL;
    }
    if(inStart > inEnd ) {
        printf("Bye");
        return NULL;
    }
    if(inEnd >= strlen(in)) {
        printf("Bye1");
        return NULL;
    }
    
    preCur++;
    
    Node *n = createNode(pre[preCur]);
    if(inStart == inEnd) {
        return n;
    }
    int index = getIndex(in, inStart, inEnd, pre[preCur]);
    n->left = buildTree(pre, in, inStart, index - 1);
    n->right = buildTree(pre, in, index + 1, inEnd);

    return n;
}

void Traverse(Node *root) {
    if(root) {
        Traverse(root->left);
        printf("%c", root->data);
        Traverse(root->right);
    }
}

int main() {

    char pre[10], in[10];
    Node *root = NULL;

    printf("Enter In Order traversal: ");
    scanf("%s", in);

    printf("Enter Pre Order traversal: ");
    scanf("%s", pre);

    root = buildTree(pre, in, 0, strlen(in) - 1);
    Traverse(root);
    return 0;
}
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


Node *buildTree(char *pre) {
    static int preCur = -1; // for each time it will increament by 1
    // Base Case
    if(strcmp(pre, "") == 0) {
        return NULL;
    }
    if(preCur >= (int)strlen(pre)) {
        return NULL;
    }

    preCur++;
    Node *n = createNode(pre[preCur]);

    if(pre[preCur] == 'L'){ // leafNode
        return n;
    }

    n->left = buildTree(pre);
    n->right = buildTree(pre);

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

    char pre[10];
    Node *root = NULL;

    printf("Enter Pre Order traversal: ");
    scanf("%s", pre);

    root = buildTree(pre);
    Traverse(root);
    return 0;
}

/* 
               I
            /     \
          L        I
                 /   \
                L     L
*/
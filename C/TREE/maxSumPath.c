#include<stdio.h>
#include<malloc.h>

typedef struct Node {
    struct Node *l;
    int data;
    struct Node *r;
}Node;

Node *createNode(int data) {
    Node *t = (Node *)malloc(sizeof(Node));
    t->data = data;
    t->l = t->r = NULL;
    return t;
}

Node *insert(Node *root, int data) {
    if(root == NULL) {
        return createNode(data);
    }
    if(data > root->data) {
        root->r = insert(root->r, data);
    }
    else if(data <  root->data) {
        root->l = insert(root->l, data);
    } else {
        printf("Duplicate data not allowed\n");
    }
    return root;
}

int max(int a, int b) {
    return a > b ? a : b;
}

int getMaxPathSum(Node *root) {
    if(root == NULL) {
        return 0;
    }
    return root->data + max(getMaxPathSum(root->l), getMaxPathSum(root->r));
}

int getMaxPath(Node *root) {
    if(root == NULL) {
        return 0;
    }
    int leftPath = getMaxPathSum(root->l);
    int rightPath = getMaxPathSum(root->r);
    int leftSubtreeSum = getMaxPath(root->l);
    int rightSubtreeSum = getMaxPath(root->r);
    return(max( leftPath + rightPath + root->data, max(leftSubtreeSum, rightSubtreeSum) ));
}

void main()
{
    Node *root = NULL;
    root = insert(root, 10);
    root = insert(root, 5);
    root = insert(root, 15);
    root = insert(root, 2);
    root = insert(root, 7);
    root = insert(root, 12);
    root = insert(root, 16);
    root = insert(root, 1);
    root = insert(root, 3);
    printf("%d", getMaxPath(root));
}
/* Matrix Chain Multiplication
    Author:- Biswajeet padhi
    Date:-   30/3/2019
    3rd sem
 */

#include<stdio.h>
#include<stdlib.h>
#define MAX 99999
typedef struct node
{
    char mat;   /* $ for actual matrix * for intermediate matrix */
    int r,c;
    struct node *left, *right;
    struct node *next, *prev;
}Node;

Node *createNode(char mat, int r, int c)
{
    Node *temp = (Node *)malloc(sizeof(Node));
    temp->mat = mat;
    temp->r = r;
    temp->c = c;
    temp->right = temp->left = NULL;
    temp->next = temp->prev = NULL;
    return temp;
}

void traverseMatrixTree(Node *matrixChain)
{
    if(matrixChain){
        if(matrixChain->mat == '*')
            printf("(");
        traverseMatrixTree(matrixChain->left);
        if(matrixChain->mat == '$')
            printf("<%d x %d>",matrixChain->r, matrixChain->c);
        traverseMatrixTree(matrixChain->right);
        if(matrixChain->mat == '*')
            printf(")");
    }
}

void traverse(Node *head){
    while(head){
        printf("%dX%d ", head->r,head->c);
        head = head->next;
    }
}

int main()
{
    int n;
    int min; /* it will hold min cost for multiplication */
    printf("Enter no of matrices: ");
    scanf("%d",&n);
    Node *matrixChain = NULL, *last = NULL;
    /* create matrix list */
    for(int i=0;i<n;i++){
        int r,c;
        printf("\nEnter row and column: ");
        scanf("%d %d",&r, &c);
        /* create new node and insert in the list */
        Node *newNode = createNode('$', r, c);
        if(matrixChain == NULL){
            matrixChain = newNode;
            last = matrixChain;
        }
        else{
           last->next = newNode;
           newNode->prev = last;
           last = newNode;
        }
    }
    /* create matrix tree */
    while(matrixChain ->next != NULL){  /* it will traverse until only one element present in the list */
        min = MAX;
        Node *temp = matrixChain;
        Node *mat1, *mat2;
        while(temp->next != NULL){   /* traverse matrix pair and find min cost */
            if( (temp->r * temp->c * temp->next->c) < min ){
                min = temp->r * temp->c * temp->next->c;
                mat1 = temp;  mat2 = temp->next;
            }
            temp = temp->next;
        }
        Node *t = createNode('*', mat1->r, mat2->c);
        t->left = mat1;
        t->right = mat2;
        t->prev = mat1->prev;
        if(t->prev)
            t->prev->next = t;
        t->next = mat2->next;
        if(t->next)
            t->next->prev = t;
        mat1->prev = mat2->prev = mat1->next = mat2->next = NULL;
        if(t->prev == NULL)   /* root node is multiplied so update matrixChain */
            matrixChain = t;
    }
    traverseMatrixTree(matrixChain);
    return 0;
}

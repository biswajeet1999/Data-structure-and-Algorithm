#include<stdio.h>
#include<stdlib.h>

/* Store the Intervals */
typedef struct Interval
{
    int low;
    int high;
}Interval;

typedef struct Node
{
    struct Node *left;
    Interval i;
    int maxBound;
    int height;
    struct Node *right;
}Node;



Node *createNode(Interval i)
{
    Node *node = (Node *)malloc(sizeof(Node));
    node->left = node->right = NULL;
    node->height = 0;
    node->i = i;
    node->maxBound = node->i.high;
    return(node);
}

int max(int a,int b)
{
    return((a>b)?a:b);
}

Node *LL(Node *root)
{
    Node *x,*y,*z;
    z=root;
    y=z->left;
    x=y->left;
    z->left=y->right;
    y->right=z;
    return y;
}

Node *LR(Node *root)
{
    Node *x,*y,*z;
    z=root;
    y=z->left;
    x=y->right;
    y->right=x->left;
    x->left=y;
    z->left=x;
    return x;
}

Node *RR(Node *root)
{
    Node *x,*y,*z;
    z=root;
    y=z->right;
    x=y->right;
    z->right=y->left;
    y->left=z;
    return y;
}

Node *RL(Node *root)
{
    Node *x,*y,*z;
    z=root;
    y=z->right;
    x=y->left;
    y->left=x->right;
    x->right=y;
    z->right=x;
    x=RR(z);
    return x;
}

int updateHeight(Node *root)
{
    if(root == NULL)   /* NULL root */
        return 0;
    else if(root->left == NULL && root->right==NULL){  /* leafNode  height = 0*/
        root->height = 0;
    }
    else{
        root->height = max(updateHeight(root->left),updateHeight(root->right))+1;
    }
    return(root->height);
}

int max3(int a, int b, int c)
{
    int max = a;
    if(max < b)
        max = b;
    if(max < c)
        max = c;
    return max;
}

int maxBound(Node *root)
{
    if(root==NULL)
        return 0;
    else if(root->left==NULL && root->right==NULL)
        root->maxBound = root->i.high;
    else
        root->maxBound = max3(maxBound(root->left),root->i.high,maxBound(root->right));
    return root->maxBound;
}

Node *insertInterval(Node *root,Interval i)
{
    if(root==NULL){     /* tree empty condition */
        root = createNode(i);
    }
    else if(i.low < root->i.low){
        root->left = insertInterval(root->left,i);
        updateHeight(root);
        int bf;
        if(root->right==NULL)
            bf = root->left->height+1;
        else
            bf = abs(root->left->height - root->right->height);
        if(bf>1){    /* rotation */
            if(i.low < root->left->i.low){
                root = LL(root);
            }
            else if(i.low > root->left->i.low){
                root = LR(root);
            }
        }
    }
    else if(i.low > root->i.low){
        root->right = insertInterval(root->right,i);
        updateHeight(root);
        int bf;
        if(root->left==NULL)
            bf = root->right->height+1;
        else
            bf = abs(root->left->height - root->right->height);
        if(bf>1){
            if(i.low > root->right->i.low)
                root = RR(root);
            else if(i.low < root->right->i.low)
                root = RL(root);
        }
    }
    else{
        if(root->i.high < i.high)
            root->i.high = i.high;
        else
            printf("Duplicate key\n");
    }
    updateHeight(root);
    maxBound(root);
    return root;
}

Node *SearchIntervalOverleap(Node *Tree,Interval i)
{
    Node *root = Tree;
    while(root){
        if(root->i.low <= i.high && i.low <= root->i.high) // intersection found
            return root;
        else if(root->left && root->left->maxBound > i.low)
            root = root->left;
        else root = root->right;
    }
    return root;   // it will return NULL
}

void inordertraversal(Node *root)
{
    if(root){
        inordertraversal(root->left);
        printf("[%d,%d,%d]",root->i.low,root->i.high,root->height);
        inordertraversal(root->right);
    }
}

void display(Node *root,int space)
{
    if(root){
        display(root->right,space+20);
        int i;
        printf("\n\n\n\n");
        for(i=1;i<=space;i++)
            printf(" ");
        system("color 2");
        printf("[(%-3d,%3d)",root->i.low,root->i.high);
        printf("max: %3d]",root->maxBound);
        display(root->left,space+20);
    }
}

int main()
{
    Node *IntervalTree = NULL;
    Interval i ={5,20};
    IntervalTree = insertInterval(IntervalTree,i);
    i.low = 10,i.high=30;
    IntervalTree = insertInterval(IntervalTree,i);
    i.low = 12,i.high=15;
    IntervalTree = insertInterval(IntervalTree,i);
    i.low = 15,i.high=20;
    IntervalTree = insertInterval(IntervalTree,i);
    i.low = 17,i.high=19;
    IntervalTree = insertInterval(IntervalTree,i);
    i.low = 30,i.high=40;
    IntervalTree = insertInterval(IntervalTree,i);
    i.low = 6,i.high=8;
    IntervalTree = insertInterval(IntervalTree,i);

    display(IntervalTree,0);

    i.low = 6; i.high = 7;
    Node *search = SearchIntervalOverleap(IntervalTree,i);
    printf("\n[%d,%d]",search->i.low,search->i.high);

    printf("\n\n\n");
}

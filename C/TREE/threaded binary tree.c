 // single threaded tree
#include<stdio.h>
#include<stdlib.h>
typedef struct node
{
    struct node *l;
    int data,isthread;
    struct node *r;
}NODE;
NODE *treeroot=NULL;
NODE *createnode(int data)
{
    NODE *temp=(NODE *)malloc(sizeof(NODE));
    temp->l=temp->r=NULL;
    temp->data=data;
    temp->isthread=0;
    return temp;
}
NODE *find(NODE *root,int data)
{
    if(root->data == data)   //  it is possible when tree has only one child
        return NULL;
    else if(root->l->data == data)
        return root;
    else if(root->l->r != NULL)
        if(root->l->r->data == data)
            return root;
    else if(root->data > data)
        return(find(root->l,data));
    else if(root->data < data)
        return (find(root->r,data));
}
void thread(NODE *root)
{
    NODE *inordersuccessor=find(treeroot,root->data);
    root->r=inordersuccessor;
    if(root->r)
        root->isthread=1;
    else
        root->isthread=0;
}
void insert(NODE **root,int data)
{
    if((*root)==NULL){
        NODE *temp=createnode(data);
        (*root)=temp;
        thread(*root);
    }
    else if((*root)->isthread && (*root)->data < data){
        NODE *temp=createnode(data);
        (*root)->r=temp;
        thread(*root);
    }
    else if(data > (*root)->data)
        insert(&((*root)->r),data);
    else if(data < (*root)->data)
        insert(&((*root)->l),data);
    else
        printf("Duplicate key\n");
}
void display(NODE *root)
{
    while(root->l)
        root = root->l;
    printf("%d ",root->data);
    if(root->right && root->isthread==0){
        root = root->r;
        printf("%d ",root->data);
    }
    if(root->isthread == 1){
        root = root->r;
        printf("%d",root->data);
        root = root->r;
    }
    if(root == NULL)
        return;
}
void main()
{
    insert(&treeroot,7);
    insert(&treeroot,5);
    insert(&treeroot,9);
    insert(&treeroot,2);
    insert(&treeroot,6);
    insert(&treeroot,8);
    insert(&treeroot,9);
    display(treeroot);
}

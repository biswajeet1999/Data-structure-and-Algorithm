#include<stdio.h>
#include<stdlib.h>
#include<string.h>
typedef struct tree
{
    struct tree *l;
    int data,hight;
    struct tree *r;
}TREE;
TREE *treeroot=NULL;
int max(int x,int y)
{
    if(x>=y)
        return x;
    else
        return y;
}
int hight(TREE *root)
{
    if(root==NULL)
        return 0;
    else if(root->l==NULL && root->r==NULL){
        root->hight=0;
        return root->hight;
    }
    else{
        root->hight=max(hight(root->l),hight(root->r))+1;
        return root->hight;
    }
}
TREE *parent(TREE *proot,TREE *root)
{
    if(proot==root)
        return NULL;
    else if(proot->r==root || proot->l==root)
        return proot;
    else if(root->data > proot->data)
        return(parent(proot->r,root));
    else
        return(parent(proot->l,root));
}
TREE *ll(TREE *root)
{
    TREE *x,*y,*z;
    z=root;
    y=z->l;
    x=y->l;
    z->l=y->r;
    y->r=z;
    return y;
}
TREE *rr(TREE *root)
{
    TREE *x,*y,*z;
    z=root;
    y=z->r;
    x=y->r;
    z->r=y->l;
    y->l=z;
    return y;
}
TREE *lr(TREE *root)
{
    TREE *x,*y,*z;
    z=root;
    y=z->l;
    x=y->r;
    y->r=x->l;
    x->l=y;
    z->l=x;
   // x=ll(z);
    return x;
}
TREE *rl(TREE *root)
{
    TREE *x,*y,*z;
    z=root;
    y=z->r;
    x=y->l;
    y->l=x->r;
    x->r=y;
    z->r=x;
    x=rr(z);
    return x;
}
TREE *insert(TREE *root,int data)
{
    if(root==NULL){
       TREE *temp=(TREE *)malloc(sizeof(TREE));
       temp->data=data;
       temp->l=temp->r=NULL;
       root=temp;
    }
    else if(data > root->data){
        root->r=insert(root->r,data);
        root->hight=hight(root);
        int bf;
        if(root->l==NULL)
            bf=root->hight;
        else
            bf=(root->l->hight) - (root->r->hight);
        if(bf <= -2 || bf >= 2){
            if(data > root->r->data)
                root=rr(root);
            else
                root=rl(root);
        }
    }
    else if(data < root->data){
        root->l=insert(root->l,data);
        root->hight=hight(root);
        int bf;
        if(root->r==NULL)
            bf=root->hight;
        else
            bf=(root->l->hight) - (root->r->hight);
        if(bf <= -2 || bf >=2){
            if(data < root->l->data){
                root=ll(root);
            }
            else
               root=lr(root);
        }
    }
    root->hight=hight(root);
    return root;
}
void preorder(TREE *root)
{
    if(root){
        printf("%d  ",root->data);
        preorder(root->l);
        preorder(root->r);
    }
}
void displayhight(TREE *root)
{
    if(root){
        printf("%d  ",root->hight);
        displayhight(root->l);
        displayhight(root->r);
    }
}
void display(TREE *root,int space)
{
    if(root){
        display(root->r,space+10);
        int i;
        printf("\n");
        for(i=1;i<=space;i++)
            printf(" ");
        printf("%d",root->data);
        display(root->l,space+10);
    }
}

void main()
{
    treeroot=insert(treeroot,1);
    treeroot=insert(treeroot,2);
    treeroot=insert(treeroot,3);
    treeroot=insert(treeroot,4);
    treeroot=insert(treeroot,5);
    treeroot=insert(treeroot,6);
    treeroot=insert(treeroot,7);
    treeroot=insert(treeroot,10);
    treeroot=insert(treeroot,15);
    treeroot=insert(treeroot,13);
    treeroot=insert(treeroot,17);

    treeroot=insert(treeroot,20);
    treeroot=insert(treeroot,60);
    treeroot=insert(treeroot,80);
    treeroot=insert(treeroot,50);
    treeroot=insert(treeroot,40);
    treeroot=insert(treeroot,45);
    treeroot=insert(treeroot,67);
    treeroot=insert(treeroot,89);
    treeroot=insert(treeroot,90);
    treeroot=insert(treeroot,23);
    treeroot=insert(treeroot,13);
    preorder(treeroot);
    printf("\n");
    int high=hight(treeroot);
   // displayhight(treeroot);
    printf("\n\n");
    display(treeroot,0);
}

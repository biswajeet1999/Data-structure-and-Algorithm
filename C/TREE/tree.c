#include<stdio.h>
#include<stdlib.h>
typedef struct tree
{
    struct tree *l;
    int data;
    struct tree *r;
}TREE;
 TREE *treeroot=NULL;
typedef struct queue
{
    int front,rear;TREE *a[20];
}QUEUE;
QUEUE *createqueue()
{
    QUEUE *q=(QUEUE *)malloc(sizeof(QUEUE));
    q->front=q->rear=-1;
    return q;
}
void enqueue(QUEUE *q,TREE *data)
{
    if((q->front==0 && q->rear==19) || q->front==q->rear+1)
        printf("Queue is full\n");
    else{
        if(q->rear==-1 && q->front==-1){
            q->front=q->rear=0;
            q->a[q->rear]=data;
        }
        else{
            q->rear=(q->rear)+1%20;
            q->a[q->rear]=data;
        }
    }
}
TREE *dequeue(QUEUE *q)
{
    if(q->front==-1)
        printf("Queue is empty\n");
    else{
        TREE *data;
        if(q->front==q->rear){
            data=q->a[q->front];
            q->front=q->rear=-1;
        }
        else{
            data=q->a[q->front];
            q->front=(q->front+1)%20;
        }
        return data;
    }
}
void insert(TREE **root,int data)
{

    if(*root==NULL){
        TREE *temp=(TREE *)malloc(sizeof(TREE));
        temp->l=temp->r=NULL;
        temp->data=data;
        *(root)=temp;
    }
    else if((*root)->l==NULL && (*root)->r==NULL){
        TREE *temp=(TREE *)malloc(sizeof(TREE));
        temp->l=temp->r=NULL;
        temp->data=data;
        if(data < (*root)->data)
            (*root)->l=temp;
        else if(data > (*root)->data)
            (*root)->r=temp;
    }
    else{
        if(data < (*root)->data)
            insert(&((*root)->l),data);
        else if(data > (*root)->data)
            insert(&((*root)->r),data);
    }
}
void preordertraversal(TREE *root)
{
    if(root){
        printf("%d\t",root->data);
        preordertraversal(root->l);
        preordertraversal(root->r);
    }
}
void postordertraversal(TREE *root)
{
    if(root){
        postordertraversal(root->l);
        postordertraversal(root->r);
        printf("%d\t",root->data);
    }
}
void inordertraversal(TREE *root)
{
    if(root){
        inordertraversal(root->l);
        printf("%d\t",root->data);
        inordertraversal(root->r);
    }
}
void levelordertraversal(TREE *root,QUEUE *q)
{
    if(root==NULL)
        printf("Tree is empty\n");
    else{
        TREE *temp=NULL;
        enqueue(q,root);
        while(q->rear!=-1){
            temp=dequeue(q);
            printf("%d  ",temp->data);
            if(temp->l)
                enqueue(q,temp->l);
            if(temp->r)
                enqueue(q,temp->r);
        }
    }
}
TREE *findmax(TREE *root)
{
    if(root->l==NULL && root->r==NULL)
        return root;
    else if(root->r==NULL)
        return root;
    else
        return findmax(root->r);
}
TREE *parent(TREE *root,int data)
{
    if(root->data==data)
        return root;
    else{
        if(root->l->data==data || root->r->data==data)
            return root;
        else{
            if(root->data > data)
                return(parent(root->l,data));
            else
                return(parent(root->r,data));
        }
    }
}
TREE *find(TREE *root,int data)  // find the address of given node
{
    if(root==NULL)
        return NULL;
    else if(root->data > data)
        return find(root->l,data);
    else if(root->data < data)
        return find(root->r,data);
    else
        return root;
}
TREE *delet(TREE *root,int data)
{
   if(root==NULL)
       printf("data not found");
   else if(data > root->data)
       root->r=delet(root->r,data);
   else if(root->data > data)
       root->l = delet(root->l,data);
   else{
      if(root->l && root->r){   //node has 2 child
          TREE *temp=findmax(root->l);
          root->data=temp->data;
          root->l=delet(root->l,root->data);
      }
      else{   // node has one or no child
          TREE *temp=root;
          if(root->l==NULL)
             root=root->r;
          else if(root->r==NULL)
            root=root->l;
          free(temp);
      }
   }
   return(root);
}


void main()
{
    insert(&treeroot,10);
    insert(&treeroot,5);
    insert(&treeroot,15);
    insert(&treeroot,2);
    insert(&treeroot,7);
    insert(&treeroot,12);
    insert(&treeroot,16);
    insert(&treeroot,1);
    insert(&treeroot,3);
    
    
    // insert(&treeroot,14);
    // insert(&treeroot,13);
    // insert(&treeroot,15);
    // insert(&treeroot,19);
    int c;
    QUEUE *q=createqueue();
    while(1){
        printf("\n1. insert   2. pre order traversal\n3. in order traversal  4. post order traversal  5. level order traversal\n6. max value   7. delete\n8. exit\n");
        scanf("%d",&c);
        switch(c){
    case 1:
        printf("Enter data\n");
        scanf("%d",&c);
        insert(&treeroot,c);
        break;
    case 2:
        preordertraversal(treeroot);
        break;
    case 3:
        inordertraversal(treeroot);
        break;
    case 4:
        postordertraversal(treeroot);
        break;
    case 5:
        levelordertraversal(treeroot,q);
        break;
    case 6:
        printf("%d",findmax(treeroot)->data);
        break;
    case 7:
        printf("Enter th value you want to delete\n");
        scanf("%d",&c);
        delet(treeroot,c);
        break;
    case 8:
        exit(1);
        }
    }
}


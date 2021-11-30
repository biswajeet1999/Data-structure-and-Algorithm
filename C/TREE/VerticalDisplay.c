#include<stdio.h>
#include<stdlib.h>

#define MAX 20

typedef struct Node
{
    int data;
    int level;
    int SpaceFromLeft;
    struct Node *l,*r;
}Node;

Node *root=NULL;

typedef struct queue{
   Node *a[MAX];
   int front,rear;
}Queue;


Queue *createQueue()
{
    Queue *temp = (Queue *)malloc(sizeof(Queue));
    temp->front = temp->rear = -1;
    return temp;
}

int isEmpty(Queue *q){
    if(q->rear==-1 && q->front == -1)
        return 1;
    return 0;
}

int isFull(Queue *q){
    if(q->front == 0 && q->rear == MAX-1)
        return 1;
    if(q->front == q->rear+1)
        return 1;
    return 0;
}

void enque(Queue *q,Node *data)
{
    if(!isFull(q)){
        if(q->front == -1 && q->rear == -1)
            q->front = q->rear = 0;
        else
            q->rear = ((q->rear) + 1)%MAX;
        q->a[q->rear] = data;
    }
}

Node *deque(Queue *q)
{
    if(q->front==-1)
        printf("Queue is empty\n");
    else{
        Node *data;
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


Node *insert(Node *root,int data)
{
    if(root == NULL){
        root = (Node *)malloc(sizeof(Node));
        root->data = data;
        root->l = root->r = NULL;
        root->level = root->SpaceFromLeft =  0;
    }
    else if(data > root->data)
        root->r = insert(root->r,data);
    else if(data < root->data)
        root->l = insert(root->l,data);
    else
        printf("Duplicate Key\n");
    return root;

}

void SetLevel(Node *root,int level)
{
    if(root == NULL)
        return;
    root->level = level;
    SetLevel(root->l,level+1);
    SetLevel(root->r,level+1);
}

int SetSpace(Node *root,int space)
{
    int temp_space;
    if(root == NULL)
        return space;
    temp_space = SetSpace(root->l,space);
    root->SpaceFromLeft = temp_space;
    temp_space= SetSpace(root->r,temp_space+5);
    return temp_space+5;
}

int check_Left_Or_Right(Node *root,int data)
{
    if(data == root->data)
        return 0;
    if(data == root->l->data)
        return -1;
    if(data == root->r->data)
        return 1;
    if(data > root->data)
        return(check_Left_Or_Right(root->r,data));
    if(data < root->data)
        return(check_Left_Or_Right(root->l,data));
}

void print(Node *temproot,int space,int prev_space,int level)
{
    int i,ch_l_r,j,k;
    if(temproot->level != level){
        printf("\n\n\n\n");
        space = temproot->SpaceFromLeft;
    }
    for(i=0;i<space;i++)
        printf(" ");
    printf("(%d)",temproot->data);
}

void PrintVerticalTree(Node *root)
{
    if(root){
        Queue *q = createQueue();
        Node *temp_root = NULL;
        int prev_level = root->level,prev_space=0;
        SetLevel(root,1);
        SetSpace(root,5);
        enque(q,root);
        while(!isEmpty(q)){
            temp_root = deque(q);
            print(temp_root, temp_root->SpaceFromLeft - prev_space,prev_space, prev_level);
            prev_space = temp_root->SpaceFromLeft;
            prev_level = temp_root->level;
            if(temp_root->l)
                enque(q,temp_root->l);
            if(temp_root->r)
                enque(q,temp_root->r);
        }
    }
}

void PrintHorizontalTree(Node *root,int space)
{
    if(root){
        int i;
        PrintHorizontalTree(root->r,space+10);
        for(i=0;i<space;i++)
            printf(" ");
        printf("(%d)\n\n\n",root->data);
        PrintHorizontalTree(root->l,space+10);
    }
}

void main()
{
   root = insert(root,50);
   root = insert(root,20);
   root = insert(root,80);
   root = insert(root,10);
   root = insert(root,30);
   root = insert(root,60);
   root = insert(root,90);
   root = insert(root,9);
  /* root = insert(root,11);
   root = insert(root,25);
   root = insert(root,35);
   root = insert(root,55);
   root = insert(root,65);
   root = insert(root,85);
   root = insert(root,95);
   root = insert(root,5);
   root = insert(root,15);
   root = insert(root,77);
   root = insert(root,4);*/
   PrintVerticalTree(root);
   printf("\n\n\n\n\n\n\n\n\n\n\n\n");
   PrintHorizontalTree(root,5);
}

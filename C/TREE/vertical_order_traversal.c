#include<stdio.h>
#include<stdlib.h>
#define MAX 10
typedef struct node
{
    int data;
    int hd;
    struct node *l,*r;
}Node;
typedef struct queue{
   Node *a[MAX];
   int front,rear;
}Queue;
typedef struct treeNode
{
    int data;
    struct treeNode *next;
}TN;
typedef struct verticalTable
{
    int data;   ///HD
    TN *down;
    struct verticalTable *next;
}VT;

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
        root->hd = 0;
    }
    else if(data > root->data)
         root->r = insert(root->r,data);
    else if(data < root->data)
         root->l = insert(root->l,data);
    return root;
}

void Hor_Dist(Node *root,int hd){  /// here hd should be always zero when fun cal initially
   if(root){
        root->hd = hd;
        Hor_Dist(root->l,hd-1);
        Hor_Dist(root->r,hd+1);
   }
}
VT *createVT(int hd)
{
    VT *table = (VT *)malloc(sizeof(VT));
    table->data = hd;
    table->down = NULL;
    table->next = NULL;
    return table;
}
TN *createTN(int data)
{
    TN *temp = (TN*)malloc(sizeof(TN));
    temp->next = NULL;
    temp->data = data;
    return temp;
}
VT *VerticalOrderTraversal(Node *root,Queue *q)
{
    if(root){
        Node *data;
        int flag;
        VT *table = NULL;
        TN *t = NULL;
        enque(q,root);
        while(!isEmpty(q)){
          int flag = 0;
          data = deque(q);
                if(table == NULL){
                    table = createVT(data->hd);
                    t = createTN(data->data);
                    t->next = table->down;
                    table->down = t;
                }
                else{
                    VT *temp = table;
                    if(data->hd == temp->data){
                        t = createTN(data->data);
                        t->next = temp->down;
                        temp->down = t;
                    }
                    else{
                        while(temp->next){
                            if(data->hd == temp->next->data){
                                t = createTN(data->data);
                                t->next = temp->next->down;
                                temp->next->down = t;
                                flag = 1;
                                break;
                            }
                            else{
                               temp=temp->next;
                            }  /// end of if
                        }  /// end of while

                        if(flag == 0){
                            temp->next = createVT(data->hd);
                            temp = temp->next;
                            temp->down = createTN(data->data);
                        }
                    }  /// end of else
                }  /// end of  outer else


          if(data->l)
            enque(q,data->l);
          if(data->r)
            enque(q,data->r);
        }
        return table;
    }
}


void print(Node *root,int space)
{
    int i;
    if(root == NULL)
        return;
    if(root->r)
        print(root->r,space+10);
    for(i=0;i<space;i++)
        printf(" ");
    printf("%3d",root->data);
    printf("\n");
    if(root->l)
        print(root->l,space+10);
}
void DisplayVerticalOrder(VT *vtr)
{
    VT *temp = vtr;
    TN *t=NULL;
    while(temp){
        printf("\n\n%5d\n",temp->data);
        printf("--------\n");
        t = temp->down;
        while(t){
            printf("%3d\n",t->data);
            t = t->next;
        }
        temp = temp->next;
    }
}
void main()
{
    Node *root=NULL;
    int HD = 0; /// HD(horizontal distance) is 0 fro root
    root = insert(root,50);
    root = insert(root,20);
    root = insert(root,80);
    root = insert(root,10);
    root = insert(root,30);
    root = insert(root,60);
    root = insert(root,90);
    Hor_Dist(root,0);
    print(root,0);
    printf("\n------------------------------------------------------------------------------------------------------------------------");
    Queue *q= createQueue();
    VT *vtr = VerticalOrderTraversal(root,q);
    DisplayVerticalOrder(vtr);
}

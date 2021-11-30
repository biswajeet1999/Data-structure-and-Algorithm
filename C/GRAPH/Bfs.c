               /* Breadth First Search*/
#include<stdio.h>
#include<stdlib.h>

typedef struct Graph
{
    int v,e;
    int **adj;
}Graph;
typedef struct vertex  ///stores vertex no and status
{
    int vertex;
    int status;
}Vertex;
typedef struct queue
{
    int capacity;
    int front,rear;
    int *a;
}Queue;
int isempty(Queue *q)
{
    if(q->front == -1 && q->rear == -1)
        return 1;
    else
        return 0;
}
Queue *creatqueue(int capacity)
{
    Queue *temp=(Queue *)malloc(sizeof(Queue));
    temp->capacity=capacity;
    temp->front=temp->rear=-1;
    temp->a=(int *)malloc(sizeof(int)*capacity);
    return temp;
}
void enqueue(Queue *q,int data)
{
    if(q->rear != (q->capacity)-1 ) /// linear queue
    {
        if(q->front ==-1 && q->rear ==-1)
            q->front = q->rear =0;
         else
            (q->rear)++;
         q->a[q->rear]=data;
    }
}
int dequeue(Queue *q)
{
    int data;
    if( q->front !=-1 && q->rear !=-1 ){
         data = q->a[q->front];
         if(q->front == q->rear)
            q->front = q->rear=-1;
         else
            (q->front)++;
    }
    return data;
}
Graph *setGraph()
{
    int u,v,i,j;
    Graph *G=(Graph *)malloc(sizeof(Graph));
    printf("Enter No of Vertex and Edges\n");
    scanf("%d %d",&G->v,&G->e);
    G->adj=(int **)malloc(G->v * sizeof(int *));
    for(i=0;i<G->v;i++)
        G->adj[i]=(int *)malloc(G->v * sizeof(int));
    for(i=0;i<G->v;i++)
        for(j=0;j<G->v;j++)
           G->adj[i][j]=0;
    for(i=0;i<G->e;i++){
        printf("Enter node pair: ");
        scanf("%d %d",&u,&v);
        G->adj[u][v]=1;
        G->adj[v][u]=1;
    }
    return G;
}
void display(Graph G)
{
    int i,j;
    for(i=0;i<G.v;i++){
        for(j=0;j<G.v;j++)
           printf("%5d",G.adj[i][j]);
        printf("\n");
    }
}
void main()
{
    int i,vertex;
    Graph *G=setGraph();
    Queue *Q=creatqueue(G->v);
    Vertex v[G->v];


    printf("************Graph*************\n");
    display(*G); /// display graph
    for(i=0;i<G->v;i++){                       ///status =1 ready state
        v[i].vertex=i;                         ///status =2 waiting for processing state
        v[i].status=1;                         ///status =3 processed state
    }
    printf("*************BFS**************\n");
    enqueue(Q,v[0].vertex);
    v[0].status=2;
    while(!isempty(Q))
    {
       vertex=dequeue(Q);   ///remove vertex from queue
       printf("%4d",vertex); /// process vertex
       v[vertex].status=3; ///update status
       for(i=0;i<G->v;i++)
       {
           if(G->adj[vertex][i]==1 && v[i].status == 1){
               enqueue(Q,i);
               v[i].status=2;
           }
       }
    }
}

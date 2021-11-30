/**
************************************
*   TopologicalSorting using QUEUE *
*   Author:- Biswajeet Padhi       *
*   Date:- 1/7/2019                *
*   B.Tech 3rd sem                 *
************************************
**/

#include<stdio.h>
#include<malloc.h>
#define MAX 20

typedef struct Edge
{
    int targetVertex;
}Edge;

typedef struct Vertex
{
    int vertexNo;
    int noOfEdges;
    int visitedStatus;  /* 1 if vertex is visited and 0 if not visited */
    Edge *edges;
}Vertex;

typedef struct Graph
{
    int noOfVertex;
    Vertex *v;
}Graph;

typedef struct Queue{
    int *array;
    int front;
    int rear;
    int count;   /* it will store the total no of data store in the queue */
}Queue;

Queue *createQ()
{
    Queue *q = (Queue *)malloc(sizeof(Queue));
    q->array = (int *)malloc(sizeof(int)*MAX);
    q->rear = q->front = -1;
    q->count = 0;
    return q;
}

void enQueue(Queue *q, int data)
{
    if(q->count == MAX){
        printf("Queue Overflow\n");
    }
    else{
        if(q->rear == -1 && q->front == -1)
            q->rear = q->front = 0;
        else
            q->rear = (q->rear+1)%MAX;
        q->array[q->rear] = data;
        q->count++;
    }
}

int deQueue(Queue *q)
{
    int data = -1;   /* initialization */
    if(q->count == 0){
        printf("Queue Underflow\n");
    }
    else{
        data = q->array[q->front];
        if(q->rear == q->front)
            q->rear = q->front = -1;
        else
            q->front++;
        q->count--;
    }
    return data;
}

Graph *createGraph()
{
    Graph *g = (Graph *)malloc(sizeof(Graph));
    printf("Enter no  of vertex: ");
    scanf("%d",&g->noOfVertex);
    g->v = (Vertex *)malloc(sizeof(Vertex)*(g->noOfVertex));
    for(int i=0; i<g->noOfVertex; i++){
        g->v[i].vertexNo = i;
        g->v[i].visitedStatus = 0;
        printf("No of edges of vertex %d ",i);
        scanf("%d",&g->v[i].noOfEdges);
        g->v[i].edges = (Edge *)malloc(sizeof(Edge)*g->v[i].noOfEdges);
        for(int j = 0;j<g->v[i].noOfEdges; j++){  /* read all edges */
            printf("Enter target node: ");
            scanf("%d",&g->v[i].edges[j].targetVertex);
        }
    }
    return g;
}

int *calculateIndegree(Graph *g)
{
    int *arr = (int *)malloc(sizeof(int)*g->noOfVertex);
    for(int i=0; i<g->noOfVertex;i++)
        arr[i] = 0;
    /* find all indegree of all vertex */
    for(int i=0;i<g->noOfVertex;i++){
        for(int j=0;j<g->v[i].noOfEdges;j++){
            arr[g->v[i].edges[j].targetVertex]++;
        }
    }
    return arr;
}

void topologicalSort(Graph *g)
{
    /* calculate indegree of all vertex */
    int *indegree = calculateIndegree(g);
    int count = 0; /* it will decide the order of vertex */
    Queue *q = createQ();
    int order[g->noOfVertex];

    /* initialize order*/
    for(int i=0; i<g->noOfVertex; i++)
        order[i] = 0;

    /* find all vertex having indegree 0 and enqueue it */
    for(int i=0;i<g->noOfVertex;i++){
        if(indegree[i] == 0)
            enQueue(q,i); /* enqueue the vertex */
    }
    /* main task */
    while(q->count != 0){
        int u = deQueue(q);
        order[u]  = count++;  /* store the order of current  vertex */
        for(int i=0; i<g->v[u].noOfEdges; i++){  /* visit all neighbor vertex of u */
            int v = g->v[u].edges[i].targetVertex;
            indegree[v]--; /* decrement its indegree value */
            if(indegree[v]==0)
                enQueue(q,v);
        }
    }

    if(count != g->noOfVertex){  /* check if it is cyclic or not */
        printf("The Graph is cyclic, so cant sort\n");
        return;
    }
    /* print all the order of all vertex */
    printf("Topological sort:\n");
    printf("%-7s:","Vertex");
    for(int i =0;i<g->noOfVertex;i++){
        printf("%3d",i);
    }
    printf("\n");
    printf("%-7s:","Order");
    for(int i =0;i<g->noOfVertex;i++){
        printf("%3d",order[i]);
    }
}

void displayGraph(Graph *g)
{
    int i,j;
    for(i=0;i<g->noOfVertex;i++){
        for(j=0; j<g->v[i].noOfEdges; j++)
            printf("%-3d---->%3d\n",i,g->v[i].edges[j]);
    }
}

main()
{
    Graph *g = createGraph();
    topologicalSort(g);
}

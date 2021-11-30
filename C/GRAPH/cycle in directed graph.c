/* This Algorithm check if there exist
 * any cycle in Directed Graph or not.
 * it is different from undirected graph algorithm.
 */

/* Author:- Biswajeet padhi
   Date:- 1/13/2019
   3rd sem
 */

#include<stdio.h>
#include<malloc.h>
#define INF 99999
#define NILL -1
#define MAX 20
#define NOT_VISITED 0
#define PROCESSING 1
#define VISITED 2

typedef struct Edge
{
    int targetVertex;
    /* int cost; */
}Edge;

typedef struct Vertex
{
    int vertexNo;
    int noOfEdges;
    Edge *edges;
}Vertex;

typedef struct Graph
{
    int noOfVertex;
    Vertex *v;
}Graph;

typedef struct stack
{
    int top;
    int *arr;
}Stack;

int Cycle_Flag = 0;

Stack *createStack()
{
    Stack *s = (Stack *)malloc(sizeof(Stack));
    s->top = -1;
    s->arr = (int *)malloc(sizeof(int)*MAX);
    return s;
}

void push(Stack *s,int data)
{
    if(s->top == MAX-1){
        printf("Stack Overflow\n");
    }
    else{
        s->arr[++s->top] = data;
    }
}

int pop(Stack *s){
    if(s->top == -1){
        printf("Stack Underflow\n");
        return -1;
    }
    else{
        s->top--;
        return s->arr[s->top+1];
    }
}

Graph *createGraph()
{
    Graph *g = (Graph *)malloc(sizeof(Graph));
    printf("Enter non Negative Cost Cyclic Graph:-\n");
    printf("Enter no  of vertex: ");
    scanf("%d",&g->noOfVertex);
    g->v = (Vertex *)malloc(sizeof(Vertex)*(g->noOfVertex));
    for(int i=0; i<g->noOfVertex; i++){
        g->v[i].vertexNo = i;
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

/* check whether the vertex already present in the array or not */
int checkVertexPresent(int *arr, int index, int u)
{
    for(int i=0;i<index;i++){
        if(arr[i] == u)
            return 1;
    }
    return 0;
}

/* it will store the current vertex in the array and process all its adjacent vertex */
void checkCycleUtil(Graph *g, int *arr, int index, int u)
{
    /* in directed graph cycle is found if while processing  neighbor(v) of parent(u),
       if parent(u) is found and all its neighbors are not visited completely */
    if(checkVertexPresent(arr, index, u) == 1){
        printf("Cycle Detected\n");
        Cycle_Flag = 1;
        return;
    }
    /* store the vertex in array and process all its neighbors */
    arr[index] = u;
    for(int i=0; i<g->v[u].noOfEdges; i++){
        checkCycleUtil(g, arr, index+1, g->v[u].edges[i].targetVertex);
        /* Cycle Detected no need to proceed further */
        if(Cycle_Flag == 1)
            return;
    }
}

void checkCycle(Graph *g)
{
    int arr[g->noOfVertex];
    int index = 0;/* it will point the top of temp */

    /* it will loop through all the vertex until cycle not found */
    //for(int i=0; i<g->noOfVertex; i++){
        checkCycleUtil(g, arr, index, 0);
        /* if cycle found no need to proceed further */
        if(Cycle_Flag == 1)
            return;
    //}
    printf("Cycle not found\n");
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
    checkCycle(g);
}

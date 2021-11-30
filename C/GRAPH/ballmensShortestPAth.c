/**
************************************
*   Ball-man ShortestPath Algorithm*
*   Author:- Biswajeet Padhi       *
*   Date:- 11/1/2019               *
*   B.Tech 3rd sem                 *
************************************
**/

// it will not work for a graph with negative cost cycle , so it is also
// used to check if negative cost cycle present in a graph or not

#include<stdio.h>
#include<malloc.h>
#define INF 99999
#define NILL -1
typedef struct Edge
{
    int targetVertex;
    int cost;
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

typedef struct VertexTable
{
    int vertex;
    int cost;
    int parent;
}VertexTable;

VertexTable *createVertexTable(int n)
{
    VertexTable *vt = (VertexTable *)malloc(sizeof(VertexTable)*n);
    for(int i = 0; i<n; i++){
        vt[i].vertex = i;
        vt[i].cost = INF;
        vt[i].parent = NILL;
    }
    return vt;
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
        g->v[i].visitedStatus = 0;
        printf("No of edges of vertex %d ",i);
        scanf("%d",&g->v[i].noOfEdges);
        g->v[i].edges = (Edge *)malloc(sizeof(Edge)*g->v[i].noOfEdges);
        for(int j = 0;j<g->v[i].noOfEdges; j++){  /* read all edges */
            printf("Enter target node: ");
            scanf("%d",&g->v[i].edges[j].targetVertex);
            printf("Enter cost: ");
            scanf("%d",&g->v[i].edges[j].cost);
        }
    }
    return g;
}

void relax(Graph *g, VertexTable *vt, int source)
{
    int u = source;
    /* visit all vertex starting from source vertex */
    for(int i=0; i<g->noOfVertex; i++){
        /* visit all edges and update parent and cost */
        for(int j=0; j<g->v[i].noOfEdges; j++){
            int v = g->v[u].edges[j].targetVertex;
            int cost = g->v[u].edges[j].cost;
            /* update cost and parent of v in vt if v is not source node because it is the starting vertex */
            if(v!=source && vt[v].cost > vt[u].cost+cost){
                vt[v].cost = vt[u].cost+cost;
                vt[v].parent = u;
            }
        }
        /* find the next source */
        /* here we start with from any source node so there may be chance of traversing in a cycle */
        u = (u+1)%g->noOfVertex;
    }
}

void BSP(Graph *g)
{
    VertexTable *vt = createVertexTable(g->noOfVertex);
    int source;
    printf("Enter Source Node: ");
    scanf("%d",&source);
    /* update starting node with no cost and no parent */
    vt[source].cost = 0;
    vt[source].parent = source;
    /* relax each edge totVertex-1 times */
    for(int i=0; i<g->noOfVertex-1; i++){
        relax(g,vt,source);
    }
    /* Display all shortest paths from source node to any other node */
    displayVertexTable(vt,g->noOfVertex);
    free(vt);
}

void displayGraph(Graph *g)
{
    int i,j;
    for(i=0;i<g->noOfVertex;i++){
        for(j=0; j<g->v[i].noOfEdges; j++)
            printf("%-3d---->%3d\n",i,g->v[i].edges[j]);
    }
}

void displayVertexTable(VertexTable *vt,int n)
{
    printf("%-8s%-6s%-8s\n","Vertex","Cost","Parent");
    for(int i=0;i<n;i++){
        printf("%-8d%-6d%-8d\n",vt[i].vertex,vt[i].cost,vt[i].parent);
    }
}

main()
{
    Graph *g = createGraph();
    BSP(g);

}

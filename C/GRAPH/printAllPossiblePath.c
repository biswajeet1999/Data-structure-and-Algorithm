#include<stdio.h>
#include<malloc.h>
#define MAXEDGES 20

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

int count; /* store no of paths */

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

void displayGraph(Graph *g)
{
    int i,j;
    for(i=0;i<g->noOfVertex;i++){
        for(j=0; j<g->v[i].noOfEdges; j++)
            printf("%-3d---->%3d\n",i,g->v[i].edges[j]);
    }
}

void findPath(Graph *g,int source, int target, int *path, int currentIndex)
{
    int i,j;
    /* terminating condition */
    if(g->v[source].visitedStatus == 1) /* already visited */
        return ;

    path[currentIndex] = source;
    g->v[source].visitedStatus = 1; /* make it visited */

    /* target node found */
    if(source == target){
        count++;
        for(j=0; j< currentIndex; j++){
            printf("%d --->",path[j]);
        }
        printf("%-3d\n",path[j]);
    }
    else{
        for(i=0; i<g->v[source].noOfEdges; i++){
            findPath(g, g->v[source].edges[i].targetVertex, target, path, currentIndex+1);
        }
    }
    g->v[source].visitedStatus = 0;
}

main()
{
    Graph *g = createGraph();
    int source,target;
    int *path = (int *)malloc(sizeof(int)*MAXEDGES);
    printf("Enter source and target node");
    scanf("%d %d",&source, &target);

    printf("Paths:\n");
    findPath(g, source, target, path, 0); /* 1 = starting index of path */
    printf("\ntotal path found: %d",count);
}

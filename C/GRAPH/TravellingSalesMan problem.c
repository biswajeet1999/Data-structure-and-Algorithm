/* Traveling Sales Man Problem
 * Author:- Biswajeet padhi
 * Date:- 2/14/2019
 * 4th sem
 */

#include<stdio.h>
#include<stdlib.h>
#define INF 9999
typedef struct Graph
{
    int v;
    /* int e; */
    int **g;
}Graph;

Graph *createGraph()
{
    Graph *g = (Graph *)malloc(sizeof(Graph));
    printf("Enter no of vertex: ");
    scanf("%d",&g->v);
    g->g = (int **)malloc(g->v*sizeof(int *));
    for(int i=0;i<g->v;i++){
        g->g[i] = (int *)malloc(g->v*sizeof(int));
    }
    /* initialize diagonal vertex to 0 */
    for(int i=0;i<g->v;i++)
        g->g[i][i] = 0;

    /* insert cost to the graph */
    for(int i=0;i<g->v;i++){
        for(int j=0;j<g->v;j++){
            if(i==j)
                continue;
            printf("Enter cost for vertex[%d]--->vertex[%d]: ",i,j);
            scanf("%d",&g->g[i][j]);
        }
    }
    return g;
}

void Display(Graph *g)
{
    printf("\nGraph:\n");
    for(int i=0;i<g->v;i++){
        for(int j=0;j<g->v;j++){
            printf("%3d",g->g[i][j]);
        }
        printf("\n");
    }
}

int allVisited(int *visited, int n)
{
    for(int i=0;i<n;i++)
        if(visited[i] == 0)
            return 0;
    return 1;
}

int TSP(Graph *g, int *visited, int pos)
{
    int min = INF;
    visited[pos] = 1;   /* make it visited */
    /* Base case */
    if(allVisited(visited,g->v)){
        visited[pos] = 0;
        return g->g[pos][0];
    }
    for(int i=0;i<g->v;i++){
        if(visited[i] == 0){
            int cost = g->g[pos][i]+TSP(g, visited, i);
            if(cost < min){
                min = cost;
            }
        }
    }
    visited[pos] = 0; /* finally make it unvisited */
    return min;
}
int main()
{
    Graph *g = createGraph();
    int visited[g->v];   /* it will store 1 if that vertex is visited else 0 */
    /* initially make all vertex as unvisited */
    for(int i=0;i<g->v;i++)
        visited[i] = 0;
    Display(g);
    printf("\nMin cost: %d",TSP(g, visited, 0));
    return 0;
}

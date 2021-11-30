#include<stdio.h>
#include<stdlib.h>
#define inf 9999

typedef struct Graph
{
    int v,e;
    int **Adj;
}Graph;

Graph *createGraph()
{
    int i,j,u,v,cost;
    Graph *G=(Graph *)malloc(sizeof(Graph));
    printf("Enter no of vertex and edges\n");
    scanf("%d %d",&G->v,&G->e);
    G->Adj=(int **)malloc((G->v)*sizeof(int *));
    for(i=0;i<(G->v);i++)
        G->Adj[i]=(int *)malloc((G->v)*sizeof(int));
    for(i=0;i<(G->v);i++){    /// initialize all elements with infinite
        for(j=0;j<(G->v);j++){
            G->Adj[i][j]=inf;
        }
    }
    for(i=0;i<(G->e);i++){
            printf("Enter nodes(start,end) for a direct edge: "); /// it will store the cost for a direct connecting edge between 2 points
            scanf("%d %d",&u,&v);
            printf("Enter cost: ");
            scanf("%d",&cost);
            G->Adj[u][v]=cost;
    }
    for(i=0;i<(G->v);i++)   /// initialize diagonal elements to 0 because the starting and ending points are same so cost is 0
        for(j=0;j<(G->v);j++)
            if(i==j)
               G->Adj[i][j]=0;
    return G;
}
void displaygraph(Graph G)
{
    int i,j;
    for(i=0;i<G.v;i++){
        for(j=0;j<G.v;j++){
            if(G.Adj[i][j]==inf)
                printf("%7s","INF");
            else
                printf("%7d",G.Adj[i][j]);
         }
         printf("\n");
    }
}
void floydwarshal(Graph *G)
{
    int i,j,k;  /// k at as the middle point i is the starting point and j is the end point
    for(k=0;k<(G->v);k++){
        for(i=0;i<(G->v);i++){
            for(j=0;j<(G->v);j++){
                if(G->Adj[i][k]+G->Adj[k][j] < G->Adj[i][j])  /// if cost of((start to mid)+(mid to end)) < cost of(start to mid point)
                    G->Adj[i][j]=G->Adj[i][k]+G->Adj[k][j];
            } /// end of j loop                               /// then change the cost value
        }/// end of i loop
    }  /// end of k loop
    return G;
}
int main()
{
    Graph *G=createGraph();
    displaygraph(*G);
    floydwarshal(G);
    printf("*************SORTEST PATH***************\n");
    displaygraph(*G);
    return 0;
}

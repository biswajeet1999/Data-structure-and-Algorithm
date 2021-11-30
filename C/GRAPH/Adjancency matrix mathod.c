#include<stdio.h>
#include<stdlib.h>
typedef struct Graph
{
    int V,E;
    int **Adj;
}Graph;
Graph *setgraph()
{
    int u,v,i;
    Graph *temp=(Graph *)malloc(sizeof(Graph));
    printf("Enter no of vertices and edges\n");
    scanf("%d %d",&temp->V,&temp->E);
    temp->Adj=(int **)malloc((temp->V)*sizeof(int *));   //  dynamically i created 2d array
    for(i=0;i<temp->V;i++)
        temp->Adj[i]=(int *)malloc((temp->V)*sizeof(int));
    for(u=0;u<temp->V;u++)     /// initialize all elements to zero
        for(v=0;v<temp->V;v++)
             temp->Adj[u][v]=0;

    for(i=0;i<(temp->E);i++){
        printf("Enter vertices pair connected by edges\n");
        scanf("%d %d",&u,&v);
        temp->Adj[u][v]=1;
        temp->Adj[v][u]=1;
    }
    return temp;
}
void displaygraph(Graph G)
{
    int i,j;
    printf("No of vertices=%d\nNo of edges=%d\n",G.V,G.E);
    printf("Adjacency Matrix is: \n");
    for(i=0;i<G.V;i++){
        for(j=0;j<G.V;j++)
            printf("%d  ",G.Adj[i][j]);
        printf("\n");
    }

}
void main()
{
    Graph *G=setgraph();
    displaygraph(*G);
}

#include<stdio.h>
#include<stdlib.h>
#define inf 9999999
#define null -1
typedef struct Graph
{
    int v,e;
    int **adj;
}Graph;
typedef struct table   /// it store key parent table
{
    int vertex;
    int key;
    int parent;
    int status;       /// it will store whether the vertex removed or not, if 1 not removed , if 0 removed
}Table;

Graph *createGraph()
{
    int u,v,i,j,cost;
    Graph *G=(Graph *)malloc(sizeof(Graph));
    printf("enter no of vertex and no of edges\n");
    scanf("%d %d",&G->v,&G->e);
    G->adj=(int **)malloc(sizeof(int *)*(G->v));
    for(i=0;i<G->v;i++)
        G->adj[i]=(int *)malloc(sizeof(int)*(G->v));
    for(i=0;i<G->v;i++)
        for(j=0;j<G->v;j++)
            G->adj[i][j]=0;
    for(i=0;i<G->e;i++){
        printf("Enter start and end vertex pair of edge: ");
        scanf("%d %d",&u,&v);
        printf("Enter cost: ");
        scanf("%d",&cost);
        G->adj[u][v]=cost;
    }
    return G;
}
int isEmpty(Table *t,int n){    /// check whether table is empty or not
    int i;
    for(i=0;i<n;i++){
        if(t[i].status == 1){
            return 0;   /// table is not empty
        }
    }
   return 1;
}
int find_min_index(Table *t,int n){
    int i,minIndex;
    for(i=0;i<n;i++){
        if(t[i].status == 1){
            minIndex = i;
            break;
        }
    }
    for(i=0;i<n;i++){
        if(t[minIndex].key > t[i].key && t[i].status == 1)
            minIndex = i;
    }
  return minIndex;
}
void Prim_mst(Graph G,Table *t)
{
    int i,j,minIndex,neighbour,u,v,cost;
    while(!isEmpty(t,G.v)){
        neighbour = 0;
        u = find_min_index(t,G.v);                         /// the min index vertex should be removed from table and neighbors should be find
        for(i=0;i<G.v;i++){                                /// it will find no. of neighbor of minIndex vertex
            if(G.adj[u][i] >0)
                neighbour++;
        }
        for(i=0;i<neighbour;i++){                          /// the loop continues no of times equal to no of neighbor
                for(j=0;j<G.v;j++){                        /// this loop find the neighbor of min index(or u)
                    if(G.adj[u][j] > 0){
                        v = j;
                        cost = G.adj[u][v];
                        G.adj[u][v] = 0;                   /// make that cost is zero, otherwise the program will find find that node only
                        break;
                    }
                }
                if(t[v].key > cost && t[v].status == 1){   /// it is the condition if the neighbor should be exist in the table
                    t[v].key = cost;
                    t[v].parent = u;
                }
        }
        t[u].status = 0;                                   /// finally remove the u(min index vertex) by making its status 0
    }
}
void main()
{
    int i;
    Graph *G=createGraph();
    Table T[G->v];                       /// it store the key parent pair of all vertex
    for(i=0;i<G->v;i++){
        T[i].vertex=i;                   /// initialize vertex field with vertex no
        T[i].key=inf;                    /// initially there no path between the vertex and tree so key(or cost) is infinite
        T[i].parent=null;                /// initially there is no parent of any vertex
        T[i].status = 1;                 /// initially all nodes are present in the table
    }
    T[0].key = 0;    /// make first vertex as root Node of MST
    Prim_mst(*G,T);
    printf(" Vertex         Key         Parent\n");
    printf("-----------------------------------\n");
    printf("%5d          %5d          %5s",T[0].vertex,T[0].key,"NILL");
    printf("\n");
    for(i=1;i<G->v;i++){
        printf("%5d          %5d          %5d",T[i].vertex,T[i].key,T[i].parent);
        printf("\n");
}
}

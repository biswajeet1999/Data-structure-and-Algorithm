#include<stdio.h>
#include<stdlib.h>
typedef struct List
{
    int vertexNo;
    struct List *next;
}List;
typedef struct Graph
{
    int v,e;
    List *Adj;
}Graph;

Graph *setgraph()
{
    int i,u,v;
    List *t,*temp=NULL;
    Graph *G=(Graph *)malloc(sizeof(Graph));
    printf("Enter no of vertex and edges\n");
    scanf("%d %d",&G->v,&G->e);
    G->Adj=NULL;
    G->Adj=(List *)malloc((G->v)*sizeof(List));
    for(i=0;i<G->v;i++){     // initialize all the vertex no of list to 0 and all next pointer points to it self
        ((G->Adj)+i)->vertexNo=i;
        ((G->Adj)+i)->next=((G->Adj)+i);
    }
    for(i=0;i<G->e;i++){
         printf("Enter two vertex of edge\n");
         scanf("%d %d",&u,&v);
         temp=(List *)malloc(sizeof(List));
         temp->vertexNo=v; temp->next=NULL;
         t=((G->Adj)+u);
         while(t->next != ((G->Adj)+u))
            t=t->next;
         temp->next=t->next;
         t->next=temp;
    }
    return G;
}
void displaygraph(Graph G)
{
    int i;
    List *temp=NULL;
    printf("\n");
    printf("No of Vertex=%d\nNo of Edges=%d\n",G.v,G.e);
    for(i=0;i<G.v;i++){
        temp=(G.Adj+i);
        if(temp->next==temp)   // the list node has no extra node i.e it points to it self so no need to display
            break;
        else{
            printf("Connected vertex are\n");
            while(temp->next != (G.Adj+i)){
                printf("%d  ",temp->vertexNo);
                temp=temp->next;
            }
            printf("%d ",temp->vertexNo);
            printf("\n");
        }
    }
}
int main()
{
    Graph *G=setgraph();
    displaygraph(*G);
    return 0;
}

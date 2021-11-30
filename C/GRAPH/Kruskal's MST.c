#include<stdio.h>
#include<stdlib.h>
#define inf 99999
typedef struct Graph
{
    int v,e;
    int **adj;
}Graph;
typedef struct node
{
    int vertex;
    struct node *next;
}Node;
Graph *createGraph()
{
    int u,v,i,cost;
    Graph *G=(Graph *)malloc(sizeof(Graph));
    printf("Enter no of vertex and edges\n");
    scanf("%d %d",&G->v,&G->e);
    G->adj=(int **)malloc(sizeof(int *)*G->v);
    for(i=0;i<G->v;i++)
        G->adj[i]=(int *)malloc(sizeof(int)*G->v);
    for(u=0;u<G->v;u++)
        for(v=0;v<G->v;v++)
            if(u==v)
                G->adj[u][v]=0;
            else
                G->adj[u][v]=inf;
    for(i=0;i<G->e;i++)
    {
         printf("Enter start and end node pair: ");
         scanf("%d %d",&u,&v);
         printf("enter cost: ");
         scanf("%d",&cost);
         G->adj[u][v]=cost;
    }
    return G;
}
int *createCostSet(Graph G)
{
    int *array=(int *)malloc(sizeof(int)*G.e);
    int i,j,k=0,temp;
    for(i=0;i<G.v;i++){
        for(j=0;j<G.v;j++){
            if(G.adj[i][j] != 0 && G.adj[i][j] != inf){
                array[k]=G.adj[i][j];
                k++;
            }
        }
    }
    for(i=1;i<G.e;i++){     /// insertion sort
        for(j=i;j>0;j--){
            if(array[j]<array[j-1]){
                temp=array[j];
                array[j]=array[j-1];
                array[j-1]=temp;
            }
        }
    }
    return array;
}
int checkInLine(Graph G,Node **ver,int u,int v)
{
    int i,flag1,flag2; /// if any one node is found then it flag 1 be 1 and another node is found then flag 2 will be 1
    Node *temp,*temp1;
    for(i=0;i<G.v;i++){    /// if 2 vertex are in same row(or set) then flag1=flag2=1
        flag1=0,flag2=0;
        temp=temp1=NULL;
        if(ver[i]==NULL);  /// if the pointer in the array is null then no need of traversing
        else{
            temp=ver[i];
            while(temp!=NULL){ /// it will traverse in the set and check the existence of vertex
                if(temp->vertex==u){ /// u is found
                    flag1=1;
                    temp1=ver[i];  /// it will search for another vertex in the same set
                    while(temp1!=NULL){
                        if(temp1->vertex==v){ /// v is found
                            flag2=1;
                            return 1;  /// both the nodes are successfully found here it returs 1
                        } /// end of if condition
                    temp1=temp1->next;
                    }/// end of inner while loop
                }/// end of outer if condition
                if(flag1==1)
                    break;
                else
                    temp=temp->next;
            }///end of outer while loop
        }///end of if condition
    }
    return 0;
}
void Kruskal(Graph G,int *New,Node **ver,int *E) /// ver contains the individual vertex set
{
    int i,j,k,u,v,l,flag,q=0,flag0=0;    /// if node will be inserted then flag will be 1,  q is used as index for new array
    Node *t1,*t2,*t3;
    for(k=0;k<G.e;k++){  /// it traverse all the old cost
        flag=0;  /// it decide wheathet 2 vertex ar in line or not and whether we should insert node to new node set or not
        flag0=0;  /// it find the u,v from below 3 lines
        for(i=0;i<G.v;i++){
            for(j=0;j<G.v;j++){
                if(G.adj[i][j]==E[k]){   /// find the start and end node of the edge
                    u=i; v=j;
                    G.adj[i][j]=0; /// if two edge have same cost then 2nd edge will not evaluated if we don't make it zero
                    flag0=1;
                    break;
                }
                if(flag0==1)
                    break;
            }/// end j loop
             if(flag0==1)
                    break;
        }/// end i loop
                                    ///flag 1 means already 2 vertex are in line(means in one set)
        flag=checkInLine(G,ver,u,v);/// if two nodes are in line then it will return 1,so flag will be 1


        if(flag==0){
            int flag1=0;
            for(l=0;l<G.v;l++){  /// it will search for one node
                flag1=0;
                t1=t2=ver[l];
                while(t2!=NULL){
                    if(t2->vertex==u){
                        flag1=1;
                        ver[l]=NULL;      /// now t1 have the complete list have node u
                        break;
                    }
                    else
                        t2=t2->next;
                }
                if(flag1==1)
                    break;
            }
            for(l=0;l<G.v;l++){  /// similar to above concept
                flag1=0;
                t2=ver[l];
                while(t2!=NULL){
                    if(t2->vertex==v){
                        flag1=1;   /// here we don't make ver[l]=NULL because if we do so then both the link will detach from the array
                        break;
                    }
                    else
                        t2=t2->next;
                }
                if(flag1==1)
                    break;
            }
            while(t2->next!=NULL)      /// here we traverse upto last node of the list then attach the list hold by t1;
                t2=t2->next;
            t2->next = t1;
            flag=2;
        }



     if(flag==2){ /// if flag ==2 insert old cost to the new cost array
        New[q]=E[k];
        q++;
     }
    }/// end k loop
}void displayMST(int *New)
{
    int i=0;
    while(New[i]!=0){
        printf("%d  ",New[i]);
        i++;
    }
}
int main()
{
    int i;
    Graph *G=createGraph();
    int NewCostSet[G->e]; /// it stores the final minimum cost set or new cost set
    int *costSet=createCostSet(*G); /// it returns increasing ordered cost set
    Node **ver=(Node **)malloc(sizeof(Node *) * (G->v));
    for(i=0;i<G->v;i++){     /// create array of node pointers to point vertex
        ver[i]=(Node *)malloc(sizeof(Node));
        ver[i]->vertex=i;
        ver[i]->next=NULL;
    }
    for(i=0;i<G->e;i++)
        NewCostSet[i]=0; /// initialize all elements to zero
    Kruskal(*G,NewCostSet,ver,costSet);
    displayMST(NewCostSet);
    return 0;
}


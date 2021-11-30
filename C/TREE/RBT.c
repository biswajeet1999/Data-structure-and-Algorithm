#include<stdio.h>
#include<stdlib.h>
typedef struct Node
{
    struct Node *l;
    int data;
    int col;   /// 1 for red , 0 for black
    struct Node *r;
}Node;

Node *root = NULL;

int flag = 0;   /// it will used while deleting to check if case 5 will be applied or not after case 3

Node *createNode(int data)
{
    Node *temp = (Node *)malloc(sizeof(Node));
    temp->data = data;
    temp->l = temp->r =NULL;
    temp->col = 1;     /// always root node is red
    return temp;
}
void IsRootBlack()
{
    if(root)
        if(root->col == 1)
            root->col = 0;
}
Node *case1(Node *root)  /// rr or ll case of uncle is black, parent and sibling is red and child is red
{
    root->col = 1;
    root->r->col = 0;
    root->l->col = 0;
    return root;
}
Node *case2(Node *root)    /// it is the rl condition and sibling is black or NULL
{
    Node *y=NULL,*x=NULL;
    y = root->r;
    x = y->l;
    y->l = x->r;
    x->r = y;
    root->r = x;
    return root;
}
Node *case3(Node *root)      /// similar to case 1 but sibling is either black or NULL
{
    root->col = 1;
    root->r->col = 0;
    Node *y;
    y = root->r;
    root->r = y->l;
    y->l = root;
    return y;
}
Node *case4(Node *root)    /// mirror case of case 2
{
    Node *y,*x;
    y = root->l;
    x = y->r;
    y->r = x->l;
    x->l = y;
    root->l = x;
    return root;
}
Node *case5(Node *root)   /// mirror case of case 3
{
    root->col = 1;
    root->l->col = 0;
    Node *y = root->l;
    root->l = y->r;
    y->r = root;
    return y;
}
Node *insert(Node *root,int data)
{
    if(root == NULL){
        Node *temp = createNode(data);
        root = temp;
        root->col = 0;
    }
    else if(data > root->data && root->r == NULL)
        root->r = createNode(data);
    else if(data < root->data && root->l == NULL)
        root->l = createNode(data);
    else if(data > root->data){
        root->r = insert(root->r,data);
        if(data > root->r->data && root->r->col == 1 && (root->l == NULL || root->l->col == 0 ) && root->r->r->col == 1)
           root = case3(root);
        else if(data > root->r->data && root->l->col == 1 && root->r->col == 1 && root->r->r->col == 1)
            root = case1(root);
        else if(data < root->r->data && root->r->col == 1 && (root->l->col == 0 || root->l == NULL) && root->r->l->col == 1){
           root = case2(root);
           root = case3(root);
        }
    }
    else if(data < root->data){
        root->l = insert(root->l,data);
        if(data < root->l->data && root->l->col == 1 && (root->r == NULL || root->r->col == 0) && root->l->l->col == 1)
            root = case5(root);
        else if(data > root->l->data && root->l->col == 1 && (root->r == NULL || root->r->col == 0 ) && root->l->r->col == 1){
            root = case4(root);
            root = case5(root);
        }
        else if(data < root->l->data && root->l->col==1 && root->r->col==1 && root->l->l->col == 1)
            root = case1(root);
    }
    else
        printf("Duplicate Key\n");
    return root;
}
void insertNode(int data)  /// after insertion a node at last it will check if root is black or not
{
    root = insert(root,data);
    IsRootBlack();
}
int findmax(Node *root)
{
    if(root->r){
        return(findmax(root->r));
    }
    return(root->data);
}

Node *deletecase4(Node *root,int data){
    if(data == root->l->data){
        Node *temp=NULL;
        if(root->l->l!= NULL)
            temp = root->l->r;
        else
            temp = root->r->r;
        free(root->l);
        root->l = temp;
        root->col = 0;
        root->r->col =1;
    }
    else if(data == root->r->data){
        Node *temp=NULL;
        if(root->r->l!= NULL)
            temp = root->r->r;
        else
            temp = root->r->r;
        free(root->r);
        root->r = temp;
        root->col = 0;
        root->l->col = 1;
    }
    return root;
}
Node *deletecase6(Node *root){
     Node *temp=NULL;
        if(root->l->l!= NULL)
            temp = root->l->r;
        else
            temp = root->l->l;
    free(root->l); root->l = temp;
    Node *z = root;
    Node *y = root->r;
    Node *x = y->r;
    z->r = y->l;
    y->l = z;
    y->col = z->col;
    z->col = 0;
    y->r->col = 0;
    return y;
}
Node *deletecase6_mirror(Node *root){
    Node *temp=NULL;
        if(root->r->l!= NULL)
            temp = root->r->r;
        else
            temp = root->r->r;
    free(root->r); root->r = temp;
    Node *z = root;
    Node *y = root->l;
    Node *x = y->l;
    z->l = y->r;
    y->col = z->col;
    z->col = 0;
    y->r = z;
    y->l->col = 0;
    return y;
}
Node *deletecase5(Node *root)
{
    Node *y = root->r;
    Node *x = y->l;
    y->col = 1; x->col = 0;
    y->l = x->r;
    x->r = y;
    root->r = x;
    root = deletecase6(root);
    return root;
}
Node *deletecase5_mirror(Node *root){
    Node *y = root-> l;
    Node *x = y->r;
    y->col = 1; x->col =0;
    y->r = x->l;
    x->l = y;
    root->l = x;
    root = deletecase6_mirror(root);
    return root;
}
Node *deletecase2(Node *root)
{
    Node *temp=NULL;
    if(root->l->l!= NULL)
        temp = root->l->r;
    else
        temp = root->r->r;
    Node *y = root;
    Node *x = root->r;
    y->col = 1;
    x->col = 0;
    y->r = x->l;
    x->l = y;
    free(x->l->l);
    x->l->l = temp;
    x->l->col = 0;
    x->l->r->col = 1;
    return x;
}
Node *deletecase2_mirror(Node *root){
    Node *temp=NULL;
        if(root->r->l!= NULL)
            temp = root->r->r;
        else
            temp = root->r->r;
    Node *y = root;
    Node *x = y->l;
    y->col = 1;
    x->col = 0;
    y->l = x->r;
    x->r = y;
    free(y->r->r);
    y->r->r = temp;
    x->r->col = 0;
    x->r->l->col = 1;
    return x;
}
Node *deletecase3(Node *temproot){
    Node *temp = NULL;
    if(temproot->l->l!= NULL)
        temp = temproot->l->l;
    else
        temp = temproot->l->r;
    free(temproot->l);
    temproot->l = temp;
    temproot->r->col = 1;
    if(root == temproot){      /// root is the global root
         flag = 0;
        return temproot;
    }
    else{
        flag = 1;
        return temproot;
    }
}
Node *deletecase3_mirror(Node *temproot)
{
    Node *temp=NULL;
    if(temproot->r->l!= NULL)
        temp = temproot->r->l;
    else
        temp = temproot->r->r;
    free(temproot->l);
    temproot->r = temp;
    temproot->l->col = 1;
    if(root == temproot)
        flag = 0;
    else
        flag =1;
    return temproot;
}
Node *additionalcase1(Node *root){
            if(root->r->col == 1 && root->r->l!=NULL && root->r->r!=NULL && root->r->l->col==0 && root->r->r->col==1){
                root->col = 1; root->r->col=0;
                Node *y = root,*x = root->r;
                y->r = x->l;
                x->l = y;
                root = x;
                root->l->col = 0; root->l->r->col =1;
            }
            else if(root->col ==1 && root->r!=NULL && root->r->col == 0 &&(root->r->r != NULL || root->r->r->col==0)){
                root->col = 0; root->r->col =1;
             }
            else if(root->col==0 && root->r->col == 0 && root->r->l!=NULL && root->r->l->col==1){
                Node *y = root,*x = root->r,*z = x->l;
                x->col = 1; x->l->col = 0;
                x->l = z->r;   z->r = x;   root->r = z;
                y = root; x = y->r;
                x->col = y->col;  y->col = 0;  x->r->col = 0;
                y->r = x->l; x->l = y;
                root = x;
            }else if(root->r->col ==0 && root->r->r!=NULL && root->r->r->col==1){
                Node *y = root,*x = y->r;
                x->col = y->col;  y->col = 0;  x->r->col = 0;
                y->r = x->l; x->l = y;
                root = x;
            }
     flag = 0;
    return root;
}
Node *additionalcase2(Node *root){
    if(root->l->col == 1 && root->l->l!=NULL && root->l->r!=NULL && root->l->l->col==0 && root->l->r->col==1){
                root->col = 1; root->l->col=0;
                Node *y = root,*x = root->l;
                y->l = x->r;
                x->r = y;
                root = x;
                root->r->col = 0; root->r->l->col =1;
            }
            else if(root->col ==1 && root->l!=NULL && root->l->col == 0 &&(root->l->l != NULL || root->l->r->col==0)){
                root->col = 0; root->l->col =1;
            }
            else if(root->col==0 && root->l->col == 0 && root->l->r!=NULL && root->l->r->col==1){
                Node *y = root,*x = root->l,*z = x->r;
                x->col = 1; x->r->col = 0;
                x->r = z->l;y->l = z;z->l=x;
                y = root,x = y->l;
                x->col = y->col;  y->col = 0;  x->l->col = 0;
                y->l = x->r; x->r = y;
                root = x;
            }else if(root->r->col ==0 && root->r->r!=NULL && root->r->r->col==1){
                Node *y = root,*x = y->l;
                x->col = y->col;  y->col = 0;  x->l->col = 0;
                y->l = x->r; x->r = y;
                root = x;
            }
     flag = 0;
    return root;
}
int getrootdata(){
   return root->data;
}
/// while deleting a node its parent is passed to delete function except root node
Node *delete(Node *root,int data)
{
    if(root== NULL){
        printf("data not found\n");
    }
   else if(data == getrootdata()){      /// it is possible only when data is present in root
        if(root->l == NULL && root->r == NULL)   /// no child
            free(root);
        else if(root->r != NULL && root->l != NULL){  /// 2 child
            int max = findmax(root->l);
            root->data = max;
            root = delete(root,max);
        }
        else{
            if(root->r == NULL){
                root->data = root->l->data;
                free(root->l);  root->l= NULL;
            }else{
                root->data = root->r->data;
                free(root->r); root->r = NULL;
            }
        }
    }
    else if(root->l != NULL && root->l->data == data){   /// data found in left side

        if(root->l->l != NULL && root->l->r != NULL){   /// -------------------------------- have two children
            int max = findmax(root->l->l);
            root->l->data = max;
            if(max ==root->l->l->data ){    ///if max node is leaf node
                if(root->l->l->col == 1){   /// if color is red
                    free(root->l->l);
                    root->l->l = NULL;
                }
                else            /// if color is black
                    root->l = delete(root->l,max);
            }
            else
                root->l->l = delete(root->l->l,max);
        }  /// end of two child condition

        else if(root->l->col == 1){  /// ------------------------------------------------- deleting red node
            if(root->l->r == NULL){   /// if right child is null
                free(root->l);
                root->l = NULL;
            }
            else{      /// if left child is null
                free(root->l);
                root->l = NULL;
            }
        } /// end of deleting red node

        else if(root->l->col == 0){    /// ---------------------------------------------------- deleting all types of black node
            if(root->l->l != NULL && root->l->l->col ==1){ /// if it has red child in left side
                Node *temp = root->l->l;
                free(root->l);
                root->l = temp;
                root->l->col = 0;
            }
            else if(root->l->r != NULL && root->l->r->col == 1){   /// if it has red child in right side
                Node *temp = root->l->r;
                free(root->l);
                root->l = temp;
                root->l->col = 0;
            }
            else if(root->col == 1&&root->r!=NULL&&root->l!=NULL&&root->r->col==0&&root->l->col==0&&((root->r->l==NULL&&root->r->r==NULL)||(root->r->l->col==0&&root->r->r->col==0))&&((root->l->l==NULL&&root->l->r==NULL)||(root->l->l->col==0&&root->l->r->col==0)))
                root = deletecase4(root,data);                                         /// ------------------- case 4
            else if(root->r->col == 0 &&root->r->r!=NULL&& root->r->r->col == 1)       /// ------------------ case 6
                root = deletecase6(root);
            else if(data == root->l->data && root->r->col ==0 && root->r->l!=NULL && root->r->l->col == 1) /// ------------------ case 5
                root = deletecase5(root);
            else if(root->r->col ==0 && root->col ==0)                  /// ----------------------------------------------------- case 3
                root = deletecase3(root);
            else if(root->col =0 && root->r->col == 1 && root->r->l->col == 0 && root->r->r->col ==0) /// ----------------------- case 2
                root = deletecase2(root);
        }
    }
    else if(root->r != NULL && root->r->data == data){   /// data found in right side

        if(root->r->r != NULL && root->r->l != NULL){    /// have two children
            int max = findmax(root->r->l);
            root->r->data = max;
            if(max == root->r->l->data){
                if(root->r->l->col == 1){    ///if max color is red
                    free(root->r->l);
                    root->r->l = NULL;
                }
                else                /// if color is black
                    root->r = delete(root->r,max);
            }
            else
                root->r->l = delete(root->r->l,max);
        }  /// end of two children condition

        else if(root->r->col == 1){  /// -------------------------------------- deleting red node
            if(root->r->l == NULL){
                Node *temp = root->r->r;
                free(root->r);
                root->r = temp;
            }
            else{
                Node *temp = root->r->l;
                free(root->r);
                root->r = temp;
            }
        } /// end of deleting red node
        else if(root->r->col == 0){    /// ---------------------------------------------------- deleting all types of black node
            if(root->r->l != NULL && root->r->l->col ==1){ /// if it has red child in left side
                Node *temp = root->r->l;
                free(root->r);
                root->r = temp;
                root->r->col = 0;
            }
            else if(root->r->r != NULL && root->r->r->col == 1){   /// if it has red child in right side
                Node *temp = root->r->r;
                free(root->r);
                root->r = temp;
                root->r->col = 0;
            }
            else if(root->col == 1&&root->l!=NULL&&root->l->col==0&&((root->l->l==NULL&&root->l->r==NULL)||(root->l->l->col==0&&root->l->r->col==0)))
                root = deletecase4(root,data);          /// --------------------------------- case 4
            else if(data == root->r->data &&root->l->col == 0 && root->l->l!=NULL && root->l->l->col == 1) /// ------------ mirror of case 6
                root = deletecase6_mirror(root);
            else if(data == root->r->data && root->l->col == 0 && root->l->r!=NULL && root->l->r->col == 1) /// --------- mirror of case 5
                root = deletecase5_mirror(root);
            else if(root->l->col ==1 && root->col ==0 && root->l->l->col ==0 && root->l->r->col ==0)
                root = deletecase2_mirror(root);
            else if(root->r->col ==0 && root->col ==0)                  /// ----------------------------------------------------- case 3
                root = deletecase3_mirror(root);
        }

    }
    else if(data > root->data){
        root->r = delete(root->r,data);
        if(flag == 1){
          if(data < root->data)
             root = additionalcase1(root);
          else
              root = additionalcase2(root); /// mirror of additional case 1
          flag = 0;
        }
    }
    else if(data < root->data){
        root->l = delete(root->l,data);
        if(flag == 1){
          if(data < root->data)
             root = additionalcase1(root);
          else
              root = additionalcase2(root); /// mirror of additional case 1
          flag = 0;
        }
    }
    return root;
}

void preorder(Node *root)
{
    if(root){
        printf("(%d,",root->data);
        (root->col)?printf("RED) "):printf("BLACK) ");
        preorder(root->l);
        preorder(root->r);
    }
}
void main()
{
    insertNode(1);
    insertNode(2);
    insertNode(3);
    insertNode(4);
    insertNode(5);
    insertNode(6);
    insertNode(7);
    insertNode(8);
    insertNode(9);
    preorder(root);
   // root = delete(root,2);
    printf("\nAfter delete: \n");
    preorder(root);
}

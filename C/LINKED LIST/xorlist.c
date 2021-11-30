#include<stdio.h>
#include<stdlib.h>
#include<inttypes.h>

typedef struct node
{
    int data;
    struct node *diff;
}Node;

Node *createNode(int data)
{
    Node *node = (Node *)malloc(sizeof(Node));
    node->data = data;
    node->diff = NULL;
    return node;
}
Node *XOR(Node *a, Node *b)
{
    return((Node *)((uintptr_t)a^(uintptr_t)b));
}
/* insert at the beginning of the list */
Node *insert(Node *head, int data)
{
    Node *temp = createNode(data);
    /* List Empty */
    if(head == NULL){
        head = temp;
    }
    /* insert at first */
    else{
        head->diff = XOR(NULL, head->diff); /* 2 line update current head Node */
        head->diff = XOR(temp, head->diff);
        temp->diff = XOR(NULL, head);    /* insert new node at the beginning */
        head = temp;
     }
    return head;
}

void display(Node *head)
{
    Node *prev=NULL;
    Node *current = head;
    Node *next = XOR(prev,current->diff);
    while(current != NULL){
        printf("%-3d",current->data);
        prev = current;
        current = next;
        if(current != NULL)
            next = XOR(prev,current->diff);
    }

}
int main()
{
    Node *head = NULL;
    head = insert(head, 5);
    head = insert(head, 10);
    head = insert(head, 30);
    head = insert(head, 40);
    display(head);
}

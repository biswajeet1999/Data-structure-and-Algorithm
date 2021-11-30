#include <stdio.h>
#include <stdlib.h>

typedef struct Node {
    struct Node *prev;
    int data;
    struct Node *next;
} Node;

typedef struct LinkedList {
    Node *head;
    Node *tail;
} LinkedList;

Node *createNode(int data) {
    Node *n = (Node *)malloc(sizeof(Node));
    n->data = data;
    n->prev = n->next = NULL;
    return n;
}
LinkedList *createLinkedList() {
    LinkedList *l = (LinkedList *)malloc(sizeof(LinkedList));
    l->head = l->tail = NULL;
    return l;
}

void insertAtFirst(LinkedList *l, int data){
    if (l->head == NULL) {
        l->head = l->tail = createNode(data);
    } else {
        Node *temp = createNode(data);
        temp->next = l->head;
        l->head->prev = temp;
        l->head = temp;
    }
}

void insertAtLast(LinkedList *l, int data){
    if (l->head == NULL) {
        l->head = l->tail = createNode(data);
    } else {
        Node *temp = createNode(data);
        l->tail->next = temp;
        temp->prev = l->tail;
    }
}

void insertAfterNode(LinkedList *l, int data, int target) {
    Node *temp = l->head;
    while(temp) {
        if(temp->data == target) {
            Node *n = createNode(data);
            n->next = temp->next;
            n->prev = temp;
            temp->next = n;
            if(n->next) {
                n->next->prev = n;
            }
            return;
        }
        temp = temp->next;
    }
    printf("data not found in list\n");
}

void display(LinkedList *l) {
    Node *temp = l->head;
    while(temp) {
        printf("%d  ", temp->data);
        temp = temp->next;
    }
}

int main() {
    LinkedList *l = createLinkedList();
    insertAtFirst(l, 5);
    insertAtFirst(l, 4);
    insertAtFirst(l, 3);
    insertAtFirst(l, 2);
    insertAtFirst(l, 1);
    insertAtLast(l, 6);
    insertAfterNode(l, 8, 6);
    insertAfterNode(l, 7, 6);
    display(l);
    return 0;
}

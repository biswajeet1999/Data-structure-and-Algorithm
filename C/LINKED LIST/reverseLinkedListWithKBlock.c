#include<stdio.h>
#include<stdlib.h>

typedef struct Node {
    int data;
    struct Node *next;
}Node;

Node *createNode(int data) {
    Node *temp = (Node *)malloc(sizeof(Node));
    temp->data = data;
    temp->next = NULL;
    return temp;
}

Node *insert(Node *head, int data) {
    if(head == NULL) {
        return createNode(data);
    }
    Node *temp = head;
    while(temp->next) {
        temp = temp->next;
    }
    temp->next = createNode(data);
    return head;
}

Node *getKthNode(Node *curr, int k) {
    for(int i = 1; i < k; i++) {
        if(curr == NULL) {
            return NULL;
        }
        curr = curr->next;
    }
    return curr;
}

Node *reverseBlockWise(Node *head, int k) {
    Node *prev = NULL;
    Node *curr =  head;
    Node *next = head;
    Node *newHead = NULL;
    Node *startOfBlock = NULL;
    Node *kthNode = NULL;

    while( (kthNode = getKthNode(curr, k)) ) {
        if(newHead == NULL) {
            newHead = kthNode;
        } else {
            startOfBlock->next = kthNode;
        }
        // reverse the k block;
        for(int i = 0; i < k; i++) {
            if(i == 0) {
                startOfBlock = curr; // holds the starting node of each k-block
            }
            next = curr->next;
            curr->next = prev;
            prev = curr;
            curr = next;
        }
    }
    // base case when k >  len of list
    if(kthNode == NULL && startOfBlock == NULL) {
        return head;
    }
    if(curr == NULL) {
        startOfBlock->next = NULL;
    } else {
        startOfBlock->next = curr;
    }
    return newHead;
}

void display(Node *head) {
    printf("\n");
    while(head) {
        printf("%d  ", head->data);
        head = head->next;
    }
}

void main() {
    int k;
    printf("Enter k: ");
    scanf("%d", &k);
    Node *head = insert(NULL, 1);
    head = insert(head, 2);
    head = insert(head, 3);
    head = insert(head, 4);
    head = insert(head, 5);
    head = insert(head, 6);
    head = insert(head, 7);
    head = insert(head, 8);
    // printf("%d", getKthNode(head, 3)->data);
    display(head);
    head = reverseBlockWise(head, k);
    display(head);
}
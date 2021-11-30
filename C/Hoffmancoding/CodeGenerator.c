
#include<stdio.h>
#include<stdlib.h>

/* node of minHeap */
typedef struct minHeapNode{
    struct minHeapNode *left;
    int frequency;
    char character;
    struct minHeapNode *right;
}MinHeapNode;

/* minHeap structure */
typedef struct minHeap{
    int capacity;   /* max size */
    int top;        /* last node index */
    MinHeapNode **minheap;
}MinHeap;

/* create node*/
MinHeapNode *createNode(char character,int freq)
{
    MinHeapNode *node = (MinHeapNode *)malloc(sizeof(MinHeapNode));
    node->left = node->right = NULL;
    node->character = character;
    node->frequency = freq;
    return node;
}

/* create minHeap */
MinHeap *createMinHeap(int capacity)
{
    MinHeap *heap = (MinHeap *)malloc(sizeof(MinHeap));
    heap->capacity = capacity;
    heap->top = -1;
    heap->minheap = (MinHeapNode **)malloc(sizeof(MinHeapNode *)*(heap->capacity));
    return heap;
}

/* insert single node into heap */
void insert(MinHeap *heap, MinHeapNode *node)
{
    int index; /* Iterator for heap */
    int parentIndex; /* hold the index of parent node */
    heap->top++;  /* increment top */
    heap->minheap[heap->top] = node;
    index = heap->top;
    while(index > 0)
    {
        parentIndex = (index%2==0)? (index/2)-1 : index/2;
        if(heap->minheap[index]->frequency < heap->minheap[parentIndex]->frequency ){ /* swap two nodes */
            MinHeapNode *temp = heap->minheap[index];
            heap->minheap[index] = heap->minheap[parentIndex];
            heap->minheap[parentIndex] = temp;
        }
        index = parentIndex;
    } // end of while
}

/* Build the min heap */
void insertIntoHeap(MinHeap *heap, char charSet[], int freqSet[], int size)
{
    int i;  /* Iterator  for  charSet and freqSet*/
    int index; /* Iterator for heap */
    int parentIndex; /* hold the index of parent node */
    for(i=0;i<size;i++)
    {
        MinHeapNode *node = createNode(charSet[i], freqSet[i]);
        insert(heap,node);
    } // end of for
}

void heapify(MinHeap *heap)
{
    int index,leftChildIndex,rightChildIndex;
    int min; /* hold min of right and left child */
    MinHeapNode *temp;
    index=0;

    while(index<heap->top){
        leftChildIndex = (index*2)+1;
        rightChildIndex = (index*2)+2;
        if(rightChildIndex > heap->top && leftChildIndex > heap->top)  /* no need to swap node already in right position */
            break;
        else if(rightChildIndex>heap->top) /* right child not exists */
            min = leftChildIndex;
        else
            min = (heap->minheap[leftChildIndex]->frequency > heap->minheap[rightChildIndex]->frequency)? rightChildIndex : leftChildIndex;

        if(heap->minheap[index]->frequency > heap->minheap[min]->frequency){
            /* swap two node */
            temp = heap->minheap[index];
            heap->minheap[index] = heap->minheap[min];
            heap->minheap[min] = temp;
            /* swap complete */
            index = min;  /* update root node index */
        }
        else
            return;

    }
}
/* remove and return first node(i.e min freq node) from heap */
MinHeapNode *extractFirstNode(MinHeap* heap)
{
    MinHeapNode *node=NULL;
    if(heap->top == -1)
        return NULL;
    node = heap->minheap[0];
    heap->minheap[0] = heap->minheap[heap->top];
    heap->top--;  /* decrease top after removal of node */
    heapify(heap);
    return node;
}

/* Build the hoffman tree */
void creatHoffmanTree(MinHeap* heap)
{
    int freqSum;
    while(heap->top > 0)  /* it will continue until there is a single node in the heap */
    {
        MinHeapNode *first = extractFirstNode(heap);
        MinHeapNode *second = extractFirstNode(heap);
        freqSum = first->frequency+second->frequency;
        MinHeapNode *internalNode = createNode('\0',freqSum);
        internalNode->left = first;
        internalNode->right = second;
        insert(heap, internalNode);
    }
}

/* display code table and write into file */
void generatePrefixCode(MinHeapNode *root,char *code, int codeIndex,FILE *f)
{
    int i;
     if(root == NULL)
        return;
     else{
         code[codeIndex]='0';
         generatePrefixCode(root->left, code, codeIndex+1,f);
         if(root->left == NULL && root->right==NULL){
            code[codeIndex] = root->character;
            printf("%c : ",code[codeIndex]);
            // write into file
            fputc(code[codeIndex],f);
            fputs(" : ",f);

            for(i = 0;i<= codeIndex-1;i++){
                printf("%c ",code[i]);
                fputc(code[i],f);  // writing file
            }
            printf("\n");
            fputs("\n",f);
         }
         code[codeIndex] = '1';
         generatePrefixCode(root->right, code, codeIndex+1,f);
     }
}

main()
{
    FILE *f = fopen("HoffmancodeTable.txt","w");
    if(!f){
        printf("Error opening file HoffmancodeTable.txt file\n");
        exit(0);
    }
    char set[]={'a', 'b', 'c', 'd', 'e', 'f'};
    int freq[]={5, 9, 12, 13, 16, 45};
    MinHeap *heap = createMinHeap(6);
    char code[heap->capacity];
    int codeIndex = 0;
    insertIntoHeap(heap, set, freq, 6);
    printf("\n");
    creatHoffmanTree(heap);
    generatePrefixCode(heap->minheap[0],code,codeIndex,f);
    fclose(f);
}

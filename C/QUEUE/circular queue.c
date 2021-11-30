#include<stdio.h>
#include<stdlib.h>
typedef struct queue
{
    int rear;
    int front;
    int capacity;
    int *array;
}QUEUE;
QUEUE *createqueue(int cap)
{
    QUEUE *queue;
    queue=(QUEUE *)malloc(sizeof(QUEUE));
    queue->rear=queue->front=-1;
    queue->capacity=cap;
    queue->array=(int *)malloc(sizeof(int)*cap);
}
int isempty(QUEUE *queue)
{
    if(queue->front==-1)
        return 1;
    else
        return 0;
}
int isfull(QUEUE *queue)
{
    if(queue->front==0 && queue->rear==queue->capacity-1)
        return 1;
    else if(queue->rear+1==queue->front)
        return 1;
    else
        return 0;
}
int availablespace(QUEUE *queue)
{
    if(queue->front==-1)
        return (queue->capacity);
    else if(queue->front<queue->rear)
        return(queue->capacity-(queue->rear-queue->front)-1);
    else if(queue->front>queue->rear)
        return (queue->front-queue->rear-1);
}
int capacity(QUEUE *queue)
{
    return (queue->capacity);
}
void doublequeue(QUEUE *queue)
{
    int *temp,i=0,j=queue->front;
    queue->capacity=queue->capacity*2;
    temp=(int *)malloc(queue->capacity*sizeof(int));
    temp[0]=queue->array[j];
    for(i=1,j=queue->front+1;j !=queue->rear+1;i++){
        temp[i]=queue->array[j];
        if(j==queue->capacity/2-1 && j > queue->rear)
            j=0;
        else
            j++;
    }
    free(queue->array);
    queue->array=temp;
    queue->front=0;
    queue->rear=i-1;  //it aslo be    queue-rear=queue->capacity/2-1
}
void halfqueue(QUEUE *queue)
{
    int *temp,i=0,j=queue->front;
    queue->capacity=queue->capacity/2;
    temp=(int *)malloc(queue->capacity*sizeof(int));
    temp[0]=queue->array[j];
    for(i=1,j=queue->front+1;j != queue->rear+1;i++){
        temp[i]=queue->array[j];
        if(j==queue->capacity*2-1 && j > queue->rear)
            j=0;
        else
            j++;
    }
    free(queue->array);
    queue->array=temp;
    queue->front=0;
    queue->rear=i-1;         //it also be   queue-rear=queue->capacity-1;
}
void enqueue(QUEUE *queue,int data)
{
    if(queue->capacity==0)
        printf("Invallid capacity\n");
    else  if(isempty(queue)){
        queue->front=queue->rear=0;
        queue->array[queue->rear]=data;
    }
    else if(isfull(queue)){
        doublequeue(queue);
        queue->array[++queue->rear]=data;
    }
    else if(queue->rear==queue->capacity-1){
        queue->rear=0;
        queue->array[queue->rear]=data;
    }
    else
        queue->array[++queue->rear]=data;
}
void dequeue(QUEUE *queue)
{
    int size;
    if(isempty(queue))
        printf("QUEUE IS EMPTY\n");
    else if(queue->rear==queue->front)
        queue->rear=queue->front=-1;
    else if(queue->front==queue->capacity-1)
        queue->front=0;
    else
        queue->front=queue->front+1;

    size=availablespace(queue);
    if(queue->front>-1)
        if((queue->capacity-size)<=queue->capacity/2)
            halfqueue(queue);
}

void main()
{
    QUEUE *queue;
    queue=createqueue(4);
    dequeue(queue);
    printf("\ncapacity= %d, front= %d, rear= %d",queue->capacity,queue->front,queue->rear);
    enqueue(queue,10);
    printf("\ncapacity= %d, front= %d, rear= %d",queue->capacity,queue->front,queue->rear);
    enqueue(queue,20);
    printf("\ncapacity= %d, front= %d, rear= %d",queue->capacity,queue->front,queue->rear);
    enqueue(queue,30);
    printf("\ncapacity= %d, front= %d, rear= %d",queue->capacity,queue->front,queue->rear);
    enqueue(queue,40);
    printf("\ncapacity= %d, front= %d, rear= %d",queue->capacity,queue->front,queue->rear);
    printf("\n%d",availablespace(queue));
     enqueue(queue,50);
    printf("\ncapacity= %d, front= %d, rear= %d",queue->capacity,queue->front,queue->rear);
    printf("\ncapacity=%d",availablespace(queue));
    dequeue(queue);
    printf("\ncapacity= %d, front= %d, rear= %d",queue->capacity,queue->front,queue->rear);
    dequeue(queue);
    printf("\ncapacity= %d, front= %d, rear= %d",queue->capacity,queue->front,queue->rear);
    dequeue(queue);
    printf("\ncapacity= %d, front= %d, rear= %d",queue->capacity,queue->front,queue->rear);
    enqueue(queue,40);
    printf("\ncapacity= %d, front= %d, rear= %d",queue->capacity,queue->front,queue->rear);
    printf("\n%d",availablespace(queue));
    enqueue(queue,40);
    printf("\ncapacity= %d, front= %d, rear= %d",queue->capacity,queue->front,queue->rear);
    printf("\n%d",availablespace(queue));
    dequeue(queue);
    printf("\ncapacity= %d, front= %d, rear= %d",queue->capacity,queue->front,queue->rear);
    enqueue(queue,50);
    printf("\ncapacity= %d, front= %d, rear= %d",queue->capacity,queue->front,queue->rear);
    printf("\ncapacity=%d",availablespace(queue));
}

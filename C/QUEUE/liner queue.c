#include<stdio.h>
#include<stdlib.h>
typedef struct queue
{
    int capacity;
    int front,rear;
    int *array;
}QUEUE;
QUEUE *createqueue()
{
    QUEUE *queue;
    queue=(QUEUE *)malloc(sizeof(QUEUE));
    queue->rear=queue->front=-1;
    printf("Enter capacity\n");
    scanf("%d",&queue->capacity);
    queue->array=(int *)malloc(queue->capacity*sizeof(int));
    return queue;
}
int isfull(QUEUE *queue)
{
    if(queue->rear==queue->capacity-1)
    {
        printf("Queue is full\n");
        return 1;
    }
    else
        return 0;
}
int isempty(QUEUE *queue)
{
    if(queue->rear==-1 && queue->front==-1){
        printf("Queue is empty\n");
        return 1;
    }
    else
        return 0;
}
void enqueue(QUEUE *queue,int data)
{
    if(!isfull(queue)){
            if(queue->rear==-1 && queue->front==-1)
                 queue->front=queue->rear=0;
            else
                queue->rear++;
        queue->array[queue->rear]=data;
    }
}
int dequeue(QUEUE *queue)
{
    if(!isempty(queue)){
        int item;
        if(queue->rear==queue->front){
             item=queue->array[queue->front];
             queue->rear=queue->front=-1;
        }else{
          item=queue->array[queue->front];
          queue->front++;
        }
        printf("You removed %d",item);
        return item;
    }
}
void main()
{
    QUEUE *queue;
    queue=createqueue();
    int data;
    printf("1.insert\t2.delete\n");
    while(1)
    {
        int choise;
        printf("Enter choise\n");
        scanf("%d",&choise);
        switch(choise)
        {
        case 1:
            printf("Enter data\n");
            scanf("%d",&data);
            enqueue(queue,data);
            break;
        case 2:
            dequeue(queue);
            break;
        default:
            printf("invallid choise\n");
        }
    }
}

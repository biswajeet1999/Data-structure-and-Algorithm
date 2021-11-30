#include<stdio.h>
#include<stdlib.h>
typedef struct queue
{
    int front;
    int rear;
    int capacity;
    int *array;
}QUEUE;
QUEUE *createqueue(int cap)
{
    QUEUE *queue;
    queue=(QUEUE *)malloc(sizeof(QUEUE));
    queue->front=queue->rear=-1;
    queue->capacity=cap;
    queue->array=(int *)malloc(sizeof(int)*cap);
    return queue;
}
int isfull(QUEUE *queue)
{
    if(queue->rear==0 && queue->rear==queue->capacity-1)
        return 1;
    else
        return 0;
}
int isempty(QUEUE *queue)
{
    if(queue->rear==-1 && queue->front==-1)
        return 1;
    else
        return 0;
}
void enqueueRIGHT(QUEUE *queue,int data)
{
    if(!isfull(queue)){
        if(queue->rear==-1 &&queue->front==-1){
             queue->rear=queue->front=0;
             queue->array[queue->rear]=data;
        }
        else if(queue->rear==queue->capacity-1)
            printf("OVER FLOW\n");
        else
            queue->array[++queue->rear]=data;
    }
    else
        printf("QUEUE IS FULL\n");
}
void enqueueLEFT(QUEUE *queue,int item)
{
    if(!isfull(queue)){
        if(queue->rear==-1 && queue->front==-1)
        {
            queue->rear=queue->front=0;
            queue->array[queue->front]=item;
        }
        else if(queue->front==0)
            printf("UNDER FLOW\n");
        else
            queue->array[--queue->front]=item;
    }
    else
        printf("QUEUE IS FULL\n");
}
int dequeueRIGHT(QUEUE *queue)
{
    if(!isempty(queue)){
        int data;
        data=queue->array[queue->rear];
        queue->rear=queue->rear-1;
        printf("you removed %d\n",data);
        return data;
    }
    else{
        printf("QUEUE IS EMPTY\n");
        return NULL;
    }
}
int dequeueLEFT(QUEUE *queue)
{
    if(!isempty(queue)){
        int data;
        data=queue->array[queue->front];
        queue->front=queue->front+1;
        printf("you removed %d\n",data);
        return data;
    }
    else{
        printf("QUEUE IS EMPTY\n");
        return NULL;
    }
}
void main()
{
    QUEUE *queue;
    int choice,data;
    queue=createqueue(10);
    printf("\n1.insert at right\t2.insert at left\t3.delete from right\t4.delete from left\t5.exit\n");
    while(1){
       printf("Enter your choice\n");
       scanf("%d",&choice);
       switch(choice){
   case 1:
       printf("Enter data\n");
       scanf("%d",&data);
       enqueueRIGHT(queue,data);
       break;
   case 2:
       printf("Enter data\n");
       scanf("%d",&data);
       enqueueLEFT(queue,data);
       break;
   case 3:
      dequeueRIGHT(queue);
       break;
   case 4:
      dequeueLEFT(queue);
      break;
   case 5:
       exit(1);
    }

  }
}

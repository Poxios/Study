#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_QUEUE_SIZE 5
#define ERROR_CODE -1

typedef struct
{
    int key;
} element;

element queue[MAX_QUEUE_SIZE];
int rear = 0;
int front = 0;

void queueFull()
{
    fprintf(stderr, "Queue is full, cannot add element\n");
    exit(EXIT_FAILURE);
}

element queueEmpty()
{
    element temp;
    temp.key = ERROR_CODE;
    fprintf(stderr, "Queue is empty, cannot delete element\n");
    return temp;
}

void addq(element item)
{
    if ((rear + 1) % MAX_QUEUE_SIZE == front)
        queueFull();
    else
    {
        rear = (rear + 1) % MAX_QUEUE_SIZE;
        queue[rear] = item;
    }
}

element deleteq()
{
    if (front == rear)
        queueEmpty();
    else
    {
        front = (front + 1) % MAX_QUEUE_SIZE;
        return queue[front];
    }
}
void printQueue()
{
    int i;
    printf("front:%d rear:%d\n", front, rear);
    printf("Queue: ");
    if (front == rear)
    {
        printf("\n");
        return;
    }
    i = front;
    while (1)
    {
        i = (i + 1) % MAX_QUEUE_SIZE;
        printf("[%d]%d ", i, queue[i].key);
        if (i == rear)
            break;
    }
    printf("\n");
}

int main(void)
{
    element item1, item2, item3;
    item1.key = 10;
    item2.key = 20;
    item3.key = 30;
    addq(item1);
    printQueue();
    addq(item2);
    printQueue();
    addq(item3);
    printQueue();
    deleteq();
    printQueue();
    deleteq();
    printQueue();
    deleteq();
    printQueue();
    deleteq();
    printQueue();
    addq(item1);
    printQueue();
    addq(item2);
    printQueue();
    addq(item3);
    printQueue();
    addq(item1);
    printQueue();
    addq(item2);
    printQueue();
    return 0;
}
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define TRUE 1
#define FALSE 0
#define ERROR_CODE -1

typedef struct
{
    int key;
} element;

element *stack;

int capacity = 1;
int top = -1;

void stackFull()
{
    stack = realloc(stack, 2 * capacity *
                               sizeof(*stack));
    capacity *= 2;
}

element stackEmpty()
{
    element temp;
    temp.key = ERROR_CODE;
    fprintf(stderr, "Stack is empty, cannot delete element\n");
    return temp;
}

int isEmpty()
{
    return top == -1;
}

int isFull()
{
    return (top == capacity - 1);
}

void push(element item)
{
    if (top >= capacity - 1)
    {
        stackFull();
    }
    stack[++top] = item;
}

element pop()
{
    if (top == -1)
    {
        stackEmpty();
    }
    return stack[top--];
}

void printStack()
{
    int i;
    printf("Stack: ");
    for (i = 0; i <= top; i++)
        printf("%d ", stack[i].key);
    printf("\n");
}
int main(void)
{
    element item1, item2, item3;
    stack = (element *)malloc(sizeof(*stack));
    item1.key = 10;
    item2.key = 22;
    item3.key = 55;
    printStack();
    push(item1);
    printStack();
    push(item2);
    printStack();
    push(item3);
    printStack();
    pop();
    printStack();
    pop();
    printStack();
    pop();
    printStack();
    return 0;
}
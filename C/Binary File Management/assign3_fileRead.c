#include <stdio.h>
#include <stdlib.h>

typedef struct
{
    int number;
    char name[20];
    char address[20];
    char hobby[20];
    char food[20];
} studentStruct;

int main(void)
{
    FILE *binFile;
    studentStruct studentA;
    binFile = fopen("my.bin", "rb");
    fread(&studentA, sizeof(studentA), 1, binFile);
    printf("%d %s %s %s %s", studentA.number, studentA.name, studentA.address, studentA.hobby, studentA.food);
    fclose(binFile);
    return 0;
}
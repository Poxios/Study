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
    scanf("%d %s %s %s %s", &studentA.number, studentA.name, studentA.address, studentA.hobby, studentA.food);
    binFile = fopen("my.bin", "wb");
    fwrite(&studentA, sizeof(studentA), 1, binFile);
    fclose(binFile);
    return 0;
}
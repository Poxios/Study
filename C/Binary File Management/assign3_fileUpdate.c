#include <stdio.h>
#include <stdlib.h>
#include <string.h>

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
    int studentNumToUpdate;
    char addressToUpdate[20];

    FILE *binFileWritter;
    FILE *binFileReader;
    studentStruct studentA;

    binFileReader = fopen("my.bin", "rb");
    fread(&studentA, sizeof(studentA), 1, binFileReader);
    fclose(binFileReader);

    printf("학번, 주소 입력: ");
    scanf("%d %s", &studentNumToUpdate, addressToUpdate);

    if (studentA.number == studentNumToUpdate)
    {
        strcpy(studentA.address, addressToUpdate);
    }

    binFileWritter = fopen("my.bin", "wb");
    fwrite(&studentA, sizeof(studentA), 1, binFileWritter);
    fclose(binFileWritter);
    return 0;
}
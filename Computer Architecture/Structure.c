#include <stdio.h>
#include <stdlib.h>
#include <string.h>

struct profile
{
    char name[20];
    double grade;
    int english;
};

void input_data(struct profile **employeesArrayRef, int employeesCount)
{
    printf("이름 학점 영어점수 순으로 입력하세요.\n");
    char name[20];
    double grade;
    int englishScore;

    for (int i = 0; i < employeesCount; i++)
    {
        struct profile *singleEmployee = malloc(sizeof(struct profile));
        scanf("%s %lf %d", name, &grade, &englishScore);
        strcpy(singleEmployee->name, name);
        singleEmployee->grade = grade;
        singleEmployee->english = englishScore;
        employeesArrayRef[i] = singleEmployee;
    }
    return;
}

void print_data(struct profile **employeesArrayRef, int employeesCount)
{
    printf("\n=====엘리트 사원=====\n");
    for (int i = 0; i < employeesCount; i++)
    {
        if (employeesArrayRef[i]->grade >= 4.0 && employeesArrayRef[i]->english >= 900)
        {
            printf("이름 : %s\n", employeesArrayRef[i]->name);
            printf("학점 : %.2lf\n", employeesArrayRef[i]->grade);
            printf("영어점수 : %d\n\n", employeesArrayRef[i]->english);
        }
    }
    return;
}

int main(void)
{
    int employeesCount;
    printf("사원 수를 입력하세요: ");
    scanf("%d", &employeesCount);

    struct profile **employeesArray = (struct profile **)malloc(sizeof(struct profile *) * employeesCount);

    input_data(employeesArray, employeesCount);
    print_data(employeesArray, employeesCount);

    return 0;
}

#include<stdio.h>

int main()
{
    int a[] = {10, 1, 2, 76, 20, 3, 20, 49, 98, 5};
    int n = 0;

    for(int i=0; i < 10; i++)
    {
        if(a[i] > 5)
            printf("%i\n", a[i]);
        else
            n++;
    }

    printf("n is %i\n", n);
}
#include <stdio.h>

int main()
{
 int i, ans = 1, num;
 printf("Enter number to find factorial : ");
 scanf("%d", &num);
 for (i = 1; i <= num; i++)
 {
  ans *= i;
 }
 printf("Factorial of the given number : %d", ans);
 return 0;
}

#include <stdio.h>

int main()
{
 int a[10], i, j, n, temp;

 printf("Enter number of elements in array : ");
 scanf("%d", &n);

 for (i = 0; i < n; i++)
 {
  printf("Enter %d elements of array : ", n);
  scanf("%d", &a[i]);
 }
 printf("Array Before Bubble Sorting : \n");
 for (i = 0; i < n; i++)
 {
  printf("%d\n", a[i]);
 }

 for (i = 0; i < n - 1; i++) // no. of passes required
 {
  for (j = 0; j < n - 1 - i; j++)
  {
   if (a[j] < a[j + 1])
   {
    temp = a[j];
    a[j] = a[j + 1];
    a[j + 1] = temp;
   }
  }
 }

 printf("Array Before Bubble Sorting:\n");
 for (i = 0; i < n; i++)
 {
  printf("%d\n", a[i]);
  // printf("Array after Binary Sorting : %d", a[i]);
 }

 return 0;
}

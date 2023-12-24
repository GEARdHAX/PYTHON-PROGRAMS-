#include <stdio.h>

int main()
{
 // Original array
 int a[5] = {1, 2, 3, 4, 5};
 int n = sizeof(a) / sizeof(a[0]);

 // Print original array
 printf("Original Array: ");
 for (int i = 0; i < n; i++)
 {
  printf("%d ", a[i]);
 }

 // Reverse array and print reversed array
 int b[5];
 printf("\nReversed Array: ");
 for (int i = n - 1; i >= 0; i--)
 {
  b[n - 1 - i] = a[i];
  printf("%d ", b[n - 1 - i]);
 }

 return 0;
}

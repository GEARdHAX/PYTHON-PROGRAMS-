#include <stdio.h>

int main(int argc, char const *argv[])
{
 int arr[] = {35, 13, 55, 12, 98, 42, 54, 21, 64, 10};
 int max = arr[0];
 int size = sizeof(arr) / sizeof(arr[0]);
 for (int i = 0; i < size; i++)
 {
  if (arr[i] > max)
  {
   max = arr[i];
  }
 }
 printf("Largest element in array : %d", max);

 return 0;
}

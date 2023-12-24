#include <stdio.h>

int main(int argc, char const *argv[])
{
 int a[] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
 int key;

 printf("Enter Key to search in array: ");
 scanf("%d", &key);

 // Print each element of the array
 printf("Array elements: ");
 for (int i = 0; i < sizeof(a) / sizeof(a[0]); i++)
 {
  printf("%d, ", a[i]);
 }

 int found = 0; // Flag to check if the key is found

 for (int i = 0; i < sizeof(a) / sizeof(a[0]); i++)
 {
  if (a[i] == key)
  {
   printf("\n%d is found at index %d\n", key, i + 1);
   found = 1; // Set the flag to indicate the key is found
   break;
  }
 }

 if (!found) // Check the flag to print "not found" message
 {
  printf("\n%d is not found in Array\n", key);
 }

 return 0;
}

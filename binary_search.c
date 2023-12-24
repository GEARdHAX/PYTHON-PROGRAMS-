#include <stdio.h>

int BinarySearch(int arr[100], int size, int key)
{
 int low, mid, high;

 low = 0;
 high = size - 1;

 while (low <= high)
 {
  mid = (low + high) / 2;

  if (arr[mid] == key)
  {
   return mid;
  }
  else if (arr[mid] < key)
  {
   low = mid + 1;
  }
  else
  {
   high = mid - 1;
  }
 }

 return -1; // Return -1 to indicate that the key was not found
}

int main()
{
 int key;
 int a[] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12};
 int size = sizeof(a) / sizeof(a[0]);

 printf("Enter Key to BinarySearch: ");
 scanf("%d", &key);

 int indexValue = BinarySearch(a, size, key);

 if (indexValue != -1)
 {
  printf("The element %d was found at index %d\n", key, indexValue);
 }
 else
 {
  printf("The element %d was not found in the array\n", key);
 }

 return 0;
}

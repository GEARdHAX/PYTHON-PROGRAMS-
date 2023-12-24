#include <stdio.h>

void main()
{
 int sp = 0, sn = 0; // Initialize sp and sn to zero
 int a[] = {5, 2, -23, 53, -10, 5};

 for (int i = 0; i < sizeof(a) / sizeof(a[0]); i++)
 {
  if (a[i] > 0)
  {
   sp += a[i];
  }
  else
  {
   sn += a[i];
  }
 }

 printf("Sum of Positive Integer : %d\nSum of Negative Integer : %d", sp, sn);
}

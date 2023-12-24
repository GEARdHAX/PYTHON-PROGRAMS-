#include <stdio.h>

int main(int argc, char const *argv[])
{
 int digit, reversed = 0;
 int num = 12321;
 int ogNum = num;
 while (num > 0)
 {
  digit = num % 10;
  reversed = reversed * 10 + digit;
  num /= 10;
 }
 if (ogNum == reversed)
 {
  printf("%d is a Palindrome.", ogNum);
 }
 else
 {
  printf("%d is not a Palindrome.", ogNum);
  /* code */
 }

 return 0;
}

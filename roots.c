#include <stdio.h>
#include <math.h>

int main()
{
 double a, b, c;
 double realPart, imaginaryPart;

 // Input from the user
 printf("Enter coefficient a: ");
 scanf("%lf", &a);

 printf("Enter coefficient b: ");
 scanf("%lf", &b); 

 printf("Enter coefficient c: ");
 scanf("%lf", &c);

 // Calculate the discriminant
 double discriminant = b * b - 4 * a * c;

 // Check the nature of the roots
 if (discriminant >= 0)
 {
  // Calculate real roots
  double root1 = (-b + sqrt(discriminant)) / (2 * a);
  double root2 = (-b - sqrt(discriminant)) / (2 * a);

  printf("Roots are real:\n");
  printf("Root 1 = %.2f\n", root1);
  printf("Root 2 = %.2f\n", root2);
 }
 else
 {
  // Calculate complex roots
  realPart = -b / (2 * a);
  imaginaryPart = sqrt(-discriminant) / (2 * a);

  printf("Roots are complex and conjugate:\n");
  printf("Root 1 = %.2f + %.2fi\n", realPart, imaginaryPart);
  printf("Root 2 = %.2f - %.2fi\n", realPart, imaginaryPart);
 }

 return 0;
}

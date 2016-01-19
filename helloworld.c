#include <stdio.h>

int main()
{
  /* hi this is a multi-line comment
     hi.
  */

  // single-line comment
  printf ("Hello world!\n");  // this works too

  // some vars and control flow
  int numDaysInYear = 365;
  printf ("days per year: %d\n", numDaysInYear);

  if (numDaysInYear == 366) {
    printf ("Seems reasonable\n");
  }
  else {
    int long someReallyLongNumber = 100000000000000L;
    printf ("Some long number: %ld\n", someReallyLongNumber);
  }

  // loops
  int i;
  for (i=0; i<5; i++) {
    printf ("i=%d\n", i);
  }

  // https://www.seas.gwu.edu/~simhaweb/C/lectures/module2/module2
  int x = 5;

  int *intPtr;

  // print mem address of variable i
  printf ("Variable x is located at memory address %lu\n", &x);

  // extract address of var i into the pointer
  intPtr = & x;
  printf ("The int at memory location %lu is %d\n", intPtr, *intPtr);

  // TODO: examine compiler warnings

}

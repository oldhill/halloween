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

}

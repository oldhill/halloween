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

  // numerical types
  float pi = 3.14F;
  double doublePi = 314.159265E-2;  // the exponent
  long double lDoublePi = 3.14159265358979L;

  // print em
  printf ("float Pi = %7.5e\n", pi);  // ... exponent format?
  printf ("double Pi = %lf\n", doublePi);
  printf ("(not actually?) long double Pi = %Lf\n", lDoublePi);


  // https://www.seas.gwu.edu/~simhaweb/C/lectures/module2/module2
  // * is used to declare and/or dereference pointers
  // & gets the memory address
  int x = 5;

  int *intPtr;

  // print mem address of variable x
  printf ("Variable x is located at memory address %lu\n", (int long)&x);

  // extract address of var x into the pointer... that is... the pointer
  // now points to the memory address holding x
  intPtr = & x;
  printf ("The int at memory location %lu is %d\n", (int long)intPtr, *intPtr);

  // "The dereference operation starts at the pointer and follows its arrow over to access its pointee.
  //  The goal may be to look at the pointee state or to change the pointee state."
  // - parlante, http://cslibrary.stanford.edu/106/

}

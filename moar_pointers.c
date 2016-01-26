#include <stdio.h>
#include <stdlib.h>  // contains malloc function

int main()
{
  int * x;
  int long * y;

  x = malloc(sizeof(int));  // Allocate an int pointee, and set x to point to it
                            // This memory is "dynamically" allocated at runtime,
                            // and is not de-allocated until "free"()'ing it.

  y = malloc(1);

  *x = 42;  // Dereference x to store 42 in its pointee

  *y = 475867957L;  // >< doesn't crash... :/

  printf ("hi\n");

  return 0;

}

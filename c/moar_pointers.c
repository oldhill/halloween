#include <stdio.h>
#include <stdlib.h>  // contains malloc function

int main()
{
  // Do some stuff with pointers
  int * x;
  x = malloc(sizeof(int));  // Allocate an int pointee, and set x to point to it
                            // This memory is "dynamically" allocated at runtime,
                            // and is not de-allocated until "free"()'ing it.
  *x = 42;  // Dereference x to store 42 in its pointee

  int * y;
  y = malloc(1);
  *y = 42;  // even though we malloc'd 1, y is allocated 16 bytes...?

  // Examine some memory allocations
  // malloc_size is a mac osx specific function for determing allocated memory of a pointer:
  // https://developer.apple.com/library/mac/documentation/Darwin/Reference/ManPages/man3/malloc_size.3.html
  int x_size = malloc_size(x);
  int y_size = malloc_size(y);
  printf ("Bytes allocated for y: %d, and for x: %d\n", y_size, x_size);
  // Those are both 16. Is that because of the it's the default buffer size on osx? see notes


  // OK try allocated more than 16 by hand... you get 32!
  int * z;
  z = malloc(20);
  int z_size = malloc_size(z);
  printf ("OK but what if we allocated more than 16 bytes..."
          "Bytes allocated for z: %d\n", z_size);

  printf ("hi\n");

  // Verify that integers take 4 byes to store...
  int int_size = sizeof(int);
  printf ("Bytes required to store an integer: %d\n", int_size);

  return 0;

}

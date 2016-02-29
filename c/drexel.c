#include <math.h>  // M_PI constant
#include <stdio.h>

// definin a random function
void something()
{
  printf("Ok called this function\n");
}

// part II
float get_pi()
{
  return M_PI;
}

// loops
void the_while()
{
  int counter = 0;
  while (counter < 5)
  {
    printf("OK counter is now equal to: %d\n", counter);
    counter = counter + 1;
  }
}

void the_for()
{
  for(int i = 0; i < 5; i = i + 1)
  {
    printf("OK i is now equal to: %d\n", i);
  }
}

// symbolic constants
#define CONST_THREE 3
#define CONST_ZERO 0

// yeah
int main()
{
  printf("Hello World!\n");

  // basic user defined function
  something();

  // user defined fn with return value that's a lib constant
  float my_pi = get_pi();
  printf("OK here's pi: %f\n", my_pi);

  // some loops though
  the_while();
  the_for();

  // use symbolic constants
  printf("This constant should be a zero: %d\n", CONST_ZERO);
  for (int j = 0; j < CONST_THREE; j = j + 1)
  {
    printf("Counting up to a symbolic constant: %d\n", j);
  }

  return 0;
}


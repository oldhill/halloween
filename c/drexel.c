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

int main()
{
  printf("Hello World!\n");

  // basic user defined function
  something();

  // user defined fn with return value that's a lib constant
  float my_pi = get_pi();
  printf("OK here's pi: %f\n", my_pi);

  return 0;
}


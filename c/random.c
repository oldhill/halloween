#include <stdio.h> // printf, etc
#include <stdlib.h>  // aye
#include <time.h>  // time

int main()
{
  time_t now = time(0);

  printf("Time: %ld\n", now);

  return 0;
}

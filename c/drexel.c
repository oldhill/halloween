#include <math.h>  // M_PI constant
#include <stdio.h>
#include <string.h> // strncopy(), strlen() etc

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

// (wildly memory unsafe) conditionals
char * some_complex_operation(int input_num)
{
  if (input_num < 0)
  {
    return "That's a negative number";
  }
  else if (input_num > 100)
  {
    return "That's a pretty big number";
  }
  else
  {
    return "That's a number between 0 and 100!";
  }
}

// maybe safer thing which modifies existing memory buffer
// passes in a reference to existing buffer... then modifies the buffer...
void populate_message(char * message, int buffersize)
{
  const char * msg = "Hello!";
  strncpy(message, msg, buffersize - 1); // copy buffersize-1 chars from msg into message
  message[buffersize - 1] = '\0'; // null terminate
}

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

  // seemingly unsafe non-pre-allocated char pointers
  char * my_message;
  my_message = some_complex_operation(5);
  printf("The message: %s\n", my_message);
  my_message = some_complex_operation(-1);
  printf("The message: %s\n", my_message);
  my_message = some_complex_operation(101);
  printf("The message: %s\n", my_message);

  // possibly safer pre-allocated memory?
  char message[15];
  printf("Initial message: %s\n", message);
  printf("Initial message length: %ld\n", strlen(message));
  populate_message(message, sizeof(message));
  printf("Updated message: %s\n", message);

  return 0;
}


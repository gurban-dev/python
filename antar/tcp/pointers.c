#include <stdio.h>

int main() {
  /* String literals in C are immutable constants,
     and modifying them leads to undefined behavior,
     even if const is omitted.

     segmentation fault (crash) because you're
     trying to modify read-only memory. */

  /* Impermissible because in C, string literals
     are always stored in read-only memory.

     It's better to include "const" because bugs
     in the program will be detected before the
     program is actually run. */
  char *str = "Hello, world!";
  str[0] = 'h';

  // *str should point to 'H'.
  // The format specifier %c tells the printf()
  // function to expect a character to be outputted.
  printf("*str: '%c'\n", *str);

  /* str is a pointer to the first character of the
     string literal "Hello, world!" (which is stored
     in read-only memory).

     In C, the * operator means "dereference this
     pointer", i.e., access the value that the
     pointer points to. */

  // Permissible:
  // char str[] = "Hello, world!";
  // str[0] = 'h';

  // %s is a format specifier in C.
  printf("%s\n", str);

  return 0;
}
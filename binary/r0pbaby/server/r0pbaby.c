#include <stdlib.h>
#include <unistd.h>
#include <stdio.h>
#include <string.h>

#define BUFSIZE 61

void get_flag(){
  gid_t gid = getegid();
  setresgid(gid, gid, gid);
  printf("\n* Awesome! you've changed the program flow and executed the get_flag()\n");
  system("/bin/cat flag2");
  printf("\n");
}

void vulnerable_function(){
  char var2[BUFSIZE];
  gets(var2);
}

void * get_pc () { return __builtin_return_address(0); }
int main(int argc, char **argv){
  printf("## Shellter Labs - Remote exploiting services (v2)");
  printf(" ##\n");
  printf("** Send-me something..\n");
  vulnerable_function();
  return 0;
}

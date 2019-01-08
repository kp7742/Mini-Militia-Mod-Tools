#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>
#include "config.h"
#include "injector.h"
#include "utils.h"

int main(int argc, char const *argv[]) {
  if (argc != 3) {
    return -1;
  }

  const char* library_path = argv[2];
  pid_t pid = atoi(argv[1]);

  if (getuid() == 0) {
	  if (IsSelinuxEnabled()) {
		  DisableSelinux();
	  }
  }

  InjectLibrary(pid, library_path);
  return 0;
}

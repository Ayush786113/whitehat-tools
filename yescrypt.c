#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <fcntl.h>
#include <crypt.h>

#define SALT "$y$j9T$c3HoRbThKBCqq6B7u16/p."
#define HASH "$y$j9T$c3HoRbThKBCqq6B7u16/p.$cr97a1Dw1H6PPlXEFFZqUTKTl3fNV2qyWZPHM8/lxhA"

int hasher(char password[1024]){
	password[strlen(password)-1] = '\0';
	char hash[1024];
	strcpy(hash, crypt(password, SALT));
	if(strcmp(hash, HASH) == 0){
		printf("Password found: %s\n", password);
		return 0;
	}
	return 1;
}

int main(int argc, char **argv){
	int fd = open(argv[1], O_RDONLY);
	FILE *fp = fdopen(fd, "r");
	char password[1024];
	int result;

	while(fgets(password, sizeof(password), fp) != NULL){
		result = hasher(password);
		if(result == 0)
			break;
	}
	return 0;
}

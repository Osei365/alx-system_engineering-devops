#include<stdio.h>
#include <sys/types.h>
#include <unistd.h>
#include <stdlib.h>

/**
 * inifinite_while - runs an infinite while llop
 * Return: 0
 */
int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}

/**
 * main - Entry poiint
 * Return: 0
 */
int main(void)
{
	int a = 0;
	pid_t pid;

	while (a < 5)
	{
		pid = fork();
		if (pid > 0)
		{
			printf("Zombie process created, PID: %d\n", pid);
			sleep(1);
			a++;
		}
		else
			exit(0);
	}

	infinite_while();

	return (0);
}

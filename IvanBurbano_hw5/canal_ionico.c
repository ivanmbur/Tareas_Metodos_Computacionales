#include <stdio.h>
#include <stdlib.h>
#include <math.h>

void main()
{
	MC("Canal_ionico.txt");
	MC("Canal_ionico1.txt");	
}

void MC(char* filename)
{
	double *x_borde  	

	FILE *in = fopen(filename, "r")
	if(!in)
	{
		printf("Problems opening the file %s\n". filename);
		exit(1);
	}
	
}

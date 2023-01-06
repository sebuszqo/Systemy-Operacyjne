#include <stdio.h>
#include <stdlib.h>

void statyczna(){
	int b;
    printf("\nZatrzymanie statyczna() przed alokacją");
    scanf("%d", &b);

	double tablica[1000000];

    printf("\nZatrzymanie statyczna() po alokacji");
	scanf("%d", &b);
	for (int i = 0 ; i < 1000000; i++){
		tablica[i] = 1;
	}

	printf("\nZatrzymanie statyczna() po zapełnieniu 1");
	scanf("%d", &b);

}

void dynamiczna(){
	int a;
	printf("\nZatrzymanie dynamiczna() przed alokacją");
	scanf("%d", &a);
	double *tablica;
	tablica = (double*)malloc(1000000*sizeof(double));
    printf("\nZatrzymanie dynamiczna() po alokacji");
	scanf("%d", &a);
	for (int i =0 ; i <1000000; i++){
        tablica[i] = 1;
    }
    printf("\nZatrzymanie dynamiczna() po zapełnieniu 1");
	scanf("%d", &a);

	free(tablica);
}

int main(void) {
	int a;
	int b;
	int c;

	printf("\nWstrzymano działanie programu");
	scanf("%d",&c);	
	statyczna();
	printf("\nKoniec funkcji statyczna()");
	scanf("%d",&a);
	dynamiczna();
	printf("\nKoniec funkcji dynamiczna()");
	scanf("%d", &b);
}
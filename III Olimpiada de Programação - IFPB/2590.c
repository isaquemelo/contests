// 7**0 = 1        - 1
// 7**1 = 7        - 7
// 7**2 = 49       - 9
// 7**3 = 343      - 3
// 7**4 = 2401     - 1
// 7**5 = 16807    - 7
// 7**6 = 117649   - 9
// 7**7 = 823543   - 3
// 7**8 = 5764801  - 1

// O ciclo se repete a cada a cada 4 pulos...

// Então, temos a sequencia [ 1,7,9,3 ] (?).
// O expoente % 4 nos daria o index do valor esperado da exponenciação

#include <stdio.h>


int main (int args){
	unsigned long long n, cases;
	char sequence[] = { 1, 7, 9, 3 };

	scanf("%llu", &cases);

	while (cases--)
		scanf("%llu", &n), printf("%hhd\n", sequence[n % 4]);

	return  0;

}
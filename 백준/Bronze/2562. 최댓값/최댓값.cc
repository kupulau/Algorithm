#include <stdio.h>

int main() {
	int max, max_id;
	max = 0;
	for (int i=1; i<10; i++) {
	int n;
	scanf("%d", &n);
	if (n > max) {
	max = n;
	max_id = i;}
	}
	printf("%d\n", max);
	printf("%d\n", max_id);
	return 0;
}
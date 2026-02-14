#include <stdio.h>

int main() {
	int total, n;
	scanf("%d", &total);
	scanf("%d", &n);
	int sum = 0;
	for (int i=0; i < n; i++) {
	int a, b;
	scanf("%d %d", &a, &b);
	sum = sum + a*b;
	}
	if (total == sum) {
	printf("Yes");}
	else {
	printf("No");}	
	return 0;
} 
#include <stdio.h>

int main() {
	int n;
	scanf("%d", &n);
	int arr[n];
	for (int i=0; i < n; i++) {
	scanf("%d",&arr[i]);}
	int v, cnt;
	scanf("%d", &v);
	cnt = 0;
	for (int i=0; i < n; i++) {
	if (arr[i]==v) {
	cnt = cnt+1;}
	}
	printf("%d", cnt);
	return 0;
} 
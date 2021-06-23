/*
Write a program in C to find the sum of all elements of the array
*/


#include <stdio.h>

int main(){
    int n;
    int i;
    printf("Enter the length of the array: ");
    scanf("%d", &n);
    int arr[n];
    printf("Enter the array elements: ");
    for(i=0; i<n; i++){
        scanf("%d", &arr[i]);
    }
    int sum = 0;
    for(i=0; i<n;i++){
        sum = sum + arr[i];
    }
    printf("The sum of array is %d", sum);
    return 0;
}
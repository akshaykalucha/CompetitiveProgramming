/*Write a program in C to find the maximum and minimum element in an array*/

#include <stdio.h>

int main(){
    int n;
    printf("Enter the number of elements in array: ");
    scanf("%d", &n);
    int arr[n];
    int i;
    for(i=0; i<n; i++){
        printf("Enter the elements of array: ");
        scanf("%d", &arr[i]);
    }
    int max=0;
    int min=999999999;
    for(i=0; i<n; i++){
        if(arr[i] > max)
            max = arr[i];
        if(arr[i] < min)
            min = arr[i];
    }
    printf("the maximum element is %d and minimum element is %d", max, min);
    return 0;
}
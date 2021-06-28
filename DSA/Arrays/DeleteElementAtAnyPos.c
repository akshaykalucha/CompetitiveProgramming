/*Write a program in C to delete an element at desired position from an array*/
#include <stdio.h>

int main()
{
    int i, j, n, pos;
    printf("Enter the number of elements in array: ");
    scanf("%d", &n);
    int arr[n];
    printf("Enter the array elements: ");
    for(i=0; i<n; i++){
        scanf("%d", &arr[i]);
    }
    int narr[n-1];
    printf("Enter the element position to be deleted: ");
    scanf("%d", &pos);
    for(i=0; i<pos; i++){
        narr[i] = arr[i];
    }
    for(i=pos; i<n-1; i++){
        narr[i] = arr[i+1];
    }
    
    for(i=0; i<n-1; i++){
        printf("%d ", narr[i]);
    }
    
    return 0;
}

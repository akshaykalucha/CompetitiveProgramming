/*

Write a program in C to copy the elements of one array into another array
Input the number of elements to be stored in the array :3
Input 3 elements in the array :
element - 0 : 15
element - 1 : 10
element - 2 : 12
Expected Output :
The elements stored in the first array are :
15 10 12
The elements copied into the second array are :
15 10 12
*/

#include <stdio.h>

int main(){
    
    int n;
    printf("Enter the number of elements in array: ");
    scanf("%d", &n);
    int arr[n];
    printf("Enter the array elements: ");
    int i;
    for(i = 0; i<n; i++){
        scanf("%d", &arr[i]);
    }
    
    int newArr[n];
    for(i=0; i<n; i++){
        newArr[i] = arr[i];
    }
    
    printf("the old array is: ");
    for(i=0; i<n; i++){
        printf("%d ", arr[i]);
    }
    
    printf("\nthe new array is: ");
    for(i=0; i<n; i++){
        printf("%d ", newArr[i]);
    }
    
    return 0;
}
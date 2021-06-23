/*
Write a program in C to print all unique elements in an array
Input the number of elements to be stored in the array: 4
Input 4 elements in the array :
element - 0 : 3
element - 1 : 2
element - 2 : 2
element - 3 : 5
Expected Output :
The unique elements found in the array are:
3 5
*/
#include <stdio.h>
int main(){
    int n;
    printf("Enter the length of array: ");
    scanf("%d", &n);
    int arr[n];
    printf("Enter the array elements: ");
    int i;
    for(i=0; i<n; i++){
        scanf("%d", &arr[i]);
    }
    for(i=0; i<n; i++){
        int curr = arr[i];
        int found = 0;
        for(int j=i+1; j<n; j++){ // checking from i to n
            if(arr[i] == arr[j]){
                found = 1;
            }
        }
        for(int j = 0; j<i; j++){ // checking from 0 to i
            if(arr[i] == arr[j]){
                found = 1;
            }
        }
        if(found==0){
            printf("%d ", arr[i]);
        }
    }
    
    return 0;
}
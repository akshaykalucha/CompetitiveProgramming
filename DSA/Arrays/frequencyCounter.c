/*
Write a program in C to count a total number of duplicate elements in an array

Input the number of elements to be stored in the array :3
Input 3 elements in the array :
element - 0 : 5
element - 1 : 1
element - 2 : 1
Expected Output :
Total number of duplicate elements found in the array is : 1
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
    int fr[n];
    int visited = -1;
    for(i=0; i<n; i++){
        int count = 1;
        for(int j=i+1; j<n; j++){
            if(arr[i]==arr[j]){
                count++;
                fr[j] = visited;
            }
        }
        if(fr[i] != visited){
            fr[i] = count;
        }
    }
    
    for(i=0; i<n; i++){
        if(fr[i] != visited){
            printf("\nthe element is %d and its frequency is %d", arr[i], fr[i]);
        }
    }
    return 0;
}
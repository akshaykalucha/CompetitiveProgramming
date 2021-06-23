/*

Check if a key is present in every segment of size k in an array
Given an array arr[] and size of array is n and one another key x, and give you a segment size k. The task is to find that the key x present in every segment of size k in arr[].
Examples: 
    Input : 
    arr[] = { 3, 5, 2, 4, 9, 3, 1, 7, 3, 11, 12, 3} 
    x = 3 
    k = 3 
    Output : Yes 
    There are 4 non-overlapping segments of size k in the array, {3, 5, 2}, {4, 9, 3}, {1, 7, 3} and {11, 12, 3}. 3 is present all segments.
    Input : 
    arr[] = { 21, 23, 56, 65, 34, 54, 76, 32, 23, 45, 21, 23, 25} 
    x = 23 
    k = 5 
    Output :Yes 
    There are three segments and last segment is not full {21, 23, 56, 65, 34}, {54, 76, 32, 23, 45} and {21, 23, 25}. 
    23 is present all window.
    Input :arr[] = { 5, 8, 7, 12, 14, 3, 9} 
    x = 8 
    k = 2 
    Output : No


*/


#include <stdio.h>
int findingElement(int arr[], int k, int x, int n){
    //incrementing i by k to slide in segments and traversing in segment
    int i = 0;
    for(i=0; i<n; i=i+k){
        int j;
        for(j=0; j<k; j++){
            if(arr[i+j] == x){
                break;
            }
        }
        if(j == k){
            return 0;
        }
    }
    //if i is a multiple of n
    if(i == n){
        return 1;
    }
    
    //checking the final segment
    int j;
    for(j=i-k; j<n; j++){
        if(arr[j] == x){
            break;
        }
    }
    if(j == n){
        return 0;
    }
    return 1;
}

int main(){
    int arr[5] = {3,3,3,3,3};
    int x = 3;
    int k = 3;
    int n = 5;
    if(findingElement(arr, k, x, n) == 1){
        printf("Yes");
    }
    else{
        printf("No");
    }
    return 0;
}
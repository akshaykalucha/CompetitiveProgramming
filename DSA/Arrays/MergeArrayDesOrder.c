/*

Write a program in C to merge two arrays of same size sorted in decending order

Input the number of elements to be stored in the first array :3
Input 3 elements in the array :
element - 0 : 1
element - 1 : 2
element - 2 : 3
Input the number of elements to be stored in the second array :3
Input 3 elements in the array :
element - 0 : 1
element - 1 : 2
element - 2 : 3
Expected Output :
The merged array in decending order is :
3 3 2 2 1 1

*/
#include <stdio.h>

int main(){
    int n = 5;
    int arr[5] = {122,2,3,4,5};
    int brr[5] = {6,7,8,9,0};
    int crr[10] = {0};
    int i;
    // merging the two arrays in a new array
    for(i=0; i<10; i++){
        if(i >= 5){
            crr[i] = brr[i-5];
        }
        else{
            crr[i] = arr[i];
        }
    }
    
    //sorting the new array
    int k, j;
    for(i=0;i<10; i++){
       for(k=0;k<10-1;k++){
            if(crr[k]<=crr[k+1]){
               j=crr[k+1];
               crr[k+1]=crr[k];
               crr[k]=j;
            }  
        }
    }
    for(i=0; i<10; i++){
        printf("%d ", crr[i]);
    }
    return 0;
}
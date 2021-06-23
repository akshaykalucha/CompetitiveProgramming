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
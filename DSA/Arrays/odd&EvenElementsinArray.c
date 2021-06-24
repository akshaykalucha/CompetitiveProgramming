/* Write a program in C to separate odd and even integers in separate arrays */

#include <stdio.h>

int main(){
    int n, i, j;
    printf("Enter the number of elements in array: ");
    scanf("%d", &n);
    int arr[n];
    for(i=0; i<n; i++){
        printf("Enter the array elements: ");
        scanf("%d", &arr[i]);
    }
    int Earr[100] = {0};
    int oddArr[100] = {0};
    int odd = 0;
    int even = 0;
    for(i=0; i<n; i++){
        if(arr[i] % 2 == 0){
            even++;
            for(j=0; j<n; j++){
                if(Earr[j] == 0){
                    Earr[j] = arr[i];
                    break;
                }
            }
        }else{
            odd++;
            for(j=0; j<n; j++){
                if(oddArr[j] == 0){
                    oddArr[j] = arr[i];
                    break;
                }
            }
        }
    }
    printf("The even elements are: ");
    for(i=0; i<even; i++){
        if(Earr[i] != 0){
            printf("%d ", Earr[i]);
        }
    }
    printf("\nThe even elements are: ");
    for(i=0; i<odd; i++){
        if(oddArr[i] != 0){
            printf("%d ", oddArr[i]);
        }
    }
    return 0;
}
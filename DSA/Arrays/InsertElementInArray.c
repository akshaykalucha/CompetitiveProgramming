/*Write a program in C to insert New value in the array*/
#include <stdio.h>

int main()
{
    int i, j, n, el, pos;
    printf("Enter the number of elements in array: ");
    scanf("%d", &n);
    int arr[n];
    printf("Enter the array elements: ");
    for(i=0; i<n; i++){
        scanf("%d", &arr[i]);
    }
    int narr[n+1];
    printf("Enter the element to be inserted: ");
    scanf("%d", &el);
    printf("Enter the position to be inserted: ");
    scanf("%d", &pos);
    
    for(i=0; i<=pos; i++){
        if(i == pos){
            narr[i] = el;
        }else{
            narr[i] = arr[i];
        }
    }
    
    for(i=pos+1; i<=n+1; i++){
        narr[i] = arr[i-1];
    }
    
    for(i=0; i<n+1; i++){
        printf("%d ", narr[i]);
    }
    
    return 0;
}

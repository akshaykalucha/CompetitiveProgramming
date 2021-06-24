/* Write a prohram that reads a 5x5 array from input and prints the row sum and column sum respectiely */

#include <stdio.h>

int main(){
    int n = 5;
    int arr[5][5] = {
        {8,3,9,0,10},
        {3,5,17,1,1},
        {2,8,6,23,1},
        {15,7,3,2,9},
        {6,14,2,6,0}
    };
    int i,j;
    int row[5];
    int col[5];
    for(i=0; i<5; i++){
        int rsum = 0;
        int csum = 0;
        for(j=0; j<5; j++){
            rsum += arr[i][j];
            csum += arr[j][i];
        }
        row[i] = rsum;
        col[i] = csum;
    }
    printf("The sum of rows is: ");
    for(i=0; i<5; i++){
        printf("%d ", row[i]);
    }
    printf("\nThe sum of columns is: ");
    for(i=0; i<5; i++){
        printf("%d ", col[i]);
    }
    return 0;
}
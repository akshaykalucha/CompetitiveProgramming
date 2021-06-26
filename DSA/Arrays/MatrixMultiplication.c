#include<stdio.h>
#include "malloc.h"

int main()
{
    int m, n, z, p, i, j, k;
    int sum = 0;
    printf("Enter the rows and column of 1st matrix: ");
    scanf("%d %d", &m, &n);
    int a[m][n];
    printf("Enter the elements of matrix A\n");
    for(i=0; i<m; i++){
        for(j=0; j<n; j++){
            scanf("%d", &a[i][j]);
        }
    }
    printf("\nYour FIRST matrix is: \n\n");
    for(i=0; i<m; i++){
        for(j=0; j<n; j++){
            printf("%d ", a[i][j]);
        }
        printf("\n");
    }
    
    printf("Enter the rows and column of 2nd matrix: ");
    scanf("%d %d", &z, &p);
    if(n != z){
        printf("Sorry matrix not compatible, columns of first matrix should be equal to rows of 2nd");
            return 0;
    }
    int b[m][n];
    printf("Enter the elements of matrix B\n");
    for(i=0; i<z; i++){
        for(j=0; j<p; j++){
            scanf("%d", &b[i][j]);
        }
    }
    
    printf("\nYour SECOND matrix is: \n\n");
    for(i=0; i<z; i++){
        for(j=0; j<p; j++){
            printf("%d ", b[i][j]);
        }
        printf("\n");
    }
    
    // multiplying both the matrices
    
    int prod[m][p];
    for(i=0; i<m; i++){
        for(j=0; j<p; j++){
            for(k=0; k<z; k++){
                sum += a[i][k] * b[k][j];
            }
            prod[i][j] = sum;
            sum = 0;
        }
    }
    
    // printing the product matrix
    printf("\n\nYour product matrix is :\n");
    for(i=0; i<m; i++){
        for(j=0; j<p; j++){
            printf("%d ", prod[i][j]);
        }
        printf("\n");
    }
}
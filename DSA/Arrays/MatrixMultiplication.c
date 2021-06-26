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

/* python adaptation: 
m, n = map(int, input("Enter rows and columns of FIRST matrix: ").split())
arr = []
for i in range(m):
    zz = list(map(int, input("Enter the values in row no {} matrix: ".format(i)).split()))
    arr.append(zz)
print("\n\nYour first matrix is: ")
for i in range(m):
    print(*arr[i])

z, p = map(int, input("Enter rows and columns of SECOND matrix: ").split())
if n != z:
    print("Sorry matrices are not compatible to multiply")
brr = []
for i in range(z):
    zz = list(map(int, input("Enter the values in row no {} matrix: ".format(i)).split()))
    brr.append(zz)
print("\n\nYour SECOND matrix is: ")
for i in range(z):
    print(*brr[i])

# multiplying the two matrix

prod = []
for i in range(m):
    prodmax = []
    sum = 0
    for j in range(p):
        for k in range(z):
            sum += arr[i][k] * brr[k][j]
        prodmax.append(sum)
        sum = 0
    prod.append(prodmax)
    

# printing the product matrux
print("\n\nYour product matrix is: ")
for i in range(m):
    print(*prod[i])
*/
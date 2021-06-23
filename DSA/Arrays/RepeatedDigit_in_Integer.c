/*

Write a program to check whether there are any digits repeting more than once in an integer

Example:
    input: 233
    output: Yes
    input: 1234
    output: no

*/


#include <stdio.h>

int main(){
    int seen[10] = {0};
    int n;
    printf("Enter the number to check: ");
    scanf("%d", &n);
    int found = 0;
    while(n > 0){
        int rem = n % 10;
        if(seen[rem] == 1){
            found = 1;
            break;
        }
        else{
            seen[rem] = 1;
        }
        
        n = n / 10;
    }
    
    if(found == 1){
        printf("Yes there is a repeated integer");
    }
    else{
        printf("NO, no repeated integer found");
    }
    return 0;
}
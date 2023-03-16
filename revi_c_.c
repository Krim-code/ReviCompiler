#include <stdio.h>

int test(int n){
   if(n < 2) {
      return 1;
   }
    return test(n-1) + test(n-2);
    }
int main(void) {
    int x = test(40);
    printf("%d \n", x);

    return 0;
}
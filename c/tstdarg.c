#include <stdarg.h>
#include <stdio.h>

int sum(int, int[], ...);

int main(){
  int array[] = {1,4,7,12,34};
  printf("%d\n", sum(3,array,2,3,5));
  return 0;
}

int sum(int n, int array[],...){
  int sum = 0;
  va_list vaArgs;
  va_start(vaArgs, array);
  while(n--) {
    int i = va_arg(vaArgs, int);
    sum += array[--i];
  }
  va_end(vaArgs);
  return sum;
}

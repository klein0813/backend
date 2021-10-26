#include<stdio.h>

int f(int);

int main(){
  printf("%d", f(5));
  return 0;
}

int f(int n) {
  if(n == 1){
    return 1;}
  else if(n == 2){
    return 2;}
  else {
    return f(n - 1) + f(n - 2);
  }
}

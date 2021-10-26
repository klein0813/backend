#include <iostream>
using namespace std;

int binarySearchRecursion(int[], int, int, int);

int main(){
  int array[] = {12, 34, 56, 134, 588};
  int result = binarySearchRecursion(array, 0, 4, 134); 
  cout<<result<<endl;
  return 0;
}

int binarySearchRecursion(int array[], int min, int max, int match) {
  if (min > max) {
    return -1;
  } 
  int mid = min + (max - min) / 2;
  if (array[mid] == match) {
    return mid;
  }
  else if (array[mid] > match) {
    max = mid -1;
  }
  else {
    min = mid + 1;
  }
  return binarySearchRecursion(array, min, max, match);   
}

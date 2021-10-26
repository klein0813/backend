#include<iostream>
#include<cstdarg>
using namespace std;

struct indexTableD {
  int value;
  int indexT;
};

int sequenceSearch(int [],int,int);
int binarySearch(int[],int,int);
int binaryRecursionSearch(int a[], int min, int max, int key);
int* indexSearch(int[],indexTableD[],int,int,...);

int main(){
  int array[] = {1,4,8,10};
  int index = sequenceSearch(array, 4, 5);
  int result = binarySearch(array, 4, 8);

  int array1[] = {11, 14, 19};
  int array2[] = {22,32,45,64,90};
  indexTableD itd;
  itd.value = 10;
  itd.indexT = 4;
  indexTableD itd1;
  itd1.value = 19;
  itd1.indexT = 3;
  indexTableD itd2;
  itd2.value = 90;
  itd2.indexT = 5;

  indexTableD itds[] = {itd, itd1, itd2};
  int result2[] = {0,0};
  cout<<"binaryRecursionSearch:"<<binaryRecursionSearch(array,0, 3, 4)<<endl;
  indexSearch(result2,itds, 64, 3, array, array1, array2);
  cout<<"sequenceSearch"<<index<<endl;
  cout<<"binarySearch:"<<result<<endl;
  cout<<"indexSearch:"<<result2[0]<<"  "<<result2[1]<<endl;
  return 0;
}

int sequenceSearch(int array[], int n, int key){
  for (int i = 0; i < n; i++){
    if (array[i] == key) {
      return i;
    } 
  }
  return -1;
}

int binarySearch(int array[], int n, int key){
  int min = 0;
  int max = n-1;
  while(min != max){
    int mid = min + (max - min)/2;
    int temp = array[mid];
    if(key == temp)
      return mid;
    else if(key > temp){
      min = mid+1;
    }
    else {
      max = mid-1;
    }
  }
  return -1;
}

int binaryRecursionSearch(int* a, int min, int max, int key){
  if(min > max)
    return -1;
  int mid = min + (max - min) / 2;
  cout<<*(a+mid)<<" "<<endl;
  if(*(a+mid) == key)
    return mid;
  else if(*(a+mid) > key)
    return binaryRecursionSearch(a, min, mid - 1, key);
  else
    return binaryRecursionSearch(a, mid + 1, max, key);
}

int* indexSearch(int result[], indexTableD itds[], int key, int n, ...){
  va_list pArgs;
  va_start(pArgs, n);
  for(int i = 0; i < n; i++){
    int* a = va_arg(pArgs, int*);
    if(itds[i].value == key){
      result[0] = i + 1;
      result[1] = itds[i].indexT;
      break;
    }
    else if(itds[i].value > key){
      result[1] = binaryRecursionSearch(a, 0, itds[i].indexT - 1, key) + 1;
      if(result[1] > 0) {
        result[0] = i + 1;
        break;
      }
    }
  }
  va_end(pArgs);
  return result;
}

#include <iostream>



void quickSort(int *data, int start, int end){
  if(start >= end){
    return;
  }
  int pivot = start;
  


}

int main(int argc, char const *argv[])
{
  int data[10] = {4, 1, 2, 3, 9, 7, 8, 6, 10, 5};
  quickSort(data, 0, sizeof(data) / sizeof(data[0]));
  return 0;
}

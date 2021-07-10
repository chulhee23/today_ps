#include <stdio.h>
#include <iostream>
using namespace std;

int main(void)
{
  int n;
  scanf("%d", &n);
  // cin >> n;

  int arr[100][100];

  for(int i = 0; i < n; i++){
    for(int j = 0; j<n; j++){
      // cin >> arr[i][j];
      scanf("%d", &arr[i][j]);
    }
  }


  for(int k = 0; k < n; k++){
    for(int i = 0; i < n; i++){
      for(int j = 0; j < n; j++){
        if(arr[i][k] == 1 && arr[k][j] == 1){
          arr[i][j] = 1;
        }
      }
    }
  }

  for(int i = 0; i < n; i++){
    for(int j = 0; j < n; j++){
      printf("%d ", arr[i][j]);
    }
    printf("\n");
  }


   

  return 0;
}


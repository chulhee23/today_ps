#include <iostream>

using namespace std;
int arr[26][2];

void preorder(int n){
  if(n == -1) return;
  cout << char(n + 'A');
  preorder(arr[n][0]);
  preorder(arr[n][1]);
}
void inorder(int n){
  if(n == -1) return;
  inorder(arr[n][0]);
  cout << char(n + 'A');
  inorder(arr[n][1]);
}
void postorder(int n){
  if(n == -1) return;
  postorder(arr[n][0]);
  postorder(arr[n][1]);
  cout << char(n + 'A');
}

int main(int argc, char const *argv[])
{
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);
  cout.tie(NULL);

  int N;
  cin >> N;
  for(int i = 0; i < N; i++){
    char root, left, right;
    cin >> root >> left >> right;
    arr[root-'A'][0] = left != '.' ? left - 'A' : -1;
    arr[root-'A'][1] = right != '.' ? right - 'A' : -1;

  }
  preorder(0);
  cout << endl;
  inorder(0);
  cout << endl;
  postorder(0);

  return 0;
}

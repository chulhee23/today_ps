#include <string.h>
#include <stdio.h>
#include <iostream>
#include <algorithm>
#include <vector>
#define LEN_MAX 10
using namespace std;


struct Trie{
  bool finish;
  bool nextChild;
  Trie *next[LEN_MAX];

  Trie() {
    finish = false;
    nextChild = false;
    fill(next, next+ LEN_MAX, nullptr);
  }

  ~Trie(){
    for(int i = 0; i < 10; i++){
      if (next[i])
        delete next[i];
    }
  }
  
  void insert(const char *key){
    if(*key == '\0'){
      finish = true;
    } else {
      int curr = *key - '0';
      if(next[curr] == NULL){
        next[curr] = new Trie();       
      }
      nextChild = true;
      next[curr] -> insert(key + 1);
    }
  }

  bool find(char *key){
    if (*key == '\0')
      return 0;
    if (finish)
      return 1;
    int now = *key - '0';
    return next[now] -> find(key + 1);
  }

};



int t;
int n;
char arr[10001][11];

void init();
void solve();


int main(int argc, char const *argv[])
{
  scanf("%d", &t);
  for (int i = 0; i < t; i++)
  {
    // memset(arr, 0, sizeof(arr)); <- 메모리 초과 발생
    init();
    solve();    
  }

  return 0;
}

void init()
{
  scanf("%d", &n);
  for (int i = 0; i < n; i++)
  {
    scanf("%s", &arr[i]);
  }
}

void solve(){
  Trie *root = new Trie();
  for(int i = 0; i < n; i++){
    root->insert(arr[i]);
  }
  
  bool tmp = false;
  for (int i = 0; i < n; i++) {
    if (root->find(arr[i]))
      tmp = true;
  }
  tmp ? cout << "NO\n" : cout << "YES\n";
  delete root;
  
}
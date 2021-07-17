#include <iostream>
#include <stdio.h>
#include <vector>
#include <algorithm>
#include <queue>

using namespace std;


int parent[100001];
bool visited[100001];
vector<vector<int>> v;

int main(int argc, char const *argv[])
{
  int n;
  scanf("%d", &n);
  v.resize(n+1);

  for(int i = 0; i < n-1; i++){
    int x, y;
    scanf("%d %d", &x, &y);
    v[x].push_back(y);
    v[y].push_back(x);
  }

  queue<int> q;
  q.push(1);
  visited[1] = true;

  while(!q.empty()){
    int x = q.front();
    q.pop();

    for(int nx: v[x]){
      if(!visited[nx]){
        parent[nx] = x;
        visited[nx] = true;
        q.push(nx);
      }
    }
  }

  for(int i = 2; i <= n; i++){
    printf("%d\n", parent[i]);
  }

  return 0;
}



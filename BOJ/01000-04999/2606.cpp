#include <stdio.h>
#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;


bool visited[101] = {false};
vector<vector<int> > map;
int computer_num, ans = 0;

void dfs(int x){
  ans++;
  visited[x] = true;
  for(int i = 0; i < map[x].size(); i++){
    if(!visited[map[x][i]]){
      dfs(map[x][i]);
    }
  }
}

int main(void)
{
  int n, from, to;
  scanf("%d %d", &computer_num, &n);
  map.resize(computer_num + 1);

  for (int i = 0; i < n; i++)
  {
    scanf("%d %d", &from, &to);
    map[from].push_back(to);
    map[to].push_back(from);
  }
  
  dfs(1);

  printf("%d", ans - 1);

  return 0;
}


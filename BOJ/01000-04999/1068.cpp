#include <iostream>
#include <vector>
#include <queue>

using namespace std;


int main(int argc, char const *argv[])
{

  int N;
  scanf("%d", &N);
  vector<vector<int>> list;
  list.resize(51);
  
  int root;
  for(int i = 0; i < N; i++){
    int tmp;
    scanf("%d", &tmp);
    if(tmp == -1){
      root = i;
    } else {
      list[tmp].push_back(i);
    }
  }

  int remove;
  scanf("%d", &remove);

  list[remove].clear();
  queue<int> q;
  q.push(root);
  int count = 0;
  if (root != remove){
    while(!q.empty()){
      int item = q.front();
      q.pop();
      
      if(list[item].size() == 0){
        count++;
      } else {
        for (auto nn = list[item].begin(); nn != list[item].end(); nn++){
          if ((*nn) == remove)
          {
            if(list[item].size() == 1) count++;
            continue;
          }
          q.push(*nn);
        }
      }
    }
  }

  printf("%d", count);

  return 0;
}
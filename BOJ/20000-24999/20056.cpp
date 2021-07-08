#include <iostream>
#include <stdio.h>
#include <vector>
#include <algorithm>

using namespace std;

const int MAX = 51;

struct Fireball{
  int x, y;
  int m;
  int s;
  int d;
};

int dx[] = { -1, -1, 0, 1, 1, 1, 0, -1 };
int dy[] = { 0, 1, 1, 1, 0, -1, -1, -1 };

int n, m, k;
vector<Fireball> map[MAX][MAX];
vector<Fireball> fireball;

void init(){
  cin >> n >> m >> k;
  // scanf("%d %d %d", n, m, k);
  for(int i = 0; i < m; i++){
    int tr, tc, tm, ts, td;
    cin >> tr >> tc >> tm >> ts >> td;
    // scanf("%d %d %d %d %d", tr, tc, tm, ts, td);
    fireball.push_back({tr, tc, tm, ts, td});
    map[tr][tc].push_back({tr, tc, tm, ts, td});
  }
}

void move(){
  // 움직일 때마다 초기화
  for(int i = 1; i <= n; i++){
    for(int j = 1; j <= n; j++){
      map[i][j].clear();
    }
  }
  for(int i = 0; i < fireball.size(); i++){
    int cx = fireball[i].x;
    int cy = fireball[i].y;
    int cm = fireball[i].m;
    int cs = fireball[i].s;
    int cd = fireball[i].d;

    int move = cs % n;
    int nx = (cx - 1 + dx[cd] * move + n) % n + 1;
    int ny = (cy - 1 + dy[cd] * move + n) % n + 1;
    // int nx = cx + dx[cd] * move;
    // int ny = cy + dy[cd] * move;
    // if (nx > n) nx -= n;
    // if (ny > n) ny -= n;
    // if (nx < 1) nx += n;
    // if (ny < 1) ny += n;

    map[nx][ny].push_back({nx, ny, cm, cs, cd});
    fireball[i].x = nx;
    fireball[i].y = ny;
  }
}

void sum(){
  vector<Fireball> tmp;
  for(int i = 1; i <= n; i++){
    for(int j = 1; j <= n; j++){
      if (map[i][j].size() == 0)
        continue;
      if (map[i][j].size() == 1){
        tmp.push_back(map[i][j][0]);
        continue;
      }

      // 2 이상
      int mSum = 0;
      int vSum = 0;
      bool odd = true;
      bool even = true;
      for(int k = 0; k < map[i][j].size(); k++){
        mSum += map[i][j][k].m;
        vSum += map[i][j][k].s;
        if(map[i][j][k].d % 2 == 0){
          odd = false;
        } else {
          even = false;
        }
      }
      int nm = mSum / 5;
      int ns = vSum / map[i][j].size();

      if(nm  == 0){
        continue;
      }

      if(even == true || odd == true){
        for(int k = 0; k < 4; k++){
          tmp.push_back({i, j, nm, ns, k * 2});
        }
      } else {
        for(int k = 1; k <= 4; k++){
          tmp.push_back({i, j, nm, ns, k * 2 - 1});
        }
      }

    }
  }
  fireball = tmp;
}

void solution(){
  for(int i = 0; i < k; i++){
    move();
    sum();
  }
  
  // 최종 fireball 질량 합 
  int ans = 0;
  for(int i = 0; i < fireball.size(); i++ ){
    ans +=fireball[i].m;
  }

  printf("%d", ans);
}

int main(void)
{
  init();
  solution();
  return 0;
}

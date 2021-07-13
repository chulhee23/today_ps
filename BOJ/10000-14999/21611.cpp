#include <iostream>
#include <vector>
using namespace std;


int arr[50][50];
int dx[5] = {0, -1, 1, 0, 0};
int dy[5] = {0, 0, 0, -1, 1};

vector<pair<int, int>> bomb;
int first = 0;
int second = 0;
int third = 0;

void remove(int, int);
bool destroy(void);
void arrange(void);

int n, m;

int main(int argc, char const *argv[])
{
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);
  cout.tie(NULL);
  

  cin >> n >> m;
  for(int i = 0; i < n; i++){
    for(int j = 0; j < n; j++){
      cin >> arr[i][j];
    }
  }
  arr[n/2][n/2] = -1;

  for(int i = 0; i < m; i++){
    int d, s;
    cin >> d >> s;
    bomb.push_back({d, s});
  }
  

  for(int i = 0; i < m; i++){
    remove(bomb[i].first, bomb[i].second);
    bomb.erase(bomb.begin());

    bool destroyed = true;
    while(destroyed){
      // 정렬
      arrange();
      // 파괴
      destroyed = destroy();
    }
  }

  return 0;
}

void remove(int d, int s){
  int cx = n / 2;
  int cy = n / 2;
  for(int i = 1; i <= s; i++){
    cx += dx[d];
    cy += dy[d];
    arr[cx][cy] = 0;
  }
}

// 빈칸 메꾸기
void arrange(){
  // 좌 3 하 2 우 4 상 1
  int changeDir = 0;
  int cx = n / 2;
  int cy = n / 2;
  int cdx[] = {0, 1, 0, -1};
  int cdy[] = {-1, 0, 1, 0};
  int count = 2;
  while(cx == 0 && cy == 0){
    if(count == 2){
      count = 0;
      changeDir = (changeDir + 1) % 4;
    }
    int ctmp = count;
    for (int i = 0; i < ctmp - 1; i++)
    {
      if (arr[cx][cy] == 0){

      }
      cx += cdx[changeDir];
      cy += cdy[changeDir];

      count++;
    }
    
  }


}

// 4개 모이면 파괴
bool destroy(){

}

#include <iostream>
#include <stdio.h>
#include <string>
#include <algorithm>

using namespace std;

int main()
{

  int dx[4] = {0, 1, 0, -1};
  int dy[4] = {-1, 0, 1, 0};
  int d = 0;
  int n;

  // scanf("%d ", &n);
  cin >> n;
  int answers[n];
  
  for(int i = 0; i < n; i++){
    string str;
    cin >> str;
    int cx = 0, cy = 0, cd = 0;
    int minX = 0, maxX = 0, minY = 0, maxY = 0;
    for(int j = 0; j < str.size(); j++){
      char c = str[j];
      if (c == 'L' || c == 'R'){
        if (c == 'L')
          cd = (cd + 3) % 4;
        else
          cd = (cd + 1) % 4;
      } else {
        if (c == 'F')
        {
          cx += dx[cd];
          cy += dy[cd];
        }
        else
        {
          cx -= dx[cd];
          cy -= dy[cd];
        }
        maxX = max(cx, maxX);
        maxY = max(cy, maxY);
        minX = min(cx, minX);
        minY = min(cy, minY);
      }
    }
    int ans = (maxX - minX) * (maxY - minY);
    answers[i] = ans;
  }

  for(int i = 0; i < n; i++){
    printf("%d \n", answers[i]);
  }

  return 0;
}

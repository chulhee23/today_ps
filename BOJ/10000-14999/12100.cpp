
#include <iostream>

#include <queue>

using namespace std;

const int MAX = 20;

int N;

int board[MAX][MAX];

int maxBlock;

void shift(int type)
{
  queue<int> q;
  //숫자들을 큐에 집어놓고 각 행의
  //해당방향 끝에서부터 숫자를 넣기 시작
  switch (type)
  {
    //왼쪽
  case 0:
    for (int i = 0; i < N; i++)
    {
      for (int j = 0; j < N; j++)
      {
        if (board[i][j])
          q.push(board[i][j]);
        board[i][j] = 0;
      }
      int idx = 0;
      while (!q.empty())
      {
        int data = q.front();
        q.pop();
        if (board[i][idx] == 0)
          board[i][idx] = data;
        else if (board[i][idx] == data)
        {
          board[i][idx] *= 2;
          //시중에 나와있는 게임과 달리 여러번 합쳐지지 않는다
          idx++;
        }
        else
        {
          idx++;
          board[i][idx] = data;
        }
      }
    }
    break;
    //오른쪽
  case 1:
    for (int i = 0; i < N; i++)
    {
      for (int j = N - 1; j >= 0; j--)
      {
        if (board[i][j])
          q.push(board[i][j]);
        board[i][j] = 0;
      }
      int idx = N - 1;
      while (!q.empty())
      {
        int data = q.front();
        q.pop();
        if (board[i][idx] == 0)
          board[i][idx] = data;
        else if (board[i][idx] == data)
        {
          board[i][idx] *= 2;
          idx--;
        }
        else
        {
          idx--;
          board[i][idx] = data;
        }
      }
    }
    break;

    //위쪽
  case 2:
    for (int i = 0; i < N; i++)
    {
      for (int j = 0; j < N; j++)
      {
        if (board[j][i])
          q.push(board[j][i]);
        board[j][i] = 0;
      }
      int idx = 0;
      while (!q.empty())
      {
        int data = q.front();
        q.pop();
        if (board[idx][i] == 0)
          board[idx][i] = data;
        else if (board[idx][i] == data)
        {
          board[idx][i] *= 2;
          idx++;
        }
        else
        {
          idx++;
          board[idx][i] = data;
        }
      }
    }

    break;
    //아래쪽
  case 3:
    for (int i = 0; i < N; i++)
    {
      for (int j = N - 1; j >= 0; j--)

      {

        if (board[j][i])

          q.push(board[j][i]);

        board[j][i] = 0;
      }

      int idx = N - 1;

      while (!q.empty())

      {

        int data = q.front();

        q.pop();

        if (board[idx][i] == 0)

          board[idx][i] = data;

        else if (board[idx][i] == data)

        {

          board[idx][i] *= 2;

          idx--;
        }

        else

        {

          idx--;

          board[idx][i] = data;
        }
      }
    }

    break;
  }
}

void DFS(int cnt)
{
  if (cnt == 5)
  {
    for (int i = 0; i < N; i++)
      for (int j = 0; j < N; j++)
        maxBlock = max(maxBlock, board[i][j]);
    return;
  }
  int copyBoard[MAX][MAX];
  //현 보드상태 저장해놓고
  for (int i = 0; i < N; i++)
    for (int j = 0; j < N; j++)
      copyBoard[i][j] = board[i][j];
  for (int i = 0; i < 4; i++)
  {
    shift(i);
    DFS(cnt + 1);
    //저장해놓은 보드상태로 원상복구
    for (int i = 0; i < N; i++)
      for (int j = 0; j < N; j++)
        board[i][j] = copyBoard[i][j];
  }
}

int main(void)
{
  cin >> N;
  for (int i = 0; i < N; i++)
    for (int j = 0; j < N; j++)
      cin >> board[i][j];
  DFS(0);
  cout << maxBlock << endl;
  return 0;
}
#include <iostream>
using namespace std;

int main(void)
{
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);
  cout.tie(NULL);
  int T;
  cin >> T;
  while (T--)
  {
    int N, M;
    cin >> N >> M;
    for (int m_idx = 0; m_idx < M; m_idx++)
    {
      int a, b;
      cin >> a >> b;
    }
    cout << N - 1 << "\n";
  }
  return 0;
}

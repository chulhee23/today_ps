#include <iostream>
#include <string>

using namespace std;

const int MOD = 1234567891;
const int MULTIPLY = 31;

int main(void)
{
  int L;
  cin >> L;
  string s;
  cin >> s;
  long long sum = 0;
  long long R = 1;
  for (int i = 0; i < s.length(); i++)
  {
    sum = (sum + (s[i] - 'a' + 1) * R) % MOD;
    R = (R * MULTIPLY) % MOD;
  }
  
  cout << sum << "\n";
  return 0;
}

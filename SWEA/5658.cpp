#include <algorithm>
#include <iostream>
#include <vector>
using namespace std;
bool comp(int a, int b)
{
  return a > b;
}
int main(int argc, char **argv)
{
  vector<int> answers;
  int test_case;
  int T;
  cin >> T;
  
  for (test_case = 1; test_case <= T; ++test_case)
  {
    int n, k, d;
    string nums;
    cin >> n >> k;
    cin >> nums;
    d = n / 4;
    vector<int> result;
    for(int i = 0; i < d+1; i++){
      for(int j = 0; j < d+1; j++){
        int start = d * j;
        int end = d * (j + 1);

        string tmp = nums.substr(start, end);
        int a = strtol(tmp.c_str(), NULL, 16);

        result.push_back(a);
      }
      char ls = nums[n - 1];
      nums.erase(n - 1);
      nums.insert(0, ls);

    }
    sort(result.begin(), result.end());
    result.erase(unique(result.begin(), result.end()), result.end());
    sort(result.begin(), result.end(), comp);
    
    answers.push_back(result[k - 1]);
    
    for(auto it=result.begin(); it != result.end(); it++){
      cout << *it << " ";
    }
  }

  for(int i = 0; i < answers.size(); i++){
    cout << "#" << i+1 << " " << answers[i] << endl;
  }

  return 0;
}
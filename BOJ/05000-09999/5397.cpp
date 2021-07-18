#include <iostream>
#include <stdio.h>
#include <list>

using namespace std;


int main(int argc, char const *argv[])
{
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);
  cout.tie(NULL);

  int test_case;
  cin >> test_case;

  for(int i = 0; i < test_case; i++){
    string str;
    cin >> str;
    list<char> ans;
    auto cur = ans.begin(); // cursor 의 초기 위치
    for(int i = 0; i < str.length(); i++){
      if(str[i] == '<'){
        if(cur == ans.begin()) continue;
        cur--;
      }
      else if(str[i] == '>'){
        if(cur == ans.end()) continue;
        cur++;
      }
      else if(str[i] == '-'){
        if(cur == ans.begin()) continue;
        cur = ans.erase(--cur); // 삭제한 원소의 다음 원소를 가리킨다 
        
      }
      else {
        ans.insert(cur, str[i]);
      }

    }

    for(auto it = ans.begin(); it != ans.end(); it++){
      cout << *it;
    }
    cout << '\n';


  }
  return 0;
}

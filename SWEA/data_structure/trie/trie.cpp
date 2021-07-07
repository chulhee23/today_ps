#include <string.h>

using namespace std;

struct Trie{
  bool finish;
  Trie* next[26]; // alphabet 26

  Trie(): finish(false){
    memset(next, 0, sizeof(next));
  }

  ~Trie(){
    for(int i = 0; i < 26; i++){
      if(next[i])
        delete next[i];
    }
  }

  void insert(const char *key){
    if(*key == '\0')
      finish = true;
    else {
      int curr = *key - 'A';
      if (next[curr] == NULL)
        next[curr] = new Trie();
      next[curr]->insert(key + 1); // 다음 문자 삽입
    }
  }

  Trie* find(const char* key){
    if(*key == '\0') return this; // 문자열 끝나는 위치 반환
    int curr = *key - 'A';
    if(next[curr] == NULL) return NULL;
    return next[curr] -> find(key + 1);
  }
};

int main(int argc, char const *argv[])
{
  Trie *root = new Trie();
  char *c[5];
  c[0] = "ABC";
  c[1] = "ACD";
  c[2] = "BCD";
  c[3] = "BCE";
  c[4] = "ABCDE";
  for (int i = 0; i < 5; i++)
  {
    root -> insert(c[i]);
  }

  
  return 0;

}

#include <stdio.h>
#include <iostream>
#include <string.h>

using namespace std;

struct Trie{
  int child;
  bool finish;
  Trie *next[26];

  Trie() : finish(false)
  {
    memset(next, 0, sizeof(next));
  }

  ~Trie()
  {
    for (int i = 0; i < 26; i++)
    {
      if (next[i])
        delete next[i];
    }
  }

  void insert(const char *key)
  {
    child++;
    if (*key == '\0')
      finish = true;
    else
    {
      int curr = *key - 'a';
      if (next[curr] == NULL)
        next[curr] = new Trie();
      next[curr]->insert(key + 1); // 다음 문자 삽입
    }
  }

  int find(const char *key)
  {
    if (*key == '\0')
      return child;
    int curr = *key - 'a';
    if (next[curr] == NULL)
      return NULL;
    return next[curr]->find(key + 1);
  }
};



Trie trie;
void init(void)
{
  trie = Trie();
}

void insert(int buffer_size, char *buf)
{
  trie.insert(buf);
}

int query(int buffer_size, char *buf)
{
  return trie.find(buf);
  return 0;
}
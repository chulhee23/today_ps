// linked list 를 배열로 구현해도 된다.
// 삽입과 삭제 시 뒤에 데이터를 옮기는 작업을 하지 않아도 되도록 구현하면 된다.

/*
push_back(data)
push_front(data)
insert(post, data)
pop_back()
pop_front()
erase(pos)
*/
#include <stdio.h>
#include <algorithm>
#include <list>
#include <iostream>

using namespace std;

struct Node {
  int prev;
  int next;
  int val;
};

const int NODE_SIZE = 30000;
const int PUSH_BACK = 0;
const int PUSH_FRONT = 1;
const int INSERT = 2;
const int POP_BACK = 3;
const int POP_FRONT = 4;
const int ERASE = 5;

int test_cmd[NODE_SIZE][3];

struct MyList{
  int head = NODE_SIZE;
  int tail = NODE_SIZE + 1;
  int pos;
  Node node[NODE_SIZE + 2];

  MyList(){
    pos = 0;
    node[head].next = tail;
    node[tail].prev = head;
  }

  void push_back(int data){
    int prev = node[tail].prev;
    int next = node[prev].next; //tail

    node[pos].val = data;
    
    node[pos].prev = prev;
    node[prev].next = pos;

    node[pos].next = next;
    node[next].prev = pos;
    ++pos;
  }

  void push_front(int data) {
    int next = node[head].next; 
    int prev = node[next].prev; // head

    node[pos].val = data;

    node[pos].prev = prev;
    node[prev].next = pos;

    node[pos].next = next;
    node[next].prev = pos;
    ++pos;
  }

  void insert(int p, int data) {
    int next = node[head].next;
    for(int i = 0; i < p; ++i){
      next = node[next].next;
    }
    int prev = node[next].prev;

    node[pos].val = data;

    node[pos].prev = prev;
    node[prev].next = pos;

    node[pos].next = next;
    node[next].prev = pos;
    ++pos;
  }

  void pop_back(){
    int target = node[tail].prev; // 리스트의 마지막
    int prev = node[target].prev;
    int next = node[target].next;
    
    node[prev].next = next;
    node[next].prev = prev;
  }

  void pop_front(){
    int target = node[head].next; // 리스트의 마지막
    int prev = node[target].prev;
    int next = node[target].next;
    
    node[prev].next = next;
    node[next].prev = prev;
  }

  void erase(int p){
    int target = node[head].next;
    for (int i = 0; i < p; ++i)
    {
      target = node[target].next;
    }
    int prev = node[target].prev;
    int next = node[target].next;

    node[prev].next = next;
    node[next].prev = prev;
  }

};

MyList my_list;
list<int> stl_list;

int main(int argc, char const *argv[])
{
  int cur_size = 0;
  for(int i = 0; i < NODE_SIZE; ++i){
    if(i < NODE_SIZE / 3){
      test_cmd[i][0] = rand() % 2;
    }
    else {
      test_cmd[i][0] = rand() % 6;
    }

    switch (test_cmd[i][0]){
      case PUSH_BACK:
      case PUSH_FRONT: {
        test_cmd[i][1] = rand();
        ++cur_size; // 리스트 사이즈 증가
        break;
      }
      case INSERT: {
        test_cmd[i][1] = rand() % cur_size;
        test_cmd[i][2] = rand();
        ++cur_size;
        break;
      }
      case POP_BACK:
      case POP_FRONT: {
        --cur_size;
        break;
      }
      case ERASE: {
        test_cmd[i][1] = rand() % cur_size;
        --cur_size;
        break;
      }
    }


    // test my list
    for(int i = 0; i < NODE_SIZE; i++){
      switch(test_cmd[i][0]){
        case PUSH_BACK: {
          my_list.push_back(test_cmd[i][1]);
          break;
        }
        case PUSH_FRONT: {
          my_list.push_front(test_cmd[i][1]);
          break;
        }
        case INSERT: {
          my_list.insert(test_cmd[i][1], test_cmd[i][2]);
          break;
        }
        case POP_BACK: {
          my_list.pop_back();
          break;
        }
        case POP_FRONT: {
          my_list.pop_front();
          break;
        }
        case ERASE: {
          my_list.erase(test_cmd[i][1]);
          break;
        }
      }
    }

  }

  return 0;
}
 
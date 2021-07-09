#include <iostream>

class Node{
public:
  int val;
  Node *nextVal;
};

template<class T> class CircleQueue{
public:
  Node *front, *rear;
  explicit CircleQueue(){front = NULL; rear = NULL;}
  ~CircleQueue(){delete []front, rear;}

};

template<typename T> void push(CircleQueue<T> *q, const T val){
  Node * tempNode = new Node;
  tempNode -> val = val;
  if(q -> front == NULL){
    q -> front = tempNode;
  } else {
    q -> rear -> nextVal = tempNode;
  }

  q -> rear = tempNode;
  q -> rear -> nextVal = q -> front;
}

template<typename T> T pop(CircleQueue<T> *q){
  if(q -> front == NULL){
    std::cout << "Queue is Empty " << std::endl;
    return 0;
  }
  T value;
  if(q -> front == q -> rear){
    value = q -> front -> val;
    free(q->front);
    q -> front = NULL;
    q -> rear = NULL;
  } else {
    Node *temp = q -> front;
    value = temp -> val;
    q -> front = q -> front -> nextVal;
    q -> rear -> nextVal = q -> front;
    free(temp);
  }
  return value;
}

template<typename T> void show(CircleQueue<T> *q){
  Node *tempNode = q->front;
  while(tempNode -> nextVal != q-> front){
    std::cout << tempNode -> val << " ";
    tempNode = tempNode -> nextVal;
  }
  std::cout << tempNode -> val << std::endl;
}

int main(){
  CircleQueue<int> *q = new CircleQueue<int>();
  push(q, 5);
  push(q, 6);
  push(q, 7);
  show(q);
  pop(q);
  show(q);


}
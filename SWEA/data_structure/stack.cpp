#include <iostream>
#include <string>


class Node{
  friend class Stack;
private:
  int val;
  Node *next;
  Node(int value = 0, Node *newNode = nullptr){
    val = value;
    next = newNode;
  }

};

class Stack{
private:
  Node *top;
public:
  explicit Stack(){top = nullptr;} // explicit : 형변환 제한
  bool isEmpty() const;
  void pushStack(const int val);
  int *popStack(int &val);
  void show()const;
};

bool Stack::isEmpty() const{
  return top == nullptr;
}

void Stack::pushStack(const int val){
  top = new Node(val, top);
}

int *Stack::popStack(int &val){
  if(!isEmpty()){
    std::cout << "Empty Stack" << std::endl;
    return 0;
  }
  Node *x = top;
  val = top -> val;
  delete x;
  return &val;
}

void Stack::show() const{
  Node *temp = top;
  while(temp != nullptr){
    std::cout << temp -> val << std::endl;
    temp = temp -> next;
  }
}
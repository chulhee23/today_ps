class Node
{
  friend class Stack;

private:
  int val;
  Node *next;
  Node(int value = 0, Node *newNode = nullptr)
  {
    val = value;
    next = newNode;
  }
};

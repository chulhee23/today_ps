// 트리 자료구조

#include <iostream>
using namespace std;

struct Node
{
  int data;
  Node *left;
  Node *right;
};

Node *insert(Node *node, int data)
{
  if (node == nullptr)
  {
    node = new Node();
    node->data = data;
    node->left = node->right = nullptr;
  }
  else if (data <= node->data)
    node->left = insert(node->left, data);
  else
    node->right = insert(node->right, data);
  return node;
}

void postorder(Node *node)
{
  if (node->left != nullptr)
    postorder(node->left);
  if (node->right != nullptr)
    postorder(node->right);
  cout << node->data << '\n';
}

int main()
{
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);
  cout.tie(NULL);
  Node *root = nullptr;
  int val;
  while (cin >> val)
  {
    if (val == EOF)
      break;
    root = insert(root, val);
  }
  postorder(root);
  return 0;
}

#include "stack.cpp"

int main(int argc, char const *argv[])
{
  Stack *stack = new Stack();
  stack -> pushStack(1);
  stack -> pushStack(2);
  stack -> pushStack(3);
  stack -> pushStack(4);
  stack -> pushStack(5);

  stack -> show();
  
  return 0;
}

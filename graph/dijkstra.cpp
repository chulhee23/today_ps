#include <iostream>
#define INT_MAX 10e9

using namespace std;

int cost[100][100], n;

int getMin(int dist[], bool visited[])
{
  int key = 0;
  int min = INT_MAX;
  for (int i = 0; i < n; i++)
  {
    if (!visited[i] && dist[i] < min)
    {
      min = dist[i];
      key = i;
    }
  }
  return key;
}

void display(int dist[], int par[])
{
  for (int i = 0; i < n; i++)
  {
    int temp = par[i];
    cout << i << " <- ";
    while (temp != -1)
    {
      cout << temp << " <- ";
      temp = par[temp];
    }
    cout << endl;
    cout << "::::Distance = " << dist[i];
    cout << endl;
  }
}

void dijkstra(int src)
{
  int par[100], dist[100];
  bool visited[100] = {0};
  fill(dist, dist + n, INT_MAX);

  dist[src] = 0;
  par[src] = -1;

  for (int g = 0; g < n - 1; g++)
  {
    int u = getMin(dist, visited);
    visited[u] = true;
    cout << " min = " << u << endl;
    for (int v = 0; v < n; v++)
    {
      if (!visited[v] && (dist[u] + cost[u][v]) < dist[v] && cost[u][v] != 9999)
      {
        par[v] = u;
        dist[v] = dist[u] + cost[u][v];
      }
    }
  }

  display(dist, par);
}

int main(void)
{
  cout << "Enter n : ";
  cin >> n;
  cout << "Enter cost matrix : \n";
  for (int i = 0; i < n; i++)
  {
    for (int j = 0; j < n; j++)
      cin >> cost[i][j];
  }
  int src;
  cout << "\nEnter source : ";
  cin >> src;
  dijkstra(src);
}
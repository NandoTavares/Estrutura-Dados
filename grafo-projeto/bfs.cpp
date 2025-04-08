#include "bfs.h"
#include <iostream>
#include <queue>
#include <vector>

void bfs(const graph& g, int s, int t) {
    vector<bool> visited(g.size(), false);
    vector<int> parent(g.size(), -1);
    queue<int> q;
    visited[s] = true;
    q.push(s);

    while (!q.empty()) {
        int u = q.front(); q.pop();
        for (int v : g.get_list()[u]) {
            if (!visited[v]) {
                visited[v] = true;
                parent[v] = u;
                q.push(v);
            }
        }
    }

    if (!visited[t]) {
        cout << "Nao ha caminho entre os vertices " << s << " e " << t << "." << endl;
        return;
    }

    vector<int> path;
    for (int v = t; v != -1; v = parent[v])
        path.push_back(v);
    reverse(path.begin(), path.end());

    cout << "Caminho de " << s << " a " << t << ": ";
    for (int v : path)
        cout << v << " ";
    cout << endl;
}
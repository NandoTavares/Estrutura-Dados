#include "dfs.h"
#include <iostream>
#include <stack>
#include <vector>

void dfs_iterativo(const graph& g, int start) {
    vector<bool> visited(g.size(), false);
    stack<int> stk;
    stk.push(start);

    while (!stk.empty()) {
        int u = stk.top(); stk.pop();
        if (!visited[u]) {
            visited[u] = true;
            cout << u << " ";
            for (int v : g.get_list()[u])
                if (!visited[v])
                    stk.push(v);
        }
    }
    cout << endl;
}
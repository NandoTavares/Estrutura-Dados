#include "graph.h"
#include <iostream>
#include <fstream>
#include <sstream>

graph::graph(int n) : num_vertices(n), mat_adj(n, vector<int>(n, 0)), lista_adj(n) {}

void graph::add_edge(int u, int v) {
    mat_adj[u][v] = 1;
    mat_adj[v][u] = 1;
    lista_adj[u].push_back(v);
    lista_adj[v].push_back(u);
}

void graph::print_matrix() {
    for (const auto& row : mat_adj) {
        for (int val : row)
            cout << val << " ";
        cout << endl;
    }
}

void graph::print_list() {
    for (int i = 0; i < num_vertices; ++i) {
        cout << i << ": ";
        for (int v : lista_adj[i])
            cout << v << " ";
        cout << endl;
    }
}

const vector<vector<int>>& graph::get_matrix() const {
    return mat_adj;
}

const vector<list<int>>& graph::get_list() const {
    return lista_adj;
}

int graph::size() const {
    return num_vertices;
}

graph* load_graph_from_file(const string& path) {
    ifstream file(path);
    int n;
    file >> n;
    graph* g = new graph(n);
    int u, v;
    while (file >> u >> v) {
        g->add_edge(u, v);
    }
    return g;
}
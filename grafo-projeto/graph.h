#ifndef GRAPH_H
#define GRAPH_H

#include <vector>
#include <list>
#include <string>

using namespace std;

class graph {
private:
    int num_vertices;
    vector<vector<int>> mat_adj;
    vector<list<int>> lista_adj;

public:
    graph(int n);
    void add_edge(int u, int v);
    void print_matrix();
    void print_list();
    const vector<vector<int>>& get_matrix() const;
    const vector<list<int>>& get_list() const;
    int size() const;
};

graph* load_graph_from_file(const string& path);

#endif
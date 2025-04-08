#include <iostream>
#include "graph.h"
#include "bfs.h"
#include "dfs.h"

using namespace std;

int main(int argc, char* argv[]) {
    if (argc < 2) {
        cout << "Uso: ./grafo <arquivo>" << endl;
        return 1;
    }

    graph* g = load_graph_from_file(argv[1]);

    cout << "Matriz de Adjacência:" << endl;
    g->print_matrix();

    cout << "\nLista de Adjacência:" << endl;
    g->print_list();

    cout << "\nBusca em Largura (BFS):" << endl;
    bfs(*g, 0, 3);

    cout << "\nBusca em Profundidade (DFS iterativo):" << endl;
    dfs_iterativo(*g, 0);

    delete g;
    return 0;
}
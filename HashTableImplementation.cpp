
#include <iostream>
#include <vector>
#include <string>
#include <list>

using namespace std;

// Função hash para o primeiro nível (mapeamento para o índice da tabela de 10 entradas)
int hashLevel1(int key) {
    return key % 10;
}

// Função hash para o segundo nível (mapeamento para listas dentro de cada tabela do nível 1)
int hashLevel2(int key, int level1Index) {
    return key / 10 % 10;  // Define o mapeamento da chave na tabela do segundo nível
}

class HashTable {
private:
    vector<list<string>> tableLevel1;  // Tabela hash de nível 1
public:
    HashTable() {
        // Inicializa a tabela de nível 1 com 10 listas
        tableLevel1.resize(10);
    }

    void insert(int key, const string& value) {
        // Usa a função hash para o primeiro nível
        int level1Index = hashLevel1(key);

        // Usa a função hash para o segundo nível
        int level2Index = hashLevel2(key, level1Index);

        // Adiciona o valor na lista do segundo nível
        tableLevel1[level1Index].push_back(value);
    }

    void printTable() {
        for (int i = 0; i < 10; ++i) {
            cout << "Nível 1 - Tabela " << i << ": ";
            for (const auto& value : tableLevel1[i]) {
                cout << value << " ";
            }
            cout << endl;
        }
    }
};

int main() {
    // Criação da tabela hash
    HashTable hashTable;

    // Inserção de dados na tabela
    hashTable.insert(12, "João");
    hashTable.insert(22, "Marco");
    hashTable.insert(32, "Marina");
    hashTable.insert(42, "Julia");
    hashTable.insert(52, "Antônio");
    hashTable.insert(62, "José");

    // Impressão da tabela
    hashTable.printTable();

    return 0;
}

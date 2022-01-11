// Davi alves Carvalho
// Ewerton Keiji Onga
// José Victor Amorim Morais

#include <iostream>
#include <vector>
#include <queue>
using namespace std;

struct Vertice
{
    int id, pai;
    long long distancia;

    Vertice(int idP, long long distanciaP = 1, int paiP = -1){
        id = idP;
        distancia = distanciaP;
        pai = paiP;
    }

    bool operator<(Vertice a) const
    {
        return a.distancia < this->distancia;
    }
};

typedef vector<vector<Vertice>> vvert;

struct Grafo {
    vvert g;
    vector<int> pais;
    int n;

    Grafo(int nP){
        n = nP;
        g = vvert(n, vector<Vertice>());
        pais = vector<int>(n);
    }
    
    void adicionarAresta(int a, int b, long long d = 0) {
        g[a].push_back(Vertice(b, d));
    }
    
    long long dijkstra(int s, int d) {
        priority_queue<Vertice> fila;
        bool visitados[n];

        fill(visitados, visitados+n, 0);
        fill(pais.begin(), pais.end(), -1);

        fila.push(Vertice(s, 0, -1));

        auto topo = fila.top();

        while (topo.id != d) {
            if (!visitados[topo.id]) {
                for (auto &filho : g[topo.id]){
                    for(auto &i : g[filho.id]){
                        if (!visitados[i.id]){
                            fila.push(Vertice(i.id, i.distancia + topo.distancia + filho.distancia, topo.id));
                        }
                    }
                }
                visitados[topo.id] = 1;
                pais[topo.id] = topo.pai;
            }
            fila.pop();
            if (fila.empty()){
                return -1;
            }
            topo = fila.top();
        }
        pais[topo.id] = topo.pai;
        return topo.distancia;
    }
};

int main() {
	int c, v, c1, c2, g;
	
    cin >> c >> v;
	Grafo grafo(c+1);
	
	for(int i = 0; i < v; i++) {
        cin >> c1 >> c2 >> g;
        grafo.adicionarAresta(c1, c2, g);
        grafo.adicionarAresta(c2, c1, g);
	}
	
    cout << grafo.dijkstra(1, c) << '\n';
}
#include <iostream>
using namespace std;

int main(){
	int n, m;
	
	while(cin >> n and n != 0){
		cin >> m;
		
		double G[n][n];
		int u, v, p;
		
		for(int i = 0; i < n; i++){
			for(int j = 0; j < n; j++){
				G[i][j] = 0.0;
			}
		}

		for(int i = 0; i < m; i++) {
			cin >> u >> v >> p;
			G[u-1][v-1] = p * 0.01;
			G[v-1][u-1] = p * 0.01;
		}
		
		for(int k = 0; k < n; k++) {
			for(int i = 0; i < n; i++) {
				for(int j = 0; j < n; j++) {
					G[i][j] = max(G[i][j], G[i][k] * G[k][j]);
				}
			}
		}		
		cout.precision(6);
		cout << fixed << G[0][n-1] * 100 << " percent\n";
	}	
}
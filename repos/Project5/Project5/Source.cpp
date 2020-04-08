#include <iostream>
#include <vector>

using namespace std;

void main()
{

const int SIZE = 1e3 + 10;
vector<int> adj[SIZE];
bool usd[SIZE];


void dfs(int cur) {
	usd[cur] = true;
	for (int i = 0; i < adj[cur].size(); ++i) {
		int nxt = adj[cur][i];
		if (!usd[nxt])
			dfs(nxt);
	}
}
int connected_components_amount_dfs() {
	int cnt = 0;
	for (int i = 1; i <= n; ++i) {
		if (!usd[i]) {
			dfs(i);
			++cnt;
		}
	}
	return cnt;
}

}
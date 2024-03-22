#include <iostream>

using namespace std;

int parent[500001];

int Find(int now) {
	if (now == parent[now]) return now;

	return parent[now] = Find(parent[now]);
}

void Union(int a, int b) {
	int root_A = Find(a);
	int root_B = Find(b);

	if (root_A == root_B) return;

	if (root_A < root_B) {
		parent[root_B] = root_A;
	}
	else {
		parent[root_A] = root_B;
	}

	return;
}




int main() {

	int N, M, ans=0;
	bool flag = false;

	cin >> N >> M;

	for (int i = 0; i < N; i++) {
		parent[i] = i;
	}


	for (int i = 0; i < M; i++) {
		int a, b;
		cin >> a >> b;

		if (flag) continue;

		if (Find(a) == Find(b)) {
			flag = true;
			ans = i + 1;
		}
		else {
			Union(a, b);
		}

	}

	
	cout << ans;

	return 0;
}

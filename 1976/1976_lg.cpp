#include <iostream>

using namespace std;

int parent[200];


int Find(int now) {
	if (now == parent[now])
		return now;

	return parent[now] = Find(parent[now]);
}

void Union(int A, int B) {
	int root_A = Find(A);
	int root_B = Find(B);

	if (root_A < root_B) {
		parent[root_B] = root_A;
	}
	else if (root_A > root_B) {
		parent[root_A] = root_B;
	}

	return;
}


int main() {

	int N, M;
	cin >> N >> M;

	for (int i = 1; i <= N; i++) {
		parent[i] = i;
	}
	
	for (int i = 1; i <= N; i++) {
		for (int j = 1; j <= N; j++) {
			int temp;
			cin >> temp;

			if (temp == 1) {
				Union(i, j);
			}
		}
	}

	int prev, cur;
	bool flag = true;

	for (int i = 0; i < M; i++) {
		int temp;
		cin >> temp;

		if (i == 0) {
			prev = temp;
		}
		else {
			cur = temp;

			if (parent[prev] != parent[cur]) {
				flag = false;
				break;
			}

			prev = cur;
		}
	}

	if (flag == true) {
		cout << "YES";
	}
	else {
		cout << "NO";
	}

	cout << endl;

	for (int i = 1; i <= N; i++) {
		cout << parent[i] << " ";
	}

	return 0;
}

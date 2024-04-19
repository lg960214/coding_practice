#include <iostream>
#include <string>
#include <unordered_map>

using namespace std;

int parents[200001];
int size_[200001];

int Find(int now) {

	if (parents[now] == now) return now;

	return parents[now] = Find(parents[now]);
}

void Union(int a, int b) {
	int root_A = Find(a);
	int root_B = Find(b);

	if (root_A == root_B) return;

	if (root_A < root_B) {
		parents[root_B] = root_A;
		size_[root_A] += size_[root_B];
	}
	else if (root_A > root_B) {
		parents[root_A] = root_B;
		size_[root_B] += size_[root_A];
	}
}

int main() {
	ios::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	int T;

	cin >> T;

	for (int t = 0; t < T; t++) {
		int N, idx = 0;
		cin >> N;

		unordered_map<string, int>umap;

		for (int i = 0; i <= 200000; i++) {
			parents[i] = i;
			size_[i] = 1;
		}

		for (int i = 0; i < N; i++) {
			string name_1, name_2;
			
			cin >> name_1 >> name_2;

			if (umap.find(name_1) == umap.end()) {
				umap[name_1] = idx++;
			}
			if (umap.find(name_2) == umap.end()) {
				umap[name_2] = idx++;
			}

			int name_idx_1 = umap[name_1];
			int name_idx_2 = umap[name_2];

			Union(name_idx_1, name_idx_2);

			int ans = Find(umap[name_1]);

			cout << size_[ans] << '\n';
		}
	}

	return 0;
}

#include <iostream>
#include <algorithm>
#include <vector>
#include <string>

using namespace std;

struct Edge {
	int a, b, cost;
};

bool cmp(Edge left, Edge right) {
	if (left.cost < right.cost)
		return true;
	if (left.cost > right.cost)
		return false;
	return false;
}

int parent[1001];

vector<Edge>v;

int N, M;

int Find(int now) {
	if (now == parent[now]) return now;

	return parent[now] = Find(parent[now]);
}

void Union(int a, int b) {
	int root_A = Find(a);
	int root_B = Find(b);

	if (root_A != root_B) {
		parent[max(root_A, root_B)] = min(root_A, root_B);
	}
}

int kruskal() {
	sort(v.begin(), v.end(), cmp);

	for (int i = 0; i < N; i++) {
		parent[i] = i;
	}

	int size_ = v.size();

	int sum_cost = 0;

	for (int i = 0; i < size_; i++) {
		Edge now = v[i];

		if (Find(now.a) == Find(now.b)) {
			sum_cost += now.cost;
			continue;
		}

		Union(now.a, now.b);
	}

	return sum_cost;
}

int main() {
	cin >> N;

	for (int i = 0; i < N; i++) {
		string temp;
		int from, to, cost;
		from = i;
		cin >> temp;
		for (int j = 0; j < N; j++) {
			to = j;
			
			if (temp[j] == '0') continue;
			else if ('A' <= temp[j] && temp[j] <= 'Z') {
				cost = (int)temp[j] - 38;
			}
			else if ('a' <= temp[j] && temp[j] <= 'z') {
				cost = (int)temp[j] - 96;
			}

			// 그래프 구성
			v.push_back({ from, to, cost });
		}
	}

	int ans = kruskal();
	int flag = 1;

	for (int i = 0; i < N; i++) {
		if (Find(i) != 0) {
			flag = 0;
			break;
		}
	}
	
	if (flag == 0) {
		cout << -1;
	}
	else {
		cout << ans;
	}

}

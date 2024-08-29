#include <iostream>

#include <queue>

using namespace std;


int N, min_ = 1e8;

int con_info[11][11];

int parent[11], pop_info[11];

int path[11];




int Find(int now) {
	
	if (now == parent[now]) return now;

	return parent[now] = Find(parent[now]);
}

void Union(int a, int b) {
	int root_A = Find(a);
	int root_B = Find(b);

	if (root_A == root_B) return;

	if (root_A > root_B) 
		swap(root_A, root_B);
	
	parent[root_B] = root_A;
}

void discriminate(int n) {

	for (int i = 1; i <= N; i++) {
		parent[i] = i;
	}

	vector<int>n1;
	vector<int>n2;

	for (int i = 1; i <= N; i++) {
		if (path[i] == 1)
			n1.push_back(i);
		else
			n2.push_back(i);
	}


	// n1끼리 연결
	for (int i = 0; i < n1.size(); i++) {
		for (int j = i + 1; j < n1.size(); j++) {
			if (con_info[n1[i]][n1[j]] == 1)
				Union(n1[i], n1[j]);
		}
	}



	// n2끼리 연결
	for (int i = 0; i < n2.size(); i++) {
		for (int j = i + 1; j < n2.size(); j++) {
			if (con_info[n2[i]][n2[j]] == 1)
				Union(n2[i], n2[j]);
		}
	}

	int cnt = 0;

	for (int i = 1; i <= N; i++) {
		if (parent[i] == i) cnt++;
	}

	if (cnt != 2) return;

	int pop1 = 0;
	int pop2 = 0;

	for (int i = 0; i < n1.size(); i++) {
		pop1 += pop_info[n1[i]];
	}

	for (int i = 0; i < n2.size(); i++) {
		pop2 += pop_info[n2[i]];
	}

	min_ = min(min_, abs(pop1 - pop2));
}



void DFS(int n, int now, int cnt) {

	if (cnt == n) {
		// 이어지는 지 판별
		discriminate(n);
	}

	for (int i = now; i <= N; i++) {

		if (path[i] == 1) continue;
		
		path[i] = 1;
		DFS(n, i + 1, cnt + 1);
		path[i] = 0;
	}


}

void solve() {

	for (int i = 1; i <= N / 2; i++) {
		DFS(i,1,0);
	}


}




int main(void)
{
	cin >> N;

	for (int i = 1; i <= N; i++) {
		cin >> pop_info[i];
	}

	for (int i = 1; i <= N; i++) {
		int num;
		cin >> num;
		for (int j = 0; j < num; j++) {
			int to;
			cin >> to;
			con_info[i][to] = 1;
		}
	}

	solve();

	if (min_ == 1e8)
		cout << -1;
	else
		cout << min_;





}
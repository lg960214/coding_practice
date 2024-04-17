#include <iostream>
#include <queue>

using namespace std;

int dx[4] = { 0, 1, 0, -1 };
int dy[4] = { -1, 0, 1, 0 };

struct Node {
	int x, y;
};

void side_BFS(int c_arr[101][101], int N, int M, int sx, int sy) {

	queue<Node>q;

	int visited[101][101] = { 0, };

	visited[sx - 1][sy - 1] = 1;

	q.push({ sx - 1, sy - 1 });
	
	while (!q.empty()) {
		Node target = q.front();
		q.pop();

		for (int i = 0; i < 4; i++) {
			int nx = target.x + dx[i];
			int ny = target.y + dy[i];

			if (nx < 0 || ny < 0 || nx >= N || ny >= M) continue;
			if (visited[nx][ny] == 1) continue;
			if (c_arr[nx][ny] != 0) continue;
			
			visited[nx][ny] = 1;
			q.push({ nx, ny });
			c_arr[nx][ny] = -1;
		}
	}
}

void prepare(int arr[101][101], int N, int M) {

	int c_arr[101][101] = { 0, };

	for (int i = 0; i < N; i++) {
		for (int j = 0; j < M; j++) {
			c_arr[i][j] = arr[i][j];
		}
	}

	// 1. 공기와 접촉
	side_BFS(c_arr, N, M, 1, 1);
	side_BFS(c_arr, N, M, 1, M);
	side_BFS(c_arr, N, M, N, 1);
	side_BFS(c_arr, N, M, N, M);

	// 2. 접촉한 공기 수 세기

	for (int i = 0; i < N; i++) {
		for (int j = 0; j < M; j++) {
			if (c_arr[i][j] != 1) continue;

			c_arr[i][j] = 0;

			for (int d = 0; d < 4; d++) {
				int nx = i + dx[d];
				int ny = j + dy[d];

				if (c_arr[nx][ny] == -1) {
					c_arr[i][j]++;
				}
			}

			if (c_arr[i][j] >= 2)
				arr[i][j] = 0;
		}
	}




	return;
}

int main() {

	int N, M;

	int day = 0;

	cin >> N >> M;

	int arr[101][101] = { 0, };

	for (int i = 0; i < N; i++) {
		for (int j = 0; j < M; j++) {
			int temp;
			cin >> temp;
			arr[i][j] = temp;
		}
	}

	bool ass = true;

	while (ass) {
		prepare(arr, N, M);

		bool flag = true;

		for (int i = 0; i < N; i++) {
			for (int j = 0; j < M; j++) {
				if (arr[i][j] == 1) {
					flag = false;
					break;
				}
			}
			if (flag == false) break;
		}

		ass = !flag;
		day++;
	}

	cout << day;

	return 0;
}

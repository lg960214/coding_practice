#include <iostream>

using namespace std;

char arr[13][13];
char forPrint[13][13];

int dx[4] = {-1, 0, 1, 0};
int dy[4] = {0, 1, 0, -1};

int N, M;

inline void Search() {

	int ix = 11;
	int ax = -1;
	int iy = 11;
	int ay = -1;

	for (int i = 0; i < N; i++) {
		for (int j = 0; j < M; j++) {
			char target = arr[i][j];

			if (target == 'X') {
				int cnt = 0;

				for (int d = 0; d < 4; d++) {
					int nx = i + dx[d];
					int ny = j + dy[d];

					if (0 > nx || 0 > ny || N <= nx || M <= ny || arr[nx][ny] == '.') {
						continue;
					}
					cnt++;
				}

				if (cnt >= 2) {
					forPrint[i][j] = 'X';
					ax = max(ax, i);
					ix = min(ix, i);
					ay = max(ay, j);
					iy = min(iy, j);
				}
				else {
					forPrint[i][j] = '.';
				}
			}
			else {
				forPrint[i][j] = '.';
			}
		}
	}

	for (int i = ix; i <= ax; i++) {
		for (int j = iy; j <= ay; j++) {
			cout << forPrint[i][j];
		}
		cout << '\n';
	}

	return;
}



int main() {

	cin >> N >> M;

	for (int i = 0; i < N; i++) {
		for (int j = 0; j < M; j++) {
			cin >> arr[i][j];
		}
	}

	Search();

	return 0;
}
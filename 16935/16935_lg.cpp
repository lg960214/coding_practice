#include <iostream>
#include <vector>

using namespace std;

int N, M, R;
int arr[101][101];


void roll_array(int n) {

	int cp_array[101][101] = {0,};

	for (int i = 0; i < N; i++) {
		for (int j = 0; j < M; j++) {
			cp_array[i][j] = arr[i][j];
		}
	}

	if (n == 1) {
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < M; j++) {
				arr[i][j] = cp_array[N-i-1][j];
			}
		}
	}

	else if (n == 2) {
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < M; j++) {
				arr[i][j] = cp_array[i][M-j-1];
			}
		}
	}

	else if (n == 3) {
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < M; j++) {
				arr[j][N-1-i] = cp_array[i][j];
			}
		}

		int temp = N;
		N = M;
		M = temp;
	}

	else if (n == 4) {
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < M; j++) {
				arr[M-j-1][i] = cp_array[i][j];
			}
		}

		int temp = N;
		N = M;
		M = temp;
	}

	else if (n == 5) {
		for (int i = 0; i < N/2; i++) {
			for (int j = 0; j < M/2; j++) {
				arr[i][(M/2)+j] = cp_array[i][j];
			}
		}

		for (int i = 0; i < N / 2; i++) {
			for (int j = M/2; j < M; j++) {
				arr[(N/2)+i][j] = cp_array[i][j];
			}
		}

		for (int i = N/2; i < N; i++) {
			for (int j = M / 2; j < M; j++) {
				arr[i][j-(M/2)] = cp_array[i][j];
			}
		}

		for (int i = N / 2; i < N; i++) {
			for (int j = 0; j < M/2; j++) {
				arr[i-(N/2)][j] = cp_array[i][j];
			}
		}
	}

	else if (n == 6) {
		for (int i = 0; i < N / 2; i++) {
			for (int j = 0; j < M / 2; j++) {
				arr[i+(N/2)][j] = cp_array[i][j];
			}
		}

		for (int i = 0; i < N / 2; i++) {
			for (int j = M / 2; j < M; j++) {
				arr[i][j-(M/2)] = cp_array[i][j];
			}
		}

		for (int i = N / 2; i < N; i++) {
			for (int j = M / 2; j < M; j++) {
				arr[i-(N/2)][j] = cp_array[i][j];
			}
		}

		for (int i = N / 2; i < N; i++) {
			for (int j = 0; j < M / 2; j++) {
				arr[i][j+(M/2)] = cp_array[i][j];
			}
		}
	}


	return;
}


int main(){

	cin >> N >> M >> R;

	for (int i = 0; i < N; i++) {
		for (int j = 0; j < M; j++) {
			int temp;
			cin >> temp;
			arr[i][j] = temp;
		}
	}
	
	for (int i = 0; i < R; i++) {
		int temp;
		cin >> temp;
		roll_array(temp);
	}

	for (int i = 0; i < N; i++) {
		for (int j = 0; j < M; j++) {
			cout << arr[i][j] << " ";
		}
		cout << '\n';
	}


	return 0;
}

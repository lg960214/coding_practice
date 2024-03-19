#include <iostream>

using namespace std;

int main() {

	int N;
	cin >> N;

	int arr[201] = { 0, };
	int dp[201] = { 0, };

	for (int i = 0; i < N; i++) {
		int temp;
		cin >> temp;
		arr[i] = temp;
	}

	dp[0] = 1;

	for (int i = 1; i < N; i++) {
		dp[i] = 1;

		for (int j = 0; j < i; j++) {
			if (arr[j] < arr[i] && dp[j] >= dp[i]) {
				dp[i] = dp[j] + 1;
			}
		}
	}

	int max_dp = 0;

	for (int i = 0; i < N; i++) {
		if (max_dp < dp[i])
			max_dp = dp[i];
	}

	cout << N - max_dp;

	return 0;
}

#include <iostream>

using namespace std;

// def 1. 2진수 1 개수 카운트해주는 함수

int cnt_binary(int target) {
	
	int cnt = 0;

	while (target) {
		cnt += target & 1;
		target >>= 1;
	}
	
	return cnt;
}

int where_binary(int target) {
	int pos = 0;
	while (target) {
		if (target & 1)
			return pos;
		pos++;
		target >>= 1;
	}
	return -1; // 모든 비트가 0인 경우
}

int main() {

	int N, K;
	cin >> N >> K;

	bool flag = true;

	int ans = cnt_binary(N);

	if (ans <= K) {
		flag = false;
		cout << 0;
	}

	int outing = 0;

	while (flag) {
		int pos = where_binary(N);

		// 1. pos만큼 더한다
		// 2. 출력 값도 pos만큼 더한다
		// 개수 채워지면 go / 아니면 반복

		int temp = (1 << pos);

		N += temp;
		outing += temp;

		ans = cnt_binary(N);

		if (ans <= K) {
			cout << outing;
			break;
		}
	}
	return 0;
}

#include <iostream>
#include <queue>
#include <algorithm>


using namespace std;

bool cmp(int a, int b) {
	if (a < b)
		return true;
	if (a > b)
		return false;
	return false;
}

bool PS(int thr, vector<int>target, int M) {

	int cnt = 0;

	for (int i = 0; i < target.size(); i++) {

		int temp = target[i];

		int Q = temp / thr;
		int R = temp % thr;

		if (R == 0) {
			cnt += Q - 1;
		}
		else if (R != 0) {
			cnt += Q;
		}
	}

	if (cnt <= M) return true;

	return false;

}



int main() {
	
	int N, M, L;

	cin >> N >> M >> L;

	vector<int>processing;
	vector<int>target;

	processing.push_back(0);
	processing.push_back(L);

	for (int i = 0; i < N; i++) {
		int temp;
		cin >> temp;

		processing.push_back(temp);
	}

	sort(processing.begin(), processing.end(), cmp);


	for (int i = 0; i < processing.size()-1; i++) {
		target.push_back(processing[i+1] - processing[i]);

	}

	int st = 1;
	int en = L;
	int mid;
	int ans;

	while (st <= en) {
		mid = (st + en) / 2;

		if (PS(mid, target, M)) {
			en = mid - 1;
			ans = mid;
		}
		else {
			st = mid + 1;
		}
	}
	
	cout << ans;

	return 0;
}

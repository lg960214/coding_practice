#include <iostream>
#include <queue>


using namespace std;


struct ex {
	long long x;

	bool operator < (ex next) const {
		if (x < next.x)
			return false;
		if (x > next.x)
			return true;
		return false;
	}
};

int main() {

	int T;
	
	cin >> T;
	
	for (int t = 0; t < T; t++) {
		int N;
		cin >> N;

		priority_queue<ex, vector<ex>>pq;

		for (int i = 0; i < N; i++) {
			long long temp;
			cin >> temp;
			pq.push({ temp });
		}

		long long total = 0;

		while (pq.size() >= 2) {
			long long temp_1 = pq.top().x;
			pq.pop();
			long long temp_2 = pq.top().x;
			pq.pop();

			long long sum_ = temp_1 + temp_2;
			total += sum_;

			pq.push({ sum_ });
		}

		cout << total << '\n';

	}


	return 0;
}

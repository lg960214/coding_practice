#include <iostream>
#include <unordered_map>
#include <queue>
#include <string>

using namespace std;

struct ct {
	int val;

	bool operator < (ct next) const {
		if (val > next.val)
			return false;
		if (val < next.val)
			return true;
		return false;
	}
};

int main() {

	int Q, num, k;
	long long ans = 0;
	string name;

	unordered_map<string, priority_queue<ct, vector<ct>>>umap;

	cin >> Q;

	for (int q = 0; q < Q; q++) {

		cin >> num >> name >> k;

		if (num == 1) {
			priority_queue<ct, vector<ct>>temp_pq = umap[name];

			for (int i = 0; i < k; i++) {
				int temp;
				cin >> temp;
				temp_pq.push({ temp });
			}

			umap[name] = temp_pq;
		}

		else if (num == 2) {
			priority_queue<ct, vector<ct>>temp_pq = umap[name];

			while ((!temp_pq.empty()) && k > 0) {
				int temp = temp_pq.top().val;
				temp_pq.pop();

				ans += temp;
				k--;
			}

			umap[name] = temp_pq;
		}
	}

	cout << ans;

	return 0;
}

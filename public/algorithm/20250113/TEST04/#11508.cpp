#include <iostream>
#include <vector>
using namespace std;

int main() {
	ios::sync_with_stdio(false);  //입출력 시간초과를 해결
	cin.tie(0);

	int N;
	cin >> N;

	vector<int> price(N);
	for (int i = 0; i < N; i++) {
		cin >> price[i];
	}

	sort(price.begin(), price.end(), greater<int>());

	long long totalPrice = 0;
	for (int i = 0; i < N; i++) {
		if ((i + 1) % 3 != 0) {
			totalPrice += price[i];
		}
	}

	cout << totalPrice;

	return 0;
}

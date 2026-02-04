#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <set>
using namespace std;

int main() {
	ios::sync_with_stdio(false);  //입출력 시간초과를 해결
	cin.tie(0);

	int N, M;
	cin >> N;

	set<int> card;
	int input;
	for (int i = 0; i < N; i++) {
		cin >> input;
		card.insert(input);
	}
	int size = card.size();

	cin >> M;
	int num;
	for (int i = 0; i < M; i++) {
		cin >> num; 
		card.insert(num);
		if (size == card.size())
			cout << '1' << ' ';
		else {
			cout << '0' << ' ';
			size = card.size();
		}
	}

	return 0;
}

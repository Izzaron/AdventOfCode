//============================================================================
// Name        : Advent17.cpp
// Author      : 
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {

	vector<int> spinlock(1);
	int current_pos = 0;
	int puzzle_input = 316;
	int num_after_zero = 0;

	for(int i = 1; i < 50000001; i++) {
		int next_pos = (current_pos + puzzle_input)%i;
		if(next_pos == 0) {
			num_after_zero = i;
		}
//		if(next_pos == spinlock.size()-1) {
//			spinlock.push_back(i);
//		} else if(next_pos < spinlock.size()-1) {
//			spinlock.insert(spinlock.begin()+next_pos+1,i);
//		} else cout << "CRITICAL ERROR! next_pos out of bounds" << endl;
		current_pos = next_pos+1;
//		if(i<200) {
//			for(vector<int>::iterator it = spinlock.begin(); it != spinlock.end(); it++) cout << *it << " ";
//			cout << endl;
//		}

	}

	//for(vector<int>::iterator it = spinlock.begin(); it != spinlock.end(); it++) cout << *it << " ";
	//cout << endl;

	//cout << *(find(spinlock.begin(),spinlock.end(),0)+1) << endl;
	cout << num_after_zero;

	return 0;
}

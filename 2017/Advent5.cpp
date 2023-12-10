//============================================================================
// Name        : Advent5.cpp
// Author      : 
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <fstream>
#include <vector>
using namespace std;

int main() {

	vector<int> instructions;
	int num;

	ifstream myfile("input.txt");
	if (myfile.is_open()) {

		while (myfile >> num) {
			instructions.push_back(num);
		}
		myfile.close();
	} else cout << "Unable to open file";

	int sum = 0;
	unsigned int pos = 0;
	while(pos<instructions.size()) {
		int old_pos = pos;
		pos += instructions[pos];
		if(instructions[old_pos]>=3)
			instructions[old_pos]--;
		else
			instructions[old_pos]++;
		sum++;
	}
	cout << sum << endl;
	/*for(vector<int>::iterator it = instructions.begin(); it != instructions.end(); it++) {
		cout << *it << endl;
	}*/
	return 0;
}

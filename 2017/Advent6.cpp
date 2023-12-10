//============================================================================
// Name        : Advent6.cpp
// Author      : 
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
#include <sstream>
using namespace std;

string vec2str(vector<int> vec) {
	string returnStr = "";
	for(vector<int>::iterator it = vec.begin(); it != vec.end(); it++) {
		stringstream ss;
		ss << *it;
		string str = ss.str();
		returnStr += str+" ";
	}
	return returnStr;
}

int findIterations(vector<int> &blocks) {
	int iterations = 0;
	vector<string> past_iter;

	while(1) {
		vector<int>::iterator max_elem = max_element(blocks.begin(),blocks.end());

		size_t active_block = max_elem - blocks.begin();
		int stack = *max_elem;
		//cout << stack << " -> ";
		*max_elem = 0;
		active_block++;
		for(int i = 0; i != stack; i++) {
			if(active_block >= blocks.size()) active_block = 0;

			blocks[active_block]++;

			active_block++;
		}

		iterations++;


		/*
		for(vector<string>::iterator it = past_iter.begin(); it != past_iter.end(); it++)
			if(vec2str(blocks) == *it)
				return iterations;
		*/
		
		if(iterations%100 == 0) cout << iterations << endl;


		if (find(past_iter.begin(),past_iter.end(),vec2str(blocks)) != past_iter.end()) {
			//cout << past_iter.end() - find(past_iter.begin(),past_iter.end(),vec2str(blocks)) << endl;
			return iterations;
		}


		//cout << past_iter.size() << endl;

		past_iter.push_back(vec2str(blocks));
		//cout << vec2str(blocks) << endl;

		/*
		for(vector<int>::iterator it = blocks.begin(); it != blocks.end(); it++) {
			cout << *it << " ";
		}
		cout << endl;
		*/
	}

	return 0;
}

int main() {
	vector<int> blocks;
	ifstream myfile("input.txt");
	if (myfile.is_open()) {

		int num;
		while (myfile >> num) {
			blocks.push_back(num);
			//cout << num << " ";
		}
		//cout << endl;
		myfile.close();
	} else cout << "Unable to open file";

	cout << vec2str(blocks) << endl;

	cout << findIterations(blocks) << endl;

	return 0;
}

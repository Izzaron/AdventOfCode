//============================================================================
// Name        : Advent10b.cpp
// Author      : 
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <iomanip>
using namespace std;

void reverse_list(vector<int> &list, int current_pos, int length) {
	vector<int> tmp_list(list.begin() + current_pos,list.end());
	tmp_list.insert(tmp_list.end(),list.begin(),list.begin() + current_pos);

	reverse(tmp_list.begin(),tmp_list.begin()+length);

	vector<int>::iterator tmp_it = tmp_list.end() - current_pos;
	for(vector<int>::iterator it = list.begin(); it != list.end(); it++) {
		if(tmp_it == tmp_list.end())
			tmp_it = tmp_list.begin();
		*it = *tmp_it;
		tmp_it++;
	}
}

int densify(vector<int>::iterator begin, vector<int>::iterator end) {

	int result = 0;
	for(vector<int>::iterator it = begin; it != end; it++)
		result = result ^ *it;

	return result;
}

int main() {

	ifstream myfile ("input.txt");

	vector<int> lengths;

	char c;
	while (myfile.get(c)) {
		lengths.push_back((int)c);
	}

	lengths.push_back(17);
	lengths.push_back(31);
	lengths.push_back(73);
	lengths.push_back(47);
	lengths.push_back(23);

	vector<int> list;
	for(int i = 0; i < 256; i++)
		list.push_back(i);

	//for(vector<int>::iterator it = lengths.begin(); it != lengths.end(); it++)
	//	cout << *it << " ";

	int current_pos = 0;
	int skip_size = 0;

	for(int i = 0; i<64;i++) {
		for(vector<int>::iterator it = lengths.begin(); it != lengths.end(); it++) {
			reverse_list(list, current_pos, *it);
			current_pos += *it + skip_size;
			current_pos = current_pos%list.size();
			skip_size++;
		}
	}

	//sparse hash -> dense hash
	vector<int> dense_list(16);
	int i = 0;
	for(vector<int>::iterator it = dense_list.begin(); it != dense_list.end(); it++) {
		*it = densify(list.begin()+i*16,list.begin()+(i+1)*16);
		i++;
	}

	//dense hash -> hexadecimal
	for(vector<int>::iterator it = dense_list.begin(); it != dense_list.end(); it++)
		//cout << hex << *it << " ";
		cout << setfill('0') << setw(2) << hex << *it;

	return 0;
}

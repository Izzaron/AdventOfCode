//============================================================================
// Name        : Advent10.cpp
// Author      : 
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
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

	/*
	for(vector<int>::iterator it = list.begin(); it != list.end(); it++)
			cout << *it << " ";
	cout << endl;
	for(vector<int>::iterator it = tmp_list.begin(); it != tmp_list.end(); it++)
			cout << *it << " ";
	*/
}

int main() {

	ifstream myfile ("input.txt");
	string data;
	stringstream ss;

	myfile >> data;
	replace(data.begin(),data.end(),',',' ');
	ss << data;

	int num;
	vector<int> lengths;
	while(ss>>num) {
		lengths.push_back(num);
	}

	vector<int> list;
	for(int i = 0; i < 256; i++)
		list.push_back(i);

	//for(vector<int>::iterator it = lengths.begin(); it != lengths.end(); it++)
	//	cout << *it << " ";

	int current_pos = 0;
	int skip_size = 0;
	for(vector<int>::iterator it = lengths.begin(); it != lengths.end(); it++) {
		reverse_list(list, current_pos, *it);
		current_pos += *it + skip_size;
		current_pos = current_pos%list.size();
		skip_size++;
	}

	//reverse_list(list,2,4);

	cout << endl;
	cout << list[0]*list[1] << endl;

	string str = "1,2,3";
	for(string::iterator it = str.begin(); it != str.end(); it++) {

		cout << (int)*it << endl;
	}

	return 0;
}

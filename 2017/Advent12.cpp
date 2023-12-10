//============================================================================
// Name        : Advent12.cpp
// Author      : 
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <map>
#include <algorithm>

using namespace std;


class Program {
public:
	string name;
	int number;
	string stands_on;
	vector<string> holds;
};

void gg_rec (Program prog, map<string,Program> namelist, vector<string> &list) {

	for(vector<string>::iterator it = prog.holds.begin(); it != prog.holds.end(); it++) {
		if(find(list.begin(),list.end(),*it) == list.end()) {
			list.push_back(*it);
			gg_rec(namelist[*it],namelist,list);
		}
	}
}

vector<string> getGroup(Program prog, map<string,Program> namelist) {

	vector<string> list;

	list.push_back(prog.name);

	for(vector<string>::iterator it = prog.holds.begin(); it != prog.holds.end(); it++) {
		if(find(list.begin(),list.end(),*it) == list.end()) {
			list.push_back(*it);
			gg_rec(namelist[*it],namelist,list);
		}
	}

	return list;
}

int main() {

	map<string,Program> namelist;
	string line;
	ifstream myfile ("input.txt");

	//Read the programs into a <string,Program*> map
	if (myfile.is_open()) {
		while ( getline (myfile,line) ) {

			istringstream iss(line);
			string word;
			while (iss>>word) {
				Program &prog = namelist[word];
				prog.name = word;
				iss>>word;
				while (iss>>word) {
					word.erase (remove(word.begin(), word.end(), ','), word.end());
					prog.holds.push_back(word);
				}
			}
		}
		myfile.close();
	} else cout << "Unable to open file";



	//Part 1
	cout << getGroup(namelist["0"],namelist).size() << endl;


	//Part 2
	map<string,Program> progs = namelist;

	int number_of_groups = 0;
	while(progs.size() != 0) {

		vector<string> curr_group = getGroup(progs.begin()->second,namelist);

		for(vector<string>::iterator it = curr_group.begin(); it != curr_group.end(); it++) progs.erase(*it);

		number_of_groups++;
	}

	cout << number_of_groups << endl;

	return 0;
}

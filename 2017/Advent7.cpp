//============================================================================
// Name        : Advent7.cpp
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
using namespace std;

class Program {
public:
	string name;
	int number;
	string stands_on;
	vector<string> holds;
};

int getsumof(Program prog,map<string,Program> &namelist) {
	int sum = prog.number;
	vector<string> holds = prog.holds;
	for(vector<string>::iterator it = holds.begin();it!=holds.end();it++) {
		sum += getsumof(namelist[*it],namelist);
	}
	return sum;
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
				sscanf(word.c_str(),"(%d)",&prog.number);
				if(iss>>word) {
					while (iss>>word) {
						word.erase (remove(word.begin(), word.end(), ','), word.end());
						prog.holds.push_back(word);
					}
				}
			}
		}
		myfile.close();
	} else cout << "Unable to open file";

	//cout << namelist.size() << endl;

	//cout << namelist["hyehtm"]->number << endl;
	vector<string> unique_list(namelist.size());
	int i = 0;
	for(map<string,Program>::iterator it = namelist.begin();it != namelist.end();it++) {
		unique_list[i] = it->second.name;
		i++;
	}

	for(map<string,Program>::iterator it = namelist.begin();it != namelist.end();it++) {
		vector<string> holds = it->second.holds;
		for(vector<string>::iterator it = holds.begin();it!=holds.end();it++) {
			unique_list.erase(remove(unique_list.begin(), unique_list.end(), *it), unique_list.end());
		}
	}

	for(vector<string>::iterator it = unique_list.begin();it!=unique_list.end();it++) {
		cout << "Part A: " << *it << endl;
	}

	//PART B


	for(map<string,Program>::iterator it = namelist.begin();it != namelist.end();it++) {
		//cout << it->second->name << endl;
		if(it->second.holds.empty()) continue;
		vector<string> holds = it->second.holds;
		int firstchildnum = getsumof(namelist[*(holds.begin())],namelist);
		for(vector<string>::iterator itt = holds.begin()+1;itt!=holds.end();itt++) {
			int otherchildsum = getsumof(namelist[*itt],namelist);
			if(firstchildnum != otherchildsum) {
				//cout << it->second->name << ": Child0: " << firstchildnum << ", Child" << itt - holds.begin() << ": " << otherchildsum << endl;
				for(vector<string>::iterator it3 = holds.begin();it3!=holds.end();it3++) {
					cout << it->second.name << ": " << namelist[*it3].name << ": " << getsumof(namelist[*it3],namelist) << endl;
				}
				cout << endl;
			}

		}
		//if(childsum != 0 && it->second->number != childsum) cout << it->second->name << "(" << it->second->number << "): " << childsum << endl;
	}

	cout << "ycpcv: " << namelist["ycpcv"].number << endl;

	vector<string> holds = namelist["ycpcv"].holds;
	for(vector<string>::iterator it = holds.begin();it!=holds.end();it++) {
		cout << namelist[*it].name << ": " << getsumof(namelist[*it],namelist) << endl;
	}

	cout << endl;
	cout << "eionkb: " << namelist["eionkb"].number << endl;
	holds = namelist["eionkb"].holds;
	for(vector<string>::iterator it = holds.begin();it!=holds.end();it++) {
		cout << namelist[*it].name << ": " << getsumof(namelist[*it],namelist) << endl;
	}

	return 0;
}

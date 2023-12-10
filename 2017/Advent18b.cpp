//============================================================================
// Name        : Advent18b.cpp
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
#include <string>
#include <cctype>
using namespace std;

int readLines(vector<string>::iterator &it, vector<string>::iterator linesbegin, vector<string>::iterator linesend, map<char,long long int> &regs, vector< vector<int> > &letter, int id, int &counter, bool &waiting) {

	//int lastplayed = 0;

	//for(vector<string>::iterator it = master_it; it != lines.end(); it++) {
	while (it != linesend) {

		string line = *it;
		string word;
		istringstream iss(line);

		if(waiting) {
			iss>>word;
			word = "rcv";
		} else {
			iss>>word;
		}

		if(word == "snd") { //DONE
			char reg;
			int val, c;
			iss >> std::ws;
			c = iss.peek();
			if ( isdigit(c) || c == '-' ) {
				iss >> val;
				if(id == 0)
					letter[1].push_back(val);
				else
					letter[0].push_back(val);
				//cout << "Playing " << val << endl;
			} else {
				iss >> reg;
				if(regs.count(reg) == 0) regs[reg] = 0;
				if(id == 0)
					letter[1].push_back(regs[reg]);
				else
					letter[0].push_back(regs[reg]);
				//cout << "Playing " << regs[reg] << endl;
			}
			counter++;
		} else if(word == "set") { //DONE
			//Read register to write to (argument 1)
			char reg1, reg2;
			iss >> reg1;
			//if(regs.count(reg1) == 0) regs[reg1] = 0; ---removed 18/12 23:49

			//Check if argument 2 is a register or a number
			int val, c;
			iss >> ws;
			c = iss.peek();

			if ( isdigit(c) || c == '-' ) {
				iss >> val;
				regs[reg1] = val;
				//cout << "setting " << reg1 << " to " << val << endl;
			} else {
				iss >> reg2;
				if(regs.count(reg2) == 0) cout << "Error at line \"" << line << "\". Cannot find " << reg2 << " in regs." << endl;
				regs[reg1] = regs[reg2];
				//cout << "setting " << reg1 << " to " << reg2 << " = " << regs[reg2] << endl;
			}
		} else if(word == "add") { //DONE
			//Read register to write to (argument 1)
			char reg1, reg2;
			iss >> reg1;
			if(regs.count(reg1) == 0) regs[reg1] = 0;

			//Check if argument 2 is a register or a number
			int val, c;
			iss >> ws;
			c = iss.peek();

			if ( isdigit(c) || c == '-' ) {
				iss >> val;
				regs[reg1] += val;
				//cout << "increasing " << reg1 << " by " << val << " = " << regs[reg1] << endl;
			} else {
				iss >> reg2;
				if(regs.count(reg2) == 0) cout << "Error at line \"" << line << "\". Cannot find " << reg2 << " in regs." << endl;
				regs[reg1] += regs[reg2];
				//cout << "increasing " << reg1 << " by " << reg2 << "(" << regs[reg2] << ") = " << regs[reg1] << endl;
			}
		} else if(word == "mul") { //DONE
			//Read register to write to (argument 1)
			char reg1, reg2;
			iss >> reg1;
			if(regs.count(reg1) == 0) regs[reg1] = 0;

			//Check if argument 2 is a register or a number
			int val, c;
			iss >> ws;
			c = iss.peek();

			if ( isdigit(c) || c == '-' ) {
				iss >> val;
				regs[reg1] *= val;
				//cout << "multiplying " << reg1 << " by " << val << " = " << regs[reg1] << endl;

			} else {
				iss >> reg2;
				if(regs.count(reg2) == 0) cout << "Error at line \"" << line << "\". Cannot find " << reg2 << " in regs." << endl;
				regs[reg1] *= regs[reg2];
				//cout << "multiplying " << reg1 << " by " << reg2 << "(" << regs[reg2] << ") = " << regs[reg1] << endl;
			}
		} else if(word == "mod") { //DONE
			//Read register to write to (argument 1)
			char reg1, reg2;
			iss >> reg1;
			if(regs.count(reg1) == 0) cout << "Error at line \"" << line << "\". Cannot find " << reg1 << " in regs." << endl;

			//Check if argument 2 is a register or a number
			int val, c;
			iss >> ws;
			c = iss.peek();

			if ( isdigit(c) || c == '-' ) {
				iss >> val;
				regs[reg1] = regs[reg1]%val;
				//cout << "mod: " << reg1 << " % " << val << " = " << regs[reg1] << endl;
			} else {
				iss >> reg2;
				if(regs.count(reg2) == 0) cout << "Error at line \"" << line << "\". Cannot find " << reg2 << " in regs." << endl;
				regs[reg1] = regs[reg1]%regs[reg2];
				//cout << "mod: " << reg1 << " % " << reg2 << "(" << regs[reg2] << ") = " << regs[reg1] << endl;
			}
		} else if(word == "rcv") { //DONE

			//cout << "Program " << id << " calling rcv. Letter length: " << letter[id].size() << endl;
			waiting = false;

			if(letter[id].empty()) {
				waiting = true;
				return 1;
			}

			char reg;
			int c;
			iss >> std::ws;
			c = iss.peek();
			if ( isdigit(c) || c == '-' ) {
				cout << "Found digit, expected register at line: " << line << endl;
				return -1;
			} else {
				iss >> reg;
				regs[reg] = letter[id].front();
				letter[id].erase(letter[id].begin());
			}

		} else if(word == "jgz") {
			char reg1, reg2;

			int c0;
			iss >> ws;
			c0 = iss.peek();
			iss >> reg1;
			if ( isdigit(c0) && c0 == '1') {
				it += 3;
				if(it<linesbegin || it >= linesend) {
					cout << "Jumped out of bounds with line \"" << line << "\"" << endl;
					return 0;
				}
				continue;
			} else {
				if(regs.count(reg1) == 0) regs[reg1] = 0;

				if(regs[reg1] == 0) {
					//cout << "Jump cancelled because " << reg1 << " = " << regs[reg1] << endl;
					it++;
					continue;
				}
			}

			int val, c;
			iss >> ws;
			c = iss.peek();
			if ( isdigit(c) || c == '-') {
				iss >> val;
				if(regs[reg1] > 0) {
					//Check bounds
					if(val == 0) {
						cout << "Infinite loop detected at line: \"" << line << "\". Second argument is " << val << endl;
						return -1;
					}

					it += val-1;

					if(it<linesbegin || it >= linesend) {
						cout << "Jumped out of bounds with line \"" << line << "\"" << endl;
						return 0;
					}
					//cout << "Jumping " << val << endl;
				}
			} else {
				iss >> reg2;
				if(regs.count(reg2) == 0 || regs[reg2] == 0) {
					cout << "Infinite loop detected at line: \"" << line << "\". Second argument is " << regs[reg2] << endl;
					return -1;
				}

				it += regs[reg2]-1;

				if(it<linesbegin || it >= linesend) {
					cout << "Jumped out of bounds with line \"" << line << "\"" << endl;
					return 0;
				}
				//cout << "Jumping " << reg2 << "(" << regs[reg2] << ")" << endl;
			}

		} else cout << "Do not recognise instruction: " << word << endl;
		it++;
	}
	return 0;
}

int main() {

	vector<string> lines;
	string line;
	ifstream myfile ("input.txt");

	if (myfile.is_open()) {
		while ( getline (myfile,line) ) {
			lines.push_back(line);
		}
		myfile.close();
	} else cout << "Unable to open file";

	map<char,long long int> regs0;
	map<char,long long int> regs1;

	regs0['p'] = 0;
	regs1['p'] = 1;

	vector< vector<int> > letter(2);

	int counter0 = 0;
	int counter1 = 0;

	vector<string>::iterator it0 = lines.begin();
	vector<string>::iterator it1 = lines.begin();

	bool waiting0 = false;
	bool waiting1 = false;

	//return -1 = error
	//return  0 = out of bounds
	//return  1 = empty letter at receive
	while(true) {

		if(letter[0].empty() && waiting0) break;
		int p0 = readLines(it0, lines.begin(), lines.end(), regs0, letter, 0, counter0, waiting0);
		cout << "p0 sends a " << letter[1].size() << " long letter to p1" << endl;
		if(p0 == -1) break;

		if(letter[1].empty() && waiting1) break;
		int p1 = readLines(it1, lines.begin(), lines.end(), regs1, letter, 1, counter1, waiting1);
		cout << "p1 sends a " << letter[0].size() << " long letter to p0" << endl;
		if(p1 == -1) break;

		//break;

	}
	cout << "Both programs terminated. counter 1 = " << counter1 << endl;

	return 0;
}

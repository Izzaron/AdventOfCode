//============================================================================
// Name        : Advent23.cpp
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

void readLines(vector<string> lines, int &mul_calls) {

//	int lastplayed = 0;
	map<char,long long int> regs;
	regs['a'] = 1;
	regs['b'] = 0;
	regs['c'] = 0;
	regs['d'] = 0;
	regs['e'] = 0;
	regs['f'] = 0;
	regs['g'] = 0;
	regs['h'] = 0;

	for(vector<string>::iterator it = lines.begin(); it != lines.end(); it++) {
		string line = *it;

//		if(line == "set e 2") {
//			for(map<char,long long int>::iterator map_it = regs.begin(); map_it != regs.end(); map_it++)
//				cout << map_it->first << " = " << map_it->second << endl;
//			cout << line << endl;
//			break;
//		}
		if(line == "set f 0") regs['e'] = 109899;

		istringstream iss(line);
		string word;
		iss>>word;

		if(word == "set") { //DONE
			//Read register to write to (argument 1)
			char reg1, reg2;
			iss >> reg1;

			//Check if argument 2 is a register or a number
			int val, c;
			iss >> ws;
			c = iss.peek();

			if ( isdigit(c) || c == '-' ) {
				iss >> val;
				regs[reg1] = val;
//				cout << reg1 << " set to " << val << endl;
			} else {
				iss >> reg2;
				if(regs.count(reg2) == 0) cout << "Error at line \"" << line << "\". Cannot find " << reg2 << " in regs." << endl;
				regs[reg1] = regs[reg2];
//				cout << reg1 << " set to " << reg2 << "(" << regs[reg2] << ")" << endl;
			}
		} else if(word == "sub") { //DONE
			//Read register to write to (argument 1)
			char reg1, reg2;
			iss >> reg1;
			if(regs.count(reg1) == 0) cout << "Error, unrecognised register: " << reg1 << endl;

			//Check if argument 2 is a register or a number
			int val, c;
			iss >> ws;
			c = iss.peek();

			if ( isdigit(c) || c == '-' ) {
				iss >> val;
				regs[reg1] -= val;
//				cout << reg1 << " - " << val << " = " << regs[reg1] << endl;
			} else {
				iss >> reg2;
				if(regs.count(reg2) == 0) cout << "Error at line \"" << line << "\". Cannot find " << reg2 << " in regs." << endl;
				regs[reg1] -= regs[reg2];
//				cout << reg1 << " - " << reg2 << "(" << regs[reg2] << ") = " << regs[reg1] << endl;
			}
		} else if(word == "mul") { //DONE
			mul_calls++;
			//Read register to write to (argument 1)
			char reg1, reg2;
			iss >> reg1;
			if(regs.count(reg1) == 0) cout << "Error, unrecognised register: " << reg1 << endl;

			//Check if argument 2 is a register or a number
			int val, c;
			iss >> ws;
			c = iss.peek();

			if ( isdigit(c) || c == '-' ) {
				iss >> val;
				regs[reg1] *= val;
//				cout << reg1 << " * " << val << " = " << regs[reg1] << endl;

			} else {
				iss >> reg2;
				if(regs.count(reg2) == 0) cout << "Error at line \"" << line << "\". Cannot find " << reg2 << " in regs." << endl;
				regs[reg1] *= regs[reg2];
//				cout << reg1 << " * " << reg2 << "(" << regs[reg2] << ") = " << regs[reg1] << endl;
			}
		} else if(word == "jnz") {
			char reg1, reg2;
			iss >> reg1;
			if(reg1 != '1') {
				if(regs.count(reg1) == 0) cout << "Error, unrecognised register: " << reg1 << endl;

				if(regs[reg1] == 0) {
//					cout << "Skipping jump because " << reg1 << " is 0" << endl;
					continue;
				}
			}// else cout << "reg1 = 1" << endl;

			int val, c;
			iss >> ws;
			c = iss.peek();
			if ( isdigit(c) || c == '-') {
				iss >> val;
				if(val == 0) {
					cout << "Infinite loop detected at line: \"" << line << "\". Second argument is " << val << endl;
					return;
				}

				it += val-1;

				if(it<lines.begin() || it >= lines.end()) {
					cout << "Jumped out of bounds with line \"" << line << "\"" << endl;
					return;
				}
//				cout << "Jumping " << val << endl;
			} else {
				iss >> reg2;
				cout << "reg2 = " << reg2 << endl;
				if(regs.count(reg2) == 0 || regs[reg2] == 0) {
					cout << "Infinite loop detected at line: \"" << line << "\". Second argument is " << regs[reg2] << endl;
					return;
				}

				it += regs[reg2]-1;

				if(it<lines.begin() || it >= lines.end()) {
					cout << "Jumped out of bounds with line \"" << line << "\"" << endl;
					return;
				}
//				cout << "Jumping " << reg2 << "(" << regs[reg2] << ")" << endl;
			}

		} else cout << "Do not recognise instruction: " << word << endl;

	}

	cout << "register h is " << regs['h'] << endl;

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

	int mul_calls = 0;
	readLines(lines, mul_calls);

	cout << mul_calls << endl;

	return 0;
}

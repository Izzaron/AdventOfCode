//============================================================================
// Name        : Advent18.cpp
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

void readLines(vector<string> lines) {

	int lastplayed = 0;
	map<char,long long int> regs;

	for(vector<string>::iterator it = lines.begin(); it != lines.end(); it++) {
		string line = *it;

		istringstream iss(line);
		string word;
		iss>>word;

		if(word == "snd") { //DONE
			char reg;
			int val, c;
			iss >> std::ws;
			c = iss.peek();
			if ( isdigit(c) || c == '-' ) {
				iss >> val;
				lastplayed = val;
				cout << "Playing " << val << endl;
			} else {
				iss >> reg;
				if(regs.count(reg) == 0) regs[reg] = 0;
				lastplayed = regs[reg];
				cout << "Playing " << regs[reg] << endl;
			}
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
				cout << "setting " << reg1 << " to " << val << endl;
			} else {
				iss >> reg2;
				if(regs.count(reg2) == 0) cout << "Error at line \"" << line << "\". Cannot find " << reg2 << " in regs." << endl;
				regs[reg1] = regs[reg2];
				cout << "setting " << reg1 << " to " << reg2 << " = " << regs[reg2] << endl;
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
				cout << "increasing " << reg1 << " by " << val << " = " << regs[reg1] << endl;
			} else {
				iss >> reg2;
				if(regs.count(reg2) == 0) cout << "Error at line \"" << line << "\". Cannot find " << reg2 << " in regs." << endl;
				regs[reg1] += regs[reg2];
				cout << "increasing " << reg1 << " by " << reg2 << "(" << regs[reg2] << ") = " << regs[reg1] << endl;
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
				cout << "multiplying " << reg1 << " by " << val << " = " << regs[reg1] << endl;

			} else {
				iss >> reg2;
				if(regs.count(reg2) == 0) cout << "Error at line \"" << line << "\". Cannot find " << reg2 << " in regs." << endl;
				regs[reg1] *= regs[reg2];
				cout << "multiplying " << reg1 << " by " << reg2 << "(" << regs[reg2] << ") = " << regs[reg1] << endl;
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
				cout << "mod: " << reg1 << " % " << val << " = " << regs[reg1] << endl;
			} else {
				iss >> reg2;
				if(regs.count(reg2) == 0) cout << "Error at line \"" << line << "\". Cannot find " << reg2 << " in regs." << endl;
				regs[reg1] = regs[reg1]%regs[reg2];
				cout << "mod: " << reg1 << " % " << reg2 << "(" << regs[reg2] << ") = " << regs[reg1] << endl;
			}
		} else if(word == "rcv") { //DONE
			char reg;
			int val, c;
			iss >> std::ws;
			c = iss.peek();
			if ( isdigit(c) || c == '-' ) {
				iss >> val;
				if(val != 0) {
					cout << "Recovered " << lastplayed;
					return;
				} else cout << "Recover failed because " << val  << " = 0" << endl;
			} else {
				iss >> reg;
				if(regs.count(reg) == 0) regs[reg] = 0;
				if(regs[reg] != 0) {
					cout << "Recovered " << lastplayed;
					return;
				} else cout << "Recover failed because " << reg << "(" << regs[reg] << ") = 0" << endl;
			}

		} else if(word == "jgz") {
			char reg1, reg2;
			iss >> reg1;
			if(regs.count(reg1) == 0) regs[reg1] = 0;

			if(regs[reg1] == 0) {
				cout << "Jump cancelled because " << reg1 << " = " << regs[reg1] << endl;
				continue;
			}

			int val, c;
			iss >> ws;
			c = iss.peek();
			if ( isdigit(c) || c == '-') {
				iss >> val;
				if(regs[reg1] > 0) {
					//CHeck bounds
					if(val == 0) {
						cout << "Infinite loop detected at line: \"" << line << "\". Second argument is " << val << endl;
						return;
					}

					it+= val-1;

					if(it<lines.begin() || it >= lines.end()) {
						cout << "Jumped out of bounds with line \"" << line << "\"" << endl;
						return;
					}
					cout << "Jumping " << val << endl;
				}
			} else {
				iss >> reg2;
				if(regs.count(reg2) == 0 || regs[reg2] == 0) {
					cout << "Infinite loop detected at line: \"" << line << "\". Second argument is " << regs[reg2] << endl;
					return;
				}

				it+= regs[reg2]-1;

				if(it<lines.begin() || it >= lines.end()) {
					cout << "Jumped out of bounds with line \"" << line << "\"" << endl;
					return;
				}
				cout << "Jumping " << reg2 << "(" << regs[reg2] << ")" << endl;
			}

		} else cout << "Do not recognise instruction: " << word << endl;

	}

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

	readLines(lines);

	return 0;
}

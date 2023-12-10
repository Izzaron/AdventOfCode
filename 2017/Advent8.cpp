//============================================================================
// Name        : Advent8.cpp
// Author      : 
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <fstream>
#include <sstream>
#include <map>
using namespace std;

void mod_register(string register_name, int incdec_val, map<string,int> &register_list) {
	if(register_list.count(register_name) == 0)
			register_list[register_name] = 0;

	register_list[register_name] += incdec_val;
}

bool test_reg_cond(string register_cond_name,string reg_cond_op, int reg_cond_val, map<string,int> &register_list) {

	if(register_list.count(register_cond_name) == 0)
		register_list[register_cond_name] = 0;

	if(reg_cond_op == "<") {
		if(register_list[register_cond_name] < reg_cond_val) return true;
	} else if(reg_cond_op == ">") {
		if(register_list[register_cond_name] > reg_cond_val) return true;
	} else if(reg_cond_op == "<=") {
		if(register_list[register_cond_name] <= reg_cond_val) return true;
	} else if(reg_cond_op == ">=") {
		if(register_list[register_cond_name] >= reg_cond_val) return true;
	} else if(reg_cond_op == "==") {
		if(register_list[register_cond_name] == reg_cond_val) return true;
	} else if(reg_cond_op == "!=") {
		if(register_list[register_cond_name] != reg_cond_val) return true;
	} else cout << "Couldnt identify operator" << endl;

	return false;
}

int main() {

	map<string,int> register_list;

	string line;
	ifstream myfile ("input.txt");

	int max_held = 0;

	if (myfile.is_open()) {
		while ( getline (myfile,line) ) {
			istringstream iss(line);
			string word;

			string register_name = word;
			iss >> register_name;

			string incdec_sign;
			iss>> incdec_sign;

			int incdec_val;
			iss >> incdec_val;

			iss >> word; //discard "if"

			string register_cond_name;
			iss >> register_cond_name;

			string reg_cond_op;
			iss >> reg_cond_op;

			int reg_cond_val;
			iss >> reg_cond_val;
			//cout << register_name << " " << incdec_sign << " " << incdec_val << " " << register_if << " " << reg_cond_op << " " << reg_cond_val << endl;

			if(test_reg_cond(register_cond_name, reg_cond_op, reg_cond_val, register_list)) {
				if(incdec_sign == "inc") {
					mod_register(register_name, incdec_val, register_list);
				} else if(incdec_sign == "dec") {
					mod_register(register_name, -1*incdec_val, register_list);
				} else cout << "neither inc nor dec" << endl;
			}

			if(register_list[register_name] > max_held)
				max_held = register_list[register_name];
		}
		myfile.close();
	} else cout << "Unable to open file";

	string max_name = register_list.begin()->first;
	int max_val = register_list.begin()->second;
	for(map<string,int>::iterator it = register_list.begin();it != register_list.end();it++) {
		if(it->second>max_val) {
			max_name = it->first;
			max_val = it->second;
		}
	}

	cout << max_name << " = " << max_val << endl;

	cout << "Max held: " << max_held << endl;

	return 0;
}

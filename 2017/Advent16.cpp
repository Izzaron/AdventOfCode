//============================================================================
// Name        : Advent16.cpp
// Author      : 
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <string>
#include <algorithm>
using namespace std;

class Instruction {
private:
	char type;
	int par1;
	int par2;
	char c1;
	char c2;
public:
	//Spin constructor
	Instruction(int p1) {
		type = 's';
		par1 = p1;
		par2 = 0;
		c1 = '0';
		c2 = '0';
	}
	//Exchange constructor
	Instruction(int p1, int p2) {
		type = 'x';
		par1 = p1;
		par2 = p2;
		c1 = '0';
		c2 = '0';
	}
	//Partner constructor
	Instruction(char ch1, char ch2) {
		type = 'p';
		par1 = 0;
		par2 = 0;
		c1 = ch1;
		c2 = ch2;
	}

	void execute(string &word) {
		if(type=='s') {
			string tmp_input = word.substr(word.size()-par1);
			tmp_input += word.substr(0,word.size()-par1);
			word = tmp_input;
		} else if(type=='x') {
			char tmp = word[par1];
			word[par1] = word[par2];
			word[par2] = tmp;
		} else if(type=='p') {
			size_t pos1 = word.find(c1);
			size_t pos2 = word.find(c2);
			char tmp = word[pos1];
			word[pos1] = word[pos2];
			word[pos2] = tmp;
		} else cout << "Unexpectedly found " << type << " as type." << endl;
	}

};

int main() {

	clock_t t = clock();

	string word = "abcdefghijklmnop";
	vector<Instruction> instructions;

	string input;
	ifstream myfile ("input.txt");

	if (myfile.is_open()) {

		//Replace all "," with spaces
		myfile >> input;
		size_t found = input.find(',');
		while(found != string::npos) {
			input[found] = ' ';
			found = input.find(',');
		}
		myfile.close();
	} else cout << "Unable to open file";

	//Process instructions
	istringstream iss(input);
	string instruction;

	while (iss>>instruction) {
		if(instruction[0] == 's') {

			//Convert instruction string to int
			istringstream spos(instruction.substr(1));
			int pos;
			spos >> pos;

			instructions.push_back(Instruction(pos));


		} else if(instruction[0] == 'x') {

			int pos1;
			int pos2;
			sscanf(instruction.c_str(),"x%d/%d)",&pos1,&pos2);

			instructions.push_back(Instruction(pos1,pos2));

		} else if(instruction[0] == 'p') {

			instructions.push_back(Instruction(instruction[1],instruction[3]));

		} else cout << "Can't read instruction" << endl;
	}



	cout << word << endl;

	string test_word = word;
	for(vector<Instruction>::iterator it = instructions.begin(); it != instructions.end(); it++)
		it->execute(test_word);

	clock_t t1 = clock();
	cout << "It took " << (double)(t1 - t)/CLOCKS_PER_SEC << " seconds to initialise." << endl;

	cout << test_word << endl;

	int iterations = 1000000000;
	for(int i = 0; i < iterations; i++) {
		string tmp_word = "abcdefghijklmnop";
		tmp_word[0] = word[3]; //a
		tmp_word[1] = word[14]; //b
		tmp_word[2] = word[4]; //c
		tmp_word[3] = word[0]; //d
		tmp_word[4] = word[8]; //e
		tmp_word[5] = word[12]; //f
		tmp_word[6] = word[11]; //g
		tmp_word[7] = word[1]; //h
		tmp_word[8] = word[13]; //i
		tmp_word[9] = word[15]; //j
		tmp_word[10] = word[9]; //k
		tmp_word[11] = word[2]; //l
		tmp_word[12] = word[7]; //m
		tmp_word[13] = word[5]; //n
		tmp_word[14] = word[10]; //o
		tmp_word[15] = word[6]; //p
		word = tmp_word;
	}

	cout << word << endl;

	cout << "It took " << (double)(clock() - t1)/CLOCKS_PER_SEC << " seconds to perform " << iterations << " iterations." << endl;

	return 0;
}

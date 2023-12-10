//============================================================================
// Name        : Advent21.cpp
// Author      : 
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <algorithm>
using namespace std;

class Grid {
private:
	vector< string > matrix;
public:
	Grid();

	Grid(int size) { for(int i = 0; i < size; i++) matrix.push_back(string(size,'.')); }

	Grid(string input) {
		size_t size = input.find('/');
		input.erase(remove(input.begin(),input.end(),'/'),input.end());
		for(size_t i = 0; i != size; i++)
			matrix.push_back(input.substr(i*size,size));
	}

	void print() {
		for(vector<string>::iterator line = matrix.begin(); line != matrix.end(); line++)
			cout << *line << endl;
	}

	int activePixels() {
		int sum = 0;
		for(vector<string>::iterator line = matrix.begin(); line != matrix.end(); line++)
			sum += count(line->begin(),line->end(),'#');
		return sum;
	}

	int size() {
		return matrix.size();
	}

	string getMoldOfSizeAt(int size, int x, int y) {
		if(size + x > matrix.size() || size + y > matrix.size() || x < 0 || y < 0 || size < 1) {
			cout << "getMoldOfSizeAt call out of bounds" << endl;
			cout << "size: " << size << ", x: " << x << ", y: " << y << " given to grid;" << endl;
			this->print();
			return "";
		}

		string gridMold = "";
		for(int i = 0; i < size; i++) {
			gridMold += matrix[y+i].substr(x,size);
			gridMold += '/';
		}

		return gridMold;
	}

	void setMoldAt(string mold, int x, int y) {
		int size = mold.find('/');
		if(size + x > matrix.size() || size + y > matrix.size() || x < 0 || y < 0 || size < 1) {
			cout << "setMoldAt call out of bounds" << endl;
			cout << "mold: " << mold << " of size " << size << " for x: " << x << ", y: " << y << " given to grid;" << endl;
			this->print();
			return;
		}

		mold.erase(remove(mold.begin(),mold.end(),'/'),mold.end());
		for(size_t i = 0; i != size; i++)
			matrix[y+i].replace(x,size,mold,i*size,size); //sätt in på rätt plats
	}
};

string flipHort(string input) {
	size_t size = input.find('/');
	if(size != 2 && size != 3) cout << "Incorrect size " << size << " given to flipHort" << endl;
	string returnStr = input;
	swap_ranges(returnStr.begin(),returnStr.begin()+size,returnStr.end()-size);
	return returnStr;
}

string flipVert(string input) {
	int size = input.find('/');
	string returnStr = input;
	if(size == 2) {
		swap(returnStr[0], returnStr[1]);
		swap(returnStr[3], returnStr[4]);
	} else if(size == 3) {
		swap(returnStr[0], returnStr[2]);
		swap(returnStr[4], returnStr[6]);
		swap(returnStr[8], returnStr[10]);
	} else cout << "Incorrect size " << size << " given to flipVert" << endl;
	return returnStr;
}

string rot(string input, int angle) {
	int size = input.find('/');
	string returnStr = input;

	if(size == 2) {
		if(angle == 1) {
			returnStr[0] = input[3];
			returnStr[1] = input[0];
			returnStr[3] = input[4];
			returnStr[4] = input[1];
		} else if(angle == 2) {
			returnStr[0] = input[4];
			returnStr[1] = input[3];
			returnStr[3] = input[1];
			returnStr[4] = input[0];
		} else if(angle == 3) {
			returnStr[0] = input[1];
			returnStr[1] = input[4];
			returnStr[3] = input[0];
			returnStr[4] = input[3];
		}
	} else if(size == 3) {
		if(angle == 1) {
			returnStr[0] = input[8];
			returnStr[1] = input[4];
			returnStr[2] = input[0];
			returnStr[4] = input[9];
			returnStr[6] = input[1];
			returnStr[8] = input[10];
			returnStr[9] = input[6];
			returnStr[10] = input[2];
		} else if(angle == 2) {
			returnStr[0] = input[10];
			returnStr[1] = input[9];
			returnStr[2] = input[8];
			returnStr[4] = input[6];
			returnStr[6] = input[4];
			returnStr[8] = input[2];
			returnStr[9] = input[1];
			returnStr[10] = input[0];
		} else if(angle == 3) {
			returnStr[0] = input[2];
			returnStr[1] = input[6];
			returnStr[2] = input[10];
			returnStr[4] = input[1];
			returnStr[6] = input[9];
			returnStr[8] = input[0];
			returnStr[9] = input[4];
			returnStr[10] = input[8];
		}
	} else cout << "Incorrect size " << size << " given to rot" << endl;

	return returnStr;
}

bool doesRuleApply(string input, string rule) {
	bool returnBool = false;
	if(input == rule) {
//		cout << rule << " matched" << endl;
		returnBool = true;
	} else if(input == rot(rule,1)) {
//		cout << rule << " matched" << endl;
		returnBool = true;
	} else if(input == rot(rule,2)) {
//		cout << rule << " matched" << endl;
		returnBool = true;
	} else if(input == rot(rule,3)) {
//		cout << rule << " matched" << endl;
		returnBool = true;
	} else if(input == flipHort(rule)) {
//		cout << rule << " matched" << endl;
		returnBool = true;
	} else if(input == rot(flipHort(rule),1)) {
//		cout << rule << " matched" << endl;
		returnBool = true;
	} else if(input == rot(flipHort(rule),2)) {
//		cout << rule << " matched" << endl;
		returnBool = true;
	} else if(input == rot(flipHort(rule),3)) {
//		cout << rule << " matched" << endl;
		returnBool = true;
	} else {
//		cout << "No matching rule for: " << input << endl;
//		cout << "-------------" << rule << "----------------" << endl;
//		cout << "\"" << input << "\" tried on \"" << rule << "\"" << endl;
//		cout << "\"" << input << "\" tried on \"" << rot(rule,1) << "\"" << endl;
//		cout << "\"" << input << "\" tried on \"" << rot(rule,2) << "\"" << endl;
//		cout << "\"" << input << "\" tried on \"" << rot(rule,3) << "\"" << endl;
//		cout << "\"" << input << "\" tried on \"" << flipHort(rule) << "\"" << endl;
//		cout << "\"" << input << "\" tried on \"" << rot(flipHort(rule),1) << "\"" << endl;
//		cout << "\"" << input << "\" tried on \"" << rot(flipHort(rule),2) << "\"" << endl;
//		cout << "\"" << input << "\" tried on \"" << rot(flipHort(rule),3) << "\"" << endl;
	}
	return returnBool;
}

string applyRule(string input, vector<string> &rules) {
	string returnStr = "";
	int size = input.find('/');
	while(input.back() == '/') input.pop_back();
	if(size == 2) {
		for(vector<string>::iterator it = rules.begin(); it != rules.begin()+6; it++) {
			if(doesRuleApply(input, it->substr(0,5))) {
				returnStr = it->substr(9,11);
				break;
			}
		}
		if(returnStr == "") cout << "No 2 rule applied to: " << input << endl;
	} else if(size == 3) {
		for(vector<string>::iterator it = rules.begin()+6; it != rules.end(); it++) {
			if(doesRuleApply(input, it->substr(0,11))) {

				returnStr = it->substr(15);
				break;
			}
		}
		if(returnStr == "") cout << "No 3 rule applied to: " << input << endl;
	} else {
		cout << "Incorrect size " << size << " given to applyRule. Input: " << input << endl;
	}
	return returnStr;
}

void growGrid(Grid* &grid, vector<string> &rules) {
	if(grid->size() % 2 == 0) {
		Grid* newGrid = new Grid((grid->size()*3)/2);

		for(int y = 0; y < grid->size(); y+=2)
			for(int x = 0; x < grid->size(); x+=2) {
				newGrid->setMoldAt(applyRule(grid->getMoldOfSizeAt(2,x,y),rules),(3*x)/2,(3*y)/2);
			}

		delete grid;
		grid = newGrid;
	} else if(grid->size() % 3 == 0) {
		Grid* newGrid = new Grid((grid->size()*4)/3);

		for(int y = 0; y < grid->size(); y+=3)
			for(int x = 0; x < grid->size(); x+=3) {
				newGrid->setMoldAt(applyRule(grid->getMoldOfSizeAt(3,x,y),rules),(4*x)/3,(4*y)/3);
			}

		delete grid;
		grid = newGrid;
	} else cout << "Grid(" << grid->size() << ") not divisible by neither 2 nor 3" << endl;
}

int main() {

	vector<string> rules;
	string line;
	ifstream myfile ("input.txt");

	if (myfile.is_open()) {
		while ( getline (myfile,line) ) {
			rules.push_back(line);
		}
		myfile.close();
	} else cout << "Unable to open file";

	Grid* main_grid = new Grid(".#./..#/###");


	int iterations = 0;

	cout << iterations << endl;
	main_grid->print();
	cout << endl;

	while(iterations < 18) {
		iterations++;
		growGrid(main_grid, rules);
		cout << iterations << endl;
		main_grid->print();
		cout << endl;
	}

	cout << main_grid->activePixels() << endl;

	return 0;
}

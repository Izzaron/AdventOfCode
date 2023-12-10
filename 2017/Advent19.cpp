//============================================================================
// Name        : Advent19.cpp
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

void printMap(vector<string> map) {
	for(vector<string>::iterator it = map.begin(); it != map.end(); it++)
		cout << *it << endl;
}

vector<string> readMapFromFile(string file_path) {
	vector<string> map;
	string line;
	ifstream myfile (file_path.c_str());
	int map_line = 0;

	if (myfile.is_open()) {
		while ( getline (myfile,line) ) {

			map.push_back( line );
			map_line++;
		}
		myfile.close();
	} else cout << "Unable to open file";

	return map;
}

int main() {

	vector<string> map = readMapFromFile("input.txt");

	vector<char> found_letters;

	int counter = 0;

	int y = 0;
	int x = map[0].find('|');

	enum Direction { up, down, left, right };
	Direction d = down;

	while(true) {
		switch(d){
		case up:
			//cout << "Going up 1 step" << endl;
			y -= 1;
			break;
		case down:
			//cout << "Going down 1 step" << endl;
			y += 1;
			break;
		case left :
			//cout << "Going left 1 step" << endl;
			x -= 1;
			break;
		case right  :
			//cout << "Going right 1 step" << endl;
			x += 1;
			break;
		default:
			cout << "Undefined direction";
	    }

		counter++;

		//cout << "map[" << x << "][" << y << "] = " << map[y][x] << endl;

		if(map[y][x] == '+') {
			switch(d) {
			case up:
				if(map[y][x-1] == '-') d = left;
				if(map[y][x+1] == '-') d = right;
				break;
			case down:
				if(map[y][x-1] == '-') d = left;
				if(map[y][x+1] == '-') d = right;
				break;
			case left :
				if(map[y-1][x] == '|') d = up;
				if(map[y+1][x] == '|') d = down;
				break;
			case right  :
				if(map[y-1][x] == '|') d = up;
				if(map[y+1][x] == '|') d = down;
				break;
			default:
				cout << "Undefined direction";
			}
		} else if(isupper(map[y][x]) || islower(map[y][x])) {
			found_letters.push_back(map[y][x]);
			if(map[y][x] == 'H') break;
		}
	}

	//cout << map[y][x] << endl;

	//Print out answer
	for(vector<char>::iterator it = found_letters.begin(); it != found_letters.end(); it++)
		cout << *it << "";
	cout << endl;

	cout << counter << endl;

	return 0;
}

//============================================================================
// Name        : Advent22b.cpp
// Author      : 
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <fstream>
#include <vector>
#include <map>
#include <string>
#include <time.h>
using namespace std;

class Grid {
private:
	map< vector<long int> ,char> matrix;
public:
	void setAt(long int y, long int x, char c) {
		vector<long int> coordinates(2);
		coordinates[0] = y;
		coordinates[1] = x;
		if(c == '.') {
			matrix.erase(coordinates);
			return;
		}
		matrix[coordinates] = c;
	}

	char getAt(long int y, long int x) {
		vector<long int> coordinates(2);
		coordinates[0] = y;
		coordinates[1] = x;
		if(matrix.count(coordinates) == 0)
			return '.';
		else
			return matrix[coordinates];
	}

	void print() {
		long int min_x = 0;
		long int min_y = 0;
		long int max_x = 0;
		long int max_y = 0;

		for(map< vector<long int> ,char>::iterator node = matrix.begin(); node != matrix.end(); node++) {
			if(node->first[0] < min_y) min_y = node->first[0];
			if(node->first[1] < min_x) min_x = node->first[1];
			if(node->first[0] > max_y) max_y = node->first[0];
			if(node->first[1] > max_x) max_x = node->first[1];
		}

		vector<string> print_grid;
		for(long int i = min_y; i <= max_y; i++)
			print_grid.push_back(string(max_x-min_x+1,'.'));

		for(map< vector<long int> ,char>::iterator node = matrix.begin(); node != matrix.end(); node++)
			print_grid[ node->first[0]-min_y ][ node->first[1]-min_x ] = node->second;

		for(vector<string>::iterator line = print_grid.begin(); line != print_grid.end(); line++)
			cout << *line << endl;
	}

	void readFromFile(string file_name) {
		string line;
		ifstream myfile (file_name.c_str());

		if (myfile.is_open()) {
			long int y = 0;
			while ( getline (myfile,line) ) {
				long int x = 0;
				for(string::iterator it = line.begin(); it != line.end(); it++) {
					this->setAt(y,x,*it);
					x++;
				}
				y++;
			}
			myfile.close();
		} else cout << "Unable to open file";
	}

	vector<long int> getMid() {
		long int min_x = 0;
		long int min_y = 0;
		long int max_x = 0;
		long int max_y = 0;

		for(map< vector<long int> ,char>::iterator node = matrix.begin(); node != matrix.end(); node++) {
			if(node->first[0] < min_y) min_y = node->first[0];
			if(node->first[1] < min_x) min_x = node->first[1];
			if(node->first[0] > max_y) max_y = node->first[0];
			if(node->first[1] > max_x) max_x = node->first[1];
		}

		vector<long int> mid_pos(2);
		mid_pos[0] = (max_y-min_y)/2;
		mid_pos[1] = (max_x-min_x)/2;

		return mid_pos;
	}
};

int main() {

	clock_t t = clock();

	Grid grid;
	grid.readFromFile("input.txt");
//	grid.print();

	long int infects = 0;

	long int y = grid.getMid()[0];
	long int x = grid.getMid()[1];
	enum Direction { up, down, left, right };
	Direction d = up;

	long int burst = 0;
	while(burst < 10000000) {

		char current_node = grid.getAt(y,x);
		if(current_node != '.' && current_node != '#' && current_node != 'F' && current_node != 'W')
			cout << "Current node unrecognised: " << current_node << endl;
		//Step 1 - Turn
		switch(d){
		case up:

			if(current_node == '#') d = right;
			else if(current_node == '.') d = left;
			else if(current_node == 'F') d = down;

			break;
		case down:
			if(current_node == '#') d = left;
			else if(current_node == '.') d = right;
			else if(current_node == 'F') d = up;

			break;
		case left:
			if(current_node == '#') d = up;
			else if(current_node == '.') d = down;
			else if(current_node == 'F') d = right;

			break;
		case right:
			if(current_node == '#') d = down;
			else if(current_node == '.') d = up;
			else if(current_node == 'F') d = left;

			break;
		default:
			cout << "Undefined direction";
		}

		//Step 2 - Infect
		if(current_node == '.') grid.setAt(y,x,'W');
		else if(current_node == 'W') {
			grid.setAt(y,x,'#');
			infects++;
		} else if(current_node == '#') grid.setAt(y,x,'F');
		else if(current_node == 'F') grid.setAt(y,x,'.');

		//Step 3 - Move
		switch(d){
		case up:
			y--;

			break;
		case down:
			y++;

			break;
		case left:
			x--;

			break;
		case right:
			x++;

			break;
		default:
			cout << "Undefined direction";
		}

		burst++;
	}

	cout << infects << " nodes infected." << endl;

	cout << (double)(clock() - t)/CLOCKS_PER_SEC << " seconds runtime."<< endl;

	return 0;
}

//============================================================================
// Name        : Advent14.cpp
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
#include <iomanip>
#include <bitset>
#include <algorithm>
using namespace std;

class Square {
public:
	int x,y,fill,counted;
	vector< Square* > neighbours;
};

void count_neighbours(Square &sq, vector< vector<Square> > &grid) {
	sq.counted = 1;

	for(vector<Square*>::iterator ng = sq.neighbours.begin(); ng != sq.neighbours.end(); ng++) {

		if((*ng)->counted == 1 || (*ng)->fill == 0) continue;
		count_neighbours(**ng,grid);
	}
}

void reverse_list(vector<int> &list, int current_pos, int length) {
	vector<int> tmp_list(list.begin() + current_pos,list.end());
	tmp_list.insert(tmp_list.end(),list.begin(),list.begin() + current_pos);

	reverse(tmp_list.begin(),tmp_list.begin()+length);

	vector<int>::iterator tmp_it = tmp_list.end() - current_pos;
	for(vector<int>::iterator it = list.begin(); it != list.end(); it++) {
		if(tmp_it == tmp_list.end())
			tmp_it = tmp_list.begin();
		*it = *tmp_it;
		tmp_it++;
	}
}

int densify(vector<int>::iterator begin, vector<int>::iterator end) {

	int result = 0;
	for(vector<int>::iterator it = begin; it != end; it++)
		result = result ^ *it;

	return result;
}

string knotHASH(string key) {

	//ifstream myfile ("input.txt");

	stringstream key_stream(key);

	vector<int> lengths;

	char c;
	while (key_stream.get(c)) {
		lengths.push_back((int)c);
	}

	lengths.push_back(17);
	lengths.push_back(31);
	lengths.push_back(73);
	lengths.push_back(47);
	lengths.push_back(23);

	vector<int> list;
	for(int i = 0; i < 256; i++) list.push_back(i);

	int current_pos = 0;
	int skip_size = 0;

	for(int i = 0; i<64;i++) {
		for(vector<int>::iterator it = lengths.begin(); it != lengths.end(); it++) {
			reverse_list(list, current_pos, *it);
			current_pos += *it + skip_size;
			current_pos = current_pos%list.size();
			skip_size++;
		}
	}

	//sparse hash -> dense hash
	vector<int> dense_list(16);
	int i = 0;
	for(vector<int>::iterator it = dense_list.begin(); it != dense_list.end(); it++) {
		*it = densify(list.begin()+i*16,list.begin()+(i+1)*16);
		i++;
	}

	//dense hash -> hexadecimal
	stringstream returnstream;
	for(vector<int>::iterator it = dense_list.begin(); it != dense_list.end(); it++)
		returnstream << setfill('0') << setw(2) << hex << *it;

	return returnstream.str();
}

string hex2bin(char x) {

	string s = "0x";
	s += x;
	stringstream stream(s);

	int y;
	stream >> hex >> y;
	return bitset<4>(y).to_string();
}

int main() {

	string puzzle_input = "nbysizxe";

	vector< vector<Square> > grid(128);

	for(int i = 0; i < 128; i++) {
		stringstream ss;
		ss << puzzle_input << "-" << i;
		string input_hash = knotHASH(ss.str());

		string hexed_hash = "";

		for(string::iterator it = input_hash.begin(); it != input_hash.end(); it++) {
			hexed_hash += hex2bin(*it);
		}

		vector<Square> hex_hash_v(128);

		for(int j = 0; j < 128; j++) {
			if(hexed_hash[j] == '0') hex_hash_v[j].fill = 0;
			else if(hexed_hash[j] == '1') hex_hash_v[j].fill = 1;
			else cout << "Hash neither 0 nor 1" << endl;
			hex_hash_v[j].x = j;
			hex_hash_v[j].y = i;
			hex_hash_v[j].counted = 0;
		}

		grid[i] = hex_hash_v;
	}

	/*
	int used = 0;
	for(vector< vector<Square> >::iterator it = grid.begin(); it != grid.end(); it++)
		for(vector<Square>::iterator itt = it->begin(); itt != it->end(); itt++)
			used += itt->fill;

	cout << used << endl;
	*/

	/*
	for(int i = 0; i < 128; i++) {
		for(int j = 0; j < 128; j++)
			cout << grid[i][j].fill << " ";
		cout << endl;
	}
	*/


	//add neighbours
	for(vector< vector<Square> >::iterator line = grid.begin(); line != grid.end(); line++)
		for(vector<Square>::iterator sq = line->begin(); sq != line->end(); sq++) {
			if(sq->x > 0 && grid[sq->y][sq->x-1].fill == 1) sq->neighbours.push_back(&grid[sq->y][sq->x-1]);
			if(sq->x < 127 && grid[sq->y][sq->x+1].fill == 1) sq->neighbours.push_back(&grid[sq->y][sq->x+1]);
			if(sq->y > 0 && grid[sq->y-1][sq->x].fill == 1) sq->neighbours.push_back(&grid[sq->y-1][sq->x]);
			if(sq->y < 127 && grid[sq->y+1][sq->x].fill == 1) sq->neighbours.push_back(&grid[sq->y+1][sq->x]);
		}

	int regions = 0;
	for(vector< vector<Square> >::iterator line = grid.begin(); line != grid.end(); line++)
		for(vector<Square>::iterator sq = line->begin(); sq != line->end(); sq++) {
			if(sq->counted == 1 || sq->fill == 0) continue;
			count_neighbours(*sq,grid);
			regions++;
		}

	cout << "There are " << regions << " regions." << endl;

	return 0;
}

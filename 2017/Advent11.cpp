//============================================================================
// Name        : Advent11.cpp
// Author      : 
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <complex>
using namespace std;

int get_dist(int x, int y) {
	double diff = abs(y)/(double)abs(x);
	if(diff == 2) {
		//cout << "=" << endl;
		return abs(x);
	} else if(diff > 2) {
		//cout << ">" << endl;
		return (abs(y)-abs(x))/2+abs(x);
	} else if(diff < 2) {
		//cout << "<" << endl;
		return abs(x);
	}

	return 0;
}

void track_max(int x, int y, int &max_dist) {
	int dist = get_dist(x,y);
	if(dist > max_dist) max_dist = dist;
}

int main() {

	ifstream myfile ("input.txt");
	string data;
	stringstream ss;

	myfile >> data;
	replace(data.begin(),data.end(),',',' ');
	ss << data;

	int n_s = 0;
	int ne_sw = 0;
	int nw_se = 0;
	int x = 0;
	int y = 0;

	string direction;
	vector<string> path;
	int max_dist = 0;
	while(ss>>direction) {
		path.push_back(direction);
		if(direction == "n") {
			n_s++;
			y += 2;
			track_max(x,y,max_dist);
		}
		else if(direction == "s") {
			n_s--;
			y -= 2;
			track_max(x,y,max_dist);
		}
		else if(direction == "ne") {
			ne_sw++;
			x++;
			y++;
			track_max(x,y,max_dist);
		}
		else if(direction == "sw") {
			ne_sw--;
			x--;
			y--;
			track_max(x,y,max_dist);
		}
		else if(direction == "nw") {
			nw_se++;
			x--;
			y++;
			track_max(x,y,max_dist);
		}
		else if(direction == "se") {
			nw_se--;
			x++;
			y--;
			track_max(x,y,max_dist);
		}
		else cout << "Error! \"" << direction << "\" is not a cardinal direction" << endl;
	}

	cout << "(Part 1) Dist: " << get_dist(x,y) << endl;

	cout << "(Part 2) Max distance: " << max_dist << endl;



	return 0;
}

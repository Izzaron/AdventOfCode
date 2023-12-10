//============================================================================
// Name        : Advent13.cpp
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
#include <algorithm>
using namespace std;

class Layer {
public:
	int depth;
	int range;
	int pos;

	void timeStep() {

		pos = (pos+1)%(2*range-2);

	}

	int getSeverity () {
		return depth*range;
	}
};

int main() {

	map<int,Layer> layerlist;
	string line;
	ifstream myfile ("input.txt");

	//Read the programs into a <string,Program*> map
	if (myfile.is_open()) {
		while ( getline (myfile,line) ) {
			istringstream iss(line);

			int depth;
			int range;
			string collon;
			iss >> depth >> collon >> range;

			Layer &layer = layerlist[depth];
			layer.depth = depth;
			layer.range = range;
			layer.pos = 0;
		}
		myfile.close();
	} else cout << "Unable to open file";

	int delay = 0;

	while(true) {
		delay++;
		if(delay%1000 == 0)	cout << delay << endl;
		int pos = -1 - delay;
		int severity_tot = 0;
		for(map<int,Layer>::iterator it = layerlist.begin(); it != layerlist.end(); it++) it->second.pos = 0;

		while (pos<91) {
			pos++;

			if(layerlist.count(pos) == 1 && layerlist[pos].pos == 0) {
				severity_tot += layerlist[pos].getSeverity();
				//cout << "Collision at: " << pos << " with severity " << layerlist[pos].getSeverity() << endl;
			}

			for(map<int,Layer>::iterator it = layerlist.begin(); it != layerlist.end(); it++) it->second.timeStep();

		}
		if(severity_tot == 0) break;
	}

	cout << delay << endl;

	//cout << severity_tot << endl;

	//for(map<int,Layer>::iterator it = layerlist.begin(); it != layerlist.end(); it++) cout << it->second.depth << " " << it->second.range << " " << it->second.depth % it->second.range << endl;;


	return 0;
}

//============================================================================
// Name        : Advent13b.cpp
// Author      : 
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <map>
#include <fstream>
#include <vector>
#include <sstream>
#include <time.h>
using namespace std;

int getSeverity(int depth, int time, map<int,int> &layerlist) {
	if(layerlist.count(depth) == 1 && time%(2*layerlist[depth]-2) == 0)
		return 1;
	return 0;
}

int main() {

	clock_t t = clock();

	map<int,int> layerlist;
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

			layerlist[depth] = range;
		}
		myfile.close();
	} else cout << "Unable to open file";

	int delay = 10;
	while(true) {
		int tot_sev = 0;
		for(map<int,int>::iterator it = layerlist.begin(); it != layerlist.end(); it++) {
			tot_sev += getSeverity(it->first,delay+it->first,layerlist);
			if(tot_sev>0) break;
		}
		if(tot_sev == 0) break;
		delay++;
	}

	cout << delay << endl;

	t = clock() - t;
	cout << "Runtime: " << (double)t/CLOCKS_PER_SEC << endl;

	return 0;
}

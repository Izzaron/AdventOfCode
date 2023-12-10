//============================================================================
// Name        : Advent24.cpp
// Author      : 
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;

int sumOfComp(vector<int> component) {
	return component[0] + component[1];
}

bool compHasPins(vector<int> comp_p, int pins) {
	return	comp_p[0] == pins || comp_p[1] == pins;
}

int findStrongest(vector< vector<int> > components, int current_pin) {

	vector< vector<int> > contestants;
	for(vector< vector<int> >::iterator it = components.begin(); it != components.end(); it++)
		if(compHasPins(*it,current_pin))
			contestants.push_back(*it);

	int max_str = 0;
	for(vector< vector<int> >::iterator it = contestants.begin(); it != contestants.end(); it++) {
		vector< vector<int> > components_to_send = components;
		components_to_send.erase(remove(components_to_send.begin(),components_to_send.end(),*it),components_to_send.end());

		int pin_to_send;
		if( (*it)[0] == current_pin )
			pin_to_send = (*it)[1];
		else if( (*it)[1] == current_pin )
			pin_to_send = (*it)[0];
		else {
			cout << "Contestant <" << (*it)[0] << "," << (*it)[1] << "> does not have the current pin:" << current_pin << endl;
			return 0;
		}

		int comp_str = sumOfComp(*it) + findStrongest(components_to_send,pin_to_send);
		if(comp_str > max_str)
			max_str = comp_str;
	}

	return max_str;
}

vector< vector<int> > getComponents(string input) {
	vector <vector<int> > components;
	string line;
	ifstream myfile (input.c_str());

	if (myfile.is_open()) {
		while ( getline (myfile,line) ) {

			vector <int> comp(2);

			sscanf (line.c_str(),"%d/%d",&comp[0],&comp[1]);

			components.push_back(comp);

		}
		myfile.close();
	} else cout << "Unable to open file" << endl;

	return components;
}

int main() {

	vector< vector<int> > components = getComponents("input.txt");

	cout << findStrongest(components,0) << endl;

	return 0;
}

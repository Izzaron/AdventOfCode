//============================================================================
// Name        : Advent24b.cpp
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

vector<int> findStrongest(vector< vector<int> > components, int current_pin) {

	vector< vector<int> > candidates;
	for(vector< vector<int> >::iterator it = components.begin(); it != components.end(); it++)
		if(compHasPins(*it,current_pin))
			candidates.push_back(*it);

	int max_str = 0;
	int max_len = 0;
	for(vector< vector<int> >::iterator it = candidates.begin(); it != candidates.end(); it++) {
		vector< vector<int> > components_to_send = components;
		components_to_send.erase(remove(components_to_send.begin(),components_to_send.end(),*it),components_to_send.end());

		int pin_to_send;
		if( (*it)[0] == current_pin )
			pin_to_send = (*it)[1];
		else if( (*it)[1] == current_pin )
			pin_to_send = (*it)[0];
		else {
			cout << "Candidate <" << (*it)[0] << "," << (*it)[1] << "> does not have the current pin:" << current_pin << endl;
			return vector<int>();
		}

		//int comp_str = sumOfComp(*it) + findStrongest(components_to_send,pin_to_send);
		vector<int> candidate_v = findStrongest(components_to_send,pin_to_send);
		int candidate_len = 1 + candidate_v[0];
		int candidate_str = sumOfComp(*it) + candidate_v[1];
		if( candidate_len > max_len) {
			max_len = candidate_len;
			max_str = candidate_str;
		} else if(candidate_len == max_len && candidate_str > max_str) {
			max_len = candidate_len;
			max_str = candidate_str;
		}
	}

	vector<int> ans_v(2);
	ans_v[0] = max_len;
	ans_v[1] = max_str;
	return ans_v;
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

	vector<int> answer = findStrongest(components,0);

	cout << "The longest bridge is " << answer[0] << " long and has a strength of " << answer[1] << "." << endl;

	return 0;
}

//============================================================================
// Name        : Advent2a.cpp
// Author      : 
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <sstream>
#include <fstream>
#include <string>
#include <vector>
#include <stdio.h>
#include <algorithm>

using namespace std;

int getCSofRow(vector<int> row) {
	for(vector<int>::iterator it = row.begin(); it != row.end()-1; it++)
		for(vector<int>::iterator itt = it+1; itt != row.end(); itt++)
			if(*it % *itt == 0) {
				//cout << *it << " " << *itt << endl;
				return *it / *itt;
			}

	return 0;
}

int main() {
	int sum = 0;
	string line;
	ifstream myfile ("input.txt");
	if (myfile.is_open())
	{
		while ( getline (myfile,line) ) {
			vector<int> row;
			istringstream iss(line);
			while (iss)
			{
				int num;
				string subs;
				iss >> subs;
				sscanf(subs.c_str(),"%d",&num);
				row.push_back(num);
			}
			row.pop_back();
			//cout << "size: " << row.size() << endl;
			//cout << *(row.end()-1) << " " << *(row.end()-2) << endl;
			sort(row.begin(),row.end());
			reverse(row.begin(),row.end());
			sum += getCSofRow(row);
		}
		myfile.close();
	}

	else cout << "Unable to open file";

	cout << sum << endl;
	return 0;
}

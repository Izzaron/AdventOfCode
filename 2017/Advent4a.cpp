//============================================================================
// Name        : Advent4a.cpp
// Author      : 
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <algorithm>
using namespace std;

bool anagram(string str1, string str2) {
	sort(str1.begin(),str1.end());
	sort(str2.begin(),str2.end());
	if (str1.compare(str2) == 0) return true;
	return false;
}

bool uniqueSentence(vector<string> &sentence) {
	for(vector<string>::iterator it = sentence.begin();it != sentence.end() ; it++) {
		for(vector<string>::iterator itt = it+1;itt != sentence.end() ; itt++) {
			if(it -> compare(*itt) == 0) return false;
			if(anagram(*it,*itt)) return false;
		}
	}
	return true;
}

int main() {

	string line;
	ifstream myfile ("input.txt");
	int sum = 0;

	if (myfile.is_open()) {
		while ( getline (myfile,line) ) {
			vector<string> sentence;

			istringstream iss(line);
			while (iss) {
				string word;
				iss >> word;
				sentence.push_back(word);
			}
			if(uniqueSentence(sentence)) sum++;
		}
		myfile.close();
	} else cout << "Unable to open file";

	cout << sum << endl;

	return 0;
}

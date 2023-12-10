//============================================================================
// Name        : Advent9.cpp
// Author      : 
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <fstream>
using namespace std;

int main() {
	ifstream myfile ("input.txt");

	char c;

	int score = 0;
	int group = 1;
	int garbage_score = 0;

	while (myfile.get(c)) {

		//Skip 1 char at '!'
		if(c == '!') {
			myfile.get(c);
			continue;
		}

		//Garbage group starts
		if(c == '<') {
			while (myfile.get(c)) {

				//Skip 1 char at '!'
				if(c == '!') {
					myfile.get(c);
					continue;
				}

				//Garbage group ends
				if(c=='>') break;

				garbage_score++;
			}
		}

		if(c=='{') {score += group; group++;} else if(c=='}') group--;
	}

	cout << "Score: " << score << endl;
	cout << "Garbage score: " << garbage_score << endl;

	myfile.close();

	return 0;
}

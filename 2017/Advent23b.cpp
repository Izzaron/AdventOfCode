//============================================================================
// Name        : Advent23b.cpp
// Author      : 
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
using namespace std;

bool isPrime(int number) {
	int d = 2;
	while(d*d <= number ) {
		if(number%d == 0)
			return false;
		d++;
	}
	return true;
}

int main() {
	long int b = 109900;
	long int c = 126900;
	long int h = 0;

	while(b <= c) {
		bool flag = false;
//		for(int d = 2; d != b; d++)
//			if(b%d == 0) flag = true;
		if(!isPrime(b)) flag = true;


		if(flag) h++;
		b += 17;
	}



	cout << h << endl;

	return 2;
}

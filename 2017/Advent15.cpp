//============================================================================
// Name        : Advent15.cpp
// Author      : 
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <bitset>
#include <time.h>
#include <vector>
//#include <climits>
using namespace std;

int main() {

	clock_t t = clock();

	long long A = 116;
	long long int B = 299;
	int Af = 16807;
	int Bf = 48271;
	int div = 2147483647;

	//cout << "lim: " << INT_MAX << endl;



	vector<int> Aans(5000000);
	vector<int> Bans(5000000);

	int i = 0;
	while(i < 5000001) {

		A = (A*Af)%div;
		if(A%4 != 0) continue;
		Aans[i] = A;
		i++;
	}

	i = 0;
	while(i < 5000001) {

		B = (B*Bf)%div;
		if(B%8 != 0) continue;
		Bans[i] = B;
		i++;
	}

	int judge = 0;
	for(int j = 0; j < 5000001; j++) {
		bitset<16> A16(Aans[j]);
		bitset<16> B16(Bans[j]);
		if(A16 == B16) judge++;
	}

	cout << judge << endl;

	t = clock() - t;
	cout << "It took me " << (double)t/CLOCKS_PER_SEC << " seconds.\n" << endl;

	return 0;
}

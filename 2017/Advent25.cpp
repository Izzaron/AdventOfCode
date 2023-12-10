//============================================================================
// Name        : Advent25.cpp
// Author      : 
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <vector>
#include <numeric>
using namespace std;

class Tape {
private:
	vector<int> tape;
	long int current_pos;

public:
	Tape() {
		current_pos = 0;
		tape.push_back(0);
	}

	int getCurrentValue() {
		return tape[current_pos];
	}

	void setCurrentValue(int value) {
		if(value != 1 && value != 0)
			cout << "Illegally wrote " << value << " to the tape!" << endl;
		tape[current_pos] = value;
	}

	void moveLeft() {
		if(current_pos == 0)
			tape.insert(tape.begin(),0);
		else
			current_pos--;
	}

	void moveRight() {
		if(current_pos == tape.size()-1) {
			tape.push_back(0);
			current_pos++;
		} else
			current_pos++;
	}

	long int getChecksum() {
		return accumulate(tape.begin(), tape.end(), 0);
	}
};

int main() {

	Tape tape;

	enum State { A, B, C, D, E, F };
	State s = A;

	long int step = 0;

	while(step < 12523873) {
		switch(s) {
		case A:
			if(tape.getCurrentValue() == 0) {
				tape.setCurrentValue(1);
				tape.moveRight();
				s = B;
			} else {
				tape.setCurrentValue(1);
				tape.moveLeft();
				s = E;
			}
			break;
		case B:
			if(tape.getCurrentValue() == 0) {
				tape.setCurrentValue(1);
				tape.moveRight();
				s = C;
			} else {
				tape.setCurrentValue(1);
				tape.moveRight();
				s = F;
			}
			break;
		case C:
			if(tape.getCurrentValue() == 0) {
				tape.setCurrentValue(1);
				tape.moveLeft();
				s = D;
			} else {
				tape.setCurrentValue(0);
				tape.moveRight();
				s = B;
			}
			break;
		case D:
			if(tape.getCurrentValue() == 0) {
				tape.setCurrentValue(1);
				tape.moveRight();
				s = E;
			} else {
				tape.setCurrentValue(0);
				tape.moveLeft();
				s = C;
			}
			break;
		case E:
			if(tape.getCurrentValue() == 0) {
				tape.setCurrentValue(1);
				tape.moveLeft();
				s = A;
			} else {
				tape.setCurrentValue(0);
				tape.moveRight();
				s = D;
			}
			break;
		case F:
			if(tape.getCurrentValue() == 0) {
				tape.setCurrentValue(1);
				tape.moveRight();
				s = A;
			} else {
				tape.setCurrentValue(1);
				tape.moveRight();
				s = C;
			}
			break;
		}
		step++;
	}


	cout << tape.getChecksum() << endl;

	return 0;
}

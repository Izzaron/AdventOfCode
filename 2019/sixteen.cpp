#include <iostream>
#include <fstream>
#include <string>
#include <iomanip>
#include <vector>

using namespace std;

vector<int> basePattern(int element,int length){
    // element är 1-indexerad

    // base = [0, 1, 0, -1]
    vector<int> base = {0, 1, 0, -1};
    
    // pattern = [base[0]]*element + [base[1]]*element + [base[2]]*element + [base[3]]*element
    vector<int> pattern;
    for (size_t i = 0; i < 4; i++)
    {
        vector<int> baseVector(element,base[i]);
        pattern.insert(pattern.end(),baseVector.begin(),baseVector.end());
    }

    // return [pattern[i%len(pattern)] for i in range(element,length + 1)];
    vector<int> returnVector;
    returnVector.reserve(length);
    for (size_t i = element; i < length+1; i++)
    {
        returnVector.push_back(pattern[i%pattern.size()]);
    }

    return returnVector;
}
vector<int> flawedFrequencyTransmission(vector<int> inputSignal){

    vector<int> returnVector;
    returnVector.reserve(inputSignal.size());

    // return [int(str(sum([x * y for x, y in zip(inputSignal[i:],basePattern(i+1,len(inputSignal)))]))[-1]) for i in range(len(inputSignal))]
    for (size_t i = 0; i < inputSignal.size(); i++) {

        vector<int> baseVector = basePattern(i+1,inputSignal.size());

        for (size_t i2 = i; i2 < inputSignal.size(); i2++) {
            returnVector.push_back(abs(inputSignal[i2] * baseVector[i2])%10);
        }

    }

    return returnVector;
}

int main() {
    // start_time = time.time()
    time_t start_time, end;
    time(&start_time);
    ios_base::sync_with_stdio(false);

    // puzzleInput = open("input16.txt").read()
    // string puzzleInput;
    // ifstream myfile ("input16.txt");
    // if (myfile.is_open()) {
    //     while ( getline (myfile,puzzleInput) );
    //     myfile.close();
    // } else {
    //     cout << "Unable to open file";
    // }

    string puzzleInput = "12345678";//"03036732577212944063491565474664";

    // inputSignal = [int(s) for s in puzzleInput]// * 10000
    vector<int> inputSignal;
    for (string::iterator it = puzzleInput.begin(); it != puzzleInput.end(); it++) {
        int i = *it - '0';
        inputSignal.push_back(i);
    }

    // offset = 0#int(puzzleInput[0:7])

    // for i in range(1,101):
    //     inputSignal = flawedFrequencyTransmission(inputSignal)
    //     // print(i)
    for (size_t i = 1; i < 2; i++)
    {
        inputSignal = flawedFrequencyTransmission(inputSignal);
        cout << i << endl;
    }

    // print(''.join([str(i) for i in inputSignal[offset:offset+8]]))
    for (vector<int>::iterator it = inputSignal.begin(); it < inputSignal.begin() + 8; it++) {
        cout << *it;
    }
    cout << endl;
    
    // print("--- %s seconds ---" % (time.time() - start_time))
    time(&end);
    double time_taken = double(end - start_time); 
    cout << "--- " << fixed << time_taken << setprecision(5); 
    cout << " seconds --- " << endl; 

    return 0;
}
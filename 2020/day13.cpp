#include <iostream>
#include <fstream>
#include <string>
#include <vector>

// __UINT64_TYPE__

using namespace std;

void tokenize(string &str, char delim, vector<string> &out)
{
    size_t start;
    size_t end = 0;

    while ((start = str.find_first_not_of(delim, end)) != string::npos)
    {
        end = str.find(delim, start);
        out.push_back(str.substr(start, end - start));
    }
}

int main () {
    string line;
    ifstream myfile ("day13input.txt");
    if (myfile.is_open())
    {
        while ( getline (myfile,line) ){}
        myfile.close();
    } else {
            cout << "Unable to open file";
            return 1;
    }

    vector<string> busLines;
    tokenize(line,',',busLines);

    // for(auto it:busLines) cout<<it<<" : ";
    // cout << endl;

    vector<int> intLines;

    for(string s : busLines) {
        if (s != "x") {
            intLines.push_back(stoi(s))
        }
    }

    

    int largestLine =

    __UINT64_TYPE__ t = 0;

    while(true) {
        int i = 0;
        for(string s : busLines) {
            if (s != "x") {
                
            }
            i++;
        }
            
        t += largestLine;
    }

    return 0;
}
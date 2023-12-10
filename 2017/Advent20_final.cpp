//============================================================================
// Name        : Advent20.cpp
// Author      : 
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <map>
#include <cmath>
#include <algorithm>
using namespace std;

class Particle {
public:
	vector<long int> acc;
	vector<long int> vel;
	vector<long int> pos;

	Particle() {
		pos = vector<long int>(3);
		vel = vector<long int>(3);
		acc = vector<long int>(3);
	}

	void update() {
		vel[0] += acc[0];
		vel[1] += acc[1];
		vel[2] += acc[2];
		pos[0] += vel[0];
		pos[1] += vel[1];
		pos[2] += vel[2];
	}
};

//Read input from file
vector<Particle> readInput(string input) {
	vector<Particle> particles;
	string line;
	ifstream myfile (input.c_str());

	if (myfile.is_open()) {
		while ( getline (myfile,line) ) {

			Particle p;
			long int &p0 = p.pos[0];
			long int &p1 = p.pos[1];
			long int &p2 = p.pos[2];
			long int &v0 = p.vel[0];
			long int &v1 = p.vel[1];
			long int &v2 = p.vel[2];
			long int &a0 = p.acc[0];
			long int &a1 = p.acc[1];
			long int &a2 = p.acc[2];

			sscanf (line.c_str(),"p=<%ld,%ld,%ld>, v=<%ld,%ld,%ld>, a=<%ld,%ld,%ld>",&p0,&p1,&p2,&v0,&v1,&v2,&a0,&a1,&a2);

			particles.push_back(p);
		}
		myfile.close();
	} else cout << "Unable to open file" << endl;

	return particles;
}

int main() {
	//Read input and store particles
	vector<Particle> particles_storage = readInput("input.txt");

	//Create a list of the remaining particles that can be manipulated
	vector<Particle*> remaining_particles(particles_storage.size());
	for(vector<Particle>::iterator it = particles_storage.begin(); it != particles_storage.end(); it++) {
		remaining_particles[it-particles_storage.begin()] = &(*it);
	}

	typedef map< vector<long int>,vector<Particle*> > particleMap;

	int i = 0;
	while(i < 100) {

		//map between collision sites and particles at those sites
		particleMap collisions;

		//add particles to collision sites
		for(vector<Particle*>::iterator it = remaining_particles.begin(); it != remaining_particles.end(); it++)
			collisions[(*it)->pos].push_back( *it );

		//find collision sites with more than 1 particle and remove those particles from the "master vector"
		for(particleMap::iterator it = collisions.begin(); it != collisions.end(); it++)
			if(it->second.size() > 1)
				for(vector<Particle*>::iterator p_it = it->second.begin(); p_it != it->second.end(); p_it++)
					remaining_particles.erase(remove(remaining_particles.begin(),remaining_particles.end(),*p_it),remaining_particles.end());

		//Update all remaining particles positions
		for(vector<Particle*>::iterator it = remaining_particles.begin(); it != remaining_particles.end(); it++)
			(*it)->update();

		i++;
	}

	cout << "Particles left: " << remaining_particles.size() << endl;

	return 0;
}

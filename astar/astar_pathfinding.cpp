#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <time.h>
#include <vector>
using namespace std;


#define length 200
#define blocked 1
#define open 0
#define visited 2
#define start 0
#define finish 39999



class searchNode{
private:
	struct NODE{
		int parent;
		int h,f,g;
		int state;
	};
	vector <int> openList;
	vector <NODE*> map;
	bool success;
public:
	int getHvalue(int);
	bool checkState(int, int);
	void readFile();
	void build();
	void findPath();
	void insert(int);
	void setRoot();
	void printResult();
	void printMap();
	void checkSuccess();
};


void searchNode::build() {
	setRoot();
	while(!success) {
		findPath();
	}
}


void searchNode::readFile() {
	ifstream instream("Map.txt");
	string line,block;
	
	while(getline(instream,line)) {
		istringstream linestream(line);
		while(getline(linestream, block, ',')) {
			NODE *n = new NODE;
			n->state = atoi(block.c_str());
			map.push_back(n);
		}
	}
}

void searchNode::setRoot() {
	success = false;

	map[start]->g = 0;
	map[start]->h = getHvalue(0);
	map[start]->f = map[start]->h; 
	map[start]->parent = -1;
	map[start]->state = visited;

	openList.push_back(start);
}

bool searchNode::checkState(int index, int preindex) {
	bool state = true;

	if(map[index]->state == blocked) { state = false; } 
	if(map[index]->state == visited) {
		if(map[preindex]->g + 14 > map[index]->g)
			state = false;
	}
	

	return state;
}

void searchNode::printResult(){
	int a;
	a = finish;

	while(a != start) {
		cout << a <<endl;
		map[a]->state = 9;
		a = map[a]->parent;
	}

	cout << start <<endl;
	cout << "cost : " << map[finish]->f;
}


void searchNode::printMap() {
	ofstream outstream("outMap.txt");

	for(int i = 0; i < map.size() - 1; i++) {
		outstream << map[i]->state << " ";
		if(i % 200 == 199)
			outstream << endl;
	}
}


void searchNode::findPath() {
	int index = openList.front();
	openList.erase(openList.begin());


	if(index/length != 0 && index%length != length-1
		&& checkState(index-length +1, index)) {
		int ru = index - length + 1;
		map[ru]->f = map[index]->f + 13;
		getHvalue(ru);
		map[ru]->g = map[ru]->f + map[ru]->h;
		map[ru]->parent = index;
		map[ru]->state = visited;
		insert(ru);
	}

	if(index%length != length-1 && checkState(index+1, index) ) {
		int r = index + 1;
		map[r]->f = map[index]->f + 10;
		getHvalue(r);
		map[r]->g = map[r]->f + map[r]->h;
		map[r]->parent = index;
		map[r]->state = visited;
		insert(r);
	}

	if(index/length != length-1 && index%length != length-1
		&& checkState(index+length+1, index)) {
		int rd = index + length + 1;
		map[rd]->f = map[index]->f + 13;
		getHvalue(rd);
		map[rd]->g = map[rd]->f + map[rd]->h;
		map[rd]->parent = index;
		map[rd]->state = visited;
		insert(rd);
	}

	if(index/length != length-1 && checkState(index+length, index)) {
		int d = index + length;
		map[d]->f = map[index]->f + 10;
		getHvalue(d);
		map[d]->g = map[d]->h + map[d]->f;
		map[d]->parent = index;
		map[d]->state = visited;
		insert(d);
	}

	if(index/length != 199 && index%length != 0
		&& checkState(index+length-1, index)) {
		int ld = index + length - 1;
		map[ld]->f = map[index]->f + 13;
		getHvalue(ld);
		map[ld]->g = map[ld]->f + map[ld]->h;
		map[ld]->parent = index;
		map[ld]->state = visited;
		insert(ld);
	}

	if(index%length != 0 && checkState(index-1, index)) {
		int l = index - 1;
		map[l]->f = map[index]->f + 10;
		getHvalue(l);
		map[l]->g = map[l]->h + map[l]->f;
		map[l]->parent = index;
		map[l]->state = visited;
		insert(l);
	}

	if(index/length != 0 && index%length != 0
		&&checkState(index-length-1, index)) {
		int lu = index - length - 1;
		map[lu]->f = map[index]->f + 13;
		getHvalue(lu);
		map[lu]->g = map[lu]->f + map[lu]->h;
		map[lu]->parent = index;
		map[lu]->state = visited;
		insert(lu);
	}

	if(index/length != 0 && checkState(index-length, index)) {
		int u = index - length;
		map[u]->f= map[index]->f + 10;
		getHvalue(u);
		map[u]->g = map[u]->f + map[u]->h;
		map[u]->parent = index;
		map[u]->state = visited;
		insert(u);
	}

	checkSuccess();
}

void searchNode::checkSuccess() {
	for(int i = 0; i < openList.size(); i++)
		if(openList[i] == finish)
			success = true;

	if(success) {
		printResult();

	}
}

int searchNode::getHvalue(int index) {
	int x_coord, y_coord, differ;

	x_coord = 199 - (index % length);
	y_coord = 199 - (index / length);
	
	differ = abs(x_coord - y_coord);
	
	return (differ * 10) + (abs(x_coord - differ) * 14);
}


void searchNode::insert(int index) {
	int m, temp;
	
	if(openList.size() == 0)
		openList.push_back(index);
	else {
		openList.push_back(index);
		for(m = openList.size() - 1; m!=0;){
			if (map[openList[m]]->f <= map[openList[m/2]]->f){
				temp = openList[m/2];
				openList[m/2] = openList[m];
				openList[m] = temp;
				m = m/2;
			} else
				break;
		}
	}
}


void main() {
	searchNode startNode;
	clock_t startTime, endTime;
	vector <int> num;
	
	startTime = clock();
	startNode.readFile();
	startNode.build();
	endTime = clock();

	startNode.printMap();

	cout << "Time : " << (double)(endTime - startTime)/CLOCKS_PER_SEC << endl;

	return;
}
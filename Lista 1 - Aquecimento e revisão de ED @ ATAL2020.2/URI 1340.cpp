#include <bits/stdc++.h>
using namespace std;

int main() {
	int quantityOfOperations;
	bool statusCheck[3];

	// EOFs false cin
	while (cin >> quantityOfOperations) {
		statusCheck[0] = true; //queue 
		statusCheck[1] = true; //stack 
		statusCheck[2] = true; //priority

		queue<int> queueTester;
		stack<int> stackTester;
		priority_queue <int, vector<int>, less<int> > priorityTester;

		for (int counter = 0; counter < quantityOfOperations; counter++) {
			int operation = 0;
			int resultOrInput;

			cin >> operation >> resultOrInput;

			if(operation == 1) {
				// cout << "1A";
				if(statusCheck[0]) queueTester.push(resultOrInput);
				if(statusCheck[1]) stackTester.push(resultOrInput);
				if(statusCheck[2]) priorityTester.push(resultOrInput);
			} else if(operation == 2) {
				// cout << "2B";

				//queue 
				if(queueTester.front() == resultOrInput) {
					queueTester.pop();
				} else {
					statusCheck[0] = false; 
				}

				//stack 
				if(stackTester.top() == resultOrInput) {
					stackTester.pop();
				} else {
					statusCheck[1] = false; 
				}

				//priority 
				if(priorityTester.top() == resultOrInput) {
					priorityTester.pop();
				} else {
					statusCheck[2] = false; 
				}

				
				
			}
		}


		if      (statusCheck[0] && !statusCheck[1] && !statusCheck[2])  printf("queue\n");
		else if (!statusCheck[0] && statusCheck[1] && !statusCheck[2])  printf("stack\n");
		else if (!statusCheck[0] && !statusCheck[1] && statusCheck[2])  printf("priority queue\n");
		else if (statusCheck[0] || statusCheck[1] || statusCheck[2])    printf("not sure\n");
		else if (!statusCheck[0] && !statusCheck[1] && !statusCheck[2]) printf("impossible\n");
		
	}

}
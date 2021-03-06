#include <iostream>
#include <cstdio>
#include "CircularArray.h"
using namespace std;
// Driver program shows class capabilities.
// System can be tested with unit tests for following cases :
// 1. an empty CircularArray rotated and looping it
// 2. Regular array looped
// Class should be extended to support changing its size dynamiclly for more practical usages.

int main()
{
	CircularArray<int> myArr(10);
	int i = 0;
	cout << "Initial array is : ";
	for (auto &v : myArr) {
		v = i;
		i++;
		cout << v << " ";
	}

	cout << "\nRotation 2 : ";

	myArr.rotate(2);

	for (auto v : myArr) {
		cout << v << " ";
	}

	cout << "\nRotation 14 : ";

	myArr.rotate(14);

	for (auto v : myArr) {
		cout << v << " ";
	}

	cout << "\n";
    return 0;
}


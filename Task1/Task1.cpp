#include <iostream>
#include <cstdio>
#include "CircularArray.h"
using namespace std;

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


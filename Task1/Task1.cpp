#include <iostream>
#include <cstdio>
#include "CircularArray.h"
using namespace std;

int main()
{
	CircularArray<int> myArr(10);
	int i = 0;
	for (auto &v : myArr) {
		v = i;
		i++;
	}

	myArr.rotate(2);

	for (auto v : myArr) {
		cout << v << "\n";
	}

    return 0;
}


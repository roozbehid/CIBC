#pragma once

#include <vector>
#include<iostream>

using std::vector;

template<typename MyData>
class CircularArray
{
private:
	vector<MyData> v;
	int rotation=0;
public:
	typename vector<MyData>::iterator begin();
	typename vector<MyData>::iterator end();

	typename vector<MyData>::const_iterator begin();
	typename vector<MyData>::const_iterator end();

	void rotate(int n);

	CircularArray();
	CircularArray(int sizeofArray);
};


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
	class iterator {
		typename vector<MyData>::iterator cursor;
		typename vector<MyData>::iterator begin;
		typename vector<MyData>::iterator end;
		int iterations;
	public:
		iterator(typename vector<MyData>::iterator begin_, typename vector<MyData>::iterator end_, typename vector<MyData>::iterator cursor_, int it) { 
			begin = begin_;
			end = end_;
			cursor = cursor_;
			iterations = it;
		}
		iterator operator++() { 
			++cursor; 
			++iterations;
			if (cursor == end)
				cursor = begin;

			return *this; 
		}

		bool operator!=(const iterator &other) const { 
			if (other.cursor == end)
				return iterations != other.iterations;

			return other.cursor != cursor || iterations != other.iterations;
		}

		MyData& operator*() const { return *cursor; }
	};


	iterator begin() { 

		return  iterator(v.begin(),v.end(), v.begin() + rotation % v.size(), 0);
	}

	iterator end()    { 
		int rot_corrected = rotation % v.size();
		if (rot_corrected != 0)
			return  iterator(v.begin(), v.end(), v.end() -  (v.size()  - rot_corrected), v.size());
		else
			return  iterator(v.begin(), v.end(), v.end(), v.size());
	}

	const MyData& operator[](int index) const {
		return v[index];
	}

	void rotate(int n);

	CircularArray();
	CircularArray(int sizeofArray);

	~CircularArray();
};




template<typename MyData>
void CircularArray<MyData>::rotate(int n)
{
	rotation = n % v.size();
}

template<typename MyData>
CircularArray<MyData>::CircularArray()
{
	v = vector<MyData>();
}

template<typename MyData>
CircularArray<MyData>::CircularArray(int sizeofArray)
{
	v = vector<MyData>(sizeofArray);
}

template<typename MyData>
CircularArray<MyData>::~CircularArray()
{
}


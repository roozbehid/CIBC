#include "CircularArray.h"


template<typename MyData>
typename vector<MyData>::iterator CircularArray<MyData>::begin()
{
	return vector<MyData>::iterator();
}

template<typename MyData>
typename vector<MyData>::iterator CircularArray<MyData>::end()
{
	return typename vector<MyData>::iterator();
}

template<typename MyData>
void CircularArray<MyData>::rotate(int n)
{
	rotation = n % v.size;
}

template<typename MyData>
CircularArray<MyData>::CircularArray()
{
}

template<typename MyData>
CircularArray<MyData>::CircularArray(int sizeofArray)
{
}



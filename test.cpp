// extern "C" int add_one(int i)
// {
//     return i+1;
// }
#include <bits/stdc++.h>
using namespace std;

extern "C" void print_array(double* array, int N)
{
    for (int i=0; i<N; i++) 
        cout << i << " " << array[i] << endl;
}

extern "C" int add_one(int i)
{
    return i+1;
}
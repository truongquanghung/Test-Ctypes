// extern "C" int add_one(int i)
// {
//     return i+1;
// }
#include <bits/stdc++.h>
using namespace std;

int n=0;
vector <int> a;

extern "C" void print_array(double* array, int N)
{
    for (int i=0; i<N; i++) 
        cout << i << " " << array[i] << endl;
}

extern "C" int add_one(int i)
{
    return i+1;
}

extern "C" void add(int i)
{
    n+=i;
    a.push_back(n);
}

extern "C" int num()
{
    return a.size();
}

extern "C" int* out()
{
    int* res = new int[a.size()];
    for (int i=0;i<a.size();i++)
        res[i] = a[i];
    return res;
}
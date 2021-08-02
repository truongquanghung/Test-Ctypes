#include <bits/stdc++.h>
using namespace std;

int n = 0;
vector<int> a;
vector<string> s;

extern "C" void print_array(double *array, int N)
{
    for (int i = 0; i < N; i++)
        cout << i << " " << array[i] << endl;
}

extern "C" int add_one(int i)
{
    return i + 1;
}

extern "C" void add(int i)
{
    n += i;
    a.push_back(n);
}

extern "C" int num()
{
    return a.size();
}

extern "C" int *out()
{
    int *res = new int[a.size()];
    for (int i = 0; i < a.size(); i++)
        res[i] = a[i];
    return res;
}

extern "C" void str(char *c, int n)
{
    // cout << n << endl;
    // for (int i = 0; i < n; i++)
    //     cout << c[i];
    // cout << endl;
    string st(c);
    s.push_back(st);
}

extern "C" int num_str()
{
    return s.size();
}

extern "C" char ** out_str()
{
    char **res = new char*[s.size()];
    for (int i = 0; i < s.size(); i++){
        res[i] = new char[s[i].length()];
        for (int j=0;j<s[i].length();j++) res[i][j] = s[i][j];
    }
    return res;
}

extern "C" int* get_size(){
    int *res = new int[s.size()];
    for (int i = 0; i < s.size(); i++)
        res[i] = s[i].length();
    return res;
}

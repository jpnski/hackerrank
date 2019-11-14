#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    int n;
    int arr[n];
    std::vector<int> v;
   
    cin >> n;
    cin >> arr[0], arr[1], arr[2], arr[3];
    
    v = arr;
    std::reverse(v.begin(), v.end());
    cout << arr;
    
    return 0;
}


#include <iostream>
#include <vector>

using namespace std;

int BS(vector<int>& lis, int target){
    int left = 0;
    int right = lis.size()-1;
    
    while (left <= right){
        int mid = (left + right) / 2;
        if (lis[mid] >= target){
            right = mid - 1;
        }
        else {
            left = mid + 1;
        }
    }
    
    return left;
}

int main()
{

    int N;
    vector<int>pole;
    
    cin >> N;
    
    for (int i=0; i<N; i++){
        int temp;
        cin >> temp;
        pole.push_back(temp);
    }

    vector<int>LIS;
    
    for (int i=0; i<N; i++){
        int pos = BS(LIS, pole[i]);
        if (pos == LIS.size()){
            LIS.push_back(pole[i]);
        }
        else {
            LIS[pos] = pole[i];
        }
    }
    
    cout << N - LIS.size();


    return 0;
}

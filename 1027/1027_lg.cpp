/******************************************************************************

                              Online C++ Compiler.
               Code, Compile, Run and Debug C++ program online.
Write your code in this editor and press "Run" button to compile and execute it.

*******************************************************************************/

#include <iostream>

using namespace std;

int main()
{
    int N;
    cin >> N;
    
    int tower[51];
    int answer[51];
    
    for (int i=0; i<N; i++){
        cin >> tower[i];
        answer[i] = 0;
    }

    // 탐색 방법 : 첫 번째 건물의 기울기보다 크면 업데이트 후 +1
    
    // 1. 모든 경우에 대하여 i-1번째에서 왼쪽으로 탐색
    
    for (int i=0; i<N; i++){
        int target = tower[51];
        int flag = 1;
        float max_gradient = 0;
        
        for (int j=i-1; j>=0; j--){
            if (flag == 1){
                flag = 0;
                max_gradient = tower[j] - tower[i];
                answer[i]++;
            }
            
            float gradient = (float)(tower[j] - tower[i]) / (float)(i-j);
            if (gradient > max_gradient){
                max_gradient = gradient;
                answer[i]++;
            }
        }
    }
    
    // 2. 모든 경우에 대하여 오른쪽 탐색
    
    for (int i=0; i<N; i++){
        int target = tower[51];
        int flag = 1;
        float max_gradient = 0;
        
        for (int j=i+1; j<N; j++){
            if (flag == 1){
                flag = 0;
                max_gradient = tower[j] - tower[i];
                answer[i]++;
            }
            
            float gradient = (float)(tower[j] - tower[i]) / (float)(j-i);
            if (gradient > max_gradient){
                max_gradient = gradient;
                answer[i]++;
            }
        }
    }
    
    
    // 3. max 값 추출
    
    int max_ = -1;
    
    for (int i=0; i<N; i++){
        if (answer[i] > max_)
            max_ = answer[i];
    }
    
    cout << max_;
    
    return 0;
}

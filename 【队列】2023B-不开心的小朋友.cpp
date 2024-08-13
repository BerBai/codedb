/*
 * @hw id=2023B lang=cpp
 *
 * 不开心的小朋友
 */

// @hw code=start
#include<iostream>
#include<vector>
#include<string>
#include<map>
using namespace std;

int main () {
    int n;
    cin >> n;
    string c;
    vector<string> wq;
    map<string, vector<bool>> state;
    int playNum = 0;
    int angryNum = 0;

    while(cin >> c) {
        if(state.find(c) == state.end()) {
            // 0 是否出现 1 是否玩上 2 是否离开
            state[c] = {false, false, false};
        }
        //第一次
        if(!state[c][0]) {
            // 标记出现
            state[c][0] = true;
            if(playNum < n) {
                // 标记玩上，正在玩+1
                state[c][1] = true;
                playNum++;
            } else {
                // 排队
                wq.push_back(c);
            }
        } else {
            //第二次，标记离开
            state[c][2] = true;
            if(state[c][1]) {
                // 在玩-1
                playNum--;
                // 是否有空位玩
                while(wq.size()>0 && playNum < n) {
                    string nc = wq.front();
                    wq.erase(wq.begin());
                    // 是否离开
                    if(!state[nc][2]) {
                        playNum++;
                        state[nc][1] = true;
                    }
                }
            } else {
                angryNum++;
            }
        }
    }

    cout << angryNum << endl;
    return 0;
}
// @hw code=end
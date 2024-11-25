// 
//  @hw id=2024E lang=python3
// 
//  德州扑克
// 

// @hw code=start
#include <iostream>
#include <vector>
#include <algorithm>
#include <map>
#include <string>

using namespace std;

// 定义结构体表示一张牌
struct Card {
    int rank;
    char suit;
};

// 比较函数，用于sort按rank升序排序
bool compareCards(const Card& a, const Card& b) {
    return a.rank < b.rank;
}

int main(){
    vector<Card> cards(5);
    string rank_str;
    char suit;

    // 定义牌大小映射
    map<string, int> rank_map = {{"J",11}, {"Q",12}, {"K",13}, {"A",14}};

    // 读取5张牌
    for(int i=0;i<5;i++) {
        cin >> rank_str >> suit;
        if(rank_map.find(rank_str) != rank_map.end()) {
            cards[i].rank = rank_map[rank_str];
        }
        else {
            cards[i].rank = stoi(rank_str);
        }
        cards[i].suit = suit;
    }

    // 按rank升序排序
    sort(cards.begin(), cards.end(), compareCards);

    // 初始化变量
    bool sameColor = true; // 同花
    bool dragon = true; // 顺子
    bool fourKind = false; // 四条
    bool threeKind = false; // 三条
    bool twoKind = false; // 对子

    // 统计每种牌大小的出现次数
    map<int, int> rank_counts;
    for(int i=0;i<5;i++) {
        rank_counts[cards[i].rank]++;
        if(i < 4){
            // 判断顺子
            if(dragon && (cards[i].rank + 1) != cards[i+1].rank) {
                dragon = false;
            }
            // 判断同花
            if(sameColor && cards[i].suit != cards[i+1].suit) {
                sameColor = false;
            }
        }
    }

    // 特殊处理A2345
    if(cards[0].rank == 2 && cards[1].rank == 3 && cards[2].rank == 4 && cards[3].rank == 5 && cards[4].rank == 14){
        dragon = true;
    }

    // 判断四条、三条和对子
    for(auto &entry : rank_counts){
        if(entry.second == 4) fourKind = true;
        if(entry.second == 3) threeKind = true;
        if(entry.second == 2) twoKind = true;
    }

    // 判断牌型
    int result;
    if(dragon && sameColor){
        result = 1; // 同花顺
    }
    else if(fourKind){
        result = 2; // 四条
    }
    else if(threeKind && twoKind){
        result = 3; // 葫芦
    }
    else if(sameColor){
        result = 4; // 同花
    }
    else if(dragon){
        result = 5; // 顺子
    }
    else if(threeKind){
        result = 6; // 三条
    }
    else{
        result = -1; // 无符合牌型
    }

    // 输出结果
    cout << result << endl;

    return 0;
}
// @hw code=end

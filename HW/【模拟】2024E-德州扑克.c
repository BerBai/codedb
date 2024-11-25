// 
//  @hw id=2024E lang=python3
// 
//  德州扑克
// 

// @hw code=start
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// 定义结构体表示一张牌
typedef struct {
    int rank;
    char suit;
} Card;

// 比较函数，用于qsort按rank升序排序
int compare(const void* a, const void* b) {
    Card* cardA = (Card*)a;
    Card* cardB = (Card*)b;
    return cardA->rank - cardB->rank;
}

int main() {
    Card cards[5];
    char rank_str[3];
    char suit;

    // 定义牌大小映射
    int rank_map[15]; // 2-14
    for(int i=2;i<=10;i++) rank_map[i]=i;
    rank_map['J'] = 11;
    rank_map['Q'] = 12;
    rank_map['K'] = 13;
    rank_map['A'] = 14;

    // 读取5张牌
    for(int i=0;i<5;i++) {
        scanf("%s %c", rank_str, &suit);
        if(strlen(rank_str)==1) { // J, Q, K, A
            cards[i].rank = rank_map[rank_str[0]];
        }
        else { // 数字牌
            cards[i].rank = atoi(rank_str);
        }
        cards[i].suit = suit;
    }

    // 按rank升序排序
    qsort(cards, 5, sizeof(Card), compare);

    // 初始化变量
    int sameColor = 1; // 同花
    int dragon = 1; // 顺子
    int fourKind = 0; // 四条
    int threeKind = 0; // 三条
    int twoKind = 0; // 对子

    // 统计每种牌大小的出现次数
    int rank_counts[15] = {0};
    for(int i=0;i<5;i++) {
        rank_counts[cards[i].rank]++;
        if(i < 4) {
            // 判断顺子
            if(dragon && (cards[i].rank + 1) != cards[i+1].rank) {
                dragon = 0;
            }
            // 判断同花
            if(sameColor && cards[i].suit != cards[i+1].suit) {
                sameColor = 0;
            }
        }
    }

    // 特殊处理A2345
    if(cards[0].rank == 2 && cards[1].rank == 3 && cards[2].rank == 4 && cards[3].rank == 5 && cards[4].rank == 14) {
        dragon = 1;
    }

    // 判断四条、三条和对子
    for(int i=2;i<=14;i++) {
        if(rank_counts[i] == 4) fourKind = 1;
        if(rank_counts[i] == 3) threeKind = 1;
        if(rank_counts[i] == 2) twoKind = 1;
    }

    // 判断牌型
    int result;
    if(dragon && sameColor) {
        result = 1; // 同花顺
    }
    else if(fourKind) {
        result = 2; // 四条
    }
    else if(threeKind && twoKind) {
        result = 3; // 葫芦
    }
    else if(sameColor) {
        result = 4; // 同花
    }
    else if(dragon) {
        result = 5; // 顺子
    }
    else if(threeKind) {
        result = 6; // 三条
    }
    else {
        result = -1; // 无符合牌型
    }

    // 输出结果
    printf("%d\n", result);

    return 0;
}
// @hw code=end

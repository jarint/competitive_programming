#include <iostream>
#include <vector>

using namespace std;

typedef unsigned long long ull;
typedef long double ld;
typedef vector<int> vi;
typedef pair<int, int> pii;

vector<vi> prices, seats, memo;

int price(int w_left, int s_left) {
    if (w_left == -1)
        return 0;
    if(s_left == 0)
        return memo[w_left][0] = 0;
    if(memo[w_left][s_left] != -1)
        return memo[w_left][s_left];
    int res = 0;
    for(int i = 0; i < seats[w_left].size(); i++){
        int s = seats[w_left][i];
        int p = prices[w_left][i];
        if(s_left >= s)
            res = max(res, p * s + price(w_left - 1, s_left - s));
        else
            res = max(res, p * s_left + price(w_left - 1, 0));
    }
    return memo[w_left][s_left] = res;
}


int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int seats_left, weeks_left;
    cin >> seats_left >> weeks_left;

    prices.resize(weeks_left + 1);
    seats.resize(weeks_left + 1);

    for (int i = 0; i <= weeks_left; i++) {
        int k;
        cin >> k;
        for (int j = 0; j < k; j++) {
            int p;
            cin >> p;
            prices[weeks_left - i].push_back(p);
        }
        for (int j = 0; j < k; j++) {
            int s;
            cin >> s;
            seats[weeks_left - i].push_back(s);
        }
    }
    vi DEF(seats_left + 1, -1);
    memo.resize(weeks_left + 1, DEF);

    int res = price(weeks_left, seats_left);

    int price = 1001;
    int x = 0;
    for(int i = 0; i < seats[weeks_left].size(); i++){
        int s = seats[weeks_left][i];
        int p = prices[weeks_left][i];
        if(seats_left >= s){
            x = p * s;
            if(weeks_left != 0)
                x += memo[weeks_left - 1][seats_left - s];
        }
        else{
            x = p * seats_left;
            if(weeks_left != 0)
                x += memo[weeks_left - 1][0];
        }
        if(x == res)
            price = min(price, p);
    }
    cout << res << "\n" << price;
    return 0;
}

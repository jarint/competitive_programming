#include <bits/stdc++.h>

using namespace std;

pair<int, int> get_result(int num) {
    bool is_prime = true;
    int factor_sum = 0;
    while (num != 1) {
        bool has_factor = false;
        for (int factor = 2; factor <= num / factor; factor++) {
            if (num % factor == 0) {
                is_prime = false;
                has_factor = true;
                while (num % factor == 0) {
                    factor_sum += factor;
                    num /= factor;
                }
            }
        }
        if (!has_factor) {
            factor_sum += num;
            break;
        }
    }
    if (is_prime) return {num, 1};
    pair<int, int> next_result = get_result(factor_sum);
    return {next_result.first, next_result.second + 1};
}

int main() {
    int input;
    while (cin >> input) {
        if (input == 4) return 0;
        pair<int, int> result = get_result(input);
        cout << result.first << ' ' << result.second << '\n';
    }
}

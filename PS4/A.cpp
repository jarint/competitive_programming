#include <iostream>
#include <vector>
#include <bitset>
#include <cmath>

using namespace std;

const int MAX_SIZE = 100000000;
bitset<MAX_SIZE> is_prime;

void generate_sieve(int limit) {
    is_prime.set();
    is_prime[0] = is_prime[1] = false;
    for (int num = 2; num <= sqrt(limit) + 1; num++) {
        if (is_prime[num]) {
            for (int multiple = num * num; multiple < limit + 2; multiple += num) {
                is_prime[multiple] = false;
            }
        }
    }
}

int main() {
    int N, Q, query, prime_count = 0;
    cin >> N >> Q;
    
    generate_sieve(N);
    
    for (int i = 2; i <= N; i++) {
        if (is_prime[i]) {
            prime_count++;
        }
    }
    
    cout << prime_count << endl;
    
    while (Q--) {
        cin >> query;
        cout << (is_prime[query] ? "1" : "0") << endl;
    }
    
    return 0;
}

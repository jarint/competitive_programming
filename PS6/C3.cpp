#include <iostream>
#include <vector>

using namespace std;

typedef unsigned long long ull;
typedef long double ld;
typedef vector<int> vi;
typedef pair<int, int> pii;

vector<vi> ticket_prices, ticket_seats, memoization;

int compute_max_revenue(int weeks_remaining, int seats_remaining) {
    if (weeks_remaining == -1)
        return 0;
    if (seats_remaining == 0)
        return memoization[weeks_remaining][0] = 0;
    if (memoization[weeks_remaining][seats_remaining] != -1)
        return memoization[weeks_remaining][seats_remaining];
    
    int max_revenue = 0;
    for (int i = 0; i < ticket_seats[weeks_remaining].size(); i++) {
        int available_tickets = ticket_seats[weeks_remaining][i];
        int ticket_price = ticket_prices[weeks_remaining][i];
        if (seats_remaining >= available_tickets)
            max_revenue = max(max_revenue, ticket_price * available_tickets + compute_max_revenue(weeks_remaining - 1, seats_remaining - available_tickets));
        else
            max_revenue = max(max_revenue, ticket_price * seats_remaining + compute_max_revenue(weeks_remaining - 1, 0));
    }
    return memoization[weeks_remaining][seats_remaining] = max_revenue;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    int total_seats, total_weeks;
    cin >> total_seats >> total_weeks;

    ticket_prices.resize(total_weeks + 1);
    ticket_seats.resize(total_weeks + 1);

    for (int i = 0; i <= total_weeks; i++) {
        int num_price_options;
        cin >> num_price_options;
        for (int j = 0; j < num_price_options; j++) {
            int price;
            cin >> price;
            ticket_prices[total_weeks - i].push_back(price);
        }
        for (int j = 0; j < num_price_options; j++) {
            int seats;
            cin >> seats;
            ticket_seats[total_weeks - i].push_back(seats);
        }
    }
    
    vi memo_init(total_seats + 1, -1);
    memoization.resize(total_weeks + 1, memo_init);

    int max_revenue = compute_max_revenue(total_weeks, total_seats);

    int optimal_price = 1001;
    int calculated_revenue = 0;
    for (int i = 0; i < ticket_seats[total_weeks].size(); i++) {
        int available_tickets = ticket_seats[total_weeks][i];
        int ticket_price = ticket_prices[total_weeks][i];
        if (total_seats >= available_tickets) {
            calculated_revenue = ticket_price * available_tickets;
            if (total_weeks != 0)
                calculated_revenue += memoization[total_weeks - 1][total_seats - available_tickets];
        } else {
            calculated_revenue = ticket_price * total_seats;
            if (total_weeks != 0)
                calculated_revenue += memoization[total_weeks - 1][0];
        }
        if (calculated_revenue == max_revenue)
            optimal_price = min(optimal_price, ticket_price);
    }
    
    cout << max_revenue << "\n" << optimal_price;
    return 0;
}

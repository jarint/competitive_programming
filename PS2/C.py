import sys

election_list = []

def parse_input():
    num_test_cases = int(sys.stdin.readline().strip())
    
    while num_test_cases > 0:
        num_candidates = int(sys.stdin.readline().strip())
        this_election = []
        for i in range(num_candidates):
            this_election.append(int(sys.stdin.readline().strip()))
        election_list.append(this_election)
        num_test_cases = num_test_cases - 1

def check_win(election):
    max_votes = max(election)
    num_can = 0
    for candidate in election:
        if candidate == max_votes:
            num_can += 1
    if num_can == 1:
        return True
    else:
        return False
    
def determine_outcome(election_list):
    for election in election_list:
        total_votes = sum(election)
        if check_win(election):
            winner = election.index(max(election)) + 1
            num_votes = max(election)
            if ((num_votes / total_votes) > 0.5):
                print(f"majority winner {winner}")
            else:
                print(f"minority winner {winner}")
        else:
            print("no winner")


parse_input()
determine_outcome(election_list)
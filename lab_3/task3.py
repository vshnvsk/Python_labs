def count_votes(votes):
    vote_count = {}

    for candidate, vote in votes:
        if candidate in vote_count:
            vote_count[candidate] += vote
        else:
            vote_count[candidate] = vote

    return vote_count


def main():
    n = int(input("Enter the number of states: "))
    votes = []

    for _ in range(n):
        candidate, vote = input("Enter candidate name and votes: ").split()
        votes.append((candidate, int(vote)))

        vote_count = count_votes(votes)

        for candidate in sorted(vote_count):
            print(f"{candidate}: {vote_count[candidate]}")


if __name__ == "__main__":
    main()
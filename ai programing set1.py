def main():
    alice_friends = {"Emma", "Olivia", "Sophia", "Mia", "Charlotte"}
    bob_friends = {"Mia", "Sophia", "James", "Benjamin", "Lucas"}
    print(f"공통된 친구:{alice_friends&bob_friends}")
    print(f"Alice만 아는친구:{alice_friends-bob_friends}")
    print(f"Alice만 아는친구:{bob_friends-alice_friends}")
main()
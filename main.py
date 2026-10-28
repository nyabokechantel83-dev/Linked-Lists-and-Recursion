from linked_list import LinkedList


def main():
    roster = LinkedList()
    for emp_id in [101, 102, 103, 104, 105]:
        roster.insert_at_end(emp_id)

    print("Employee roster:   ", roster)
    print("Sum of IDs:        ", roster.recursive_sum())

    for target in (103, 999):
        found = roster.recursive_search(target)
        print(f"Search for {target}:   ", "Found" if found else "Not found")

    roster.recursive_reverse()
    print("Reversed roster:   ", roster)


if __name__ == "__main__":
    main()
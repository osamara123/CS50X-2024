import csv
import sys


def main():

    # TODO: Check for command-line usage
    if len(sys.argv) != 3:
        print("Invalid command line argument")
        sys.exit(1)

    # TODO: Read database file into a variable
    csv_file = open(sys.argv[1], 'r')
    csv_reader = csv.DictReader(csv_file)

    # TODO: Read DNA sequence file into a variable
    txt_file = open(sys.argv[2], 'r')
    txt_reader = txt_file.read()

    # TODO: Find longest match of each STR in DNA sequence
    AGATC_count = longest_match(txt_reader, "AGATC")
    AATG_count = longest_match(txt_reader, "AATG")
    TATC_count = longest_match(txt_reader, "TATC")

    # TODO: Check database for matching profiles
    for row in csv_reader:
        if int(row["AGATC"]) == AGATC_count and int(row["AATG"]) == AATG_count and int(row["TATC"]) == TATC_count:
            print(row["name"])
            return

    print("No match\n")


def longest_match(sequence, subsequence):
    """Returns length of longest run of subsequence in sequence."""

    # Initialize variables
    longest_run = 0
    subsequence_length = len(subsequence)
    sequence_length = len(sequence)

    # Check each character in sequence for most consecutive runs of subsequence
    for i in range(sequence_length):

        # Initialize count of consecutive runs
        count = 0

        # Check for a subsequence match in a "substring" (a subset of characters) within sequence
        # If a match, move substring to next potential match in sequence
        # Continue moving substring and checking for matches until out of consecutive matches
        while True:

            # Adjust substring start and end
            start = i + count * subsequence_length
            end = start + subsequence_length

            # If there is a match in the substring
            if sequence[start:end] == subsequence:
                count += 1

            # If there is no match in the substring
            else:
                break

        # Update most consecutive matches found
        longest_run = max(longest_run, count)

    # After checking for runs at each character in seqeuence, return longest run found
    return longest_run


main()

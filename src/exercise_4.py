def run_length_code_sequence(sequence: str):

    previous_char = sequence[0]
    counter = 0

    # We will save the char and its number of occurrences
    occurrences = []

    for _s in sequence:
        if _s == previous_char:
            counter = counter + 1
            continue

        # Save the number of occurrences
        occurrences.append([previous_char, counter])

        # Update the previous char
        previous_char = _s
        counter = 1

    # Add the last character occurrences
    occurrences.append([previous_char, counter])

    print(occurrences)


def main():
    st = "wwwwaaadexxxxxxywww"
    run_length_code_sequence(st)


if __name__ == "__main__":
    main()

"""Solution for Exercise 4."""


def run_length_code_str_byte_sequence(sequence: bytes,
                                      encoding: str = "utf-8") -> bytes:
    """
    Apply run-length encoding to the given byte sequence.

    :param sequence: Byte string sequence to apply the run-length encoding\
    :param encoding: encoding type. default: utf-8
    per character
    :return: string representing the code from the run-length encoding
    """
    # Decode the sequence
    sequence_str = sequence.decode(encoding)

    previous_char = sequence_str[0]
    counter = 0

    # We will save the char and its number of occurrences
    occurrences = []

    for _s in sequence_str:
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

    # Compute the final string
    code = ''.join([f"{_c}{_o}" for _c, _o in occurrences])

    return bytes(code, encoding)


def main():
    """
    Show an example of how to use the constructed functions.

    :return: no return
    """
    byte_string_sequence = b"wwwwaaadexxxxxxywww"

    code = run_length_code_str_byte_sequence(byte_string_sequence)

    print(code)


if __name__ == "__main__":
    main()

# @pytest.fixture
# def sequences():
#    return ["agctctt", "tggtgta", "gcttagt", "aaaagtctgt"]


def simple_loop(sequences):
    lengths = []
    for sequence in sequences:
        lengths.append(len(sequence))
    return lengths


def double_loop(sequences):
    all_ascii_codes = []
    for sequence in sequences:
        ascii_codes = []
        for char in sequence:
            ascii_codes.append(ord(char))
        all_ascii_codes.append(ascii_codes)
    return all_ascii_codes


def set_comprehension(sequences):
    alphabet = set([])
    for sequence in sequences:
        for char in sequence:
            alphabet.add(char)

    return alphabet


def two_operations(sequences):
    lens = []
    for sequence in sequences:
        adjusted_sequence = sequence.replace("a", "")
        lens.append(len(adjusted_sequence))
    return lens


def len_sum(sequences):
    total = 0
    for sequence in sequences:
        total += len(sequence)

    return total


def len_filter(sequences):
    a_counts = []
    for sequence in sequences:
        if len(sequence) > 5:
            a_counts.append(sequence.count("a"))
    return a_counts


def age_filter(sequences, ages):
    assert len(sequences) == len(ages)
    a_counts = []
    for i in range(len(sequences)):
        if ages[i] >= 15:
            a_counts.append(sequences[i].count("a"))
    return a_counts

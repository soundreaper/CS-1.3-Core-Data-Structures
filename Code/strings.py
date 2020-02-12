#!python

def contains(text, pattern):
    """Return a boolean indicating whether pattern occurs in text."""
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)
    # TODO: Implement contains here (iteratively and/or recursively)
    """
    Best case runtime: O(1) if pattern occurs at 0th index
    Worst case: O(n) if pattern is at the very end
    """
    if find_index(text, pattern) is not None:
        return True
    else:
        return False

def find_index(text, pattern, p_letter=0, index=0):
    """Return the starting index of the first occurrence of pattern in text,
    or None if not found."""
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)
    # TODO: Implement find_index here (iteratively and/or recursively)
    """
    Best case runtime: O(1) if pattern occurs at 0th index
    Worst case: O(n) if pattern is at the very end
    """
    if pattern == '':
        return index

    while index < len(text):
        if text[index] == pattern[p_letter]:
            if p_letter == len(pattern) - 1:
                return index - p_letter
            i = find_index(text, pattern, index + 1, p_letter + 1)
            if i is not None:
                return i
        elif p_letter > 0:
            return None
        index += 1
    return None

def find_all_indexes(text, pattern):
    """Return a list of starting indexes of all occurrences of pattern in text,
    or an empty list if not found."""
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)
    # TODO: Implement find_all_indexes here (iteratively and/or recursively)
    indexes = []

    i = find_index(text, pattern)
    
    if i is not None:
        indexes.append(i)
    else:
        return indexes
    for index in indexes:
        i = find_index(text, pattern, index + 1)
        if i is not None and i < len(text):
            indexes.append(i)
        else:
            break
    return indexes
    
def test_string_algorithms(text, pattern):
    found = contains(text, pattern)
    print('contains({!r}, {!r}) => {}'.format(text, pattern, found))
    # TODO: Uncomment these lines after you implement find_index
    index = find_index(text, pattern)
    print('find_index({!r}, {!r}) => {}'.format(text, pattern, index))
    # TODO: Uncomment these lines after you implement find_all_indexes
    indexes = find_all_indexes(text, pattern)
    print('find_all_indexes({!r}, {!r}) => {}'.format(text, pattern, indexes))


def main():
    """Read command-line arguments and test string searching algorithms."""
    import sys
    args = sys.argv[1:]  # Ignore script file name
    if len(args) == 2:
        text = args[0]
        pattern = args[1]
        test_string_algorithms(text, pattern)
    else:
        script = sys.argv[0]
        print('Usage: {} text pattern'.format(script))
        print('Searches for occurrences of pattern in text')
        print("\nExample: {} 'abra cadabra' 'abra'".format(script))
        print("contains('abra cadabra', 'abra') => True")
        print("find_index('abra cadabra', 'abra') => 0")
        print("find_all_indexes('abra cadabra', 'abra') => [0, 8]")

if __name__ == '__main__':
    main()

import re


def count_substring(string, sub_string):
    matches = re.findall(f"(?={sub_string})", string)
    return len(matches)


if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)


"""
Without the "(?= ... )" structure, the regex won't match properly, because some of the characters may have
been "used up" in a previous match.

The"(?= ... )" structure tells the regex that those characters must be included for the match to succeed,
but the characters they match are still available for future searches. Think of it like a head and a body.
Every match must contain a head and a body. But part of the body can be used as the head of a future search.
In the example, "CDC" is the match, "C" is the head and "DC" is the body. The second "C" (in the body) can
be used as a future head in another search.
"""

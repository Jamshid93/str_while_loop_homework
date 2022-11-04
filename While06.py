def main(s):
    """
    A variable of type str is given. Find and return how many consonant letters there are.
    Args:
        s: str
        consonant: other than vowels(a, e, i, o, u)
    Returns:
        int: return answer
    """
    i=0
    count=""
    consonant="aeiou"
    while i<len(s):
        if s[i].lower() not in consonant:
            count+=s[i]
        i+=1
    count=len(count)
    return int(count)
print(main("CodeschoolUz"))
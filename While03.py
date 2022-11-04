from string import punctuation
def main(s):
    """
    A variable of type str is given. Find how many punctuations it contains and return.
    Args:
        s: str
    Returns:
        int: return answer
    """
    i=0
    punct=""
    while i<len(s):
        if s[i] in punctuation:
            punct+=s[i]
        i+=1
    punct=len(punct)
    return int(punct)
print(main("#hashtag@$"))
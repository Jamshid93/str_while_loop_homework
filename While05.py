def main(s):
    """
    A variable of type str is given. Find how many lowercase letters there are and return.
    Args:
        s: str
    Returns:
        int: return answer
    """
    i=0
    lower=""
    while i<len(s):
        if s[i].islower():
            lower+=s[i]
        i+=1
    lower=len(lower)
    return int(lower)
print(main("CodeschoolUz"))
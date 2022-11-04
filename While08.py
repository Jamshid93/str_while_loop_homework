def main(s):
    """
    A string of numbers is given. Find how many odd numbers there are and return.
    Args:
        s: str
    Returns:
        int: return answer
    """
    i=0
    count=""
    while i<len(s):
        if int(s[i])%2!=0:
            count+=s[i]
        i+=1
    count=len(count)
    return int(count)
print(main("3489769"))
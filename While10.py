def main(s):
    """
    A string of numbers is given. Find and return the sum of all odd numbers.
    Args:
        s: str
    Returns:
        int: return answer
    """
    i=0
    q = 0
    while i<len(s):
        i_s = int(s[i])
        if i_s % 2 == 1:
            q+=i_s
        i+=1
    return q 
print(main("589765"))    
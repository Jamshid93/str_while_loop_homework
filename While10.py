def main(s):
    """
    A string of numbers is given. Find and return the sum of all odd numbers.
    Args:
        s: str
    Returns:
        int: return answer
    """
    i=0
    a=int(s)
    while a!=0:
        a=a%10
        a//=10
        if a%2!=0:
            i+=a
    return i
print(main("589765"))    
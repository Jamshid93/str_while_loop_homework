def main(s):
    """
    A string of numbers is given. Find the sum of all the numbers and return.
    Args:
        s: str
    Returns:
        int: return answer
    """
    i=0
    a=int(s)
    while a!=0:
        i+=a%10
        a=a//10
    return i
print(main("987654"))    
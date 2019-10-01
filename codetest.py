def average(L):
    if not L:

      return None
    else:
        return sum(L)/len(L)
if __name__ == "__main__":
    L = [1,2,3,4,5,6,7]
    expected_result = 3.0
    assert expected_result == average(L), "average() produce incorrect result"
    print(average(L))


def average(N):
    if not N:
        return None
    return sum(N) / len(N)


if __name__ == '__main__':
    x = [2, 4, 5, 8]
    except_result = 4.75
    result = average(x)
    if except_result == result:
        print("Test Passed")
    else:
        print(f"Test failed! Received result: {result}, Excepted: {except_result}")

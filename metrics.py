def window_max(data: list, n: int) -> list:
    """
    Calculate maximum value of every "n"-size window

    Args:
        data (list[int]): list of integers representing heart rate samples
        n (int): The size of your window
    Returns:
        list[int]: list of maximums from each window (size should be len(data)//6)
    """
    maximums = []

    for j in range(0,len(data),n):
        maximum = data[j:j + n]
        maximums.append(max(maximum))
    return maximums

def window_average(data: list, n: int) -> list:
    results = []

    for j in range(0,len(data),n):
        window = data[j:j + n]
        window_average = sum(window) /len(window)
        results.append(window_average)
    return results

def window_stddev(data: list, n: int) -> list:
    results = []
    
    for j in range(0,len(data), n):
        window = data[j+j+n]
        if len(window) == 1:
            continue
        window_average = sum(window) / len(window)
        variance =sum((j - window_average)** 2 for j in window) / (len(window) -1)
        result.append(round(std_dev,2))

    return results

def list_avg(
    sequence: list
) -> float:  # this means sequence needs to be a list.  Can also do : str or : int, and others to say what needs to be passed into the argument
    return sum(sequence) / len(sequence)


print(list_avg((123, 123)))

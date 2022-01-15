"""
A difference sequence(계차수열 in Korean) is a sequence of differences between two neighbored elements.
For example, if the sequence B consists of the difference of two neighbored elements of the sequence A,
then we call sequence B as the difference sequence of sequence A.

Let's look at an example.
Where seq A = [0, 1, 4, 9, 16, 25, 36], then the difference sequence of A is:
                \/ \/ \/ \/ \ /  \ /
      seq B = [ 1, 3, 5, 7,  9,  11]

What we are going to do are:
1. Declare the function 'create_difference_sequence' that returns a difference sequence.

   The usage of the function will be:
   diff_seq = create_difference_sequence([0, 1, 4, 9, 16, 25, 36])
   print(diff_seq)  # the result will be [1, 3, 5, 7, 9, 11]

2. Using the function 'create_difference_sequence',
   store the difference sequence of the sequence [0, 1, 4, 9, 16, 25, 36] to the element 'diff_seq' then print it.
"""


def create_difference_sequence(sequence):
    diff_seq = []

    for i in range(1, len(sequence)):
        diff_seq.append(sequence[i] - sequence[i-1])

    return diff_seq


sequence = [0, 1, 4, 9, 16, 25, 36]
diff_seq = create_difference_sequence(sequence)
print(diff_seq)

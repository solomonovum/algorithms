def quick_sort(data):
    """To sort data as an increase order by divide and conquer method."""

    def q_sort(left_index, right_index):
        """Do quicksort recursively."""

        if right_index <= left_index:
            return

        # Sort sub partition.
        part = partition(left_index, right_index)

        # Handle left-side.
        q_sort(left_index, part - 1)

        # Handle right-side.
        q_sort(part + 1, right_index)

    def partition(low_index, high_index):
        """Do partition by quicksort method."""

        # Set pivot.
        pivot, pivot_index = data[high_index], high_index
        high_index -= 1

        while low_index <= high_index:
            while data[low_index] < pivot:
                low_index += 1
            while data[high_index] > pivot:
                high_index -= 1

            if low_index < high_index:
                data[low_index], data[high_index] = data[high_index], data[low_index]
                low_index, high_index = low_index + 1, high_index - 1

        data[low_index], data[pivot_index] = data[pivot_index], data[low_index]

        return low_index

    # Call quick sort main function.
    return q_sort(0, len(data) - 1)

def bubble_sort(data):
    """To sort data as an increase order by bubble sort method."""

    total_length_for_loop = len(data) - 1

    for sorted_item_count in range(total_length_for_loop):
        for item_index in range(total_length_for_loop - sorted_item_count):
            is_swap = False

            # swap
            if data[item_index] > data[item_index + 1]:
                data[item_index], data[item_index + 1] = data[item_index + 1], data[item_index]
                is_swap = True

        # if sorted already
        if is_swap is False:
            break

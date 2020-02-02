from linkedlist.singlylinkedlist import Node
from linkedlist.singlylinkedlist import SinglyLinkedList

if __name__ == '__main__':
    node1 = Node(15)
    node2 = Node(8.2)
    node3 = Node(3)

    track = SinglyLinkedList()

    # Append
    print('append')
    track.append(56)
    track.append(40)
    track.append(1)
    track.append(30)
    track.append(20)
    track.append(10)

    for item in track:
        print(item)

    # Insert
    print('\ninsert')
    track.insert(5, 77)

    for item in track:
        print(item)

    # Index
    print('\nindex')
    search_item = 77
    print(f'{search_item} is at {track.index(search_item)}')

    # Remove
    print('\nremove')
    removed_item = 10
    track.remove(removed_item)

    for item in track:
        print(item)

    # Pop
    print('\npop')
    print(track.pop())

    # Reverse
    print('\nbefore reverse')
    for item in track:
        print(item)

    print('\nreverse')
    track.reverse()

    for item in track:
        print(item)

    # Sort
    print('\nsort')
    track.sort()

    for item in track:
        print(item)

    # Clear
    print('\nclear')
    track.clear()

    for item in track:
        print(item)

    print(f'total length : {track.size()}')

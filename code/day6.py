import logging


def reallocate(blocks):
    max_block = max(blocks)
    for i in range(len(blocks)):
        if blocks[i] == max_block:
            blocks[i] = 0
            index = i + 1
            break

    for i in range(max_block):
        if index >= len(blocks):
            index = 0
        blocks[index] += 1
        index += 1


if __name__ == '__main__':
    logging.basicConfig(filename='day6.log', filemode='w', level=logging.DEBUG)
    file = open('day6.txt', 'r')
    text = file.read()
    blocks = [int(n) for n in text.split('\t')]

    view = tuple(blocks)
    logging.debug(view)
    views = [view]
    while True:
        reallocate(blocks)
        view = tuple(blocks)
        logging.debug(view)
        if view in views:
            break
        views.append(view)

    final_view = view
    print(final_view)
    counter = 0
    while True:
        reallocate(blocks)
        view = tuple(blocks)
        if view == final_view:
            break
        counter += 1

    print(counter)
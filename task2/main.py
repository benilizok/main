if __name__ == '__main__':

    # Splitting string into list
    lst = input().split()
    word_count = len(lst)

    # Calculating parameters of input list
    # different words count
    diff_word_count = 0
    # maximal length of word
    max_len = 0
    unique_lst = []
    for x in lst:
        if x not in unique_lst:
            diff_word_count += 1
            unique_lst.append(x)
            if len(x) > max_len:
                max_len = len(x)

    # Creating 2D array (diff_word_count rows, 3 cols)
    mas = []
    for i in range(diff_word_count):
        mas.append([unique_lst[i], 0, 0])

    # Filling array
    max_freq = 0
    for i in range(word_count):
        for j in range(diff_word_count):
            if lst[i] == mas[j][0]:
                mas[j][1] += 1
                if mas[j][1] > max_freq:
                    max_freq = mas[j][1]
                break

    # Calculating relative frequencies and filling low_lines
    for i in range(diff_word_count):
        # low_lines
        if len(mas[i][0]) < max_len:
            mas[i][0] = '_'*(max_len-len(mas[i][0]))+mas[i][0]
        # frequencies
        if mas[i][1] == max_freq:
            mas[i][2] = 10
        else:
            mas[i][2] = round((mas[i][1])*10/max_freq)

    # Output the relative frequencies diagram
    for i in range(diff_word_count):
        print(mas[i][0], ' ', '.'*mas[i][2])

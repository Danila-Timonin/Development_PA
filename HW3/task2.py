def min_el(in_st, flag):
    a = in_st.split(" ")
    min = int(a[0])
    if flag == 1:
        return a[0]
    else:
        for i in range(len(a) - 1):
            if int(a[i + 1]) < min:
                min = int(a[i + 1])
        return min
def valid(l):
    return l[0] * 10 + l[1] < 24 and l[2] * 10 + l[3] < 60


def max_valid_time(A, B, C, D):

    l = [A, B, C, D]
    s = [(2, 1,), (3, 9), (5,), (9,)]
    h = []

    try:
        for i, v in enumerate(s):
            if len(h) == 1:
                m = max(list(filter(lambda x: x <= v[1] if h[0] <= 1 else x <= v[0], l)))
            else:
                m = max(list(filter(lambda x: x <= v[0], l)))
            
            h.append(m)
            l.remove(m)

        return "%s%s:%s%s" % tuple(h)

    except ValueError:
        try:
            h = []
            l = [A, B, C, D]
            for i, v in enumerate(s):
                if len(h) < 2:
                    m = max(list(filter(lambda x: x <= v[1], l)))
                else:
                    m = max(list(filter(lambda x: x <= v[0], l)))
                h.append(m)
                l.remove(m)

            return "%s%s:%s%s" % tuple(h)
        
        except ValueError:
            return "NOT POSSIBLE !"




print(max_valid_time(1,2,7,9))
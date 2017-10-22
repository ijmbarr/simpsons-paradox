
def create_table(df):

    wrap = lambda s, tag, option="": "<" + tag + " " + option + ">" + s + "</" + tag + ">"
    wrap_list = lambda lst, tag: "".join(map(lambda s: wrap(str(s), tag), lst))

    table = ""

    table += wrap(wrap("z", "th") + 
                  wrap("X=0","th","colspan='2'") +
                  wrap("X=1","th","colspan='2'"), "tr")



    for z in sorted(df.z.unique()):
        d = df[df.z == z].set_index(["x", "y"])["count"].to_dict()

        n0 = int(d[(0,0)] + d[(0,1)])
        p0 = d[(0,1)] / n0 if n0 != 0 else 0
        n1 = int(d[(1,0)] + d[(1,1)])
        p1 = d[(1,1)] / n1 if n1 != 0 else 0
        
        f0 = "{}/{}".format(int(d[(0,1)]), n0) 
        f1 = "{}/{}".format(int(d[(1,1)]), n1)
        p0s = "{:.2f}".format(p0)
        p1s = "{:.2f}".format(p1) 
        
        if p0 >= p1:
            f0 = wrap(f0, "b")
            p0s = wrap(p0s, "b")
        else:
            f1 = wrap(f1, "b")
            p1s = wrap(p1s, "b")

        table += wrap(wrap_list([z, f0, p0s, f1, p1s], "td"), "tr")

    d = df.groupby(["x", "y"])["count"].sum().to_dict()

    n0 = int(d[(0,0)] + d[(0,1)])
    p0 = d[(0,1)] / n0 if n0 != 0 else 0
    n1 = int(d[(1,0)] + d[(1,1)])
    p1 = d[(1,1)] / n1 if n1 != 0 else 0

    f0 = "{}/{}".format(int(d[(0,1)]), n0) 
    f1 = "{}/{}".format(int(d[(1,1)]), n1)
    p0s = "{:.2f}".format(p0)
    p1s = "{:.2f}".format(p1) 

    if p0 >= p1:
        f0 = wrap(f0, "b")
        p0s = wrap(p0s, "b")
    else:
        f1 = wrap(f1, "b")
        p1s = wrap(p1s, "b")

    table += wrap(wrap_list(["total:", f0, p0s, f1, p1s], "td"), "tr")

    return table

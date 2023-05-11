def pythag_expct(table, t_name=""):
    if t_name != "":
        team = table.query('Squad == @t_name')
        gf = team["GF"].values[0]
        ga = team["GA"].values[0]
        return gf ** 1.35 / (gf ** 1.35 + ga ** 1.35) * 38

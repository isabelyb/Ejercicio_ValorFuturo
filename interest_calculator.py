def f_value(p_val,  p_int, t_per):
    f_val = round((p_val * (1 + p_int)**t_per), 1)
    return f_val


def p_value(f_val, p_int, t_per):
    p_val = round((f_val / (1 + p_int)**t_per), 1)
    return p_val


def p_interest(p_val, t_per, f_val):
    p_int = round(((f_val/p_val)**(1/t_per)  - 1),3)
    return p_int


def t_period(p_val, f_val, p_int):
    t_per = round((np.log(f_val/p_val) / np.log(1+p_int)), 1)
    return t_per


def run():
    pass


if __name__ == '__main__':
    run()
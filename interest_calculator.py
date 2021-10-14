import numpy as np


def main():     
    intro = """
    What do you want to calculate: 
    1 -> Future value
    2 -> Present Value
    3 -> Interest period
    4 -> Total period
    5 -> Nominal interest by the period

    Option: """    

    option = int(input(intro)) 

    if option == 1:
        print(f'The future value calculated is {f_value()}')
    elif option == 2:
        print(f'The present value calculated is {p_value()}')
    elif option == 3:
        print(f'The periodic interest calculated is {p_interest()} %')
    elif option == 4:
        print(f'The total period calculated is {t_period()} periods')
    elif option == 5:
        print(f'The nominal interest by period calculated is {n_interest()} %')
    else:
        print("Select a correct option")
        main()


def f_value():
    p_val = float(input('How much is the present value? '))
    p_int = float(input('What is the period interest in percentage? '))
    t_per = float(input('What is the total periods? '))
    f_val = round((p_val * (1 + p_int/100)**t_per), 1)
    return f_val


def p_value():
    f_val = float(input('How much is the future value? '))
    p_int = float(input('What is the period interest in percentage? '))
    t_per = float(input('What is the total periods? '))
    p_val = round((f_val / (1 + p_int/100)**t_per), 1)
    return p_val


def p_interest():
    p_val = float(input('How much is the present value? '))
    t_per = float(input('What is the total periods? '))
    f_val = float(input('How much is the future value? '))
    p_int = (f_val/p_val)**(1/t_per) - 1
    return round((p_int*100),2)


def t_period():
    p_val = float(input('How much is the present value? '))
    f_val = float(input('How much is the future value? '))
    p_int = float(input('What is the period interest in percentage? '))
    t_per = round((np.log(f_val/p_val) / np.log(1+(p_int/100))), 1)
    return t_per


def n_interest():
    p_int = float(input('What is the period interest in percentage? '))
    t_per = float(input('What is the total periods? '))
    n_int = ((((p_int/100)+1)**(1/t_per))-1)*t_per
    return round((n_int*100),5)


if __name__ == '__main__':
    main()
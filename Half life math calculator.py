# Simple math graphers and half life calculators
import math, matplotlib.pyplot, numpy
input_1 = input("Exponential Equation Grapher(1), Half life calculator(2), Linear Equation Grapher(3), Compound interest calculator(4) : ")

if input_1 == "2":
    while True:
        Q_input = input("""What part of the half life formula are you trying to find? 
                        A:(1), A_0:(2), T:(3), H:(4): """)
        if Q_input == "1":
            A_0 = float(input("What is the initial amount?: "))
            Time = float(input("What is the total amount of time?: "))
            Half_life = float(input("What is the Half Life?: "))
            sub_pow = Time / Half_life
            Power_1 = pow(0.5, sub_pow)
            A = A_0 * Power_1
            print("The A is", A)


        if Q_input == "2":
            A = float(input("What is the final amount?: "))
            Time = float(input("What is the total amount of time?: "))
            Half_life = float(input("What is the Half Life?: "))
            sub_pow = Time/Half_life
            Power_1 = pow(0.5, sub_pow)
            A_0 = A / Power_1
            print("The A_0 is", A_0)


        if Q_input == "3":
            A = float(input("What is the final amount?: "))
            Half_life = float(input("What is the Half Life?: "))
            A_0 = float(input("What is the initial amount?: "))
            pt_1 = math.log(A / A_0)
            pt_2 = math.log(0.5)
            pt_combined = pt_1 / pt_2
            Time = Half_life * pt_combined
            print("The total time is", Time)


        if Q_input == "4":
            A = float(input("What is the final amount?: "))
            A_0 = float(input("What is the initial amount?: "))
            Time = float(input("What is the total amount of time?: "))
            pt_1 = Time * math.log(0.5)
            pt_2 = math.log(A / A_0)
            Half_life = pt_1 / pt_2
            print("The half life is", Half_life)
        input_graph = input("Would you like to graph your equation? Yes(1), No(2) : ")
        if input_graph == "1":
            start_input = int(input("Where would you like your graph to start?: "))
            end_input = int(input("Where would you like your graph to end?: "))
            if start_input < 0:
                print("ERROR: The starting point cannot be less than 0")
                start_input = 0
            if end_input < Time:
                end_input = Time
            acc_input = input("""How accurate do you want your graph to be?
                               less accurate(1), accurate(2), more accurate(3) : """)
            if acc_input == "1":
                acc_input = 4
            if acc_input == "2":
                acc_input = 9
            if acc_input == "3":
                acc_input = 15
                acc_input = 9
            points = int(Time) * acc_input
            x_val = numpy.linspace(start_input, end_input, points)
            A = A_0 * (0.5) ** (x_val / Time)
            matplotlib.pyplot.plot(x_val, A, label = "Graph of your Half life Equation")
            matplotlib.pyplot.xlabel("Time")
            matplotlib.pyplot.ylabel("Total amount over time")
            matplotlib.pyplot.title("Graph of your Half life Equation")
            matplotlib.pyplot.grid(True)
            matplotlib.pyplot.legend()
            matplotlib.pyplot.show()
            break
        if input_graph == "2":
            break
if input_1 == "1":
    while True:
        A_1 = int(input("What is the y intercept of your equation?: "))
        B_1 = int(input("What is the Growth or decay or your equation?: "))
        start_input = int(input("Where do you want the graph to start?: "))
        end_input = int(input("Where do you want the graph to end?: "))
        acc_input = int(input("""How accurate do you want your graph to be?
                              less accurate(1), accurate(2), more accurate(3) : """))
        if acc_input == "1":
            acc_input = 4
        if acc_input == "2":
            acc_input = 8
        if acc_input == "3":
            acc_input = 14
            acc_input = 9
        points = (abs(start_input) + abs(end_input)) * acc_input
        X = numpy.linspace(start_input, end_input, points)
        Y_1 = pow(B_1, X)
        Y = A_1 * Y_1
        matplotlib.pyplot.plot(X, Y, label='Your exponential function graph')
        matplotlib.pyplot.xlabel("X")
        matplotlib.pyplot.ylabel("Y")
        matplotlib.pyplot.title("Plot of your exponential graph")
        matplotlib.pyplot.grid(True)
        matplotlib.pyplot.legend()
        matplotlib.pyplot.show()
        break

if input_1 == "3":
    while True:
        m = int(input("What is the slope of your equation?: "))
        b = int(input("What is the y-intercept of your equation?: "))
        start_input = int(input("Where do you want the graph to start?: "))
        end_input = int(input("Where do you want the graph to end?: "))
        acc_input = input("""How accurate do you want the graph to be? 
                         less accurate(1), accurate(2), more accurate(3) : """)
        if acc_input == "1":
            acc_input = 3
        if acc_input == "2":
            acc_input = 6
        if acc_input == "3":
            acc_input = 10
        else:
            print("ERROR: The input you gave was not valid")
            acc_input = 6
        points = (abs(start_input) + abs(end_input)) * acc_input
        X = numpy.linspace(start_input, end_input, acc_input)
        y = m*X+b
        matplotlib.pyplot.plot(X, y, label ="Your linear equation")
        matplotlib.pyplot.xlabel("X")
        matplotlib.pyplot.ylabel("Y")
        matplotlib.pyplot.title("Graph of your linear equation")
        matplotlib.pyplot.grid(True)
        matplotlib.pyplot.legend()
        matplotlib.pyplot.show()
        break

if input_1 == "4":
    while True:
        P_1 = int(input("What is the inital amount of money you put in?: "))
        R_1 = float(input("What is the interest rate in decimal?: "))
        N_1 = int(input("What is the amount of times compounded per year?: "))
        T_1 = int(input("What is the total amount of time?: "))
        pt_1 = 1 + R_1 / N_1
        pt_2 = N_1 * T_1
        pt_comb = pow(pt_1, pt_2)
        A = P_1 * pt_comb
        print("The total amount is", A)
        input_graph = input("Would you like to graph this equation? Yes(1) No(2) : ")
        if input_graph == "1":
            start_input = int(input("Where do you want your graph to start?: "))
            if start_input < 0:
                print("ERROR: The starting input for compound interests cant be less than 0")
                start_input = 0
            end_input = int(input("Where do you want your graph to end?: "))
            acc_input = input("""How accurate do you want your graph to be?
                                   less accurate(1), accurate(2), more accurate(3) : """)
            if acc_input == "1":
                acc_input = 4
            if acc_input == "2":
                acc_input = 8
            if acc_input == "3":
                acc_input = 12
            else:
                print("ERROR: The input you gave was not valid")
                acc_input = 8
            points = T_1 * acc_input
            x_val = numpy.linspace(start_input, end_input, points)
            A_val = P_1 * (1 + R_1 / N_1) ** (N_1 * x_val)
            matplotlib.pyplot.plot(x_val, A_val, label = "Your compound interest graph")
            matplotlib.pyplot.xlabel("Inital amount")
            matplotlib.pyplot.ylabel("Total amount")
            matplotlib.pyplot.title("Your compound interest graph")
            matplotlib.pyplot.grid(True)
            matplotlib.pyplot.legend()
            matplotlib.pyplot.show()
            break
        if input_graph == "2":
            break
        

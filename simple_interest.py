def calculate_simple_interest(principal, rate, time):
    return (principal * rate * time) / 100

def__name__== "__main__":

p = float(input("Enter Principal: "))
r = float(input("Enter Rate: "))
t = float(input("Enter Time: "))
si = calculate_simple_interest(p, r, t)
print("Simple Interest:", si)
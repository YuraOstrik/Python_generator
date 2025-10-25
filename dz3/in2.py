def fibonaci(start, end):
    a = 0
    b = 1

    while a <= end:
        if a >= start:
            yield a

        a, b = b, a + b

st = 50
end = 500

for num in fibonaci(st, end):
    print(num)

# Second

c = [1,2,3,4,5,6]
d = [2,5,6,7,8]

def sum(c,d):
    if len(c) < len(d):
        middle = len(c)
    else:
        middle = len(d)
    for i in range(middle):
        yield c[i] + d[i]

print(list(sum(c,d)))

# Third


list_to_work = [1,2,3,4,5,6]

def square(number):
    return number ** 2

def cube(number):
    return number ** 3

def calculate(list_to_work, function_to_call):
    return list(map(function_to_call, list_to_work))

print(calculate(list_to_work, cube))


#Fourth

def organization(func):
    def wrapper(*args, **kwargs):
        original = func(*args, **kwargs)
        
        header = "Звіт"
        return header + original
    return wrapper

def generate(company, period):
    return (f"Компанія: {company}\n"
            f"Період: {period}\n"
            f"Дохід: 1000000\n"
            f"Прибуток: 300000")

@organization
def report():
    return generate("MyCorp LLC", "Q4")

print(report())










def divisors(num):
    divisors = []
    for i in range(1, num + 1):
        if num % i == 0:
            divisors.append(i)
    return divisors

def execute():
    num = int(input("Debes ingresar un número: "))
    print(divisors(num))
    print("Terminó mi programa")

def run():
    try:
        num = int(input("Inresa un número: "))
        print(divisors(num))
        print("Terminó mi programa")
    except ValueError:
        execute()

if __name__ == "__main__":
    run()
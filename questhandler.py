import questparser as qp
import questloader as ql

def start_quest(number):
    data = ql.load_quest(number)
    if qp.is_doable(data) != True:
        print("Something is heavily fucked up!")
        return None

start_quest("1")
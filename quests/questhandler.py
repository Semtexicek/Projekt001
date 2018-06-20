import quests.questparser as qp
import quests.questloader as ql

def perform_quest(number):
    data = ql.load_quest(number)
    if qp.is_doable(data) != True:
        print("Something is heavily fucked up!")
        return None

    start = start_quest(data)
    if start:
        progress = continue_quest(data)
    if progress != -1:
        finish = finish_quest(data, progress)

    if start and progress != -1:
        datadone = ql.set_done(data)
        # ql.save_and_close_json(datadone, number)
        return finish

    else:
        print("Still horribly broken")
        return -1

def start_quest(data):
    print(qp.get_name(data))
    print(qp.get_description(data))

    if qp.get_type(data) == "fight":
        if start_fight(qp.get_enemy(data)) != True:
            return False

    return True



def continue_quest(data):
    options = []
    x = 0

    for i in qp.get_phases(data):
        print("{0}: {1}".format(i["option"], i["description"]))
        options.append(str(i["option"]))

    while(x < 3):
        option = input("vyber cislo:\n")
        if option in options:
            return int(option)
        print("zadavas picoviny!")
        x += 1

    return -1

def finish_quest(data, option):
    phase = qp.get_phases(data)[option - 1]
    print(phase["result"])
    return phase["continues"]

def start_fight(enemyId):
    return True
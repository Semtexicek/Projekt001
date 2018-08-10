import quest as q
import questloader as ql
import messagehandler as m
import discord
from discord.ext import commands

class Questhandler(object):
    def __init__(self, bot):
        self.bot = bot

def perform_quest(number):
    q.is_doable()
    data = ql.load_quest(number)
    if qp.is_doable(data) != True:
        m.post_message("Something is heavily fucked up!")
        return None

    start = start_quest(data)
    if start:
        progress = continue_quest(data)
    if progress != -1:
        finish = finish_quest(data, progress)

    if start and progress != -1:
        # datadone = ql.set_done(data)
        # ql.save_and_close_json(datadone, number)
        return finish

    else:
        m.post_message("Still horribly broken")
        return -1

def start_quest(data):
    m.post_message(qp.get_name(data))
    m.post_message(qp.get_description(data))

    if qp.get_type(data) == "fight":
        if start_fight(qp.get_enemy(data)) != True:
            return False

    return True



def continue_quest(data):
    options = []
    x = 0

    for i in qp.get_phases(data):
        m.post_message("{0}: {1}".format(i["option"], i["description"]))
        options.append(str(i["option"]))

    while(x < 3):
        option = input("vyber cislo:\n")
        if option in options:
            return int(option)
        m.post_message("zadavas picoviny!")
        x += 1

    return -1

def finish_quest(data, option):
    phase = qp.get_phases(data)[option - 1]
    m.post_message(phase["result"])
    return phase["continues"]

def start_fight(enemyId):
    return True
import quests.questhandler as qh
import messagehandler as m

q = "1"

m.post_message("let's do it")
while q != 0:
    q = qh.perform_quest(str(q))
    
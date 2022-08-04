# Exercice 3 : Memory game

import random
import time
import os

def clear_screen():
    if(os.name == 'posix'):
        os.system('clear')
    else:
        os.system('cls')

def gen_new_nbr(old_nbr):
	new_nbr = old_nbr + str(random.randint(0, 9))
	return new_nbr


def gen_first_nbr():
	nbr = str(random.randint(0, 9))
	nbr_str = nbr
	for i in range(2):
		nbr = str(random.randint(0, 9))
		nbr_str += nbr
	return nbr_str


def sleep_clear(nb_sec):
	time.sleep(nb_sec)
	clear_screen()

nb = gen_first_nbr()
ans_check = True
score = 0
clear_screen()
while ans_check == True:
	nb = gen_new_nbr(nb)
	print("Retenez la séquence : ")
	sleep_clear(1)
	print(nb)
	sleep_clear(3)
	usr_ans = input("Votre réponse : ")
	ans_check = usr_ans == nb
	if ans_check:
		score += 1
		print("Bonne réponse ! ")
		print(f"Votre score : {score}")
		sleep_clear(1)
	else:
		print(f"Mauvaise réponse... La séquence était {nb}")
		print(f"Score final : {score}")


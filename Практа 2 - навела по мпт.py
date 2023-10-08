
slova = ["1. БД - АДМИНИСТРАТОР БАЗ ДАННЫХ" , "2. П - ПРОГРАММИСТ "] 
colors = {"красный диплом", "Зелёный"}
colors.add("обычный диплом")
colors.remove("Зелёный")
def introduction():
    print("Добро пожаловать в МПТ!")
    name = input("Представьтесь, пожалуйста: ")
    print(f"Приятно познакомиться, {name}!")

def one_path():
    print("Вы пошли на БД и теперь перед вами стал сложный выбор.")
    print("1. Пойти на пары")
    print("2. Я пошёл на БД , зачем мне туда ходить?")
    choice = input("Введите номер действия: ")
    return choice

def go_for_a_couple():
    print("Вы пошли на пару и зайдя в кабинет поняли , что кроме вас никого на паре нет . Ваши действия?.")
    print("1. Пойти на следующую пару")
    print("2. Уйти домой")
    choice = input("Введите номер действия: ")
    return choice


def Go_home():
    print("Вы ушли домой . Спустя ещё 2 года вы с кайфом живёте и забираете свой ")
    print("История закончена.")

def I_am_a_Diligent_student_Sit_the_next_couple():
    print("Вы решили и дальше ходить на пары , учиться . Спустя два года вы забрали свой диплом , но когда наконце увидели своих одногруппников , которые тоже получили диплом не учась , впали в глубокую дипрессию и умерли")
    print("История закончена.")
def choose_path():
    print("Перед вами стал выбор специальности , куда пойдете?")
    print(slova)
    choice = input("Введите номер специальности: ")
    return choice

def pone_path():
    print("Вы пошли на П и теперь перед вами стал сложный выбор.")
    print("1. Пойти на пары")
    print("2. Пойти на пары , иначе отчислят")
    choice = input("Введите номер действия: ")
    return choice

def Pgo_for_a_couple():
    print("Вы пошли на пару и вам задали практос . Ваши действия?.")
    print("1. Делать практос , иначе отчислят")
    print("2. Делать практос ")
    choice = input("Введите номер действия: ")
    return choice


def PGo_home():
    print("Вы сделали практос , так продолжалось ещё 2 года . По окончанию учёбы вы забрали свой красный диплом и с кайфом живёте")
    print("История закончена.")

def PI_am_a_Diligent_student_Sit_the_next_couple():
    print("Вы делали практосы под страхом того , что вас отчислят, если не сделать их.Так продолжалось ещё 2 года . По окончанию учёбы вы забрали свой красный диплом и с кайфом живёте")
    print("История закончена.")

def main():
    introduction()
    
    choice_1 = choose_path()
    if choice_1 == "1":
        choice_2 = one_path()
        if choice_2 == "1":
            choice_3 = go_for_a_couple() 
            if choice_3 == "1":
                I_am_a_Diligent_student_Sit_the_next_couple()
            else:
                Go_home()
        else:
            print("Вы ушли домой . Спустя ещё 2 года вы забрали свой красный диплом и с кайфом живёте.")
    elif choice_1 == "2":
        choice_2 = pone_path()
        if choice_2 == "1":
            choice_3 = Pgo_for_a_couple() 
            if choice_3 == "1":
                PI_am_a_Diligent_student_Sit_the_next_couple()
            else:       
                PGo_home()
        else: choice_3 = Pgo_for_a_couple() 
        if choice_3 == "1":
                PI_am_a_Diligent_student_Sit_the_next_couple()
        else:       
                PGo_home()
if __name__ == "__main__":
    main()

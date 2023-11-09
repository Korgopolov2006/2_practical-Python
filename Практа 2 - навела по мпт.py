import json
import csv
import os



player = {
    "имя": "Герой",
    "уровень": 1,
    "опыт": 0,
    "здоровье": 100,
    "атака": 10,
    "защита": 5,
    "Уровень сложности": 0
}


enemy = {
    
}

goblin1 = {
    "имя": "Гоблин первого уровня",
    "здоровье": 55,
    "атака": 8,
    "защита": 2
}

goblin2 = {
    "имя": "Гоблин второго уровня",
    "здоровье": 60,
    "атака": 9,
    "защита": 2
}

goblin3 = {
    "имя": "Гоблин третьего уровня",
    "здоровье": 65,
    "атака": 10,
    "защита": 2
}

goblin4 = {
    "имя": "Гоблин четвёртого уровня",
    "здоровье": 70,
    "атака": 11,
    "защита": 2
}

goblin6 = {
    "имя": "Гоблин шестого уровня",
    "здоровье": 75,
    "атака": 12,
    "защита": 3
}

goblin7 = {
    "имя": "Гоблин седьмого уровня",
    "здоровье": 80,
    "атака": 13,
    "защита": 3
}

goblin8 = {
    "имя": "Гоблин восьмого уровня",
    "здоровье": 90,
    "атака": 14,
    "защита": 3
}

goblin9 = {
    "имя": "Гоблин девятого уровня",
    "здоровье": 100,
    "атака": 15,
    "защита": 3
}

goblin11 = {
    "имя": "Гоблин одиннадцатого уровня",
    "здоровье": 105,
    "атака": 16,
    "защита": 4
}

goblin12 = {
    "имя": "Гоблин двенадцатого уровня",
    "здоровье": 110,
    "атака": 17,
    "защита": 4
}

goblin13 = {
    "имя": "Гоблин тринадцатого уровня",
    "здоровье": 115,
    "атака": 18,
    "защита": 4
}

goblin14 = {
    "имя": "Гоблин четырнадцатого уровня",
    "здоровье": 130,
    "атака": 19,
    "защита": 4
}

goblin16 = {
    "имя": "Гоблин шестнадцатого уровня",
    "здоровье": 140,
    "атака": 20,
    "защита": 5
}

goblin17 = {
    "имя": "Гоблин семнадцатого уровня",
    "здоровье": 150,
    "атака": 21,
    "защита": 5
}

goblin18 = {
    "имя": "Гоблин восемнадцатого уровня",
    "здоровье": 160,
    "атака": 22,
    "защита": 5
}

goblin19 = {
    "имя": "Гоблин девятнадцатого уровня",
    "здоровье": 170,
    "атака": 23,
    "защита": 5
}

boss1 = {
    "имя": "Босс",
    "здоровье": 200,
    "атака": 15,
    "защита": 10
}
boss2 = {
    "имя": "Босс",
    "здоровье": 300,
    "атака": 20,
    "защита": 10
}
boss3 = {
    "имя": "Босс",
    "здоровье": 350,
    "атака": 25,
    "защита": 10
}
boss4 = {
    "имя": "Босс",
    "здоровье": 400,
    "атака": 30,
    "защита": 10
}


def save_progress():
    with open("прогресс.json", "w", encoding='utf-8') as file:
        json.dump(player, file, indent=4, ensure_ascii=False)
        
        


def load_progress():
    global player
    with open("прогресс.json", "r", encoding='utf-8') as file:
        player = json.load(file)


def delete_progress():
    global player
    player = {
        "имя": "Герой",
        "уровень": 1,
        "опыт": 0,
        "здоровье": 100,
        "атака": 10,
        "защита": 5,
        "Уровень сложности": 1
    }
    
    save_progress()

def load_to_csv():
    player_list = []
    player_list.append(player)
    if not(os.path.exists("данные.csv")):
        with open("данные.csv", "a", newline="",  encoding='cp1251') as file:
            fields = ["имя", "уровень", "опыт", "здоровье", "атака", "защита","Уровень сложности"]
            writer = csv.DictWriter(file, delimiter=';', fieldnames=fields)
            writer.writeheader()
            writer.writerows(player_list)
    else:
        with open("данные.csv", "a", newline="",  encoding='cp1251') as file:
            fields = ["имя", "уровень", "опыт", "здоровье", "атака", "защита","Уровень сложности"]
            writer = csv.DictWriter(file, delimiter=';', fieldnames=fields)
            writer.writerows(player_list)

def camp():
    global player
    print ("Вы в лагере")
    print(f"Ваше здоровье : {player['здоровье']}")
    print(f"Ваш уровень : {player['уровень']}")
    Camp = input("Выберите действие (1 - Восстановить здоровье, 2 - Пойти фармить лес , 3 - Вернуться в бой, 4 - Выйти из игры): ")      
    if Camp == "1": 
     os.system("cls") 
     player['здоровье'] += 60
     print("Вы восстановили здоровье и остались в лагере")
     camp()
    elif Camp == "2":  
     os.system("cls")
     lvl_up()
     player['опыт'] += 40
     print("Вы пофармили лесочек и вернулись в лагерь")
     camp()
    elif Camp == "3":
     os.system("cls")  
     new_battle()
    elif Camp == "4":
        print("Вы вышли из игры")
        os.system("cls")  
        load_to_csv()
        save_progress()
        menu()
    else :
        print("Вы ввели неправильное действие")
        camp()

def lvl_up():
    if player['опыт'] >= player['уровень'] * 100:  
                    player['уровень'] += 1
                    player['атака'] += 5
                    player['защита'] += 2
                    print("Уровень повышен!")
                    save_progress()


            

def new_battle():
    global player
    global goblin1 
    global goblin2
    global goblin3
    global goblin4
    global goblin6
    global goblin7
    global goblin8
    global goblin9
    global goblin11
    global goblin12
    global goblin13
    global goblin14
    global goblin16
    global goblin17
    global goblin18
    global goblin19
    global boss1
    global boss2
    global boss3
    global boss4
    
    print("Начинается новый бой!")
    while True:
        print("----------------------")
        print(f"{player['имя']} (Уровень {player['уровень']})")
        print(f"Здоровье: {player['здоровье']}")
        print(f"Атака: {player['атака']}")
        print(f"Защита: {player['защита']}")
        print("----------------------")
        if player["Уровень сложности"] == 5 :  
            enemy = boss1
        elif player["Уровень сложности"] == 10 :  
            enemy = boss2
        elif player["Уровень сложности"] == 15 :  
            enemy = boss3
        elif player["Уровень сложности"] == 20 :  
            enemy = boss4
        elif player["Уровень сложности"] == 1 :  
            enemy = goblin1
        elif player["Уровень сложности"] == 2 :  
            enemy = goblin2
        elif player["Уровень сложности"] == 3 :  
            enemy = goblin3
        elif player["Уровень сложности"] == 4 :  
            enemy = goblin4
        elif player["Уровень сложности"] == 6 :  
            enemy = goblin6
        elif player["Уровень сложности"] == 7 :  
            enemy = goblin7
        elif player["Уровень сложности"] == 8 :  
            enemy = goblin8
        elif player["Уровень сложности"] == 9 :  
            enemy = goblin9
        elif player["Уровень сложности"] == 11 :  
            enemy = goblin11
        elif player["Уровень сложности"] == 12 :  
            enemy = goblin12
        elif player["Уровень сложности"] == 13 :  
            enemy = goblin13
        elif player["Уровень сложности"] == 14 :  
            enemy = goblin14
        elif player["Уровень сложности"] == 16 :  
            enemy = goblin16
        elif player["Уровень сложности"] == 17:  
            enemy = goblin17
        elif player["Уровень сложности"] == 18 :  
            enemy = goblin18
        elif player["Уровень сложности"] == 19 :  
            enemy = goblin19
           
        print(f"{enemy['имя']}")
        print(f"Здоровье: {enemy['здоровье']}")
        print(f"Атака: {enemy['атака']}")
        print(f"Защита: {enemy['защита']}")
        print("----------------------")

        change = input("Выберите действие (1 - Атаковать, 2 - Убежать, 3 - Выйти из игры): ")

        if change == "1":  
            os.system("cls")
            damage_player = max(0, player['атака'] - enemy['защита'])
            enemy['здоровье'] -= damage_player

      
            damage_enemy = max(0, enemy['атака'] - player['защита'])
            player['здоровье'] -= damage_enemy
            
            

            if enemy['здоровье'] <= 0:  
                print(f"{enemy['имя']} побежден!")
                player["Уровень сложности"] += 1
                player['опыт'] += 60
                lvl_up()
                if player["Уровень сложности"] == 21: 
                    print("Поздравляем! Вы победили всех гоблинов и боссов!")
                    menu()
                
            elif player['здоровье'] <= 0: 
                print(f"{player['имя']} погиб!")
                load_to_csv()
                break
        elif change == "2": 
            os.system("cls")
            camp()
        elif change == "3":  
            os.system("cls")
            print("Вы вышли из игры")
            load_to_csv()
            save_progress()
            menu()
            break
        else:
            os.system("cls")
            print("Неверное действие, попробуйте еще раз!") 
        





def menu():
    change3 = input("Выберите действие (1 - Новая игра, 2 - Загрузить игру, 3 - Удалить сохранение): ")
    if change3 == "1":
        os.system("cls")
        delete_progress()  
        new_battle()
    elif change3 == "2": 
        os.system("cls") 
        load_progress()
        print ("Прогресс был загружен")
        new_battle()
    elif change3 == "3": 
        os.system("cls") 
        delete_progress()
        print("Сохранение удалено!")
        change4 = input("Выберите действие (1 - Новая игра, 2 - выйти из игры): ")
        if change4 == "1": 
            os.system("cls") 
            new_battle()
        elif change4 == "2": 
            os.system("cls") 
            load_to_csv()
            save_progress()
            print("Вы вышли из игры")
        else:
            os.system("cls")
            print("Неверное действие, попробуйте еще раз!")
menu()



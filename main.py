class Students:
    def __init__(self):
        self.nameList = []
        self.ageList = []
        self.courseList = []
        
    
    def input_validation(self, input_context: str) -> int:
        while True:
            print(input_context)
            try:
                return int(input())
            except ValueError as exc:
                print(f"Введеная строка не является числов. Попробуйте снова. \nПодробнее: {exc}")


    def add_student(self, name, age, course):
        self.nameList.append((name))
        self.ageList.append((age))
        self.courseList.append((course))

        place = len(self.nameList)
        for i in range(place):
            print(f"\nИмя: {self.nameList[i]} \nВозраст: {self.ageList[i]} \nКурс: {self.courseList[i]}")

    def search_student(self, name):
        flag = 0
        place = len(self.nameList)
        for i in range(place):
            if self.nameList[i] == name:
                flag += 1
                print(f"\nИмя: {self.nameList[i]} \nВозраст: {self.ageList[i]} \nКурс: {self.courseList[i]}\n")

        if flag == 0:
            print("студент не найден(")
            

    def delete_student(self, name):
        flag = 0
        for i in self.nameList:
            if i == name:
                flag += 1
                index = self.nameList.index(name)
                self.nameList.pop(index) 
                self.ageList.pop(index) 
                self.courseList.pop(index)

        if flag == 0:
            print("студент не найден(\n")

        place = len(self.nameList)
        for i in range(place):
            print(f"Имя: {self.nameList[i]} \nВозраст: {self.ageList[i]} \nКурс: {self.courseList[i]}")


    def get_input(self):
        while True:
            print("\nmenu:\n1:Добавление студента\n2:Поиск студента по имени\n3:удаление студента\n4:выход из программы")
            f = input('Ввод действия:  ')

            if f == '1': 
                name = input('Введите Имя:\n') 
                age = self.input_validation('Введите возраст:') 
                course = self.input_validation('Введите курс:') 
                self.add_student(name, age, course)

            if f == '2':
                self.search_student(input("Введите имя:\n"))

            if f == '3':
                self.delete_student(input("Введите имя:\n"))

            if f == '4':
                break
        

def main():
    obj = Students()
    obj.get_input()


if __name__ == "__main__":
    main()    

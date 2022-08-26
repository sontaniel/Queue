workers = {
        "Tom":{'Login':'tom106',
               'Password':'qwerty12345'},
        "Bob": {'Login':'bom120',
               'Password':'qwty1245'}
        }

while 3>2:
  
    print("\n\n")
    print("Операции:")
    print("1 - найти пользователя")
    print("2 - добавить пользователя/атрибут")
    print("3 - удалить пользователя")
    print("4 - изменить значение атрибута пользователя\n")
    
    a=int(input("Выберите операцию (1,2,3,4): "))

    if a==1:
        key1=input("Введите пользователя: ")

        if key1 in workers :
            print(workers[key1])
        else:
            print("Такого пользователя нет")
    if a==2:
      
        workers.setdefault(input("Введите пользователя: "),\
                           {}).setdefault(input("Введите атрибут: "),input("Введите значение:"))
        print(workers)
      
    if a==3:
        key1=input("Пользователь: ")
        if key1 in workers:
            del workers[key1]
            print(f"Пользователь {key1} удален")
            print(workers)
        else:
            print("Такого пользователя нет")
    if a==4:
        key1=input("Введите пользователя: ")
        key2=input("Введите атрибут: ")
        
        if key1 in workers and key2 in workers[key1]:
            workers[key1][key2]=input("Введите новое значение:")
            print(workers)
        else:
            print("Такого пользователя/атрибута нет")


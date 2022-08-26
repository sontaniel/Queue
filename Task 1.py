class queue:
    def __init__(self, queuelen):
        self.queuelen=queuelen
        self.queuelist=["None" for i in range(queuelen)]


    def addstring(self,newstring): # добавление нового элемента в очередь
        for i in range(self.queuelen):
            if self.queuelist[i]=="None":
                self.queuelist[i]=newstring
                break




    def removestring(self):  # удалить первый элемент
        for i in range(self.queuelen):
            if self.queuelist[i]!="None": # основные три строчки, отличающие этот код
                self.queuelist[i]="None"  # от соответсвующего кода стека
                self.rearrange() # функция rearrange() двигает элементы в очереди вперед
                break
                
    def rearrange(self): # движение очереди вперед после удаления переднего элемента
        for i in range (self.queuelen):
            if self.queuelist[i]=="None":
                for j in range(i,self.queuelen):
                    if j==self.queuelen-1:
                        self.queuelist[j]="None"
                    else:
                        self.queuelist[j]=self.queuelist[j+1]
                break

    def showqueue(self): # показать последний элемент
        for i in range(self.queuelen):       
            if self.queuelist[i]=="None":
                break
            else:
                print(self.queuelist[i]) 
        
    def fullcheck(self): # полна ли очередь
        for i in range(self.queuelen):
            if self.queuelist[i]=="None":
                print("Очередь не заполнена.")
                return 0
        print("Очередь заполнена.")
        return 1 # Если ни один виток предыдущего цикла не запустил return,
                 # значит очередь не содержит "None"



    def emptycheck(self): # пуста ли очередь?
        for i in range(self.queuelen):
            if self.queuelist[i]!="None":
                print("Очередь не пустая")
                return 0

        print("Очередь пустая.")
        return 1


    def stringcount(self): # подсчет строк в очереди
        count=0
        for i in range(self.queuelen):
            if self.queuelist[i]!="None":
                count+=1
        print (count)    
        return count


    def clearqueue(self): # полная очистка очереди
        for i in range(self.queuelen):
            self.queuelist[i]="None"
        
        
                
        
#MAIN

elemcount=int(input("Введите максимальное число элементов в очереди: "))

queue1=queue(elemcount)
while 3>2:
    print("")
    print("1. Добавить строку в очередь")
    print("2. Удалить строку из очереди")
    print("3. Подсчитать кол-во строк в очереди")
    print("4. Проверить, пустая ли очередь")
    print("5. Проверить, полная ли очередь")
    print("6. Очистить очередь")
    print("7. Показать очередь")

    print("")

    option=int(input("Выберите опцию (1,2,3,4,5,6,7): "))

    print("")

    if option==1:
        queue1.addstring(input("Введите новую строку:"));
    elif option==2:
        queue1.removestring()
    elif option==3:
        queue1.stringcount()
    elif option==4:
        queue1.emptycheck()
    elif option==5:
        queue1.fullcheck()
    elif option==6:
        queue1.clearqueue()
    elif option==7:
        queue1.showqueue()
    else:
        print("Ошибка ввода!")
        


    
            

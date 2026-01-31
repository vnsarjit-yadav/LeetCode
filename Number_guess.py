import random


while(True):
   option=int(input('''choose only one option of the following option
                    1.want to guess number 
                    2.want to exit..
                    enter here..'''))
   if option==1:
      guess_num=int(input("Enter your gusee number(between 1 to 10):"))
      sys_num=random.randint(1,10)
   
      if guess_num==sys_num:
         print("congratulation.. you guess the correct number.. system genereted number is :",sys_num,"your number is:",guess_num)

      else:
          print("sorry you loose.. you  guess wrong number ")
          print("random number is :",sys_num,"your number is:",guess_num)
   elif option==2:
      break
   else:
      print("enter correct option")
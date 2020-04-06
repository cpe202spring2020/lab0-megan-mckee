def weight_on_planets():
   # write your code here
   weight = int(input("What do you weigh on earth? "))
   # Use print formatting in order to round the weight
   # and concatinate it to a string
   print(f"\nOn Mars you would weigh {weight * 0.38:0.2f} pounds.\n"
         f"On Jupiter you would weigh {weight * 2.34:0.2f} pounds.")
   
   
if __name__ == '__main__':
   weight_on_planets()
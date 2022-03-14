def Symmetry(s):
   half = int(len(s) / 2)
   first_string = s[:half]
   
   if len(s) % 2 == 0:
       second_string = s[half:]
   else:
       second_string = s[half+1:]
       
   if first_string == second_string[::-1]:  # ''.join(reversed(second_str)) [slower]
        return True
   else:
        return False
       

def main():
        T = int(input())
        print(T)
        while(T > 0):
            S = input()
            
            if (Symmetry(S)):
                print("This is Symmetry")
            else:
                print("This is not Symmetry")
            T -= 1
        
if __name__ == "__main__":
    main()

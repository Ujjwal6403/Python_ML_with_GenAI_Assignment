# Write a program which accepts one character and checks whether it is vowel or consonant.

#input : a
#output : Vowel

def Checkvowel(name):
   
   if((name == 'a')|(name == 'e')|(name == 'i')|(name == 'o')|(name == 'u')):
      
      return True
   else:
      return False
   
def main():
   
   name = input("Enter the character : ")
   bRet = False
   bRet = Checkvowel(name)
   
   if(bRet == True):
      print("vowel")
   else:
      print("consonant")


if __name__ == "__main__":
   main()
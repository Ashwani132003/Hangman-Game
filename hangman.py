import random
hangman = (
    """
       |
    """,
    """
       |
       0
    """,
    """
       |
       0
     --+--
    """,
    """
       |
       0
    \--+--
     
    """,
    """
       |
       0
    \--+--/
    """,
    """
       |
       0
    \--+--/
       |
    """,
    """
       |
       0
    \--+--/
       |
       |
    """,
    """
       |
       0
    \--+--/
       |
       |
      |
      | 
    """,
    """
       |
       0
    \--+--/
       |
       |
      | |
      | |
    """
)

Max_wrong = len(hangman)-1

Words = ("RAKESH","SIWACH","KACHRU","SAROJ")

Word=random.choice(Words)

ans="_"*len(Word)
wrong = 0
used=[]

print(ans)
while wrong<Max_wrong and ans!=Word:
   
   guess = input("\nMake a guess:")
   guess=guess.upper()
   if guess not in used:
      
      if guess in Word:
         new="" 
         for i in range(len(Word)):
            if guess == Word[i] :
               new = new+guess
            else:
               new=new+ans[i]   
         ans=new 
         print(ans)     
      else:
         print("\nWrong Guess")       
         wrong+=1
         print(hangman[wrong])
         print(ans)
   else:
      print("\nAlready Guessed!!")  
   
   used.append(guess)
   print("\n\nUsed: ",used)
   
   
if wrong==Max_wrong:
   print("\nGame Over!!,You Lost the Game")
   print("Corect word was:",Word)
else:
   print("\nBooyah!! You Guessed it Correct")         
      
             
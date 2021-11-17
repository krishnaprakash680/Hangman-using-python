from random import choice

def word_gen():
    word_list=['python','chennai','coimbatore','salem','cochin','kerala','madurai','dindukal']
    return choice(word_list)

word='python'
guessed=""
turns=int(len(word)*1.5)

while(True):
    print('\nyou are left with '+str(turns)+ 'turns')
    inp=input("make a guess: ")
    turns=turns-1
    if inp in word:
        guessed=guessed+inp
    unguessed_char=0    
    for i in word:
        if i in guessed:
            print(i,end="")
        else:
            unguessed_char += 1
            print("*",end="")
    if unguessed_char==0:
        print("Hurray!! you won..")
        break
    if turns==0:
        print("\n you ran out of attempts...")
        break

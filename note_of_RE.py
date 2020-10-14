import  re
# import re
# Creating Regular Expression(Regex) object
# \d mean digit character
# eg = re.compile(r'\d ....) *r mean raw string

#re.compile(r<The pattern>) store the pattern ***use the raw string***
    # U can add another pattern by increase the group .eg :(\d\d)-(\d\d\d)
    #-.group(1/2) will display first and second group respectively
    #-.group(0/'') will display the all group
        #-.groups() will return a turple of multiple values
        #U can use this eg : V1,V2 = txt.groups()
        #V1 = "group 1" , V2 = "group 2"
    #If ur pattern got () then u need add the escape eg:.compile(r'(\(\d\d\d\))')
    #Matching multiple Groups with the Pipe (|) eg: (r"Bat|Man")
        #It's mean the pattern either is Bat or Man
            #eg: (r"Bat|(man|mobile|food)")
                #It's mean the pattern either Batman or Batmobile and so on
    #(?) mean the optional matching
        #eg: (r"(battt)?tabbbbb")
            #Mean it is either battttabbbbb or tabbbbb
    #Matching zero or more by using (-)*
        #eg: _.compile(r'Bat(wo)*man)
            #Mean Batman , Batwoman , Batwowowowman
    #Mathcing one or more by using (-)+
        #eg: _.compile(r"Bat(wo)+man)
            #Mean Batwoman or Batwowowowowoman
    #Matching specific Repetition with curly Bracket {,}
        #(ha){3} = (ha)(ha)(ha)
        #(ha){0,3} = ((ha)(ha)(ha))|((ha)(ha)(ha)(ha)|......
        #(ha){3}? mean declare a nongreedy match
        #greedy in re mean the result always match with the longest string possible
        #Try me -> notefunction2()

#-.search(<The message>) return Match/None
    #-.findall(<The message>) return all objects in the serached string
        #But the result is in the list  eg : ["fff","ggg"]
        #if got there groups then the list of tuple instead eg : [("333", "334"),("334,333)]

#-.group() return the match object

#Character Classes -\d mean any numeric digit 0 to 9
#                  -\D mean all characters except 0 to 9
#                  -\w all letter and digit -word
#                  -\W opposite of \w
#                  -\s any space, tab or newline character
#                  -\S any character that is not a space,tab or newline

    # eg: a = b.compile(r'\d+\s\w+')  + mean one or more

#Making ur own classes (r'[-]')
    # Using - to include the range of letters and numbers
    #[a-zA-Z] mean a to z
    # Using caret ^ to make a neagtive character class  eg : a = b.compile(r'[^abc]')
    #**** inside the [] , the ecape no need to put
    # "Carrot cost dollar" eg : -.compile(r'^-$')
        #carrot mean the match must occur at the beginning of the searched text
        #dollar mean the match must occur at the end of the searched text
    # "Wildcard character" to match any character except for a newline.
        #eg : a = b.compile(r'.at')
        # so the matching object is like hat , fat etc .....
        # The importance thing is the dot is matching only one character
        # So the flat is not matching
    # Matching everything with dot - star  (.*)
    # Matching newlines with the dot character  eg: a = b.compile(".*",re.DOTALL)
        #Mean it will match everything included the newline
            #('Serve the public agent. \nProtect the innocent.")
                # Try it -> : notefunction()
#Case-Insensitive Matching by passing re.I
    #eg : a = b.compile(r'abc',re.I)
    #eg : mean the matching object is abc , ABC and etc ...
#Substituting strings with the sub() Method
    # eg: txt = -.sub('replace one', 'string that u want to search')
    # print( txt )
        # Try it -> : notefucntion3()
    # You also can specific the group that u want to substitu
        # Try it -> : notefucntion3a()

##Managing the complex regex##
    #VERBOSE Mode (ignore the space , comments inside the expression)
    #IGNORECASE Mode
    #DOTAIL Mode
    # If you wanna combine those modes in one , using bitwise |
        #-.compile(r"---",re.VERBOSE | re.DOTAIL | re.IGNORECASE)



#Difference btw findall() and group
def notefunction0():
    mssg = '222444'

    a = re.compile(r"\d\d\d")

    fa = a.findall(mssg)
    print("findall : ")
    print(fa)
    gp = a.search(mssg)
    print("group : ")
    print(gp.group())

def notefunction() :
    a =  re.compile(r".*",re.DOTALL)
    A = re.compile(r".*")
    txt = a.search("hello my friend \nsuch a long time didn't see u  ")
    Txt = A.search("hello my friend \nsuch a long time didn't see u  ")
    print(Txt.group()) #without re.DOTALL
    space()
    print(txt.group()) #with re.DOTALL

def notefunction2():
    a = re.compile(r"(ha){3}")
    txt = a.search("hahaman")
    Txt = a.search("hahahassss")
    try:
        print(txt.group())
    except AttributeError:
        print(txt==None)
    print(Txt.group())

def notefunction3() :
    a = re.compile(r'Joseph \w+')
    txt = a.sub('Censored', 'Joseph Lim win a Nobel prize and Joseph Lim is continue his ...')
    print(txt)

def notefunction3a() :
    a = re.compile(r"Agent (\w)\w*")
    b = a.sub(r"\1***" , "Agent Lim is doing some spy activity")
    print(b)


def space():
    print('')
def new_note(n):
    if n == '1' :
        notefunction()
    elif n == '0' :
        notefunction0()
    elif n == '2' :
        notefunction2()
    elif  n == '3' :
        notefunction3()
    elif  n == '4' :
        notefunction3a()
#Loop
while True :
    print("What example you want me to show ?")
    num = input()
    new_note(num)


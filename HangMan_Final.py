import random
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
### imports ###'
SAT=[
"autonomous",
"brevity",
"astute",
"belie",
"cajole",
"austere",
"benevolent",
"capricious",
"consensus",
"constraint",
"corroborate",
"conviction",
"criterion",
"cryptic",
"contentious",
"credulity",
"cursory",
"censorious",
"censure",
"coercion",
"commemorate",
"concise",
"compliance",
"condone",
"conciliatory",
"conflagration",
"diminution",
"discerning"
"discordant",
"discrepancy" ,
"disdain" ,
"disinclination" ,
"dismiss" ,
"disparage" ,
"disparity" ,
"decorum" ,
"delineate" ,
"denounce",
"depravity" ,
"deprecate",
"deride",
"despondent",
"deterrent",
"digression",
"disperse",
"disseminate",
"divergent",
"dogmatic",
"duplicity",
"eclectic",
"eloquence",
"elusive",
"embellish",
"ascetic",
"incorrigible",
"ingenious",
"innocuous",
"indict",
"inherent",
"innovation",
"induce",
"innate",
"insipid",
"instigate",
"ironic",
"levity",
"intrepid",
"laud",
"listless",
"inundate",
"lethargic",
"malicious",
"materialism",
"mitigate",
"notoriety",
"meticulous",
"morose",
"nurture",
"miserly",
"mundane",
"oblivion",
"opaque",
"ostentatious",
"peripheral",
"opportunist",
"pacifist",
"pervasive",
"opulence",
"partisan",
"pessimism",
"philanthropist",
"piety",
"placate",
"ponderous",
"pragmatic",
"preclude",
"precocious",
"predecessor",
"presumptuous",
"pretentious",
"profane",
"proliferation",
"prevalent",
"profound",
"prolific",
"prodigal",
"profusion",
"proximity",
"prudent",
"rebuttal",
"redundant",
"quandary",
"recluse",
"refute",
"rancor",
"rectify",
"relegate",
"renounce",
"reprove",
"retract",
"reprehensible",
"repudiate",
"rhetorical",
"reprimand",
"reticence",
"sanction",
"satirical",
"servile",
"stagnant",
"scrupulous",
"skeptic",
"substantiate",
"scrutinize",
"somber",
"succinct",
"superficial",
"surreptitious",
"terse",
"superfluous",
"sycophant",
"transient",
"surpass",
"taciturn",
"turbulence",
"undermine",
"venerate",
"virtuoso",
"usurp",
"verbose",
"volatile",
"vacillate",
"vilify",
"zealot",
"ambiguous",
"adversity",
"abridge",
"advocate",
"adulation",
"apathy",
"ascendancy",
"alleviate",
"altruistic",
"aesthetic",
"adversary",
"affirmation",
"arbitrary",
"anarchist",
"articulate",
"acclaim",
"abstract",
"ambivalence"]
Food=[
'fish',
'meat',
'chicken',
'cheese',
'milk',
'butter',
'eggs',
'vegetables',
'fruit',
'rice',
'bread',
'pasta',
'grapes',
'lettuce',
'apple',
'banana',
'pear',
'orange',
'grapefruit',
'lemon',
'lime',
'blackberries',
'tangerine',
'peach',
'cherry',
'apricot',
'plum',
'strawberries',
'raspberries',
'blueberries',
'watermelon',
'melon',
'papaya',
'mango',
'kiwi',
'pineapple',
'coconut',
'raisins',
'prunes',
'figs',
'dates',
'cabbage',
'carrot',
'radishes',
'beets',
'tomato',
'bellpepper',
'beans',
'celery',
'cucumber',
'spinach',
'corn',
'broccoli',
'cauliflower',
'turnips',
'potato',
'onion',
'scallions',
'peas',
'artichokes',
'eggplants',
'squash',
'zucchini',
'asparagus',
'mushroom',
'parsley',
'chilipeppers',
'garlic',
'tuna',
'yogurt',
'oil',
'sugar',
'coffee',
'candy',
'cookies',
'cake',
'roast',
'steak',
'beef',
'liver',
'tripe',
'ham',
'pork',
'bacon',
'sausage',
'duck',
'turkey',
'trout',
'catfish',
'salmon',
'swordfish',
'shellfish',
'crab',
'lobster',
'shrimp',
'scallops',
'mussels',
'oysters',
'clams',
'pastrami',
'cheddar',
'mozzarella',
'seafood',
'juice',
'soda',
'water',
'omelet',
'hamburger',
'fries',
'cheeseburger',
'sandwich',
'pizza',
'hotdog',
'nachos',
'taco',
'burrito',
'icecream',
'milkshake',
'donut',
'muffin',
'ketchup',
'mustard',
'mayonnaise',
'salad',
'biscuits',
'pancakes',
'waffles',
'cereal',
'pickle',
'coleslaw',
'meatballs',
'spaghetti']
Animals=['shark','cod','bass','squid','tuna','octopus','swordfish','ray','eel','seahorse','jellyfish','flounder','coral','starfish','mussel','shrimp','scallop','crab','seaurchin','snail','worm','toad','newt','frog','salamander','dolphin','porpoise','whale','walrus','sealion','seal','alligator','crocodile','tortoise','turtle','lizard','cobra','rattlesnake','gartersnake','owl','bluejay','sparrow','woodpecker','eagle','hummingbird','goose','peacock','pigeon','robin','wasp','beetle','butterfly','caterpillar','moth','mosquito','ladybug','tick','fly','spider','scorpion','cow','pig','donkey','goat','horse','rooster','hen','sheep','cat','kitten','dog','puppy','rabbit','guineapig','parakeet','goldfish','rat','mouse','gopher','chipmunk','squirrel','moose','coyote','opossum','wolf','buffalo','bison','bat','armadillo','beaver','porcupine','bear','skunk','raccoon','deer','fox','anteater','monkey','chimpanzee','rhinoceros','gorilla','hyena','baboon','giraffe','zebra','leopard','antelope','lion','tiger','camel','orangutan','panther','panda','elephant','hippopoptamus','kangaroo','koala',
         'platypus']
Geography=[
'afghanistan',
'kabul',
'iran',
'tehran',
'albania',
'tirana',
'algeria',
'algiers',
'angola',
'luanda',
'argentina',
'armenia',
'yerevan',
'australia',
'canberra',
'austria',
'vienna',
'azerbaijan',
'baku',
'bahrain',
'manama',
'bangladesh',
'dhaka',
'barbados',
'bridgetown',
'belarus',
'minsk',
'belgium',
'brussels',
'belize',
'belmopan',
'sarajevo',
'botswana',
'gaborone',
'brazil',
'brasilia',
'brunei',
'bulgaria',
'sofia',
'cambodia',
'cameroon',
'yaounde',
'canada',
'ottawa',
'praia',
'chad',
'chile',
'china',
'santiago',
'colombia',
'beijing',
'comoros',
'moroni',
'congo',
'brazzaville',
'zagreb',
'croatia',
'cuba',
'havana',
'cyprus',
'nicosia',
'denmark',
'copenhagen',
'prague',
'dominica',
'roseau',
'ecuador',
'quito',
'egypt',
'cairo',
'asmara',
'estonia',
'finland',
'france',
'paris',
'gabon',
'germany',
'berlin',
'ghana',
'accra',
'greece',
'athens',
'guinea',
'hungary',
'budapest',
'haiti',
'iceland',
'reykjavik',
'india',
'delhi',
'iraq',
'baghdad',
'ireland',
'dublin',
'indonesia',
'jakarta',
'jamaica',
'kingston',
'italy',
'rome',
'russia',
'moscow',
'jordan',
'japan',
'tokyo',
'amman',
'kenya',
'kazakhstan',
'korea',
'seoul',
'pyongyang',
'kuwait',
'lebanon',
'beirut',
'macedonia',
'maldives',
'male',
'malaysia',
'mexico',
'monaco',
'morocco',
'rabat',
'nepal',
'kathmandu',
'netherlands',
'amsterdam',
'nigeria',
'norway',
'oslo',
'pakistan',
'peru',
'poland',
'portugal',
'lisbon',
'qatar',
'lima',
'doha',
'rwanda',
'senegal',
'serbia',
'victoria',
'toronto',
'spain',
'madrid',
'sudan',
'syria',
'taiwan',
'switzerland',
'tajikistan',
'tunis',
'turkey',
'istanbul',
'ankara',
'london',
'venezuela',
'yemen',
'zambia']
keshvar=['iran','korea','japan','turkey','pakestan']
ashya=['kif','ketab','alangoo','saat','daftar']
heyvan=['ahoo','shir','gonjesk','gorbe','dolfin']
input_word=""

### main window ###
mainwin=Tk()
mainwin.minsize(905,905)
mainwin.maxsize(905,905)
mainwin.config(bg='skyBlue')
def hangman():
    pressed=[]
    win = Toplevel(mainwin)
    win.minsize(905, 905)
    win.maxsize(905, 905)
    ### background ###
    pic_back = Image.open("back.jpg")
    back = ImageTk.PhotoImage(pic_back)
    label_back = Label(win, image=back)
    label_back.place(x=0, y=0)
    ### random function ###
    def rand_w(cat):
        cat=int(cat)
        word=''
        if cat==1:
            word = random.choice(SAT)
        elif cat==2:
            word = random.choice(Food)
        elif cat==3:
            word = random.choice(Animals)
        elif cat==4:
            word=random.choice(Geography)
        print(word)
        return  word

    ################
    def print_w(word):
        e_word = ""
        for i in range(len(word)):
            e_word = e_word + '-'
        print(e_word)
        return (e_word)

    global word_g
    word_g = rand_w(choose())
    global joon
    joon = 7

    ### ax hay daaar ###
    pic_dar = Image.open("dar.jpg")
    dar = ImageTk.PhotoImage(pic_dar)

    pic_joon1 = Image.open("joon1.jpg")
    joon1 = ImageTk.PhotoImage(pic_joon1)

    pic_joon2 = Image.open("joon2.jpg")
    joon2 = ImageTk.PhotoImage(pic_joon2)

    pic_joon3 = Image.open("joon3.jpg")
    joon3 = ImageTk.PhotoImage(pic_joon3)

    pic_joon4 = Image.open("joon4.jpg")
    joon4 = ImageTk.PhotoImage(pic_joon4)

    pic_joon5 = Image.open("joon5.jpg")
    joon5 = ImageTk.PhotoImage(pic_joon5)

    pic_joon6 = Image.open("joon6.jpg")
    joon6 = ImageTk.PhotoImage(pic_joon6)

    pic_joon7 = Image.open("joon7.jpg")
    joon7 = ImageTk.PhotoImage(pic_joon7)

    label_dar = Label(win,image=dar)
    label_dar.place(relx=0.5, y=192, anchor=CENTER)

    def joon_1():
        label_dar.config(image=joon1)

    def joon_2():
        label_dar.config(image=joon2)

    def joon_3():
        label_dar.config(image=joon3)

    def joon_4():
        label_dar.config(image=joon4)

    def joon_5():
        label_dar.config(image=joon5)

    def joon_6():
        label_dar.config(image=joon6)

    def joon_7():
        label_dar.config(image=joon7)

    ###############
    global input_word
    input_word = print_w(word_g)
    global l
    l = Label(win, text=input_word, font=('', 100),bg='white')
    l.place(relx=.5, rely=.65, anchor=CENTER)

    ### Guess ###
    def POST(event):
        global input_word
        global list_alpha
        global word_g
        g = str(list_alpha[event.widget]).lower()
        print(g)  # pak shavad
        if word_g.find(g) == -1:
            global joon
            if g in pressed:
                joon+=1
            joon = joon - 1
            if joon == 6:
                joon_1()
            elif joon == 5:
                joon_2()
            elif joon == 4:
                joon_3()
            elif joon == 3:
                joon_4()
            elif joon == 2:
                joon_5()
            elif joon == 1:
                joon_6()
            elif joon == 0:
                joon_7()
                question_lose = messagebox.askquestion("GAME OVER", 'You are loose\nCorrect word: ' + word_g + '\nPlay Again?')
                if question_lose == 'yes':
                    win.destroy()
                    hangman()
                else:
                    win.destroy()
        pressed.append(g)
        print(pressed)
        for i in range(len(input_word)):
            if g == word_g[i]:
                new = list(input_word)
                new[i] = g
                input_word = ''.join(new)

        print(input_word)
        print(joon)

        l.config(text=input_word)
        if word_g == input_word:
            question_win = messagebox.askquestion("Congrats", "You are win\nPlay Again?")
            if question_win == 'yes':
                win.destroy()
                hangman()
            else:
                win.destroy()

    ################
    def key_pressed(event):
        print(event.char)
        global input_word
        global list_alpha
        global word_g
        g = event.char
        print(g)  # pak shavad
        if word_g.find(g) == -1:
            global joon
            if g in pressed:
                joon+=1
            joon = joon - 1
            if joon == 6:
                joon_1()
            elif joon == 5:
                joon_2()
            elif joon == 4:
                joon_3()
            elif joon == 3:
                joon_4()
            elif joon == 2:
                joon_5()
            elif joon == 1:
                joon_6()
            elif joon == 0:
                joon_7()
                question_lose = messagebox.askquestion("GAME OVER", 'You are loose\nCorrect word: ' + word_g + '\nPlay Again?')
                if question_lose == 'yes':
                    win.destroy()
                    hangman()
                else:
                    win.destroy()
        pressed.append(g)
        print(pressed)
        for i in range(len(input_word)):
            if g == word_g[i]:
                new = list(input_word)
                new[i] = g
                input_word = ''.join(new)

        print(input_word)
        print(joon)

        l.config(text=input_word)
        if word_g == input_word:
            question_win = messagebox.askquestion("Congrats", "You are win\nPlay Again?")
            if question_win == 'yes':
                win.destroy()
                hangman()
            else:
                win.destroy()
    win.bind("<Key>",key_pressed)
    ### Keyboard ###
    alphabet = ['A', 'B', 'C', 'D', 'E', 'F',
                'G', 'H', 'I', 'J', 'K', 'L',
                'M', 'N', 'O', 'P', 'Q', 'R',
                'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    global list_alpha
    list_alpha = {}

    for i in range(26):
        btn = Button(win, text=alphabet[i],bg='orange')
        if i<13:
            btn.place(relx=.15 + i /17 , rely=.8, relheight=0.03, relwidth=0.05, anchor=CENTER)
        elif i >12:
            btn.place(relx=.15 + (i-13) / 17, rely=.84, relheight=0.03, relwidth=0.05, anchor=CENTER)

        list_alpha[btn] = alphabet[i]  # maghadir
        btn.bind("<Button-1>", POST)
    win.mainloop()
welcome_label=Label(mainwin, text='Welcome to Hang Man Game',bg='skyBlue',font=('',40))
welcome_label.place(relx=.5,rely=.1, anchor=CENTER)
btn=Button(mainwin,text='Play', command=hangman, font=('', 20, "bold"), bg='orange')
btn.place(relx=.5,rely=.75, relheight=.06, relwidth=.2, anchor=CENTER)
### Radio Buttons ###
v=StringVar(mainwin,"1")
cats={"SAT" : "1",
      "Food" : "2",
      "Animals" : "3",
      "Geography" : "4"
      }
def choose():
    return (v.get())
for (cat,value) in cats.items():
    Radiobutton (mainwin,text=cat,variable=v,value=value,bg='skyBlue',font=("",15,"bold"),command=choose)\
        .place(relx=.5,rely=.3+int(value)/15, anchor=CENTER)
mainwin.mainloop()





    







            

            






        
        
    
    

        
    

    
        
        
        

    

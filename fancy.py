##Makes the output in the Terminal better looking.
##Temporary use until GUI

def generate(print_word="",filler_char="",special_char="|",size=100,align="center"):#The main brain that controls everything
    word_length=len(print_word)
    if word_length >= size:
        print(print_word,end="")
    else:
        if special_char=="":    special_char=filler_char
        special_char_length=len(special_char)
        usable_length=size-word_length-(special_char_length*2)
        left_fill_limit=int(usable_length/2) + usable_length%2
        right_fill_limit=int(usable_length/2)
        left_fill_word=str()
        right_fill_word=str()
        for i in range(left_fill_limit) :    left_fill_word  += filler_char
        for i in range(right_fill_limit):    right_fill_word += filler_char
    if align=="center":
        print(special_char + left_fill_word + print_word + right_fill_word + special_char, end="")
    elif align=="left":
        print(special_char + print_word + left_fill_word + right_fill_word + special_char, end="")
    elif align=="right":
        print(special_char + left_fill_word + right_fill_word + print_word + special_char, end="")


def heading(word=""):
    generate(filler_char="=")
    print()
    generate(print_word=word, filler_char=" ")
    print()
    generate(filler_char="=")
    print()

def subheading(word=""):
    generate(filler_char="-")
    print()
    generate(print_word=word, filler_char=" ")
    print()
    generate(filler_char="-")
    print()

def dashline(word=""):
    generate(print_word=word, filler_char="-")
    print()

def underline(word=""):
    generate(print_word=word, filler_char="_")
    print()

def line(word="",align="left"):
    generate(print_word=word,filler_char=" ",align=align)
    print()

def invalid():
    generate(print_word="!!!   Invalid Option   !!!",filler_char=" ")
    print()

def table(data,size=100):
    no_of_rows=len(data)
    no_of_columns=len(data[0])
    cell_size=int(size/no_of_columns)
    for i in range(no_of_rows):
        for j in range(no_of_columns):
            generate(filler_char="-",size=cell_size)
        print()
        for j in range(no_of_columns):
            generate(print_word=str(data[i][j]),filler_char=" ",size=cell_size)
        print()
    for i in range(no_of_columns):
        generate(filler_char="-",size=cell_size)
    print()
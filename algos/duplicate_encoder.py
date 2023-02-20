"""
Goal — transform a string into a new string, where each symbol in a anew string is «(», if that symbol has no duplicates, and «)», 
if that symbol has duplicates. Need to ignore capital letters.

Examples:
"din"      =>  "((("
"recede"   =>  "()()()"
"Success"  =>  ")())())"
"(( @"     =>  "))(("

"""

def duplicates(string):
    string = string.lower()
    new_word = ""
    for i in string:
        if string.count(i) > 1:
            new_word += ")"
        else:
            new_word += "("
    print(new_word)



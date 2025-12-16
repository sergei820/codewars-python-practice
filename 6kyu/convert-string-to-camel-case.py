# Convert string to camel case
# Complete the method/function so that it converts dash/underscore delimited words into camel casing.
# The first word within the output should be capitalized only if the original word was capitalized
# (known as Upper Camel Case, also often referred to as Pascal case). The next words should be always capitalized.
#
# Examples
#
# "the-stealth-warrior" gets converted to "theStealthWarrior"
# "The_Stealth_Warrior" gets converted to "TheStealthWarrior"
# "The_Stealth-Warrior" gets converted to "TheStealthWarrior"

def to_camel_case(text):
    if not text:
        return ''
    # naive solution O(4n)
    # text = text.replace('_', '-')
    # words = text.split('-')
    #
    # first_word = words[0]
    # other_words = [word.capitalize() for word in words[1:]]
    #
    # return first_word + ''.join(other_words)

    # better solution O(n)
    capitalize_next = False
    result = []  # DON'T USE '' HERE, str is immutable, it will create a new str each time!

    for i, c in enumerate(text):
        if c == '-' or c == '_':
            capitalize_next = True
        else:
            if i == 0:
                result.append(c)
            else:
                if capitalize_next:
                    result.append(c.upper())
                    capitalize_next = False
                else:
                    result.append(c)

    return ''.join(result)



if __name__ == "__main__":
    print(to_camel_case("the-stealth-warrior"))
    print(to_camel_case("The_Stealth_Warrior"))
    print(to_camel_case("The_Stealth-Warrior"))

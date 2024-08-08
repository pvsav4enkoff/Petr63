def count_calls():
    global calls
    calls += 1
def string_info(string):

    kor_1 = ()
    kor_1 = kor_1 + (len(string), string.upper(), string.lower())
    count_calls()
    return kor_1
def is_contains(string, list_to_search):

    count_calls()
    for word in list_to_search:
        if string.lower() == word.lower():
            return True
        elif word.lower() == string.lower():
            return True
    return False

global calls
calls = 0

print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBan
print(is_contains('cycle', ['recycle', 'cyclic'])) # No matches
print(calls)

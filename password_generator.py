import random
import string
def generate_password():
    index_size=random.randint(2, 12)
    lowercase_letters=string.ascii_lowercase
    uppercase_letters=string.ascii_uppercase
    digits=string.digits
    symbols=string.punctuation
    all_chars=lowercase_letters+uppercase_letters+digits+symbols
    all_chars_list=list(all_chars)
    random.shuffle(all_chars_list)
    password=(random.choice(lowercase_letters)+random.choice(uppercase_letters)+random.choice(digits)+random.choice(symbols))
    for i in range(index_size):
        password+=random.choice(all_chars_list)
    return password
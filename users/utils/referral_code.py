import random

alphabet = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]

digits = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']


def generate_referral_code():
    new_referral_code = ''.join(
        random.choice(alphabet + [letter.upper() for letter in alphabet] + digits)
        for i in range(8)
    )
    return new_referral_code

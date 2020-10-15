from captcha.image import ImageCaptcha
import random
import string


def get_random_string(length):
    # Random string with the combination of lower and upper case
    letters = string.ascii_letters
    result_str = ''.join(random.choice(letters) for i in range(length))
    print("Random string is:", result_str)

    n = random.randint(0,100)
    if n == 0:
        print("file is already there")
        print(n)
    else:
        print(n)
        image =ImageCaptcha()
        data = image.generate(result_str)
        image.write(result_str, str(n) +'.png')

get_random_string(8)




    








    




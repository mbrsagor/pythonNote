user_input = int(input('Enter your first input number:'))
user_input2 = int(input('Enter your first input number:'))


def division():
    try:
        result = user_input / user_input2
        print(f'Total result is: {result}')
    except ZeroDivisionError as e:
        print(e)
    finally:
        print('Thank you!!')


division()

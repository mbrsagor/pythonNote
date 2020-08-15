def about_me(user_input):
    text_file = open('about_me.html', 'w')
    text_file.write(user_input)
    text_file.close()
    print("successfully created the file.", text_file)


about_me('I am HTML')


def show_file():
    show_text = open('about_me.text', 'r')
    print(show_text.read())
    show_text.close()


show_file()

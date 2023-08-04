import tkinter as tk
import random
from colorama import Fore, init
import pyperclip

def generate_password():
    characters = ''
    options_list = []

    if uppercase_var.get():
        characters += 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        options_list.append('1')
    if lowercase_var.get():
        characters += 'abcdefghijklmnopqrstuvwxyz'
        options_list.append('2')
    if digits_var.get():
        characters += '0123456789'
        options_list.append('3')
    if special_var.get():
        characters += '!@#$%^&*()-_=+[]{}|:;,.<>?\/*~`'

    password_length = int(length_var.get())
    password = ''.join(random.choice(characters) for _ in range(password_length))
    result_label.config(text='Сгенерированный пароль: ' + password)
    copy_button.config(state='normal')  # Включаем кнопку "Копировать"

def copy_password():
    generated_password = result_label.cget('text')[23:]  # Получаем текст пароля
    with open("C:\\Users\\Maksim\\Desktop\\Python\\Pass Generator\\password.txt", "w") as file:
        file.write(generated_password + '\n')
    pyperclip.copy(generated_password)  # Копируем текст в буфер обмена 
    label1 = tk.Label(frame, text='пароль сохранен')
    label1.pack()


root = tk.Tk()
root.title('Генератор паролей')
root.geometry("320x330+650+100")
root.resizable(False, False)
logo = tk.PhotoImage(file='C:/Users/Maksim/Desktop/Python/graphic interface/pngimage.png')
root.iconphoto(False, logo)
uppercase_var = tk.IntVar()
lowercase_var = tk.IntVar()
digits_var = tk.IntVar()
special_var = tk.IntVar()
length_var = tk.StringVar(value='16')

frame = tk.Frame(root, padx=10, pady=10)
frame.pack()


options_label = tk.Label(frame, text='Выберите опции для использования:')
options_label.pack()

uppercase_check = tk.Checkbutton(frame, text='Заглавные буквы (A-Z)', variable=uppercase_var)
uppercase_check.pack(anchor='w')

lowercase_check = tk.Checkbutton(frame, text='Строчные буквы (a-z)', variable=lowercase_var)
lowercase_check.pack(anchor='w')

digits_check = tk.Checkbutton(frame, text='Цифры (0-9)', variable=digits_var)
digits_check.pack(anchor='w')

special_check = tk.Checkbutton(frame, text='Специальные символы (!@#$%^&*)', variable=special_var)
special_check.pack(anchor='w')

length_label = tk.Label(frame, text='Введите длину пароля:')
length_label.pack()

length_entry = tk.Entry(frame, textvariable=length_var)
length_entry.pack()

generate_button = tk.Button(frame, text='Сгенерировать пароль', command=generate_password)
generate_button.pack()

result_label = tk.Label(frame, text='')
result_label.pack()

exit_button = tk.Button(frame, text='Выход', command=root.quit)
exit_button.pack()

copy_button = tk.Button(frame, text='Копировать', state='disabled', command=copy_password)
copy_button.pack()

root.mainloop()
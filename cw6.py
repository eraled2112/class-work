#a = ('bin ', 'cdrom ', 'etc ', 'lib ', 'lib64 ', 'lost+found ', 'mnt ', 'proc ', 'run ', 'snap ', 'swapfile ', 'tmp ', 'var ', 'boot ', 'dev ', 'home ', 'lib32 ', 'libx32 ', 'media ', 'opt ', 'root ', 'sbin ', 'srv ', 'sys ', 'usr')

#with open('file.txt', 'w') as f:
#    f.write(''.join(a))
#print('Finished!')

#2
#with open('users.txt', 'a') as f:
#    a = input('Введите логин: ')
#    b = input('Введите пароль: ')
#    f.write(a)
#    f.write(b)
#print('Finished!')

#3
#with open('file.txt', 'r') as f:
#    text = f.read()
#    if 'w' in text:
#        print(w)
#        print('Да, в тексте есть w')
#    elif 'w' not in text:
#        print('Нет, в тексте нет w')

#4
#a = ('Python is a widely used high-level programming language for general-purpose programming, created by Guido van Rossum and first released in 1991. An interpreted language, Python has a design philosophy that emphasizes code readability (notably using whitespace indentation to delimit code blocks rather than curly brackets or keywords), and a syntax that allows programmers to express concepts in fewer lines of code than might be used in languages such as C++ or Java.')
#b = a.split()
#t_words = [ ]
#with open('python.txt', 'w') as f:
#    text = f.write(''.join(b))
#    for i in b:
#        if 't' in i:
#            t_words.append(i)
#print(t_words)

#1.1-----------------------
#with open('database.txt', 'w') as f:
#    a = f.write('l: eraled, p: 211205; l: aselas, p: 290901')

#b = int(input('Хотите (1)войти или (2)зарегистрироваться? '))
#if b == 1:
#    l = input('Логин: ')
#    if l in a:
#        print('Такой логин уже существует')
#        p = input('Введите пароль: ')
#    else:
#        c = input('Введите пароль: ')
#        d = input('Повторите пароль: ')
#        if c == d:
#            a.write(d)
#            print('Вы зарегистрировались!')
#        else:
#            print('Пароли не совпадают!')
#elif b == 2:
#    e = input('Введите логин: ')
#    t = input('ВВедите пароль: ')
#    m = input('')
#    if m == t:
#        a.write(m)
#    else:
#        print('Пароли не совпадают!')

#-------------------------


#1.2
#a = input('Введите логин: ')
#b = input('Введите пароль: ')
#c = input('Вставьте полный путь к фото: ')
#try:
#    file = open(c)
#except IOError as e:
#    print('Такого файла не существует')
#import os
#d = os.path.splitext(c)
#if d == '.jpeg' or 'jpg' or 'png':
#    with open('regist.txt', 'w') as f:
#        f.write(a)
#        f.write(b)
#        f.write(c)
#        print('Регистрация успешна!')


#2.1
#a = input('Путь до картинки которую нужно изменить: ')
#b = input('Путь до картинки на которую надо изменить: ')
#try:
#    file1 = open(a)
#except IOError as e:
#    print(a, 'Not found')
#print(file1)
#try:
#    file2 = open(b)
#except IOError as r:
#    print(b, 'Not found')
#if file1 and file2:
#    a == file2
#    b == file1
#    print('Done')


#2.2-----------------------------------------
#salaries = {
##    'January':'18000',
##    'February':'32641',
##    'March':'28300',
##    'April':'11200',
##    'May':'21100',
##    'June':'19000',
##    'July':'8000',
##    'August':'72000',
##    'September':'12300',
##    'October':'17000',
##    'November':'25000',
##    'December':'30000'
##}

#sal = ('January', (1)18000, 'February', (3)32641, 'March', (5)28300, 'April', (7)11200, 'May', (9)21100, 'June', 19000, 'July', 8000, 'August', 72000, 'September', 12300, 'October', 17000, 'November', 25000, 'December', 30000),
#with open('salaries.txt', 'w') as f:
#    f.write(sal)
#    a = f.read()
#print(a)

#3.1


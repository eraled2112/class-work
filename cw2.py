#1
lang1 = 'Rust'
languages = ['go', 'java', 'php', 'python', 'javascript', 'ruby']
for a in languages:
    print(a)
    if lang1 == languages:
        print('this language is in list')

#2
languages = ['go', 'java', 'php', 'python','javascript', 'ruby']
for a in languages:
    print(a)
    if a == 'php':
        break

#3
b = 7
for a in range(5):
    b *= 7
    print(b)

#4
languages = ['go', 'java', 'php', 'python','javascript', 'ruby']
for i in enumerate(languages, 0):
   print(i)

#5
#for a in range(1, 11):
  #  print(a)
 #   if a == 10:
#        print()

#6
#names = ('Максат','Лязат','Данияр','Айбек','Атай','Салават','Адинай','Жоомарт','Алымбек','Эрмек','Дастан','Бекмамат','Аслан')
#for i in names:
    #if names.index() 

#7
names = ('Максат','Лязат','Данияр','Айбек','Атай','Салават','Адинай','Жоомарт','Алымбек','Эрмек','Дастан','Бекмамат','Аслан')
counter = 0
for i in names:
    if counter % 2 == 0:
    counter += 1
print(i)

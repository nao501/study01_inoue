if  __name__ =='__main__':
    
    pass1=r'C:\Users\奈央也\Desktop\python (F)\test\character_name.csv'
    with open(pass1) as f:
         character_name = list(f.readlines())
         for a in character_name:
             print(a.strip())
        


def search ():
    word = input('名前を入力してください：')
    if word in character_name:
        print('{}が見つかりました。'.format(word))
    else:
        print('{}が見つかりませんでした。'.format(word))
        character_name.append(word)

if  __name__ =='__main__':
    search()
    pass1=r'C:\Users\奈央也\Desktop\python (F)\test\test.csv'
    import csv
    with open(pass1,mode='w') as f:
         f.writelines("\n".join(str(character_name)))
        
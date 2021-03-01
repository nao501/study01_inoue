if  __name__ =='__main__':
    
    pass1=r'C:\Users\奈央也\Desktop\python (F)\test\character_name.csv'
    with open(pass1) as f:
         character_name = f.readlines()
         character_deta =[ deta.strip() for deta in character_name ]
         for  deta in character_name:
             print(deta.strip())
        


def search ():
    word = input('名前を入力してください：')
    if word in character_deta:
        print('{}が見つかりました。'.format(word))
    else:
        print('{}が見つかりませんでした。'.format(word))
        character_deta.append(word)

if  __name__ =='__main__':
    search()
    pass1=r'C:\Users\奈央也\Desktop\python (F)\test\character_name.csv'
    with open(pass1,mode='w') as f:
         f.writelines("\n".join(character_deta))
        
word = input()
if word == 'vertebrado':
    word2 = input()
    if word2 == 'ave':
        word3 = input()
        if word3 == 'carnivoro':
            print('aguia')
        elif word3 == 'onivoro':
            print('pomba')
    elif word2 == 'mamifero':
        word3 = input()
        if word3 == 'herbivoro':
            print('vaca')
        elif word3 == 'onivoro':
            print('homem')
if word == 'invertebrado':
    word2 = input()
    if word2 == 'inseto':
        word3 = input()
        if word3 == 'hematofago':
            print('pulga')
        elif word3 == 'herbivoro':
            print('lagarta')
    elif word2 == 'anelideo':
        word3 = input()
        if word3 == 'hematofago':
            print('sanguessuga')
        elif word3 == 'onivoro':
            print('minhoca')

import world_gen as wg
import functions as fun

wid, hei, name, pal = 60, 60, 'gen_map', wg.colors1
while 1:
    print('Greetings. wanna make your own map or use default settings? <y/n>')
    print('to exit enter <e>')
    inp = input('->')
    if inp == 'e':
        print('bye.')
        break
    elif inp == 'y':
        print('Nice. wanna make your own palette or use mine with 3 colors? <y/n>')
        if input('->') == 'y':
            n = int(input('how many colors do you want to use? ->'))
            print('now enter colors in RGB logic (like 10 22 34). new color - new line')
            pal = fun.colors(n)
        else:
            print('k.')
        wid, hei = map(int, input('what sizes you want (enter as 20 20 etc) ->').split())
        name = input('how should be called the exit file? ->')

    print('done.')
    wg.main((wid, hei), name, pal)
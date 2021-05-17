cont = int(0)
casos = int(input())
while cont < casos:
    num = str(input())
    cont1 = int(0)
    led = int(0)
    tamanho = int(len(num))
    while cont1 < tamanho:
        if (num[cont1] == '2' or num[cont1] == '3' or num[cont1] == '5'):
            led = led + 5
        else:
            if (num[cont1] == '6' or num[cont1] == '0' or num[cont1] == '9'):
                led = led + 6
            else:
                if (num[cont1] == '8'):
                    led = led + 7
                else:
                    if (num[cont1] == '1'):
                        led = led + 2
                    else:
                        if (num[cont1] == '4'):
                            led = led + 4
                        else:
                            led = led + 3
        cont1 = cont1 + 1
    print("{} leds".format(led))
    cont = cont + 1
import pyautogui
from time import sleep
#registrar usuario
pyautogui.click(672,438,duration=2)
pyautogui.click(766,383,duration=2)
pyautogui.write('robert')
pyautogui.click(676,411,duration=2)
pyautogui.write('12345')
pyautogui.click(615,439,duration=2)
#clicar digitar meu usuario
pyautogui.click(709,387,duration=2)
pyautogui.write('robert')

#clicar e digitar a senha

pyautogui.click(706,410,duration=2)
pyautogui.write('12345')

#clicar em entrar
pyautogui.click(592,436,duration=2)

#extrair cada produto
with open ('produtos.txt', 'r') as arquivo:
    for linha in arquivo:
        produto = linha.split(',')[0]
        quantidade = linha.split(',')[1]
        preco = linha.split(',')[2]

        pyautogui.click(423,372,duration=2)
        pyautogui.write(produto)
        pyautogui.click(475,404, duration=2)
        pyautogui.write(quantidade)
        pyautogui.click(418,424,duration=2)
        pyautogui.write(preco)
        pyautogui.click(322,581,duration=1)
        sleep(1)

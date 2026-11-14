#imports
from pynput.keyboard import Key, Controller
import time
kboard = Controller() #our controller for the keyboard

#since this code hates me i have to type it out CHARACTER BY CHARACTER >:(
def typeChar(codeStr: str):
    for i in range(0, len(codeStr)):
        kboard.tap(codeStr[i])
        time.sleep(.01)


def writeCode():
    typeChar('#include <iostream>')
    kboard.tap(Key.enter)
    time.sleep(.01)
    typeChar('using namespace std;')
    for i in range(0, 3):
        kboard.tap(Key.enter)
        time.sleep(.01)
    typeChar('int main() {')
    kboard.tap(Key.enter)
    time.sleep(.01)
    kboard.tap(Key.tab)
    time.sleep(.01)
    typeChar('return 0;')
    kboard.tap(Key.enter)
    time.sleep(.1)
    #kboard.tap(Key.backspace)
    time.sleep(.01)
    typeChar('}')


def main():
    print('There is a 5 second delay to let you change programs.')
    time.sleep(5)
    writeCode()

main()
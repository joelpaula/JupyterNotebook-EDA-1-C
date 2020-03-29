# Python program to print
# colored text and background
def prRed(skk): print("\033[91m] {}\033[00m]" .format(skk))
def prGreen(skk): print("\033[92m] {}\033[00m]" .format(skk))
def prYellow(skk): print("\033[93m] {}\033[00m]" .format(skk))
def prLightPurple(skk): print("\033[94m] {}\033[00m]" .format(skk))
def prPurple(skk): print("\033[95m] {}\033[00m]" .format(skk))
def prCyan(skk): print("\033[96m] {}\033[00m]" .format(skk))
def prLightGray(skk): print("\033[97m] {}\033[00m]" .format(skk))
def prBlack(skk): print("\033[98m] {}\033[00m]" .format(skk))


prCyan("Hello World, ")
prYellow("It's")
prGreen("Geeks")
prRed("For")
prGreen("Geeks")

setMenu = {"Eggs", "Bacon"}
print(setMenu)
# > {'Bacon', 'Eggs'}
setMenu = set(list(setMenu) + list({"Spam"}))
print(setMenu)
# > {'Bacon', 'Spam', 'Eggs'}
setAdditions = {"Lobster", "Sausage"}
setMenu = set(list(setMenu) + list(setAdditions))
print(setMenu)
# > {'Lobster', 'Spam', 'Eggs', 'Sausage', 'Bacon'}

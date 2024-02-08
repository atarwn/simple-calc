MainLoop = True
print('# Simple calculator on python')
print('# Copyleft "QOSP" atarwn, 2024')
print('# Write exit to exit')
while MainLoop:
    h = input("~$> ")
    if h != "exit":
        try:
            print(eval(h))
        except:
            print("An error occurred!")
    else:
        MainLoop = False

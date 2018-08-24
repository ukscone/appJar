import sys
sys.path.append("../../")

from appJar import gui

def keyPress(key): print(key, 'pressed')

def press(btn):
    if btn == 'ENABLE': app.enableMenuItem('a', 'w')
    elif btn == 'DISABLE': app.disableMenuItem('a', 'w')
    elif btn == 'DELETE': app.deleteMenuItem('a', 'w')

def pressm(btn):
    if btn == 'ENABLEM': app.enableMenu('22')
    elif btn == 'DISABLEM': app.disableMenu('22')
    elif btn == 'DELETEM': app.deleteMenu('22')

def pressb(btn):
    print(btn)
    if btn == 'ENABLEB': app.enableMenubar()
    elif btn == 'DISABLEB': app.disableMenubar()
    elif btn == 'DELETEB': app.deleteMenubar()
    elif btn == 'Click Me': print('help')

with gui() as app:
    app.setLogLevel('trace')
    app.label('hello world')
    app.addMenuItem('a', '5 ', shortcut='Command-Key-5', func=keyPress)
    app.addMenuItem('a', 'w', shortcut='Control-w', func=keyPress)
    app.addMenuItem('a', 'e', shortcut='Option-e', func=keyPress)
    app.addMenuItem('a', '-')
    app.addSubMenu('a', '22')
    app.addMenuItem('22', '1', shortcut='Key-1', func=keyPress)
    app.addMenuItem('22', '2', shortcut='Control-Key-2', func=keyPress)
    app.addMenuItem('22', '3', shortcut='Alt-Key-3', func=keyPress)
    app.addMenuItem('22', '4', shortcut='Option-Key-4', func=keyPress)
    app.addMenuItem('a', '-')
    app.addMenuItem('a', 'a', shortcut='Control-Shift-a', func=keyPress)
    app.addMenuItem('a', 's', shortcut='Control-Alt-s', func=keyPress)
    app.addMenuItem('a', 'h', shortcut='Alt-Control-h', func=keyPress)
    app.addMenuItem('a', 'd', shortcut='Alt-shift-d', func=keyPress)
    app.addMenuItem('a', 'f', shortcut='Control-Shift-f', func=keyPress)
    app.addMenuItem('a', 'g', shortcut='Control-shift-g', func=keyPress)
    app.addMenuItem('c', 'u', shortcut='Shift-u', func=keyPress)
    app.addMenuItem('c', 'r', shortcut='r', func=keyPress)
    app.addMenuItem('c', 'U', shortcut='u', func=keyPress)

#    print('binding ctrl-shift-S')
#    app.topLevel.bind_all('<Control-Shift-S>', keyPress)
#    app.bindKey('<Control-Shift-E>', keyPress)
#    app.bindKey('<Control-Shift-R>', keyPress)
#    app.bindKey('<z>', keyPress)
#    app.bindKey('<Control-x>', keyPress)

    app.addButtons(['DISABLE', 'ENABLE','DELETE'], press)
    app.addButtons(['DISABLEM', 'ENABLEM','DELETEM'], pressm)
    app.addButtons(['DISABLEB', 'ENABLEB','DELETEB'], pressb)

    app.entry('text')
    app.addMenuEdit(inMenuBar=True)
    app.createRightClickMenu('Details', showInBar=True) 
    app.addMenuItem('Details', 'Info Menu', pressb)
    app.disableMenuItem('Details', 'Info Menu')
    app.addMenuItem('Details', '-')
    app.addMenuItem('Details', 'Click Me', pressb)
    app.label('press me', right='Details')
#    app.setLabelRightClick('press me', 'Details')

    app.addMenuPreferences(pressb)
    app.addMenuWindow()
    app.addMenuHelp(pressb)
    app.addMenuItem("appJar", "Help", app.appJarHelp)
    app.addMenuItem("appJar", "About", app.appJarAbout)

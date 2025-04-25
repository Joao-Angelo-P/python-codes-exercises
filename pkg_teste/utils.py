""" import function from this module """ 
def _test():
 main = __import__('__main__')
 from tkinter import Label, Button, Tk
 root = Tk()
 texto = Label(master=root, text="-Teste \"\xe7\"-")
 root.teste = texto
 #root.teste['text'] += '{0}{1}'.format('\n', main.sys.argv[0])
 b = Button(master=root, text="Click Aqui!",
 command=lambda root=root: root.teste.configure(text="*%s*" % root.teste['text']))
 texto.pack()
 Label(root, text='{}'.format(main.sys.argv[0])).pack()
 b.pack()
 Button(root, text="Quit", command=root.destroy).pack()
 root.iconify(); root.update(); root.deiconify()
 root.mainloop()
 

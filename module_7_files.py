import tkinter

window = tkinter.Tk()
window.title("Проводник")
window.geometry("350x150")
window.configure(bg='black')
window.resizable(False,False)
text = tkinter.Label(window,text = 'Файл', height=5, width=50, background='silver')
text.grid(column=1,row=1)
botton_select=tkinter.Button(window, width=20, height=3, text='Выбрать файл')
botton_select.grid(column=1, row=2)



window.mainloop()
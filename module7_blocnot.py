import tkinter as tk
from tkinter import filedialog, Text
import subprocess
"""
Руководство
"""
class TextEditor(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Простой текстовый редактор")
        self.geometry("600x400")

        self.text = Text(self)
        self.text.pack(fill="both", expand=True)

        self.menu_bar = tk.Menu(self)
        self.config(menu=self.menu_bar)

        self.file_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="Файл", menu=self.file_menu)
        self.file_menu.add_command(label="Открыть", command=self.open_file)
        self.file_menu.add_command(label="Сохранить", command=self.save_file)
        dir_path = r"C:\1\probe"
        self.path = r"C:\1\probe" + '/'+'repka.txt'
        self.menu_bar.add_cascade(label="Руководство", command = self.open_file_2)

    def open_file(self):
        filepath = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
        with open(filepath, "r",encoding="utf-8") as file:
            self.text.insert("1.0", file.read())

    def save_file(self):
        filepath = filedialog.asksaveasfilename(defaultextension=".txt")
        with open(filepath, "w",encoding="utf-8") as file:
            file.write(self.text.get("1.0", "end"))

    def open_file_2(self):
        print(self.path)
        # try:
        #     with open(self.path, 'r',encoding="utf-8") as file:
        #         content = file.read()
        #         subprocess.run(["type", self.path])
        #         # print(content)
        # except FileNotFoundError:
        #     print(f"Файл '{self.path}' не найден.")
        # except Exception as e:
        #     print(f"Произошла ошибка при чтении файла: {e}")

if __name__ == "__main__":
    app = TextEditor()
    app.mainloop()
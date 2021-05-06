import tkinter as tk


class Application(tk.Frame):
    def __init__(self, master=None):
        # Windowの初期設定を行う。
        super().__init__(master)

        # Windowの画面サイズを設定する。
        self.master.geometry("300x200")

        # Window内にFrameを作成する。
        tk.Frame(self.master)

        # ラベル1Widgetを作成する。
        label1 = tk.Label(text="1",
                          width=30, height=15, bg="orchid4")
        # ラベル2Widgetを作成する。
        label2 = tk.Label(text="2",
                          width=30, height=15, bg="dark turquoise")
        # ラベル3Widgetを作成する。
        label3 = tk.Label(text="3",
                          width=30, height=15, bg="MidnightBlue")

        # Windowを親要素とした場合に、それぞれラベルWidgetをどのように配置するのか?
        label1.pack()
        label2.pack()
        label3.pack()


if __name__ == "__main__":
    root = tk.Tk()
    app = Application(master=root)
    # Windowをループさせて、継続的にWindow表示させる。
    app.mainloop()

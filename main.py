import tkinter as tk

class Application(tk.Frame):
    def __init__(self, master=None):
        # Windowの初期設定を行う。
        super().__init__(master)

        # Windowの画面サイズを設定する。
        # geometryについて : https://kuroro.blog/python/rozH3S2CYE0a0nB3s2QL/
        self.master.geometry("300x200")

        # Windowを親要素をとして、frame Widget(Frame)を作成する。
        # Frameについて : https://kuroro.blog/python/P20XOidA5nh583fYRvxf/
        frame = tk.Frame(self.master)
        # Windowを親要素とした場合に、frame Widget(Frame)をどのように配置するのか?
        frame.pack()

        # frame Widget(Frame)を親要素として、label Widgetを作成する。
        # text : テキスト情報
        # width : 幅設定
        # height : 高さ設定
        # bg : 背景色設定
        # 色の設定を変更する場合 : http://www.tcl.tk/man/tcl/TkCmd/colors.htm
        # Labelについて : https://kuroro.blog/python/Pj4Z7JBNRvcHZvtFqiKD/
        label1 = tk.Label(frame, text="label1", width=30, height=15, bg="red")
        # frame Widget(Frame)を親要素として、label Widgetを作成する。
        # text : テキスト情報
        # width : 幅設定
        # height : 高さ設定
        # bg : 背景色設定
        # 色の設定を変更する場合 : http://www.tcl.tk/man/tcl/TkCmd/colors.htm
        # Labelについて : https://kuroro.blog/python/Pj4Z7JBNRvcHZvtFqiKD/
        label2 = tk.Label(frame, text="label2", width=30, height=15, bg="green")
        # frame Widget(Frame)を親要素として、label Widgetを作成する。
        # text : テキスト情報
        # width : 幅設定
        # height : 高さ設定
        # bg : 背景色設定
        # 色の設定を変更する場合 : http://www.tcl.tk/man/tcl/TkCmd/colors.htm
        # Labelについて : https://kuroro.blog/python/Pj4Z7JBNRvcHZvtFqiKD/
        label3 = tk.Label(frame, text="label3", width=30, height=15, bg="blue")

        # frame Widget(Frame)を親要素とした場合に、label1 Widgetをどのように配置するのか?
        label1.pack()
        # frame Widget(Frame)を親要素とした場合に、label2 Widgetをどのように配置するのか?
        label2.pack()
        # frame Widget(Frame)を親要素とした場合に、label3 Widgetをどのように配置するのか?
        label3.pack()


if __name__ == "__main__":
    root = tk.Tk()
    app = Application(master=root)
    # Windowをループさせて、継続的にWindow表示させる。
    # mainloopについて : https://kuroro.blog/python/DmJdUb50oAhmBteRa4fi/
    app.mainloop()

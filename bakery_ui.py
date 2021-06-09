import tkinter
from tkinter import *


class BakeryView:
    def __init__(self, window):
        self.__init_window(window)

    def __init_window(self, window):
        window.title("빵집")
        window.geometry('400x200')
        label = Label(window, text='주문내역')
        label.pack()
        self.orderText = Text(window)
        self.orderText.pack()

    def add_order(self, orders):
        self.orderText.insert(0.0, orders + "\n")


class CustomerView:
    def __init__(self, name, window, bakery_view):
        self.name = name
        self.__init_window(window)
        self.bakeryView = bakery_view

    def __init_window(self, window):
        window.title("고객: " + self.name)
        window.geometry('350x200')

        OF = Frame(window, bg="WHITE")
        OF.pack(anchor=CENTER, pady=(40, 0))

        self.menus = {"샌드위치": 5000, "케이크": 20000}
        self.menu_ui = []
        self.order = []

        for menu, val in self.menus.items():
            MF = Frame(OF)
            menu_text = f"{menu} ({val}원)"
            Label(MF, text=menu_text).pack(side=LEFT)

            self.order.append(Entry(MF))
            self.order[-1]["width"] = 10
            self.order[-1].pack(side=RIGHT)

            self.menu_ui.append(MF)
            self.menu_ui[-1].pack(fill=BOTH, padx=10, pady=(5, 0))

        BF = Frame(OF)
        BF.pack(pady=5)

        self.SBtn = Button(BF, text="주문하기", command=self.send_order)

        self.orderstate = StringVar()

        LF = Frame(window)
        LF.pack()

        Label(LF, textvariable=self.orderstate).pack(pady=(10, 0))

        self.orderstate.set(value="주문해주세요")

        self.SBtn.pack()

    def send_order(self):
        order_text = f"{self.name}:"
        test_len = len(order_text)

        text_list = [f" {menu} ({val}원) " for menu, val in self.menus.items()]
        num_list = [E.get() for E in self.order]

        # 여기에 + 기호 판별은 없으므로, + 기호가 있는 것은 문자라 판단하겠습니다.
        for idx, val in enumerate(num_list):
            if len(val) == 0:
                val = "0"
            if val[0] == "-" and val[1:].isdecimal():
                self.orderstate.set(
                    value="정상적이지 않은 주문입니다.(음수 입력)\n다시 입력해주시기 바랍니다.")
                return
            if not val.isdecimal():
                self.orderstate.set(
                    value="정상적이지 않은 주문입니다.(문자 입력)\n다시 입력해주시기 바랍니다.")
                return
            if int(val) == 0:
                continue
            order_text += text_list[idx] + f"{val}개,"

        if len(order_text) <= test_len:
            self.orderstate.set(value="주문이 입력되지 않았습니다.\n다시 입력해주시기 바랍니다.")
            return

        self.bakeryView.add_order(order_text[:-1])
        self.orderstate.set(value="주문이 접수되었습니다. 감사합니다.")


if __name__ == '__main__':
    app = Tk()
    bakery = BakeryView(app)
    CustomerView('고객A', Toplevel(app), bakery)
    CustomerView('고객B', Toplevel(app), bakery)
    app.mainloop()

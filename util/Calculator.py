import tkinter as tk
from conversions import from_decimal, to_decimal

class Calculator:
    def __init__(self) -> None:
        self.input = ""
        self.operation = ""
        self.number_system_mode: int

        self.root = tk.Tk()
        self.root.geometry("400x550")
        self.root.title("NUMBER SYSTEMS CALCULATOR")
        self.root.bind("<KeyPress>", self.__shortcut)
        self.root.resizable(False, False)

        self.mode_label= tk.Label(self.root, text="Mode: ", font=('Arial', 11))
        self.mode_label.pack(padx=10)
        self.display_label = tk.Label(self.root, text="0", font=('Arial', 18))
        self.display_label.pack(padx=10, pady=20)

        self.button_frame = tk.Frame(self.root)
        self.buttons = []

        self.__create_buttons()
        

    def run(self):
        self.root.mainloop()


    def __create_buttons(self):
        row = 2
        column = 0
        counter = 0
        is_hexa = False
        unicode_str = 65
        btn_state = "active"

        for i in range(0, 18):
            self.button_frame.columnconfigure(i, weight=1)

        dec_btn = tk.Button(self.button_frame, text="DEC", font=('Arial', 18), width="10", command=lambda: self.__change_number_system(10))
        bin_btn = tk.Button(self.button_frame, text="BIN", font=('Arial', 18), width="10", command=lambda: self.__change_number_system(2))
        oct_btn = tk.Button(self.button_frame, text="OCT", font=('Arial', 18), width="10", command=lambda: self.__change_number_system(8))
        hex_btn = tk.Button(self.button_frame, text="HEX", font=('Arial', 18), width="10", command=lambda: self.__change_number_system(16))
        clear_btn = tk.Button(self.button_frame, text="Clear", font=('Arial', 18), width="10", command=self.__clear_buffer)
        backspace_btn = tk.Button(self.button_frame, text="<-", font=('Arial', 18), width="10", command=self.__erase)

        dec_btn.grid(row=0, column=0, sticky="we")
        bin_btn.grid(row=0, column=1, sticky="we")
        oct_btn.grid(row=0, column=2, sticky="we")
        hex_btn.grid(row=1, column=0, sticky="we")
        clear_btn.grid(row=1, column=1, sticky="we")
        backspace_btn.grid(row=1, column=2, sticky="we")

        for i in range(0, 16):
            counter += 1
            btn = None
            btn_text: str

            if is_hexa:
                btn_text = chr(unicode_str)
                unicode_str += 1
            else:
                btn_text = str(i)

            btn = tk.Button(self.button_frame, text=btn_text, font=('Arial', 18), width="10", command=lambda btn_text=btn_text: self.__number_click(btn_text), state=btn_state)
            btn.grid(row=row, column=column, sticky="we")
            self.buttons.append(btn)

            column += 1

            if i == 9:
                is_hexa = True
                btn_state = "disabled"

            if counter % 3 == 0:
                row += 1
                column = 0
                counter = 0


        add_btn = tk.Button(self.button_frame, text="+", font=('Arial', 18), width="10", command=lambda: self.__change_operation("+"))
        subtract_btn = tk.Button(self.button_frame, text="-", font=('Arial', 18), width="10", command=lambda: self.__change_operation("-"))
        multiply_btn = tk.Button(self.button_frame, text="*", font=('Arial', 18), width="10", command=lambda: self.__change_operation("*"))
        divide_btn = tk.Button(self.button_frame, text="/", font=('Arial', 18), width="10", command=lambda: self.__change_operation("/"))
        equal_btn = tk.Button(self.button_frame, text="=", font=('Arial', 18), width="10", command=self.__get_result)

        add_btn.grid(row=7, column=1, sticky="we")
        subtract_btn.grid(row=7, column=2, sticky="we")
        multiply_btn.grid(row=8, column=0, sticky="we")
        divide_btn.grid(row=8, column=1, sticky="we")
        equal_btn.grid(row=8, column=2, sticky="we")

        self.mode_label.config(text="Mode: Dec")
        self.number_system_mode = 10
        self.button_frame.pack(fill="x")


    def __shortcut(self, event):
        if event.keysym == "Escape":
            self.root.quit()


    def __change_operation(self, operation: chr):
        self.operation = operation
        print(self.operation)


    def __get_result(self):
        print("equals")


    def __change_number_system(self, mode: int):
        prev_number_system = self.number_system_mode
        limit: int
        temp_conv = None
        final_conv = None
        modes = {
            2: "Bin",
            8: "Oct", 
            10: "Dec",
            16: "Hex"
        }

        self.number_system_mode = mode
        print(self.number_system_mode)

        if prev_number_system == 2:
            temp_conv = to_decimal.binary_to_decimal(int(self.input))
        elif prev_number_system == 8:
            temp_conv = to_decimal.octal_to_decimal(int(self.input))
        elif prev_number_system == 10:
            temp_conv = int(self.input)
        else:
            temp_conv = to_decimal.hexadecimal_to_decimal(self.input)
        
        if self.number_system_mode == 2:
            final_conv = from_decimal.decimal_to_binary(temp_conv)
        elif self.number_system_mode == 8:
            final_conv = from_decimal.decimal_to_octal(temp_conv)
        elif self.number_system_mode == 10:
            final_conv = temp_conv
        else:
            final_conv = from_decimal.decimal_to_hexadecimal(temp_conv)

        limit = self.number_system_mode
        accepted_range = list(range(0, limit))
        self.mode_label.config(text="Mode: " + modes[self.number_system_mode])

        self.input = str(final_conv)
        self.display_label.config(text=self.input)

        for i in range(0, 16):
            if i in accepted_range:
                self.buttons[i].config(state="active")
            else:
                self.buttons[i].config(state="disabled")


    def __number_click(self, number: chr):
        if self.input == '0':
            self.input = number
        else:
            self.input += number

        self.display_label.config(text=self.input)
        print(number)


    def __clear_buffer(self):
        self.input = "0"
        self.display_label.config(text=self.input)


    def __erase(self):
        self.input = self.input[:-1]

        if self.input == '':
            self.input = '0'

        self.display_label.config(text=self.input)

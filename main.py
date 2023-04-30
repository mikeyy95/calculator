from tkinter import *

# defining the function to perform calculations
def click(event):
    global fvalue
    text = event.widget.cget("text")

    if text == "=":
        # evaluating the expression when "=" is pressed
        if fvalue.get().isdigit():
            value = int(fvalue.get())
        else:
            try:
                value = eval(fvalue.get())
            except Exception as e:
                value = "Error"

        fvalue.set(value)
        input_field.update()

    elif text == "clear":
        # clearing the input field when "clear" is pressed
        fvalue.set("")
        input_field.update()
    else:
        fvalue.set(fvalue.get() + text)
        input_field.update()


# creating the main window
root = Tk()
root.geometry("330x380")
root.title("Calculator")
root.config(bg="#232931")

# setting the font and color of the input field
fvalue = StringVar()
fvalue.set("")
input_field = Entry(root, textvar=fvalue, width=22, font=("Arial", 18, "bold"), bd=5, bg="#ececec")
input_field.grid(row=0, column=1, columnspan=3, padx=10, pady=10)

# creating the buttons
button1 = Button(root, text="1", padx=20, pady=10, font=("Arial", 18, "bold"), bd=4, bg="#FFC300")
button2 = Button(root, text="2", padx=20, pady=10, font=("Arial", 18, "bold"), bd=4, bg="#FFC300")
button3 = Button(root, text="3", padx=20, pady=10, font=("Arial", 18, "bold"), bd=4, bg="#FFC300")
button4 = Button(root, text="4", padx=20, pady=10, font=("Arial", 18, "bold"), bd=4, bg="#FFC300")
button5 = Button(root, text="5", padx=20, pady=10, font=("Arial", 18, "bold"), bd=4, bg="#FFC300")
button6 = Button(root, text="6", padx=20, pady=10, font=("Arial", 18, "bold"), bd=4, bg="#FFC300")
button7 = Button(root, text="7", padx=20, pady=10, font=("Arial", 18, "bold"), bd=4, bg="#FFC300")
button8 = Button(root, text="8", padx=20, pady=10, font=("Arial", 18, "bold"), bd=4, bg="#FFC300")
button9 = Button(root, text="9", padx=20, pady=10, font=("Arial", 18, "bold"), bd=4, bg="#FFC300")
button0 = Button(root, text="0", padx=20, pady=10, font=("Arial", 18, "bold"), bd=4, bg="#FFC300")
button_plus = Button(root, text="+", padx=18, pady=10, font=("Arial", 18, "bold"), bd=4, bg="#FF5733")
button_minus = Button(root, text="-", padx=20, pady=10, font=("Arial", 18, "bold"), bd=4, bg="#FF5733")
button_into = Button(root, text="*", padx=20, pady=10, font=("Arial", 18, "bold"), bd=4, bg="#FF5733")
buttondivide = Button(root, text="/", padx=20, pady=10, font=("Arial", 18, "bold"), bd=4, bg="#FF5733")
buttonequal = Button(root, text="=", padx=20, pady=10, font=("Arial", 18, "bold"), bd=4, bg="#FF5733")
buttonclear = Button(root, text="clear", padx=20, pady=10, font=("Arial", 18, "bold"), bd=4, bg="#FF5733")
buttonpoint=Button(root,text=".",padx=20, pady=10, font=("Arial", 18, "bold"), bd=4, bg="#FF5733")
button_two_zero=Button(root,text="00",padx=20, pady=10, font=("Arial", 18, "bold"), bd=4, bg="#FF5733")


#__binding buttons__

button1.grid(row=1, column=0)
button1.bind("<Button-1>", click)
button2.grid(row=1, column=1)
button2.bind("<Button-1>", click)
button3.grid(row=1, column=2)
button3.bind("<Button-1>", click)

button4.grid(row=2, column=0)
button4.bind("<Button-1>", click)
button5.grid(row=2, column=1)
button5.bind("<Button-1>", click)
button6.grid(row=2, column=2)
button6.bind("<Button-1>", click)

button7.grid(row=3, column=0)
button7.bind("<Button-1>", click)
button8.grid(row=3, column=1)
button8.bind("<Button-1>", click)
button9.grid(row=3, column=2)
button9.bind("<Button-1>", click)

button0.grid(row=0, column=0)
button0.bind("<Button-1>", click)

button_plus.grid(row=0, column=4)
button_plus.bind("<Button-1>", click)
button_minus.grid(row=1, column=4)
button_minus.bind("<Button-1>", click)
button_into.grid(row=2, column=4)
button_into.bind("<Button-1>", click)
buttondivide.grid(row=3, column=4)
buttondivide.bind("<Button-1>", click)
button_two_zero.grid(row=4,column=4)
button_two_zero.bind("<Button-1>",click)

buttonequal.grid(row=4, column=0)
buttonequal.bind("<Button-1>", click)
buttonclear.grid(row=4, column=1)
buttonclear.bind("<Button-1>", click)
buttonpoint.grid(row=4,column=2)
buttonpoint.bind("<Button-1>",click)


#__running mainloop__

root.mainloop()
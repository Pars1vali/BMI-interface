from tkinter import *
from tkinter import messagebox, ttk

isLight = True

def calculate_bmi():
    kg = int(weight_tf.get())
    m = int(height_tf.get())/100
    bmi = kg/(m*m)
    bmi = round(bmi, 1)
    with open("history.txt", 'a') as file:
        file.write(str(bmi) + " " + str(kg) + " " + str(m) + "\n")

    if bmi < 18.5:
        messagebox.showinfo('', f'ИМТ = {bmi} соответствует недостаточному весу')
    elif (bmi >= 18.5) and (bmi <= 24.9):
        messagebox.showinfo('', f'ИМТ = {bmi} соответствует нормальному весу')
    elif (bmi >= 24.9) and (bmi <= 29.9):\
        messagebox.showinfo('', f'ИМТ = {bmi} соответствует избыточному весу')
    else:
        messagebox.showinfo('', f'ИМТ = {bmi} соответствует ожирению')
def change_color():
    global isLight
    isLight = not isLight

    if isLight:
        window.config(bg=baseColor)
        height_lb.config(bg=baseColor)
        height_lb.config(bg = baseColor)
        height_lb.config(fg="black")
        weight_lb.config(bg=baseColor)
        weight_lb.config(fg="black")
        btn_theme.config(text="Dark theme")
        btn_theme.config(fg="white", bg="black")

    else:
        window.config(bg="black")
        height_lb.config(bg = "black")
        height_lb.config(fg="white")
        weight_lb.config(bg="black")
        weight_lb.config(fg="white")
        btn_theme.config(text="Light theme")
        btn_theme.config(fg="black", bg="white")
def history():
    history_w = Tk()
    history_w.title("History")
    history_w.geometry("250x200+500+350")
    # history_w.config(bg=baseColor)
    # history_w.resizable(0, 0)

    people = [
        ("Tom", 38, "tom@email.com"), ("Bob", 42, "bob@email.com"), ("Sam", 28, "sam@email.com"),
        ("Alice", 33, "alice@email.com"), ("Kate", 21, "kate@email.com"), ("Ann", 24, "ann@email.com"),
        ("Mike", 34, "mike@email.com"), ("Alex", 52, "alex@email.com"), ("Jess", 28, "jess@email.com"),
    ]

    columns = ("name", "age", "email")

    tree = ttk.Treeview(columns=columns, show="headings")
    tree.place(fill=BOTH, expand=1)

    tree.heading("name", text="Имя")
    tree.heading("age", text="Возраст")
    tree.heading("email", text="Email")

    for person in people:
        tree.insert("", END, values=person)

    scrollbar = ttk.Scrollbar(orient=VERTICAL, command=tree.yview)
    tree.configure(yscroll=scrollbar.set)
    scrollbar.grid(row=0, column=1, sticky="ns")
    history_w.mainloop()


window = Tk()
window.title("Калькулятор индекса массы тела (ИМТ)")
window.geometry('500x300')
baseColor = window.cget("background")
window.config(bg=baseColor)
window.resizable(width=False, height=False)

height_lb = Label(
    text="Введите свой рост (в см)",
    fg="black"
)
height_lb.place(x=90, y=90)

weight_lb = Label(text="Введите свой вес (в кг) ")
weight_lb.place(x=270, y=90)

height_tf = Entry()
height_tf.place(x=96.5, y=110, width=130)

weight_tf = Entry()
weight_tf.place(x=270, y=110, width=130)

cal_btn = Button(
 text='BMI',
 command=calculate_bmi,
 font=('Terminal',10)
)
cal_btn.place(x=185, y=160)


btn_theme = Button(
    bg = "black",
    fg="white",
    text="Dark theme",
    command = change_color,
    font=('Terminal', 10)
)
btn_theme.place(x=200, y=250)

btn_history = Button(
    text="History",
    font=("Terminal", 10),
    command=history
)
btn_history.place(x=250, y=160)

window.mainloop()
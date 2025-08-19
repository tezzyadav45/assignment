import tkinter as tk

def click(btn):
    if btn == "=":
        try:
            result.set(eval(entry.get()))
        except:
            result.set("Error")
    elif btn == "C":
        result.set("")
    else:
        result.set(result.get() + btn)

# UI
root = tk.Tk()
root.title("Simple Calculator")

result = tk.StringVar()
entry = tk.Entry(root, textvariable=result, font=("Arial", 20), justify="right")
entry.grid(row=0, column=0, columnspan=4)

buttons = [
    "7","8","9","/",
    "4","5","6","*",
    "1","2","3","-",
    "0",".","C","+",
    "="
]

row, col = 1, 0
for b in buttons:
    action = lambda x=b: click(x)
    tk.Button(root, text=b, width=5, height=2, font=("Arial", 18), command=action)\
        .grid(row=row, column=col, sticky="nsew")
    col += 1
    if col > 3:
        col, row = 0, row + 1

root.mainloop()
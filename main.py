import tkinter as tk

def on_click(event):
  button=event.widget()
  current= entry.get()
  text= button ['text']
  
  if text== '=':
    try:
      result=eval(current)
      entry.delete(0,tk.END)
      entry.insert(tk.END, str(result))
    except Exception as e:
      entry.delete(0,tk.END)
      entry.insert(tk.END, "Error")
  elif text== 'C':
    entry.delete (0, tk.END)
  else:
    entry.insert(tk.END, text)

root=tk.Tk()
root.title("Simple calculator")

entry= tk.Entry(root, width=16,font=('Arial', 20))
entry.grid(row=0,column=0,columnspan=4)

buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', 'C', '+',
    '='
]

row = 1
col = 0
for button_text in buttons:
    
    button = tk.Button(root, text=button_text, width=4, font=('Arial', 20))
    button.grid(row=row, column=col)

    
    button.bind('<Button-1>', on_click)

    col += 1
    if col > 3:
        col = 0
        row += 1


root.mainloop()

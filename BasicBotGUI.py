import tkinter as tk
from tkinter import scrolledtext

root = tk.Tk()
root.title('Simple Chatbot')
root.geometry('500x615')
root.configure(bg = 'whitesmoke')

def getText(user_input):
    user_input = user_input.lower()
    if 'hello' in user_input:
        return 'Hello! How can I help you today?'
    elif 'how are you' in user_input:
        return "I am fine. How about you?"
    elif 'fine' in user_input:
        return 'Great to know that your fine. :)'
    elif 'why do we have fevers?' in user_input:
        return 'Our body heats ourselves up to fight the germs.'
    elif 'best suspense book' in user_input:
        return "A Good Girl's Guide to Murder"
    elif 'good morning' in user_input:
        return 'Good Morning. May you have a good day.'
    elif 'good night' in user_input:
        return 'Good night! Sleep well.'
    elif 'bye' in user_input:
        return 'Bye, night was a good conversation.'
    else:
        return "Sorry, I didn't understand."

def send():
    user_input = inputArea.get()
    text_area.config(state = tk.NORMAL)
    text_area.insert(tk.END, 'You: '+user_input+'\n')
    inputArea.delete(0,tk.END)
    response = getText(user_input)
    text_area.insert(tk.END, 'Bot: '+response+'\n\n')
    text_area.config(state = tk.DISABLED)
    text_area.yview(tk.END)
    
text_area = scrolledtext.ScrolledText(root, wrap = tk.WORD, width = 55, height = 27)
text_area.place(x = 25, y = 25)

inputArea = tk.Entry(root, width = 75)
inputArea.place(x = 25, y = 515)
inputButton = tk.Button(root, bg = 'blue', text = 'Enter', command = send)
inputButton.place(x = 250, y = 545)

root.bind('<Return>', lambda event: send())
root.mainloop()
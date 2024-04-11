import tkinter as tk

def count_words():
    text = text_entry.get()
    word_count = len(text.split())
    word_count_label.config(text="Word count: {}".format(word_count))

root = tk.Tk()
root.title("Word Counter")


root.configure(bg="lightgray")


root.geometry("500x500")

text_entry = tk.Entry(root, width=100)  
text_entry.pack()

count_button = tk.Button(root, text="Count Words", command=count_words)
count_button.pack()

word_count_label = tk.Label(root, text="Word count: ")
word_count_label.pack()

root.mainloop()


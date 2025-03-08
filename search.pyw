import tkinter as tk
import webbrowser

def search_google():
    query = search_box.get()
    if query:
        url = f"https://www.google.com/search?q={query}"
        webbrowser.open(url)

root = tk.Tk()
root.title("NeT Search Bar")
root.geometry('400x50+1000+0')
root.configure(bg='lightblue')

search_box = tk.Entry(root, width=30)
search_box.pack(side="left", padx=5)

search_button = tk.Button(root, text="Search", command=search_google)
search_button.pack(side="left", padx=5)

root.mainloop()

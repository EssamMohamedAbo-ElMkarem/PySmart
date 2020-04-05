
def new():
    Application()


def display_answer():
    pass


def contact_us():
    pass


def about():
    tkinter.messagebox.showinfo("About", "This script has been written by EssamMohamed")


Answer = ""


class Menu(object):

    def __init__(self, general_root):
        self.menu = tkinter.Menu(general_root)
        self.file_menu = tkinter.Menu(self.menu, tearoff=0)
        self.file_menu.add_command(label="New", command=new)
        self.file_menu.add_command(label="Exit", command=general_root.destroy)
        self.menu.add_cascade(label="File", menu=self.file_menu)
        self.help = tkinter.Menu(self.menu, tearoff=0)
        self.help.add_command(label="ContactUs", command=contact_us)
        self.help.add_command(label="About", command=about)
        self.menu.add_cascade(label="Help", menu=self.help)


class Application(object):

    def __init__(self):
        # This is the main window
        self.root = tkinter.Tk()
        self.root.title("SmartPy")
        self.root.maxsize(500, 150)
        self.root.minsize(500, 150)
        # This is the menu bar
        menu = Menu(general_root=self.root)
        self.root.configure(menu=menu)
        # This is the interactive part of SmartPy
        self.welcome = tkinter.Label(self.root, fg="darkred", text="Welcome to SmartPy...", )
        self.welcome.pack(padx=5, pady=5)
        self.accepting = tkinter.Label(self.root, fg="darkgreen", text="AskMe...")
        self.accepting.pack(padx=5, pady=5)
        self.input = tkinter.Entry(self.root, relief="flat", width=80)
        self.input.pack()
        self.submit = tkinter.Button(self.root, text="SubmitQuestion", fg="white", relief="flat", bg="royalblue")
        self.submit["command"] = self.send_query
        self.submit.pack(pady=10)
        self.root.mainloop()

    def send_query(self):
        coming_input = str(self.input.get())
        try:
            client = wolframalpha.Client("id")
            res = client.query(coming_input)
            for pod in res.pods:
                print('{p.title}: {p.text}'.format(p=pod))
        except():
            try:
                ans = wikipedia.summary(coming_input)
                ans = "  ".join(ans.split("  "))
                print(ans)
            except():
                print("Sorry,But I don't know")

                
class AnswerClass(object):
    def __init__(self):
        # This is the main window
        self.root = tkinter.Tk()
        self.root.title = "Answer"
        self.root.maxsize(500, 150)
        self.root.minsize(500, 150)
        # This is the menu bar
        menu = Menu(general_root=self.root)
        self.root.configure(menu=menu)
        # This is the interactive part of SmartPy


if __name__ == "__main__":
    import wolframalpha
    import wikipedia
    import tkinter
    import tkinter.messagebox
    app = Application()

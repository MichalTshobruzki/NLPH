from tkinter import *

def start_gui():
    input_text=None
    root = Tk()
    root.geometry("500x450")
    root.title(" Automated Summarization ")


    def take_input():
        input_text = input_txt.get("1.0", "end-1c")
        print(input_text)


    l1 = Label(text="enter the text you want to preprocessing")
    input_txt = Text(root, height=10, width=55, bg="light yellow")
    l2 = Label(text="the text after preprocessing")
    Output = Text(root, height=10, width=55, bg="light cyan")

    start_pipeline_button = Button(root, height=2, width=20, text="Start Pipeline", command=lambda: take_input())

    l1.pack()
    input_txt.pack()
    start_pipeline_button.pack()
    l2.pack()
    Output.pack()
    root.quit()

    mainloop()
    return str(input_text)


start_gui()
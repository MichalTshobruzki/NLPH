from tkinter import *
import main

def start_gui():
    input_text = None
    root = Tk()
    root.geometry("500x450")
    root.title(" Automated Summarization ")

    def take_input():
        #input_text = input_txt.get("1.0", "end")
        #main(str(input_text.get()))
        text_label = Label(root, text="The text is: " + input_txt.get())
        text_label.pack()
        print(input_txt)
        print(str(input_txt))
        main.preprocessing(input_txt.get())

    l1 = Label(text="enter the text you want to preprocessing")
    # input_txt = Text(root, height=10, width=55, bg="light yellow")
    input_txt = Entry(root, bd=5)
    # l2 = Label(text="the text after preprocessing")
    # Output = Text(root, height=10, width=55, bg="light cyan")

    start_pipeline_button = Button(root, height=2, width=20, text="Start Pipeline", command=lambda: take_input())

    l1.pack()
    input_txt.pack()
    start_pipeline_button.pack()
    #l2.pack()
    #Output.pack()
    root.quit()

    root.mainloop()
    return str(input_text)


start_gui()
import requests
import json
import pandas as pd
import os
from tkinter import *
import GUI

TOKENIZED = 'tokenized_text'
SEGMENTED = 'segmented_text'
LEMMAS = 'lemmas'
DEPENDENCY_TREE = 'dep_tree'
MA_LATTICE = 'ma_lattice'
MD_LATTICE = 'md_lattice'


#text = GUI.start_gui()
#print(type(text))
#print(text)
# text = "בתוך עיניה הכחולות"
# Escape double quotes in JSON.


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
        input_text = input_txt.get()
        preprocessing(input_txt.get())

    l1 = Label(text="enter the text you want to preprocessing")
    # input_txt = Text(root, height=10, width=55, bg="light yellow")
    input_txt = Entry(root, bd=5)

    start_pipeline_button = Button(root, height=2, width=20, text="Start Pipeline", command=lambda: take_input())

    l1.pack()
    input_txt.pack()
    start_pipeline_button.pack()
    root.quit()

    root.mainloop()
    #return str(input_text)








def preprocessing(text):
    text = text.replace(r'"', r'\"')
    url = 'https://www.langndata.com/api/heb_parser?token=84bca6503e3bb5fd85727a9f926fe4ef'
    _json = '{"data":"' + text + '"}'
    headers = {'content-type': 'application/json'}
    r = requests.post(url, data=_json.encode('utf-8'), headers={'Content-type': 'application/json; charset=utf-8'})
    json_object = r.json()

    json_formatted_str = json.dumps(json_object, indent=2, ensure_ascii=False)
    # print(json_formatted_str)
    dict_from_json = json.loads(json_formatted_str) # the website return the tags
    create_csv(dict_from_json)

def create_dataframe_with_head_row(row):  # head_row = the first row that contain all the column names:
    df = pd.DataFrame(columns=row.keys())

    return df


def load_data_from_json_to_df(df, data):
    for key, value in data.items():
        df = df.append(value, ignore_index=True)

    return df


if os.path.exists("output_file.csv"):
    print("exists")
    os.remove("output_file.csv")

def create_csv(dict_from_json):
    dep_tree_df = create_dataframe_with_head_row(dict_from_json[DEPENDENCY_TREE]['0'])
    ma_lattice = create_dataframe_with_head_row(dict_from_json[MA_LATTICE]['0'])
    md_lattice = create_dataframe_with_head_row(dict_from_json[MD_LATTICE]['0'])

    dep_tree_df = load_data_from_json_to_df(dep_tree_df, dict_from_json[DEPENDENCY_TREE])
    ma_lattice = load_data_from_json_to_df(ma_lattice, dict_from_json[MA_LATTICE])
    md_lattice = load_data_from_json_to_df(md_lattice, dict_from_json[MD_LATTICE])

    dep_tree_df.to_csv('output_file.csv',encoding='utf-8-sig', mode='a')
    ma_lattice.to_csv('output_file.csv',encoding='utf-8-sig', mode='a')
    md_lattice.to_csv("output_file.csv",encoding='utf-8-sig',mode='a')

start_gui()
import tkinter
from tkinter import messagebox
from datetime import datetime
import sqlite3


def submit_data():
    date = date_entry.get()
    weight = weight_entry.get()
    fat = fat_entry.get()
    sugar = sugar_entry.get()
    pulse = pulse_entry.get()
    bp = bp_entry.get()

    if date == current_date:
        print(date, weight, fat, sugar, pulse, bp)

        submitted_vitals = [weight, fat, sugar, pulse, bp]
        blank_value = 0
        for v in submitted_vitals:
            if v == '0':
                blank_value += 1
            print(blank_value)

        if blank_value > 0:
            messagebox.showerror('Blank value detected', 'Please fill in form completely')
            return
        elif blank_value == 0:
            messagebox.showinfo('Success!', 'Your data has been recorded.')
    else:
        messagebox.showerror('Error', 'You entered a date that is not today\'s date. '
                                      'To update a previous entry please use "Update".')
    conn = sqlite3.connect('data.db')
    table_create_query = '''CREATE TABLE IF NOT EXISTS vitals_db (date TEXT, weight TEXT, fat TEXT,
     sugar TEXT, pulse TEXT, bp TEXT)'''
    conn.execute(table_create_query)

    data_insert_query = '''INSERT INTO vitals_db (date, weight, fat, sugar, pulse, bp) VALUES (?, ?, ?, ?, ?, ?)'''
    data_insert_tuple = (date, weight, fat, sugar, pulse, bp)
    cursor = conn.cursor()
    cursor.execute(data_insert_query, data_insert_tuple)
    conn.commit()
    conn.close()


if __name__ == '__main__':
    window = tkinter.Tk()
    window.title('Daily Vital Tracking')
    window.geometry('600x400')
    frame = tkinter.Frame(window)
    frame.pack()

    current_date = datetime.today().strftime('%m/%d/%Y')

    vitals_frame = tkinter.LabelFrame(frame)
    vitals_frame.grid(rows=5, column=3)

    top_banner = tkinter.Label(vitals_frame, text='Please enter your Vitals for today')
    top_banner.grid(row=1, column=3, pady=10)
    top_banner.config(font=24)

    date_frame = tkinter.Label(vitals_frame, text='Date')
    date_frame.grid(row=2, column=3)
    date_entry = tkinter.Entry(vitals_frame, width=10)
    date_entry.grid(row=3, column=3, pady=(0, 5))
    date_entry.insert(0, current_date)

    weight_frame = tkinter.Label(vitals_frame, text='Weight')
    weight_frame.grid(row=4, column=2)
    weight_entry = tkinter.Entry(vitals_frame, width=18)
    weight_entry.grid(row=5, column=2, padx=5, pady=(0, 5))
    weight_entry.insert(0, '0')

    fat_frame = tkinter.Label(vitals_frame, text='Body Fat')
    fat_frame.grid(row=4, column=4)
    fat_entry = tkinter.Entry(vitals_frame,)
    fat_entry.grid(row=5, column=4, padx=5, pady=(0, 5))
    fat_entry.insert(0, '0')

    sugar_frame = tkinter.Label(vitals_frame, text='Blood Sugar')
    sugar_frame.grid(row=6, column=3)
    sugar_entry = tkinter.Entry(vitals_frame,)
    sugar_entry.grid(row=7, column=3, padx=5, pady=(0, 5))
    sugar_entry.insert(0, '0')

    pulse_frame = tkinter.Label(vitals_frame, text='Pulse')
    pulse_frame.grid(row=8, column=2)
    pulse_entry = tkinter.Entry(vitals_frame,)
    pulse_entry.grid(row=9, column=2, padx=5, pady=(0, 5))
    pulse_entry.insert(0, '0')

    bp_frame = tkinter.Label(vitals_frame, text='Blood Pressure')
    bp_frame.grid(row=8, column=4)
    bp_entry = tkinter.Entry(vitals_frame,)
    bp_entry.grid(row=9, column=4, padx=5, pady=(0, 5))
    bp_entry.insert(0, '0')

    submit = tkinter.Button(window, text='SUBMIT', bg='#a9a9a9', command=submit_data)
    submit.config(font=48)
    submit.pack(pady=30)

    update = tkinter.Button(window, text='UPDATE', bg='#a9a9a9')
    update.config(font=48)
    update.pack()

    window.mainloop()

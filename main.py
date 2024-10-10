import tkinter
from tkinter import messagebox
from tkinter import ttk
from datetime import datetime
import sqlite3


def add_item_table():
    date = view_vitals_date_selection.get()
    conn = sqlite3.connect('data.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM vitals_db WHERE date = '" + date + "'")
    data = cursor.fetchall()
    for item in data:
        table.insert('', 'end', text=item[0], values=item[1:])
    conn.close()


def add_multi_item_table():
    date = view_vitals_date_selection.get()
    date_range = range_date_selection.get()
    conn = sqlite3.connect('data.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM vitals_db WHERE date BETWEEN '" + date + "' and '" + date_range +
                   "' ORDER by date")
    data = cursor.fetchall()
    for item in data:
        table.insert('', 'end', text=item[0], values=item[1:])
    conn.close()


def clear_table():
    for item in table.get_children():
        table.delete(item)


def submit_data():
    date = date_entry.get()
    weight = weight_entry.get()
    fat = fat_entry.get()
    sugar = sugar_entry.get()
    pulse = pulse_entry.get()
    bp = bp_entry.get()

    if date == current_date:
        conn = sqlite3.connect('data.db')
        cursor = conn.cursor()
        cursor.execute(f"SELECT exists(SELECT 1 FROM vitals_db WHERE date = '" + date + "') AS row_exists;")
        row_exists = cursor.fetchone()

        if 1 in row_exists:
            messagebox.showerror('Error', 'You have already entered your vitals for today. If you would like to '
                                          'update today\'s vitals pleas use "UPDATE" instead.')
            return
        else:
            submitted_vitals = [weight, fat, sugar, pulse, bp]
            blank_value = 0
            for v in submitted_vitals:
                if v == '0':
                    blank_value += 1
            if blank_value == 0:
                conn = sqlite3.connect('data.db')
                table_create_query = '''CREATE TABLE IF NOT EXISTS vitals_db (date TEXT, weight TEXT, fat TEXT,
                     sugar TEXT, pulse TEXT, bp TEXT)'''
                conn.execute(table_create_query)

                data_insert_query = '''INSERT INTO vitals_db (date, weight, fat, sugar, pulse, bp)
                 VALUES (?, ?, ?, ?, ?, ?)'''
                data_insert_tuple = (date, weight, fat, sugar, pulse, bp)
                cursor = conn.cursor()
                cursor.execute(data_insert_query, data_insert_tuple)
                conn.commit()
                conn.close()

                messagebox.showinfo('Success!', 'Your data has been recorded.')

            if blank_value > 0:
                messagebox.showerror('Blank value detected', 'Please fill in form completely')
                return

    else:
        messagebox.showerror('Error', 'You entered a date that is not today\'s date. '
                                      'To update a previous entry please use "Update" instead.')


def update_data():
    date = date_entry.get()
    weight = weight_entry.get()
    fat = fat_entry.get()
    sugar = sugar_entry.get()
    pulse = pulse_entry.get()
    bp = bp_entry.get()

    conn = sqlite3.connect('data.db')
    cursor = conn.cursor()
    cursor.execute(f"SELECT exists(SELECT 1 FROM vitals_db WHERE date = '" + date + "') AS row_exists;")
    row_exists = cursor.fetchone()

    if 1 in row_exists:
        submitted_vitals = [weight, fat, sugar, pulse, bp]
        blank_value = 0
        for v in submitted_vitals:
            if v == '0':
                blank_value += 1
        if blank_value == 0:
            conn = sqlite3.connect('data.db')
            table_create_query = '''CREATE TABLE IF NOT EXISTS vitals_db (date TEXT, weight TEXT, fat TEXT,
                             sugar TEXT, pulse TEXT, bp TEXT)'''
            conn.execute(table_create_query)

            data_insert_query = '''INSERT INTO vitals_db (date, weight, fat, sugar, pulse, bp)
                         VALUES (?, ?, ?, ?, ?, ?)'''
            data_insert_tuple = (date, weight, fat, sugar, pulse, bp)
            delete_stmt = (f'delete FROM vitals_db where date = "' + date + '"')
            cursor = conn.cursor()
            cursor.execute(delete_stmt)
            cursor.execute(data_insert_query, data_insert_tuple)
            conn.commit()
            conn.close()

            messagebox.showinfo('Success!', 'Your data has been recorded.')

        if blank_value > 0:
            messagebox.showerror('Blank value detected', 'Please fill in form completely')
            return

    else:
        submitted_vitals = [weight, fat, sugar, pulse, bp]
        blank_value = 0
        for v in submitted_vitals:
            if v == '0':
                blank_value += 1
        if blank_value == 0:
            conn = sqlite3.connect('data.db')
            table_create_query = '''CREATE TABLE IF NOT EXISTS vitals_db (date TEXT, weight TEXT, fat TEXT,
                                     sugar TEXT, pulse TEXT, bp TEXT)'''
            conn.execute(table_create_query)

            data_insert_query = '''INSERT INTO vitals_db (date, weight, fat, sugar, pulse, bp)
                                 VALUES (?, ?, ?, ?, ?, ?)'''
            data_insert_tuple = (date, weight, fat, sugar, pulse, bp)
            cursor = conn.cursor()
            cursor.execute(data_insert_query, data_insert_tuple)
            conn.commit()
            conn.close()

            messagebox.showinfo('Success!', 'Your data has been recorded.')

        if blank_value > 0:
            messagebox.showerror('Blank value detected', 'Please fill in form completely')
            return

    conn.close()


if __name__ == '__main__':
    window = tkinter.Tk()
    window.title('Daily Vital Tracking')
    window.geometry('600x600')

    current_date = datetime.today().strftime('%m/%d/%Y')

    notebook = ttk.Notebook(window)

    input_tab = ttk.Frame(notebook)
    input_tab_label = tkinter.Label(input_tab)
    input_tab_label.pack()

    view_vitals_tab = ttk.Frame(notebook)
    view_vitals_tab_label = tkinter.Label(view_vitals_tab)
    view_vitals_tab_label.pack()

    notebook.add(input_tab, text='Input Vitals')
    notebook.add(view_vitals_tab, text='View Vitals')
    notebook.pack()

    vitals_frame = tkinter.LabelFrame(input_tab)
    vitals_frame.pack()

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

    submit = tkinter.Button(vitals_frame, text='SUBMIT', bg='#a9a9a9', command=submit_data)
    submit.config(font=48)
    submit.grid(row=11, column=3, pady=(25, 0))

    update = tkinter.Button(vitals_frame, text='UPDATE', bg='#a9a9a9', command=update_data)
    update.config(font=48)
    update.grid(row=13, column=3, pady=10)

    view_vitals_frame = tkinter.LabelFrame(view_vitals_tab)
    view_vitals_frame.pack()

    view_vitals_select_label = tkinter.Label(view_vitals_frame, text='Single date')
    view_vitals_select_label.grid(row=1, column=0,)
    view_vitals_date_selection = tkinter.Entry(view_vitals_frame, width=10)
    view_vitals_date_selection.grid(row=2, column=0, pady=(10, 0))
    view_vitals_date_selection.insert(0, current_date)

    range_select_label = tkinter.Label(view_vitals_frame, text='Date range')
    range_select_label.grid(row=1, column=1, )
    range_date_selection = tkinter.Entry(view_vitals_frame, width=10)
    range_date_selection.grid(row=2, column=1, pady=(10, 0))
    range_date_selection.insert(0, current_date)

    view_vitals_label_button = tkinter.Button(view_vitals_frame, text='Single Date', bg='#a9a9a9',
                                              command=add_item_table)
    view_vitals_label_button.grid(row=3, column=0, padx=(10, 0), pady=10)

    range_view_vitals_label_button = tkinter.Button(view_vitals_frame, text='Multiple Dates', bg='#a9a9a9',
                                                    command=add_multi_item_table)
    range_view_vitals_label_button.grid(row=3, column=1, padx=10, pady=10)

    clear_table_button = tkinter.Button(view_vitals_frame, text='CLEAR', bg='#a9a9a9', command=clear_table)
    clear_table_button.grid(row=3, column=2, padx=(0, 10))

    table = ttk.Treeview(view_vitals_tab_label, height=20)
    table['columns'] = ('Weight', 'Fat %', 'Sugar', 'Pulse', 'Blood Pressure')
    table.column('#0', anchor='center', width=85)
    table.heading('#0', anchor='center', text='Date')
    table.column('#1', anchor='center', width=50)
    table.heading('#1', anchor='center', text='Weight')
    table.column('#2', anchor='center', width=50)
    table.heading('#2', anchor='center', text='Fat %')
    table.column('#3', anchor='center', width=50)
    table.heading('#3', anchor='center', text='Sugar')
    table.column('#4', anchor='center', width=50)
    table.heading('#4', anchor='center', text='Pulse')
    table.column('#5', anchor='center', width=100)
    table.heading('#5', anchor='center', text='Blood Pressure')
    table.pack()

    window.mainloop()

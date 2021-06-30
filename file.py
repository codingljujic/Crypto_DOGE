from tkinter import *
from tkinter.ttk import *
from tkcalendar import DateEntry
from datetime import date
import numpy as np
import pandas as pd

# Create a centered window
window = Tk()
window.title("Dogellionaire app")
doge_width = 790
doge_height = 450

screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
x = (screen_width / 2) - (doge_width / 2)
y = (screen_height / 2) - (doge_height / 2)

window.geometry(f'{doge_width}x{doge_height}+{int(x)}+{int(y)}')

# Add BG image
bg = PhotoImage(file="Pics/stonks.png")
canvas1 = Canvas(window, width=790, height=450)
canvas1.pack(fill="both")

# Display BG image
canvas1.create_image(0, 0, image=bg, anchor="nw")

# Add dogecoin image
doge = PhotoImage(file="Pics/dogecoin.png")
canvas1.create_image(690, 00, image=doge, anchor="nw")


# Second window with results
def second_window():
    # Create second window center positioned
    window2 = Toplevel()
    app_width = 500
    app_height = 250
    pc_screen_width = window2.winfo_screenwidth()
    pc_screen_height = window2.winfo_screenheight()
    xw = (pc_screen_width / 2) - (app_width / 2)
    yh = (pc_screen_height / 2) - (app_height / 2)
    window2.geometry(f'{app_width}x{app_height}+{int(xw)}+{int(yh)}')

    # Add BG image to second window
    doge_img = PhotoImage(file="Pics/Doge_back2.png")
    my_label = Label(window2, image=doge_img)

    # Displaying all result and button to return back
    result = Label(window2, text="On the: " + calendar_fct(), background="#FEDDBA")
    result2 = Label(window2, text="You invested: " + ("{:,}".format(int(spin_fct()))) + " USD", background="#FEDDBA")
    result3 = Label(window2, text="In: " + combo_fct(), background="#FEDDBA")
    result4 = Label(window2, text="You bought: " + ("{:,}".format(round(coins_bought()))) + " coins that day.",
                    background="#FEDDBA")
    result5 = Label(window2, text="On 20-04-21 :) your stake is worth around: " + (
        "{:,}".format(round(coins_pot_day()))) + " USD", background="#FEDDBA")
    result6 = Label(window2, text="During that period your " + str(gain_loss()), background="#FEDDBA")
    result7 = Label(window2, text="The same day you bought " + str(combo_fct()) + ", you could have bought: " + (
        "{:,}".format(round(doge_bought()))) + " Dogecoins.", background="#FEDDBA")
    result8 = Label(window2, text="On 20-04-21 :) your stake in Dogecoin would be worth around: " + (
        "{:,}".format(round(doge_pot_day()))) + " USD", background="#FEDDBA")
    result9 = Label(window2, text=check_if(), background="#FEDDBA")
    btn2 = Button(window2, text="Try again!", command=window2.destroy)
    btn2.grid(column=0, row=22)
    my_label.place(x=0, y=0, relwidth=1, relheight=1)
    result.grid(column=0, row=0)
    result2.grid(column=0, row=3)
    result3.grid(column=0, row=5)
    result4.grid(column=0, row=8)
    result5.grid(column=0, row=9)
    result6.grid(column=0, row=10)
    result7.grid(column=0, row=14)
    result8.grid(column=0, row=18)
    result9.grid(column=0, row=20)
    window2.mainloop()


# Button projecting the second window
btn = Button(window, text="Travel in time!", command=second_window)
canvas1.create_window(345, 250, anchor="nw", window=btn)

# Create title and texts
canvas1.create_text(400, 35, text="Dogellionaire", font="Arial 30 bold", fill="White")
canvas1.create_text(400, 70, text="Imagine if you invested...", font="Arial 15 bold", fill="White")
canvas1.create_text(450, 100, text="USD", font="Arial 15 bold", fill="White")
canvas1.create_text(510, 100, text="(max 1B USD)", font="Arial 7 italic bold ", fill="White")
canvas1.create_text(390, 125, text="in", font="Arial 15 bold", fill="White")
canvas1.create_text(390, 180, text="back in", font="Arial 15 bold", fill="White")
canvas1.create_text(495, 180, text="(5 years max", font="Arial 7 italic ", fill="White")
canvas1.create_text(495, 190, text="*Binance: max 25-07-17", font="Arial 7 italic bold ", fill="White")
canvas1.create_text(495, 200, text="*Tron: max 13-09-17", font="Arial 7 italic bold ", fill="White")
canvas1.create_text(495, 210, text="*Cardano: max 01-10-17)", font="Arial 7 italic bold ", fill="White")

# Create spinbox for amount of USD invested
spin = Spinbox(window, from_=0, to=1000000000, width=10)
canvas1.create_window(390, 100, window=spin)

# Create combobox with options of currencies
data = ("Bitcoin", "Ethereum", "Litecoin", "Ripple", "Tether", "Binance", "Tron", "Cardano")
combo = Combobox(values=data)
canvas1.create_window(390, 150, window=combo)

# Create calendar with set minimum and maximum dates.
calendar = DateEntry(date_pattern='dd-mm-yy', mindate=date(2016, 4, 20), maxdate=date(2021, 4, 19))
canvas1.create_window(390, 210, window=calendar)


# Functions

# Dollars invested
def spin_fct():
    spinbox_value = spin.get()
    return str(spinbox_value)


# Currency chosen
def combo_fct():
    combo_value = combo.get()
    return str(combo_value)


# Calendar date
def calendar_fct():
    calendar_value = calendar.get()
    return str(calendar_value)


# Number of coins bought at a given date
def coins_bought():
    df = pd.read_csv("CSV/All_top_coins-updated-21.csv")
    a = spin.get()
    b = combo.get()
    c = calendar.get()
    row = df[df['Currency'].str.contains(b) & df['Date'].str.contains(c)]
    result = row.iloc[0, 5]
    val = np.float32(result)
    py_val = val.item()
    d = int(a) / py_val
    return d


# Value of coins worth at 4/20
def coins_pot_day():
    result_bought = coins_bought()
    df = pd.read_csv("CSV/All_top_coins-updated-21.csv")
    b = combo.get()
    row = df[df['Currency'].str.contains(b) & df['Date'].str.contains('20-04-21')]
    result = row.iloc[0, 5]
    val = np.float32(result)
    py_val = val.item()
    d = result_bought * py_val
    return d


# Gain or loss of investment
def gain_loss():
    result_today = coins_pot_day()
    a = spin.get()
    result = (100 * ((result_today - int(a)) / int(a)))
    if result > 0:
        return "investment grew by: " + str(round(result)) + " %"
    else:
        return "investment dropped by: " + str(round(result)) + " %"


# Doge coins bought the same day as chosen by user
def doge_bought():
    df = pd.read_csv("CSV/Doge_coin.csv")
    a = spin.get()
    c = calendar.get()
    row = df[df['Date'].str.contains(c)]
    result = row.iloc[0, 5]
    val = np.float32(result)
    py_val = val.item()
    d = int(a) / py_val
    return d


# Value of Dogecoin at 4/20
def doge_pot_day():
    df = pd.read_csv("CSV/Doge_coin.csv")
    a = spin.get()
    result_today = doge_bought()
    row = df[df['Date'].str.contains('20-04-21')]
    result = row.iloc[0, 5]
    val = np.float32(result)
    py_val = val.item()
    d = result_today * py_val
    return d


# Checks if Doge value on 4/20 > Currency value on 4/20
def check_if():
    a = doge_pot_day()
    b = coins_pot_day()
    if a > b:
        return "Be smart, invest in Dogecoin!"
    else:
        return "You are smart, Dogecoin didn't perform well during this period..."


window.mainloop()

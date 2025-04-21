
# libraries Import
from tkinter import *
import customtkinter
import sys

# Main Window Properties

window = Tk()
window.title("ERLC")
window.geometry("800x350")
window.configure(bg="#585555")

# Handle window close event
def on_closing():
    window.destroy()
    sys.exit()

window.protocol("WM_DELETE_WINDOW", on_closing)


def on_calculate_cash_click():
    price_input = Entry_id3.get()
    output = calculate_percentage(price_input)
    if output is not None:
        Label_id8.configure(text=f"Price: {output}")
    else:
        Label_id8.configure(text="Invalid Input")

Button_id1 = customtkinter.CTkButton(
    master=window,
    text="Calculate Cash",
    font=("undefined", 14),
    text_color="#000000",
    hover=True,
    hover_color="#949494",
    height=30,
    width=95,
    border_width=2,
    corner_radius=6,
    border_color="#000000",
    bg_color="#585555",
    fg_color="#F0F0F0",
    command=on_calculate_cash_click
)
Button_id1.place(x=560, y=60)
Label_id9 = customtkinter.CTkLabel(
    master=window,
    text="    ",
    font=("Arial", 14),
    text_color="#000000",
    height=26,
    width=95,
    corner_radius=20,
    bg_color="#585555",
    fg_color="#ffffff",
    )
Label_id9.place(x=680, y=190)
Entry_id3 = customtkinter.CTkEntry(
    master=window,
    placeholder_text="Input Here Price",
    placeholder_text_color="#454545",
    font=("Arial", 14),
    text_color="#000000",
    height=30,
    width=400,
    border_width=2,
    corner_radius=6,
    border_color="#000000",
    bg_color="#585555",
    fg_color="#F0F0F0",
    )
Entry_id3.place(x=70, y=60)
Label_id5 = customtkinter.CTkLabel(
    master=window,
    text="Dealership",
    font=("Arial", 14),
    text_color="#ffffff",
    height=30,
    width=95,
    corner_radius=0,
    bg_color="#585555",
    fg_color="#585555",
    )
Label_id5.place(x=80, y=30)
Label_id10 = customtkinter.CTkLabel(
    master=window,
    text="Ver 0.0.5",
    font=("Courier New", 14),
    text_color="#000000",
    height=30,
    width=95,
    corner_radius=0,
    bg_color="#585555",
    fg_color="#585555",
    )
Label_id10.place(x=710, y=320)
Entry_id2 = customtkinter.CTkEntry(
    master=window,
    placeholder_text="Speed",
    placeholder_text_color="#454545",
    font=("Arial", 14),
    text_color="#000000",
    height=30,
    width=400,
    border_width=2,
    corner_radius=6,
    border_color="#000000",
    bg_color="#585555",
    fg_color="#F0F0F0",
    )
Entry_id2.place(x=70, y=180)
def on_calculate_speed_click():
    speed_input = Entry_id2.get()
    output = calculate_percentage(speed_input)
    if output is not None:
        Label_id9.configure(text=f"Speed: {output}")
    else:
        Label_id9.configure(text="Invalid Input")

Button_id4 = customtkinter.CTkButton(
    master=window,
    text="Calculate",
    font=("undefined", 14),
    text_color="#000000",
    hover=True,
    hover_color="#949494",
    height=36,
    width=95,
    border_width=2,
    corner_radius=6,
    border_color="#000000",
    bg_color="#585555",
    fg_color="#F0F0F0",
    command=on_calculate_speed_click
)
Button_id4.place(x=560, y=180)
Label_id8 = customtkinter.CTkLabel(
    master=window,
    text="    ",
    font=("Arial", 14),
    text_color="#000000",
    height=23,
    width=95,
    corner_radius=23,
    bg_color="#585555",
    fg_color="#ffffff",
    )
Label_id8.place(x=680, y=60)
Label_id6 = customtkinter.CTkLabel(
    master=window,
    text="Max Speed",
    font=("Arial", 14),
    text_color="#ffffff",
    height=30,
    width=95,
    corner_radius=0,
    bg_color="#585555",
    fg_color="#585555",
    )
Label_id6.place(x=80, y=150)

def calculate_percentage(price_str):
  try:
    # Remove commas before converting to float
    price = float(price_str.replace(",", ""))
    percentage = 0.6443
    result = price * percentage
    return "{:,.2f}".format(result)  # Format the result with commas and 2 decimal places
  except ValueError:
    return None

def calculate_percentage(speed_str):
  try:
    # Remove commas before converting to float
    speed = float(speed_str.replace(",", ""))
    percentage = 0.6323
    result = speed * percentage
    return "{:,.2f}".format(result)  # Format the result with commas and 2 decimal places
  except ValueError:
    return None
  
#run the main loop
window.mainloop()

#Dealership Cash Calculator
if __name__ == "__main__":
  while True:
    price_input = Entry_id3.get()
    output = calculate_percentage(price_input)
    if output is not None:
      print(f"The result of {price_input} multiplied by 64.43% is: {output}")
      print("You might be able to get more than this amount.")
      print("This is only the minimum amount you should expect.")
      break  # Exit the loop after successful input
    else:
      print("Invalid input. Please enter a valid number for the price.")

#Speed Calculator

if __name__ == "__main__":
  while True:
    speed_input = Entry_id2.get()
    output = calculate_percentage(speed_input)
    if output is not None:
      print(f"The result of {speed_input} multiplied by 61.46% is: {output}")
      break  # Exit the loop after successful input
    else:
      print("Invalid input. Please enter a valid number for the price.")
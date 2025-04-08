import math
import time

def calculate_percentage(speed_str):
  """Calculates 61.46% of a given speed string, respecting commas for thousands."""
  try:
    # Remove commas before converting to float
    speed = float(speed_str.replace(",", ""))
    percentage = 0.6323
    result = speed * percentage
    return "{:,.2f}".format(result)  # Format the result with commas and 2 decimal places
  except ValueError:
    return None

if __name__ == "__main__":
  while True:
    speed_input = input("Enter the speed (you can use commas for thousands): ")
    output = calculate_percentage(speed_input)
    if output is not None:
      print(f"The result of {speed_input} multiplied by 61.46% is: {output}")
      break  # Exit the loop after successful input
    else:
      print("Invalid input. Please enter a valid number for the price.")

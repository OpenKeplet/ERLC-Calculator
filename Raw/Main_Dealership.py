def calculate_percentage(price_str):
  """Calculates 61.46% of a given price string, respecting commas for thousands."""
  try:
    # Remove commas before converting to float
    price = float(price_str.replace(",", ""))
    percentage = 0.6443
    result = price * percentage
    return "{:,.2f}".format(result)  # Format the result with commas and 2 decimal places
  except ValueError:
    return None

if __name__ == "__main__":
  while True:
    price_input = input("Enter the price (you can use commas for thousands): ")
    output = calculate_percentage(price_input)
    if output is not None:
      print(f"The result of {price_input} multiplied by 64.43% is: {output}")
      print("You might be able to get more than this amount.")
      print("This is only the minimum amount you should expect.")
      break  # Exit the loop after successful input
    else:
      print("Invalid input. Please enter a valid number for the price.")

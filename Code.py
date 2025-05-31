# Importing necessary libraries
import time  # For timer functionality in order processing
import os    # For clearing the terminal screen
import random # For generating random bulletin entries and order numbers
# Bulletin board entries containing cafe announcements and events
bulletin = ["2074-01-01: Happy New Year! Welcome to 2074 - cafe reopens at noon!",
           "2074-01-05: New Year resolutions - healthy menu options highlighted!",
           "2074-01-10: January detox specials - green smoothies and salads!",
           "2074-01-15: Martin Luther King Jr. Day - community service appreciation!",
           "2074-01-20: Inauguration Day viewing party with political-themed snacks!",
           "2074-01-25: Burns Night celebration - Scottish space haggis special!",
           "2074-02-01: February love month - romantic dinner packages available!",
           "2074-02-05: Groundhog Day - shadow puppet shows for kids!",
           "2074-02-10: Chinese New Year - fortune cookie specials all week!",
           "2074-02-14: Valentine's Day 2074 - new couple's dessert menu!",
           "2074-02-17: Presidents Day - presidential favorite dishes featured!",
           "2074-02-22: Leap year preparation - extra day means extra specials!",
           "2074-03-01: Women's History Month - celebrating female astronauts!",
           "2074-03-05: Spring menu preview - fresh ingredients arriving!",
           "2074-03-10: Daylight Saving Time begins - extra morning energy drinks!",
           "2074-03-15: Ides of March - Caesar salad specials all day!",
           "2074-03-17: St. Patrick's Day 2074 - green space food galore!",
           "2074-03-20: Spring Equinox - balanced flavors, balanced prices!",
           "2074-03-25: Earth Hour participation - candlelit dining experience!",
           "2074-04-01: April Fools' 2074 - mystery menu items return!",
           "2074-04-05: Spring cleaning week - fresh start, fresh flavors!",
           "2074-04-10: Easter preparations - cosmic egg hunt planning!",
           "2074-04-15: Tax Day relief - free stress-busting smoothies!",
           "2074-04-20: Easter Sunday - bunny-shaped cosmic treats!",
           "2074-04-22: Earth Day 2074 - carbon-neutral delivery options!",
           "2074-04-30: April showers special - rainy day comfort food!",
           "2074-05-01: May Day celebration - flower power smoothies!",
           "2074-05-05: Cinco de Mayo 2074 - expanded Mexican space cuisine!",
           "2074-05-10: Mother's Day brunch - interstellar breakfast buffet!",
           "2074-05-15: Armed Forces Day - military appreciation discounts!",
           "2074-05-20: Victoria Day (Canada) - royal space tea service!",
           "2074-05-26: Memorial Day weekend - extended patriotic menu!",
           "2074-06-05: World Environment Day - eco-friendly packaging launch!",
           "2074-06-10: Flag Day preparations - red, white, blue desserts!",
           "2074-06-15: Father's Day 2074 - dad joke contest with prizes!",
           "2074-06-20: Summer Solstice - midnight sun celebration!",
           "2074-06-25: Mid-year inventory - introducing new space delicacies!",
           "2074-07-01: Canada Day - maple syrup space pancakes!",
           "2074-07-04: Independence Day 2074 - fireworks viewing area!",
           "2074-07-10: Summer camp partnerships - kid-friendly menu expansion!",
           "2074-07-15: Ice cream month - frozen treats festival!",
           "2074-07-20: Moon Day anniversary - lunar-themed everything!",
           "2074-07-25: Dog days of summer - pet cooling stations added!",
           "2074-08-01: Friendship Day - group dining discounts!",
           "2074-08-05: International Beer Day - cosmic brew tasting!",
           "2074-08-10: Meteor shower viewing party this weekend!",
           "2074-08-15: Back to school prep - student meal plans available!",
           "2074-08-20: Solar maximum - extra solar-powered menu items!",
           "2074-08-25: Late summer harvest - local space farmer partnerships!",
           "2074-09-01: Labor Day 2074 - worker appreciation week!",
           "2074-09-05: Back to school rush - study fuel combos!",
           "2074-09-10: Grandparents Day - vintage space recipes featured!",
           "2074-09-15: International Day of Democracy - voting on new menu items!",
           "2074-09-20: Autumn Equinox - seasonal menu transition!",
           "2074-09-25: World Tourism Day - dishes from across the galaxy!",
           "2074-10-01: October fest 2074 - Germanic space cuisine returns!",
           "2074-10-05: World Teachers' Day - educator discounts!",
           "2074-10-10: Indigenous Peoples' Day - native space plant ingredients!",
           "2074-10-15: Halloween month begins - spooky atmosphere incoming!",
           "2074-10-20: International Chefs Day - guest chef collaborations!",
           "2074-10-25: Pre-Halloween celebrations - costume contest prep!",
           "2074-10-31: Halloween 2074 - midnight monster menu!",
           "2074-11-01: Day of the Dead - colorful celebration cuisine!",
           "2074-11-05: Guy Fawkes Night - bonfire-themed hot drinks!",
           "2074-11-10: Veterans Day 2074 - expanded military appreciation!",
           "2074-11-15: Thanksgiving preparations - space turkey pre-orders!",
           "2074-11-20: World Children's Day - kid-friendly cosmic creations!",
           "2074-11-27: Thanksgiving 2074 - gratitude feast packages!",
           "2074-11-28: Black Friday 2074 - biggest discounts of the year!",
           "2074-12-01: Holiday season kickoff - festive decorations up!",
           "2074-12-05: St. Nicholas Day - gift card specials!",
           "2074-12-10: Human Rights Day - unity-themed menu items!",
           "2074-12-15: Holiday party bookings - group celebration packages!",
           "2074-12-20: Winter Solstice - longest night, warmest atmosphere!",
           "2074-12-24: Christmas Eve 2074 - special family hours!",
           "2074-12-25: Christmas Day - closed for family time!",
           "2074-12-31: New Year's Eve party - countdown celebration!",
           "2075-01-01: Happy New Year! Welcome to 2075 - cafe reopens at noon!",
           "2075-01-05: New Year resolutions - healthy menu options highlighted!",
           "2075-01-10: January detox specials - green smoothies and salads!",
           "2075-01-15: Martin Luther King Jr. Day - community service appreciation!",
           "2075-01-20: Inauguration Day viewing party with political-themed snacks!",
           "2075-01-25: Burns Night celebration - Scottish space haggis special!",
           "2075-02-01: February love month - romantic dinner packages available!",
           "2075-02-05: Groundhog Day - shadow puppet shows for kids!",
           "2075-02-10: Chinese New Year - fortune cookie specials all week!",
           "2075-02-14: Valentine's Day 2075 - new couple's dessert menu!",
           "2075-02-17: Presidents Day - presidential favorite dishes featured!",
           "2075-02-22: Leap year preparation - extra day means extra specials!",
           "2075-03-01: Women's History Month - celebrating female astronauts!",
           "2075-03-05: Spring menu preview - fresh ingredients arriving!",
           "2075-03-10: Daylight Saving Time begins - extra morning energy drinks!",
           "2075-03-15: Ides of March - Caesar salad specials all day!",
           "2075-03-17: St. Patrick's Day 2075 - green space food galore!",
           "2075-03-20: Spring Equinox - balanced flavors, balanced prices!",
           "2075-03-25: Earth Hour participation - candlelit dining experience!",
           "2075-04-01: April Fools' 2075 - mystery menu items return!",
           "2075-04-05: Spring cleaning week - fresh start, fresh flavors!",
           "2075-04-10: Easter preparations - cosmic egg hunt planning!",
           "2075-04-15: Tax Day relief - free stress-busting smoothies!",
           "2075-04-20: Easter Sunday - bunny-shaped cosmic treats!",
           "2075-04-22: Earth Day 2075 - carbon-neutral delivery options!",
           "2075-04-30: April showers special - rainy day comfort food!",
           "2075-05-01: May Day celebration - flower power smoothies!",
           "2075-05-05: Cinco de Mayo 2075 - expanded Mexican space cuisine!",
           "2075-05-10: Mother's Day brunch - interstellar breakfast buffet!",
           "2075-05-15: Armed Forces Day - military appreciation discounts!",
           "2075-05-20: Victoria Day (Canada) - royal space tea service!",
           "2075-05-26: Memorial Day weekend - extended patriotic menu!",
           "2075-06-05: World Environment Day - eco-friendly packaging launch!",
           "2075-06-10: Flag Day preparations - red, white, blue desserts!",
           "2075-06-15: Father's Day 2075 - dad joke contest with prizes!",
           "2075-06-20: Summer Solstice - midnight sun celebration!",
           "2075-06-25: Mid-year inventory - introducing new space delicacies!",
           "2075-07-01: Canada Day - maple syrup space pancakes!",
           "2075-07-04: Independence Day 2075 - fireworks viewing area!",
           "2075-07-10: Summer camp partnerships - kid-friendly menu expansion!",
           "2075-07-15: Ice cream month - frozen treats festival!",
           "2075-07-20: Moon Day anniversary - lunar-themed everything!",
           "2075-07-25: Dog days of summer - pet cooling stations added!",
           "2075-08-01: Friendship Day - group dining discounts!",
           "2075-08-05: International Beer Day - cosmic brew tasting!",
           "2075-08-10: Meteor shower viewing party this weekend!",
           "2075-08-15: Back to school prep - student meal plans available!",
           "2075-08-20: Solar maximum - extra solar-powered menu items!",
           "2075-08-25: Late summer harvest - local space farmer partnerships!",
           "2075-09-01: Labor Day 2075 - worker appreciation week!",
           "2075-09-05: Back to school rush - study fuel combos!",
           "2075-09-10: Grandparents Day - vintage space recipes featured!",
           "2075-09-15: International Day of Democracy - voting on new menu items!",
           "2075-09-20: Autumn Equinox - seasonal menu transition!",
           "2075-09-25: World Tourism Day - dishes from across the galaxy!",
           "2075-10-01: October fest 2075 - Germanic space cuisine returns!",
           "2075-10-05: World Teachers' Day - educator discounts!",
           "2075-10-10: Indigenous Peoples' Day - native space plant ingredients!",
           "2075-10-15: Halloween month begins - spooky atmosphere incoming!",
           "2075-10-20: International Chefs Day - guest chef collaborations!",
           "2075-10-25: Pre-Halloween celebrations - costume contest prep!",
           "2075-10-31: Halloween 2075 - midnight monster menu!",
           "2075-11-01: Day of the Dead - colorful celebration cuisine!",
           "2075-11-05: Guy Fawkes Night - bonfire-themed hot drinks!",
           "2075-11-10: Veterans Day 2075 - expanded military appreciation!",
           "2075-11-15: Thanksgiving preparations - space turkey pre-orders!",
           "2075-11-20: World Children's Day - kid-friendly cosmic creations!",
           "2075-11-27: Thanksgiving 2075 - gratitude feast packages!",
           "2075-11-28: Black Friday 2075 - biggest discounts of the year!",
           "2075-12-01: Holiday season kickoff - festive decorations up!",
           "2075-12-05: St. Nicholas Day - gift card specials!",
           "2075-12-10: Human Rights Day - unity-themed menu items!",
           "2075-12-15: Holiday party bookings - group celebration packages!",
           "2075-12-20: Winter Solstice - longest night, warmest atmosphere!",
           "2075-12-24: Christmas Eve 2075 - special family hours!",
           "2075-12-25: Christmas Day - closed for family time!",
           "2075-12-31: New Year's Eve 2075 - monument transition celebration!"]

# List to store customer suggestions for the bulletin board
bulletin_suggestions = []

# Menu dictionary containing categories and items with prices
menu = {
  "Drinks": {
    "Coke": 2.50, "Pepsi": 2.50, "Sprite": 2.50, "Cosmic Cola": 4.99, 
    "Nebula Nectar": 6.75, "Red Planet Punch": 5.25, "Martian Mist": 7.50, 
    "Galactic Green Tea": 4.25, "Asteroid Ale": 8.99, "Crater Coffee": 3.75, 
    "Solar Smoothie": 6.50, "Meteorite Mocha": 5.99, "Jupiter Juice": 5.75, 
    "Saturn Soda": 4.99, "Alien Elixir": 12.99, "Space Sparkler": 3.99, 
    "Lunar Lemonade": 4.50, "Zero-G Zinger": 9.25
  },
  "Food": {
    "Pizza": 12.99, "Burger": 10.50, "Fries": 4.99, "Martian Meatballs": 14.75, 
    "Galactic Grilled Cheese": 8.99, "Nebula Nachos": 11.50, "Space Station Sandwich": 13.25, 
    "Asteroid Appetizers": 9.75, "Cosmic Curry": 15.99, "Red Planet Ribs": 18.50, 
    "Saturn Ring Soup": 7.99, "Lunar Lasagna": 16.25, "Alien Alfredo": 14.99, 
    "Meteor Mac & Cheese": 11.99, "Cosmic Quesadilla": 12.75, "Solar Salad": 9.50, 
    "Plutonian Pasta": 13.99, "Venusian Veggie Wrap": 10.25
  },
  "Dessert": {
    "Cake": 6.99, "Ice Cream": 4.50, "Pie": 5.99, "Cosmic Cookies": 3.75, 
    "Martian Mousse": 7.25, "Galactic Gelato": 5.50, "Nebula Nuggets": 4.99, 
    "Space Sundae": 8.75, "Asteroid Apple Crisp": 6.50, "Lunar Lemon Bars": 4.25, 
    "Solar Sorbet": 5.75, "Meteoric Milkshake": 6.99, "Plutonian Pudding": 5.25, 
    "Venusian Vanilla Wafers": 3.99, "Cosmic Cupcakes": 4.75, "Red Planet Raspberry Tart": 7.50, 
    "Zero-G Zebra Cake": 8.99, "Alien Éclair": 6.25
  }
}

# Shopping cart to store selected items
cart = []

# Helper function to pause execution until user presses 'x'
def press_x():
  """Wait for user to press 'x' to continue, then clear screen"""
  while True:
    if input("\n Press x to exit: ") == "x":
      os.system('clear')
      break

# Function to handle invalid input choices
def invalidity():
  """Display error message for invalid choices and wait for user input"""
  os.system('clear')
  print("Invalid choice. Please try again.")
  press_x()
  os.system('clear')

# Main bulletin board management function
def bulletin_command():
  """Handle all bulletin board operations including viewing, adding, and managing suggestions"""
  while True:
    # Display bulletin board menu options
    print("Welcome to the Oasis Cafe Bulletin Board!")
    print("1. View Bulletin")
    print("2. Add suggestions")
    print("3. View suggestions")
    print("4. Remove suggestions")
    print("5. Quit")
    bulletin_choice = input("Enter your choice: ")

    # View bulletin - display 10 random entries
    if bulletin_choice == "1":
      os.system('clear')
      if len(bulletin) == 0:
        print("Sorry, theres no important announcements")
      else:
        # Select 10 random bulletin entries and display them sorted
        random_indexes = random.sample(bulletin, 10)
        sorted_indexes = sorted(random_indexes)
        for index in sorted_indexes:
          print(index)
        press_x()

    # Add new suggestion to bulletin suggestions
    elif bulletin_choice == "2":
      os.system('clear')
      item = input("Enter suggestion: ")
      # Check if suggestion already exists to avoid duplicates
      if item in bulletin_suggestions:
        print("Suggestion already in bulletin")
        press_x()
      else:
        bulletin_suggestions.append(item)
        print("Suggestion added")
        press_x()
        os.system('clear')

    # View all current suggestions
    elif bulletin_choice == "3":
      os.system('clear')
      if len(bulletin_suggestions) == 0:
        print("No items in bulletin")
        press_x()
      else:
        # Display all suggestions
        print("bulletin:")
        for item in bulletin_suggestions:
          print(item)
        press_x()

    # Remove suggestions from the list
    elif bulletin_choice == "4":
      os.system('clear')
      # Display current suggestions
      for each in bulletin_suggestions:
        print(each)
      if len(bulletin_suggestions) == 0:
        print("No suggestions in bulletin")
        press_x()
      else:
        # Allow user to remove a specific suggestion
        item = input("Enter item to remove: ")
        if item in bulletin_suggestions:
          bulletin_suggestions.remove(item)
          print("suggestion removed")
        else:
          print("suggestion not found")
          press_x()
          continue
      os.system('clear')

    # Exit bulletin board
    elif bulletin_choice == "5":
      os.system('clear')
      print("Goodbye")
      press_x()
      break
    else:
      # Handle invalid bulletin choices
      invalidity()

# Function to handle menu viewing and order placement options
def menu_command():
  """Handle menu viewing and provide option to place orders"""
  while True:
    # Display menu options
    print("1. View items")
    print("2. Quit")
    menu_choice = input("Enter your choice: ")
    
    if menu_choice == "1":
      os.system('clear')
      # Show all available categories
      for category in menu.keys():
        print(f"- {category}")
      print()
      
      # Get user's category preference
      user_preference = input("Enter the category you would like to view: ")
      if user_preference.title() in menu:
        # Display items and prices in selected category
        for item, price in menu[user_preference.title()].items():
          print(f"{item}: ${price:.2f}")
        print()
        
        # Offer order placement option
        print("Would you like to place an order?")
        print("1. Place Order")
        print("2. Quit")
        Menu_redirection = input("Enter your choice: ")
        if Menu_redirection == "1":
          os.system('clear')
          # Redirect to add items to cart
          Online_order_redirect_to_add_cart()
        elif Menu_redirection == "2":
          os.system('clear')
        else:
          invalidity()
      os.system('clear')
    
    # Exit menu viewing
    elif menu_choice == "2":
      os.system('clear')
      print("Goodbye")
      press_x()
      break
    else:
      # Handle invalid menu choices
      invalidity()

# Function to directly add items to cart (redirected from menu viewing)
def Online_order_redirect_to_add_cart():
  """Handle adding items to cart when redirected from menu viewing"""
  while True:
    os.system('clear')
    # Display available menu categories
    print("Available categories:")
    for category in menu.keys():
      print(f"- {category}")
    print()
    
    user_preference = input("Enter your preference: ")
    if user_preference.title() in menu:
      # Show items in selected category
      for item, price in menu[user_preference.title()].items():
        print(f"{item}: ${price:.2f}")
      print()
      
      adding_to_cart = input("Enter item to add to cart: ")
      
      # Find the item case-insensitively to handle user input variations
      found_item = None
      for item in menu[user_preference.title()]:
        if item.lower() == adding_to_cart.lower():
          found_item = item
          break

      if found_item:
        # Add item to cart and display current cart contents
        cart.append(found_item)
        print(f"{found_item} added to cart")
        print("Your cart so far:")
        for item in cart:
          print(f"- {item}")
        
        # Ask if user wants to add more items
        Add_to_cart_again = input("Would you like to add another item?: ")
        if Add_to_cart_again.lower() == "yes":
          continue
        elif Add_to_cart_again.lower() == "no":
          os.system('clear')
          # Return to main online ordering menu
          Online_order()
          break
        else:
          invalidity()
          continue
      else:
        # Item not found in selected category
        invalidity()
    else:
      # Invalid category selection
      invalidity()

# Main online ordering system function
def Online_order():
  """Main online ordering system with full menu, cart, and checkout functionality"""
  while True:
    # Display main ordering menu
    print("Welcome to the Oasis Cafe Online Ordering System!")
    print("1. View Menu")
    print("2. Add to Cart")
    print("3. View Cart")
    print("4. Checkout")
    print("5. Exit")
    choice = input("Enter your choice: ")

    # View menu option
    if choice == "1":
      os.system('clear')
      menu_command()

    # Add items to cart option
    elif choice == "2":
      Online_order_redirect_to_add_cart()

    # View current cart contents
    elif choice == "3":
      os.system('clear')
      # Check if cart has items
      if len(cart) == 0:
        print("Your cart is empty")
        press_x()
      else:
        # Display all items in cart
        print("Your cart:")
        for item in cart:
          print(f"- {item}")
        press_x()

    # Checkout process
    elif choice == "4":
      os.system('clear')
      # Check if cart has items for checkout
      if len(cart) == 0:
        print("Your cart is empty")
        press_x()
      else:
        # Display cart with prices and calculate total
        print("Your cart:")
        total = 0
        for item in cart:
          # Find item price in menu categories
          for category, items in menu.items():
            if item in items:
              print(f"- {item}: ${items[item]:.2f}")
              total += items[item]
        
        print(f"Total: ${total:.2f}")
        
        # Apply discount for orders over $100
        if total >= 100:
          print("You get a 20% discount!")
          total *= 0.8
          print(f"New Total: ${total:.2f}")
        
        # Confirm order placement
        Order_confirmation = input("Are you sure you want to confirm your order?: ")
        if Order_confirmation.lower() == "yes":
          # Generate random order preparation time and order number
          Order_ready_time = random.randint(10, 15)
          print("Thank you for your order!")
          print(f"Your order will be ready in {Order_ready_time} minutes")
          print("Your order number is: ", random.randint(100000, 999999))
          print("Please wait for your order to be ready")
          
          # Countdown timer for order preparation (The timer was assisted by collaboration)
          while Order_ready_time:
              mins, secs = divmod(Order_ready_time, 60)
              timer = '{:02d}:{:02d}'.format(mins, secs)
              print(timer, end="\r")
              time.sleep(1)
              Order_ready_time -= 1
          # End of timer
          
          print("Your order is ready! Thank you for ordering!")
          press_x()
          # Clear cart after successful order
          cart.clear()
          break
        elif Order_confirmation.lower() == "no":
          print("Order cancelled")
          press_x()
        else:
          invalidity()
    
    # Exit online ordering system
    elif choice == "5":
      os.system('clear')
      print("Thank you for visiting the Oasis Cafe Online Ordering System!")
      break
    else:
      # Handle invalid online order choices
      invalidity()

# Main program function - entry point of the application
def main_program():
  """Main program loop - displays main menu and handles user navigation"""
  while True:
    # Display main cafe menu options
    print("Welcome to the Oasis Cafe!")
    print("1. Bulletin Board")
    print("2. View Menu")
    print("3. Online Order")
    print("4. Exit")
    choice = input("Enter your choice: ")

    # Navigate to bulletin board management
    if choice == "1":
      os.system('clear')
      bulletin_command()
    # Navigate to menu viewing
    elif choice == "2":
      os.system('clear')
      menu_command()
    # Navigate to online ordering system
    elif choice == "3":
      os.system('clear')
      Online_order()
    # Exit the application
    elif choice == "4":
      os.system('clear')
      print("Thank you for visiting the Oasis Cafe!")
      break
    else:
      # Handle invalid main menu choices
      invalidity()

# Start the application
main_program()

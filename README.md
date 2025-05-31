# Marsnet-Oasis-Cafe
This Repository contains a README File, a copy of the Program code in Python, and more.

Oasis Cafe Management System 🚀☕
Welcome to the Oasis Cafe - your friendly neighborhood space-themed cafe management system! This Python application brings together futuristic dining with classic cafe charm, complete with bulletin boards, cosmic cuisine, and an integrated ordering system.

What Does This Do?
This is a terminal-based cafe management system that lets you run a space-themed cafe in the year 2074-2075. Think of it as a digital cafe where customers can browse menus, place orders, and stay updated with announcements - all with a fun cosmic twist!

Key Features
🗓️ Dynamic Bulletin Board

View random cafe announcements and seasonal events (10 random selections from 146 total entries)
Add customer suggestions for new menu items or events with duplicate prevention
Manage and remove suggestions through an interactive interface
Features events spanning 2074-2075 with space-themed celebrations like "Solar Maximum" and "Meteor Shower Viewing Parties"
🍕 Interactive Menu System

Browse three categories: Drinks (18 items), Food (18 items), and Desserts (18 items)
Cosmic-themed items like "Martian Meatballs" ($14.75) and "Galactic Green Tea" ($4.25)
Prices range from $2.50 for basics to $18.50 for premium space cuisine
Case-insensitive item selection for user convenience
🛒 Full Online Ordering

Add items to your cart from any menu category with real-time confirmation
Real-time cart viewing and management with itemized display
Automatic total calculation with 20% discount automatically applied on orders over $100
Order confirmation with random preparation times (10-15 minutes) and 6-digit order numbers
Live countdown timer with MM:SS format that updates every second until your order is ready
How to Run
Simply run the Python file in your terminal:

bash
python oasis_cafe.py
Make sure you have Python 3.x installed - the program uses standard libraries only (time, os, random).

Navigation Guide
The system uses a simple number-based menu system:

Main Menu: Choose between Bulletin Board, Menu viewing, Online Orders, or Exit
Bulletin Board: View announcements, add suggestions, manage the community board
Menu: Browse items by category, with option to jump directly into ordering
Online Order: Full ordering experience from browsing to checkout
Just enter the number corresponding to your choice and follow the prompts!

The Space Theme
What makes this cafe special? Everything has a cosmic twist! You'll find:

Drinks: From basic sodas to "Alien Elixir" ($12.99) and "Zero-G Zinger"
Food: Classic items alongside "Cosmic Curry" and "Saturn Ring Soup"
Desserts: "Meteoric Milkshakes" and "Red Planet Raspberry Tarts"
Events: Space-themed celebrations like Moon Day and meteor shower viewing parties
Technical Notes
Cart Management: Items persist in your cart until checkout or program exit. The cart is implemented as a simple Python list that stores item names, allowing multiple quantities of the same item.
Screen Clearing: Uses os.system('clear') for a clean terminal experience (works on Unix/Mac systems). For Windows users, you may need to change this to os.system('cls') in the code.
Input Handling: Case-insensitive item selection using .lower() comparison and robust error handling through the invalidity() function that catches invalid menu choices and prompts users to try again.
Random Elements:
Bulletin entries use random.sample() to select 10 random announcements from the 146 total entries
Order numbers are generated using random.randint(100000, 999999) for 6-digit confirmation numbers
Preparation times vary between 10-15 minutes using random.randint(10, 15)
Timer Feature: Real countdown during order preparation using time.sleep(1) with formatted display showing minutes:seconds ({:02d}:{:02d}) that updates in place using carriage return (\r)
Fun Details
Smart Discounting: Orders over $100 automatically get a 20% discount (because who doesn't love a good deal in space?). The calculation uses total *= 0.8 to apply the discount and displays both original and discounted totals.
Dynamic Bulletin Display: The bulletin board contains 146 pre-written announcements covering all major holidays and events across 2074-2075. Each viewing shows 10 random events using random.sample(), then sorts them chronologically for easy reading.
Order Processing:
Order numbers are randomly generated 6-digit numbers (100,000-999,999 range)
Preparation times vary between 10-15 minutes with a live countdown timer
The timer uses divmod() to convert seconds into MM:SS format
Cart clearing happens automatically after successful order completion
Duplicate Prevention: The bulletin suggestion system checks for existing entries using if item in bulletin_suggestions to prevent duplicate suggestions from being added.
Menu Pricing Strategy: Items are strategically priced with basic drinks starting at $2.50, specialty cosmic items ranging $4-15, and premium items like "Red Planet Ribs" reaching $18.50.
Code Structure
The program is organized into clear functions with specific responsibilities:

main_program(): Main navigation hub that displays the primary menu and routes users to different system sections
bulletin_command(): Handles all bulletin board operations including viewing announcements, adding suggestions, managing the suggestion list, and removing items
menu_command(): Menu browsing functionality that displays categories, shows items with prices, and provides seamless transition to ordering
Online_order(): Complete ordering system managing the full customer experience from menu browsing to checkout
Online_order_redirect_to_add_cart(): Specialized function for adding items to cart when redirected from menu viewing, handles category selection and item validation
Helper Functions:
press_x(): Utility function that pauses execution until user presses 'x', then clears the screen
invalidity(): Error handling function that displays error messages for invalid choices and manages screen clearing
Data Structures:

bulletin: List containing 146 pre-written announcements spanning 2074-2075
bulletin_suggestions: Dynamic list storing customer suggestions
menu: Nested dictionary organized by categories (Drinks, Food, Dessert) with item names as keys and prices as values
cart: Simple list storing selected items for order processing
Perfect for learning Python basics, practicing menu-driven programming, or just having fun with a space cafe simulation! 🌟

Ready to serve the galaxy, one cosmic coffee at a time!


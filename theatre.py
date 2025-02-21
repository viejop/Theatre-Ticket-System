#constants for seat layout
NUM_COLUMNS = 8
NUM_ROWS = 9

#function to display seating
def display_seating(array):
    all_sold_out = True  #flag to check if all seats are sold out
    for row in range(NUM_ROWS - 1, -1, -1):  #reverse rows (start from last row)
        for col in range(NUM_COLUMNS):
            if array[row][col] == 0:  #seat is sold out
                print(" X", end="    ")
            else:
                print(f"${array[row][col]}", end="   ")
                all_sold_out = False
        print()
    
    #if all are are sold out display sold out message
    if all_sold_out:
        print("\nTheater is sold out!")

#function to select a seat
def select_seat(array):
    while True:
        try:
            row = int(input("Select Row (1-9): ")) - 1
            col = int(input("Select Column (1-8): ")) - 1
            if 0 <= row < NUM_ROWS and 0 <= col < NUM_COLUMNS:
                if array[row][col] != 0:  #if seat is available
                    print(f"Ticket price: ${array[row][col]}")
                    array[row][col] = 0  #mark the seat as sold
                    break
                else:
                    print("Seat already sold, try again.")
            else:
                print("Invalid seat, try again.")
        except ValueError:
            print("Invalid input, please enter valid numbers.")

#function to sell out all tickets
def sell_out_immediately(array):
    for row in range(NUM_ROWS):
        for col in range(NUM_COLUMNS):
            array[row][col] = 0  # Mark all seats as sold
    print("All tickets have been rented out by Marcos.\n")

#main function
def main():
    #initial seating arrangement (price per seat)
    seating = [
        [40, 50, 50, 50, 50, 50, 50, 40],
        [30, 30, 40, 50, 50, 40, 30, 30],
        [20, 30, 30, 40, 40, 30, 30, 20],
        [10, 20, 20, 20, 20, 20, 20, 10],
        [10, 20, 20, 20, 20, 20, 20, 10],
        [10, 20, 20, 20, 20, 20, 20, 10],
        [10, 10, 10, 10, 10, 10, 10, 10],
        [10, 10, 10, 10, 10, 10, 10, 10],
        [10, 10, 10, 10, 10, 10, 10, 10]
    ]
    
    while True:
        print("\nAvailable Theater Seating:")
        display_seating(seating)
        
        #ask if the user wants to sell out all tickets immediately
        choice = input("Do you want to sell out all tickets immediately? (y/n): ").strip().lower()
        if choice == 'y':
            sell_out_immediately(seating)
            display_seating(seating)
            break
        
        #otherwise, proceed with seat selection
        select_seat(seating)
        

main()

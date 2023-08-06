from termcolor import colored
class Hall:
    def __init__(self, rows, cols, hall_no) -> None:
        self._rows = rows
        self._cols = cols
        self._hall_no = hall_no
        self._seats = {id: [[ None for _ in range(cols)] for _ in range(rows)]}  # 2D list to store seat status
        self._show_list = [] # List of tuples to store show information
        
        # Add the Hall object to the Star_Cinema hall_list
        Star_Cinema.entry_hall(self)
        
    
    def entry_show(self, show_id, movie_name, time):
        show_info = (show_id, movie_name, time)
        self._show_list.append(show_info)
        self._seats[show_id] = [[None for _ in range (self._cols)] for _ in range(self._rows)]
    
    def book_seats(self, show_id, seats_to_book):
        seats_for_show = self._seats.get(show_id)
        print("\n")
        if seats_for_show is None:
            print(f"Show with ID {show_id} not found.")
            return
        else:
            for row, col in seats_to_book:
                if not (1 <= row <= self._rows and 1 <= col <= self._cols):
                    text_for_invalid_seat = colored(f"Invalid seat location for : {row}{chr(col + 64)} ", 'red', attrs=['reverse','blink'])
                    print(f"\t\t{text_for_invalid_seat}")
                
                elif seats_for_show[row - 1][col - 1] is not None:
                    text_for_already_booked_seat = colored(f"Seat already booked for : {row}{chr(col + 64)} ",'yellow')
                    print(f"\t\t{text_for_already_booked_seat}")
                
                else:
                    seats_for_show[row - 1][col - 1] = "Booked"
                    text_for_booked_successfully = colored(f"Seat booked successfully for : {row}{chr(col + 64)} ",'green')
                    print(f"\t\t{text_for_booked_successfully}")
                    
    def view_show_list(self):
        print("\n\t\t<<<<<< Shows Running >>>>>>\n")
        for show in self._show_list:
            print(f"ID : {show[0]}, \t Movie : {show[1]}, \t Time : {show[2]}")
    
    def view_available_seats(self,show_id):
        seats_for_show = self._seats.get(show_id)
        if seats_for_show is None:
            id_not_found_txt = colored(f"Show With ID {show_id} Not Found.","red",attrs=['reverse', 'blink'])
            print(f"\n\t\t{id_not_found_txt}")
            return
        print(f"\n\t<<<<<< Available Seats For Movie ID of -> {show_id} >>>>>>\n")
        for row in range(1,self._rows + 1):
            for col in range(1, self._cols + 1):
                if seats_for_show[row - 1][col - 1] is None:
                    text = colored(f"{row}{chr(col + 64)}",'blue',attrs=['reverse', 'blink'])
                    print(text, end = " ")
                    # print(f"{row}{chr(col+64)}", end = " ")
                else:
                    text = colored('XX', 'red', attrs=['reverse', 'blink'])
                    print(f"{text}", end = " ")
            print()
                

class Star_Cinema:
    _hall_list = [] 
    
    @classmethod
    def entry_hall(cls,hall_object):
        if isinstance(hall_object, Hall):
            cls._hall_list.append(hall_object)
            print(f"\n \t \t **** Hall {hall_object._hall_no} Added To The Hall List. ****")
        else:
            print("invalid object type. Only valid hall objects can be added")


hall = Hall(rows=5, cols=5, hall_no=1)
hall.entry_show(1, "Prem er Shomadhi", "12:00 PM")
hall.entry_show(2, "Poran er Pakhi", "04:00 PM")


y = True
while(y):
    print("\n")
    print("1. View Show List.")
    print("2. View Available Seats.")
    print("3. Book your Seats.")
    print("0. Quit.")
    
    x = int(input("\nPress the key you want to access : "))
    
    if x == 1:
        hall.view_show_list()
        
    elif x == 2:
        print("Enter Movie Id : ",end = "")
        movie_id = int(input())
        hall.view_available_seats(movie_id)
        
    elif x == 3:
        inp_movie_id = int(input("Enter Movie Id : "))
        list = []
        seats_quantity = int(input("How Much Seats Do You Need : "))
        for i in range(seats_quantity):
            tuple = ()
            print(f"Enter Seat Position For Seat Holder Number {i + 1} :")
            x = int(input("row : "))
            y = ord(input("col : ").upper()) - 64
            tuple += (x,)
            tuple += (y,)
            list.append(tuple)
            
        hall.book_seats(inp_movie_id,list)
        
    elif x==0 :
        print("\n \t \t****** Thanks for visiting our site. ******\n")
        y = False
            
        



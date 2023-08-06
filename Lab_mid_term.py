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
        show_info = (movie_name, show_id, time)
        self._show_list.append(show_info)
        self._seats[show_id] = [[None for _ in range (self._cols)] for _ in range(self._rows)]
    
    def book_seats(self, show_id, seats_to_book,name,contact):
        seats_for_show = self._seats.get(show_id)
        print("\n")
        successful_list = []
        flag = 0
        
        if seats_for_show is None:
            print(colored(f"\t\t...... Show with ID {show_id} not found ......",'red'))
            return
        else:
            for row, col in seats_to_book:
                seat = ()
                if not (1 <= row <= self._rows and 1 <= col <= self._cols):
                    text_for_invalid_seat = colored(f"... Invalid seat location for : {row}{chr(col + 64)} ...", 'red', attrs=['reverse','blink'])
                    print(f"\t\t{text_for_invalid_seat}")
                
                elif seats_for_show[row - 1][col - 1] is not None:
                    text_for_already_booked_seat = colored(f"Seat already booked for : {row}{chr(col + 64)} ",'yellow')
                    print(f"\t\t{text_for_already_booked_seat}")
                
                else:
                    seats_for_show[row - 1][col - 1] = "Booked"
                    row = row
                    col = chr(col + 64)
                    seat += (row,)
                    seat += (col,)
                    successful_list.append(seat)
                    flag = 1
                  
        
        if flag == 1:
            print(colored("\t\t<<<<<< TICKET BOOKED SUCCESSFULLY. >>>>>>\n",'green'))
            print(f"Name : {name}")
            print(f"CONTACT : {contact}")
            for show in self._show_list:
                if show[1] == show_id:
                    print(f"MOVIE NAME : {show[0]} \t Time : {show[2]}")
            print("TICKETS : ",end="")
            for ticket in successful_list:
                print(f"{ticket[0]}{ticket[1]}",end=" ")
            print()
            print(f"Hall : {self._hall_no}")
                     
                    
    def view_show_list(self):
        print("\n\t\t<<<<<< Shows Running >>>>>>\n")
        for show in self._show_list:
            print(f"MOVIE NAME: {show[0]}, \t SHOW ID : {show[1]}, \t Time : {show[2]}")
    
    def view_available_seats(self,show_id):
        seats_for_show = self._seats.get(show_id)
        if seats_for_show is None:
            id_not_found_txt = colored(f"\t\t... Show With ID {show_id} Not Found ...",'red',attrs=['reverse', 'blink'])
            print(id_not_found_txt)
            return
        print(f"\n\t<<<<<< Available Seats For Movie ID of -> {show_id} >>>>>>\n")
        for show in self._show_list:
            if show[1] == show_id:
                print(f"MOVIE NAME: {show[0]},\t\t Time : {show[2]}\n")
                
        for row in range(1,self._rows + 1):
            for col in range(1, self._cols + 1):
                if seats_for_show[row - 1][col - 1] is None:
                    text = colored(f"{row}{chr(col + 64)}\t",'blue',attrs=['reverse', 'blink'])
                    print(f"{text}", end = " ")
                    # print(f"{row}{chr(col+64)}", end = " ")
                else:
                    text = colored('XX\t', 'red', attrs=['reverse', 'blink'])
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
hall.entry_show(1, "Prem er Shomadhi", "Aug 08 2023 06:00 PM")
hall.entry_show(2, "Poran er Pakhi", "Aug 08 2023 09:00 PM")


y = True
while(y):
    print("\n")
    print("1. VIEW ALL SHOWS TODAY.")
    print("2. VIEW AVAILABLE SEATS.")
    print("3. BOOK TICKETS.")
    print("0. QUIT.")
    
    x = int(input("\nENTER OPTION : "))

    
    if x == 1:
        hall.view_show_list()
        
    elif x == 2:
        print("Enter Movie Id : ",end = "")
        movie_id = int(input())
        hall.view_available_seats(movie_id)
        
    elif x == 3:
        customer_name = input("ENTER YOUR NAME : ")
        customar_contact = input("ENTER YOUR CONTACT NUMBER : ")
        inp_movie_id = int(input("Enter SHOW Id : "))
        list = []
        seats_quantity = int(input("ENTER NUMBER OF TICKETS : "))
        for i in range(seats_quantity):
            tuple = ()
            print(f"Enter Seat Position For Seat Holder Number {i + 1} :")
            x = int(input("row : "))
            y = ord(input("col : ").upper()) - 64
            tuple += (x,)
            tuple += (y,)
            list.append(tuple)
            
        hall.book_seats(inp_movie_id,list,customer_name,customar_contact)
        
    elif x==0 :
        print("\n \t \t****** Thanks for visiting our site. ******\n")
        y = False
            
        



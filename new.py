class Hall:
    def __init__(self, rows, cols, hall_no):
        self._rows = rows
        self._cols = cols
        self._hall_no = hall_no
        self._seats = {id: [[None for _ in range(cols)] for _ in range(rows)]}  # 2D list to store seat status
        self._show_list = []  # List of tuples to store show information

        # Add the Hall object to the Star_Cinema hall_list
        Star_Cinema.entry_hall(self)

    def entry_show(self, show_id, movie_name, time):
        show_info = (show_id, movie_name, time)
        self._show_list.append(show_info)
        # Allocate seats with rows and cols using 2D list, initially all seats will be free.
        self._seats[show_id] = [[None for _ in range(self._cols)] for _ in range(self._rows)]

    def book_seats(self, show_id, seats_to_book):
        seats_for_show = self._seats.get(show_id)
        if seats_for_show is None:
            print(f"Show with ID {show_id} not found.")
            return

        for row, col in seats_to_book:
            if not (1 <= row <= self._rows and 1 <= col <= self._cols):
                print(f"Invalid seat location: Row {row}, Col {col}")
            elif seats_for_show[row - 1][col - 1] is not None:
                print(f"Seat already booked: Row {row}, Col {col}")
            else:
                seats_for_show[row - 1][col - 1] = "Booked"
                print(f"Seat booked successfully: Row {row}, Col {col}")

    def view_show_list(self):
        print("Shows running:")
        for show in self._show_list:
            print(f"ID: {show[0]}, Movie: {show[1]}, Time: {show[2]}")

    def view_available_seats(self, show_id):
        seats_for_show = self._seats.get(show_id)
        if seats_for_show is None:
            print(f"Show with ID {show_id} not found.")
            return

        print(f"Available seats for Show ID {show_id}:")
        for row in range(1, self._rows + 1):
            for col in range(1, self._cols + 1):
                if seats_for_show[row - 1][col - 1] is None:
                    print(f"Row {row}, Col {col}")

class Star_Cinema:
    _hall_list = []  # Class attribute to store hall objects

    @classmethod
    def entry_hall(cls, hall_object):
        if isinstance(hall_object, Hall):
            cls._hall_list.append(hall_object)
            print(f"Hall {hall_object._hall_no} added to the hall_list.")
        else:
            print("Invalid object type. Only Hall objects can be added.")

# Example usage:
if __name__ == "__main__":
    hall1 = Hall(rows=5, cols=10, hall_no=1)
    hall1.entry_show(1, "Movie A", "12:00 PM")
    hall1.entry_show(2, "Movie B", "3:00 PM")

    hall1.book_seats(1, [(2, 5), (3, 7), (4, 3)])  # Booking seats for show ID 1

    hall1.view_show_list()
    hall1.view_available_seats(1)

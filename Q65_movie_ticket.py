
# Q65: MovieTicket Class Using Constructor

class MovieTicket:

    def __init__(self, movie_name, theatre, seat_number):

        self.movie_name = movie_name
        self.theatre = theatre
        self.seat_number = seat_number

    def display_ticket(self):

        print("Movie Name:", self.movie_name)
        print("Theatre:", self.theatre)
        print("Seat Number:", self.seat_number)


# Create three movie ticket objects
ticket1 = MovieTicket("Kantara", "INOX", "A1")
ticket2 = MovieTicket("Leo", "PVR", "B5")
ticket3 = MovieTicket("Interstellar", "Cinepolis", "C3")

# Display ticket details
print("Ticket 1")
ticket1.display_ticket()

print("\nTicket 2")
ticket2.display_ticket()

print("\nTicket 3")
ticket3.display_ticket()

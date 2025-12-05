from django.db import models

# Litle DB, house can only have these values
HOUSES = [
    ('Gryffindor', 'Gryffindor'),
    ('Slytherin', 'Slytherin'),
    ('Ravenclaw', 'Ravenclaw'),
    ('Hufflepuff', 'Hufflepuff'),
]

class Booking(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    # Dont forget, ForeignKey bcause Room is an unknown key
    room = models.ForeignKey('rooms.Room', on_delete=models.CASCADE)
    house = models.CharField(max_length=20, choices=HOUSES) # <= choices to apply
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self):
        return f"{self.room} - {self.house}"
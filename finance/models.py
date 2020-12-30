from django.db import models

# Create your models here.
class Apple(models.Model):
    date = models.DateField(db_column='Date', blank=True, null=True)  # Field name made lowercase.
    high = models.IntegerField(db_column='High', blank=True, null=True)  # Field name made lowercase.
    low = models.IntegerField(db_column='Low', blank=True, null=True)  # Field name made lowercase.
    open = models.IntegerField(db_column='Open', blank=True, null=True)  # Field name made lowercase.
    close = models.IntegerField(db_column='Close', blank=True, null=True)  # Field name made lowercase.
    volume = models.IntegerField(db_column='Volume', blank=True, null=True)  # Field name made lowercase.
    adj_close = models.IntegerField(db_column='Adj Close', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'apple'
        ordering = ['-date']

class date_input(models.Model):
    input_index = models.AutoField(primary_key=True)
    year = models.IntegerField(null=True)
    mon = models.IntegerField(null=True)
    day = models.IntegerField(null=True)
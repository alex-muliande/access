from django.db import models



class scoreModel(models.Model):
    Accepted = 'Accepted'
    Rejected = 'Rejected'
    Undecided = 'Undecided'

    STATUS= (Accepted,'Accepted'),(Rejected,'Rejected')
    name=models.CharField(max_length=250)
    email=models.EmailField(max_length=250)
    number=models.IntegerField()
    score=models.TextField(max_length=25)
    assesment_time=models.CharField(max_length=250)
    status=models.CharField(max_length=250,choices=STATUS, default='undecided')

    def save(self, *args, **kwargs):
        if not self.pk:
            print(self.score)
            l = self.score
            score, total = self.score.split('/')
            if int(score) > 11:
                self.status = 'Accepted'
            else:
                self.status = 'Rejected'
        super().save(*args, **kwargs)

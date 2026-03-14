
from django.db import models

class Ticket(models.Model):

 CATEGORY=[
 ('technical','Technical'),
 ('billing','Billing'),
 ('account','Account'),
 ('general','General')
 ]

 PRIORITY=[
 ('low','Low'),
 ('medium','Medium'),
 ('high','High'),
 ('critical','Critical')
 ]

 STATUS=[
 ('open','Open'),
 ('progress','In Progress'),
 ('resolved','Resolved'),
 ('closed','Closed')
 ]

 title=models.CharField(max_length=200)
 description=models.TextField()
 category=models.CharField(max_length=20,choices=CATEGORY,default='general')
 priority=models.CharField(max_length=20,choices=PRIORITY,default='medium')
 status=models.CharField(max_length=20,choices=STATUS,default='open')
 created=models.DateTimeField(auto_now_add=True)


from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.db.models import Count
from .models import Ticket
from .serializers import TicketSerializer
from .ai import classify

@api_view(['GET','POST'])
def tickets(request):

 if request.method=='GET':
  qs=Ticket.objects.all().order_by('-created')
  return Response(TicketSerializer(qs,many=True).data)

 if request.method=='POST':
  s=TicketSerializer(data=request.data)
  if s.is_valid():
   s.save()
   return Response(s.data)
  return Response(s.errors,400)

@api_view(['POST'])
def classify_api(request):
 desc=request.data.get('description','')
 return Response(classify(desc))

@api_view(['GET'])
def stats(request):

 total=Ticket.objects.count()
 open=Ticket.objects.filter(status='open').count()

 critical=Ticket.objects.filter(priority='critical').count()

 return Response({
 'total':total,
 'open':open,
 'critical':critical
 })

@api_view(['PATCH'])
def update_status(request,id):
 t=Ticket.objects.get(id=id)
 t.status=request.data.get('status')
 t.save()
 return Response({'ok':True})

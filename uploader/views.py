from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser
from .serializers import CSVSerializer
from rest_framework.response import Response
from utilities import response_writer
from rest_framework import status
from .models import ContactsModel
import csv
import io
import re
from .tasks import csv_extract

# Create your views here.
class ExtractContactsAPIView(APIView):
    parser_classes = (MultiPartParser,)

    def get(self, request):
        contact_data = ContactsModel.objects.values()
    
        response = response_writer("success", contact_data, 200, "Contacts received")
        return Response(response, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = CSVSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
    
        # file = io.StringIO(serializer.validated_data["file"].file.read().decode())

        # csv_extract.delay(request.user, file)
        # csv_extract.delay(file)
        csv_extract.apply_async(request.user.username, serializer.validated_data["file"].file.read().decode())
 
        # csv_reader = csv.DictReader(file)

        # phone_no_pattern = re.compile(r"(?P<ccode>\d{2})\s?(?P<number>\d{10})")

        # for row in csv_reader:
        #     name = row["name"]
        #     phone_no = row["phone_no"]

        #     if match:=re.match(phone_no_pattern, phone_no):
        #         phone_no = int(match.group("ccode")+match.group("number"))
        #         print(ContactsModel.objects.create(name=name, phone_no=int(phone_no), user=request.user))

        response = response_writer("success", None, 200, "Contacts added")
        return Response(response, status=status.HTTP_200_OK)
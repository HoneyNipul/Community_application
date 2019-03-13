import json
import this

import MySQLdb
import time

from django.core import serializers
from django.db.models import Q
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from .models import Member, Relation,eventRegistration
from .serializers import AddressSerializer, EventsSerializer
from .serializers import MemberSerializer

db = MySQLdb.connect(host="localhost",    # your host, usually localhost
                     user="honey",         # your username
                     passwd="honey",  # your password
                     db="mycommunity")
male_relations = {

}
female_relations = []
json_data = {"daughter": {"male":"Father", "female":"Mother"},
            "son": {"male":"Father", "female":"Mother"},
            "mother": {"male":"Son", "female":"Daughter"},
            "father": {"male":"Son", "female":"Daughter"},
            "grandmother":{"female":"Grand-Daughter","male":"Grand-Son"},
            "grandfather":{"female":"Grand-Daughter","male":"Grand-Son"},
            "husband": {"female":"wife"},
            "wife": {"male":"husband"},
            # "newphew": ["uncle", "aunty"],
            # "niece": ["uncle", "aunty"],
            # "uncle":["newphew","niece"],
            # "aunty":{"newphew","neice"},
            # "brother": ["sister", "brother","cousin-sister", "cousin-brother","step-sister","step-brother"],
            # "sister": ["sister", "brother","cousin-sister", "cousin-brother","step-sister","step-brother"],
            # "daughter-in-law": ["mother-in-law","father-in-law"],
            # "son-in-law": ["mother-in-law","father-in-law"],
            # "mother-in-law": ["son-in-law", "daughter-in-law"],
            # "father-in-law": ["son-in-law", "daughter-in-law"]
            }



#data = json.loads(json_data)

class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)

# Create your views here.
@csrf_exempt
def get_detail(request, id):

    member = Member.objects.get(pk = id)

    serializer = MemberSerializer(member)

    return JSONResponse(serializer.data)

@csrf_exempt
def get_eventDetail(request, id):
    print id
    cur = db.cursor()
    # matches = eventRegistration.objects.filter(Q(event_type = 'PU')| Q(inviters_id_id = id))
    # data = serializers.serialize('json', list(matches), fields('id','event_name','event_description','start_date','end_date','inviters_id_id',''))
    #
    # array = json.dumps(matches.__dict__)
    # return JSONResponse(array , status=201)

    cur.execute("select* from eventRegistration where event_type ='PU' or inviters_id_id= '%s' or id in(select event_id_id from eventinvitee where member_id_id ='%s') GROUP BY id" %((str(id)),str(id)))
    row = cur.fetchall()
    print row
    return JSONResponse(row, status=201)

    # event = eventRegistration.objects.all()
    #
    # serializer = EventsSerializer(event, many=True)
    #


@csrf_exempt
def add_address(request):

    if request.method== 'POST':
        data = json.loads(request.body)
        serializer = AddressSerializer(data = data)
        if serializer.is_valid():
            serializer.save()

            return JSONResponse(serializer.data, status=201)

        return JSONResponse(serializer.errors, status=400)
    return JSONResponse({"error":"Invalid Request Method GET"}, status=400)





@csrf_exempt
def add_member(request):
    if request.method== 'POST':
        data = json.loads(request.body)
        serializer = MemberSerializer(data = data)
        if serializer.is_valid():
            serializer.save()

            # auth_userMapping(data)
            if 'currentMemberId' in data and 'relation' in data:
                currentMember =  Member.objects.get(pk = data['currentMemberId'])
                relative = Member.objects.get(pk = serializer.data["id"])
                relate = data['relation']
                relation = Relation()
                relation.member = currentMember
                relation.related_person = relative
                relation.relation = relate
                opposite_relation = json_data[relate][currentMember.gender]
                oppositeRelation = Relation()
                oppositeRelation.member = relative
                oppositeRelation.related_person = currentMember
                oppositeRelation.relation = opposite_relation
                relation.save()
                oppositeRelation.save()



            return JSONResponse(serializer.data, status=201)

        return JSONResponse(serializer.errors, status=400)
    return JSONResponse({"error":"Invalid Request Method GET"}, status=400)



# @csrf_exempt
# def auth_userMapping(data):
#         email= data['email']
#         username= data['username']
#         password = data['password']
#         first_name = data['first_name']
#         last_name = data['last_name']
#
#         cur = db.cursor()
#         id = cur.execute("select id from member where email='%s'" %((email)))
#         print id
#         cur.execute("insert into auth_user (memberId, username, password, first_name,last_name,email) values(id,username,password,first_name,last_name,email)")
#
#         return

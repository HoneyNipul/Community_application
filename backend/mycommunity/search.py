import MySQLdb
from django.core.serializers import json
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
import json

from mycommunity.models import Member
from mycommunity.serializers import MemberSerializer

db = MySQLdb.connect(host="localhost",    # your host, usually localhost
                     user="honey",         # your username
                     passwd="honey",  # your password
                     db="mycommunity")        # name of the data base

class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)

@csrf_exempt
def searchMember(request):
    print "honey"
    if request.method== 'POST':
            data = json.loads(request.body)
            first= data['first_name']
            middle=data['middle_name']
            last=data['last_name']
            print first
            cur = db.cursor()
            cur.execute("select * from Member where first_name ='%s' or middle_name='%s' or last_name='%s' "%((first , middle , last)))
            print cur.rowcount
            # row = cur.fetchone()
            row =cur.fetchall()
            return JSONResponse(row, status=201)

@csrf_exempt
def searchRelation(request):

    if request.method== 'POST':
        data = json.loads(request.body)
        member= data['member']

        cur = db.cursor()
        cur.execute("select count(*) from Relation where member_id ='%s' "%((member)))
        print cur.rowcount
        row = cur.fetchall()


    return JSONResponse(row,status=201)

@csrf_exempt
def findRelatedPerson(request):
    if request.method=='POST':
        data=json.loads(request.body)
        member= data['member']
        cur = db.cursor()
        cur.execute("SELECT member.first_name,Relation.related_person_id, member.last_name,Relation.relation FROM member JOIN Relation ON member.id = Relation.related_person_id WHERE Relation.member_id ='%s'"%((member)))
        row = cur.fetchall()
        return JSONResponse(row, status=201)











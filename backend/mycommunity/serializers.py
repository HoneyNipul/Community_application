from rest_framework import serializers
from rest_framework import viewsets

from mycommunity.models import Address, Member, Relation, eventRegistration, eventInvitee


class AddressSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Address
        fields = ('id','address_line1', 'address_line2', 'landmark', 'area', 'city', 'state', 'country', 'postal_code', 'phone_number1', 'phone_number2')

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return Address.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.address_line1 = validated_data.get('address_line1', instance.address_line1)
        instance.address_line2 = validated_data.get('address_line2', instance.address_line2)
        instance.landmark = validated_data.get('landmark', instance.landmark)
        instance.area = validated_data.get('area', instance.area)
        instance.city = validated_data.get('city', instance.city)
        instance.street = validated_data.get('street', instance.street)
        instance.country = validated_data.get('country', instance.country)
        instance.postal_code = validated_data.get('postal_code', instance.postal_code)
        instance.phone_number1 = validated_data.get('phone_number1', instance.phone_number1)
        instance.phone_number2 = validated_data.get('phone_number2', instance.phone_number2)
        instance.save()
        return instance

class RelationSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Relation
        fields = ('member', 'related_person', ' relation')

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return Relation.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.member = validated_data.get('member', instance.member)
        instance.related_person = validated_data.get('related_person', instance.related_person)
        instance.relation = validated_data.get('relation', instance.relation)

class MemberSerializer(serializers.ModelSerializer):
    address = AddressSerializer
    # Relation = RelationSerializer(many=True)

    class Meta:
        model = Member
        fields = ('id','address','first_name', 'middle_name', 'last_name', 'gender', 'birth_date',
                  'email','occupation', 'marital_status', 'mobile_number1', 'mobile_number2', 'office_number', 'photo')

# class ArticleViewSet(viewsets.ModelViewSet):
#     serializer_class = MemberSerializer
#     queryset = Member.objects.all().prefetch_related('Relation')[:10]





class EventsSerializer(serializers.ModelSerializer):

    class Meta:
        model = eventRegistration
        fields = ('event_name', 'inviters_id', 'event_description','start_date', 'event_type','end_date')


class Event_registerySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = eventInvitee
        fields = ('event_id', 'member_id', 'message')

# class EventnotificationSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model =  eventnotification
#         fields = ('event_id', 'notification_type', 'notification_description', 'notification_start', 'notification_end')
#
# class GroupSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = group
#         fields = ('group_name', 'admin_id')
#
# class Group_memberSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = group_member
#         fields = ('group_id', 'mem_id')



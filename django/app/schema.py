
import graphene
from graphene_django.filter import DjangoFilterConnectionField
from graphene_django import DjangoObjectType
from graphql import GraphQLError
from .models import Event

class EventType(DjangoObjectType):
    class Meta:
        model = Event
        fields = ('name', 'source', 'uuid', 'created_at', 'updated_at', 'description')

class EventNode(DjangoObjectType):
    class Meta:
        model = Event
        filter_fields = ['name', 'source', 'uuid', 'created_at', 'updated_at', 'description']
        interfaces = (graphene.relay.Node, )


class Query(graphene.ObjectType):
    all_events = graphene.List(EventType)
    event_by_uuid = graphene.Field(EventType, event_uuid=graphene.String())
    filter_events = DjangoFilterConnectionField(EventNode)

    def resolve_all_events(root, info, **kwargs):
        return Event.objects.all()

    def resolve_event_by_uuid(root, info, event_uuid, **kwargs):
        event = Event.objects.get(uuid=event_uuid)
        try:
            return event
        except:
            raise Exception('Wrong UUID')

class EventInput(graphene.InputObjectType):
    name = graphene.String(required=True)
    source = graphene.String(required=True)
    description = graphene.String(required=True)

class CreateEvent(graphene.Mutation):
    class Arguments:
        input = EventInput(required = True)

    event = graphene.Field(EventType)

    @classmethod
    def mutate(cls, root, info, input):
        if input.name and input.source and input.description:
            event = Event()
            event.name= input.name
            event.source = input.source
            event.description = input.description
            event.save()
            return CreateEvent(event=event)
        else:
            raise GraphQLError(f'Some fileds are empty: \n{input.name=}\n {input.source=}\n{input.description=}')

class UpdateEvent(graphene.Mutation):
    class Arguments:
        input = EventInput(required=True)
        uuid = graphene.String()

    event = graphene.Field(EventType)
    
    @classmethod
    def mutate(cls, root, info, input, uuid):
        event = Event.objects.get(uuid=uuid)
        if event:
            event.name = input.name if input.name else event.name
            event.source = input.source if input.source else event.source
            event.description = input.description if input.description else event.description
            event.save()
            return UpdateEvent(event=event)
        else:
            raise GraphQLError(f'Wrong uuid, {uuid=}')

class DeleteEvent(graphene.Mutation):
    class Arguments:
        uuid = graphene.String()

    event = graphene.Field(EventType)
    
    @classmethod
    def mutate(cls, root, info, uuid):
        event = Event.objects.get(uuid=uuid)
        if event:
            event.delete()
            return 'Deleted successfully\n' + DeleteEvent(event=event)
        else:
            raise GraphQLError(f'No event with this uuid\n{uuid=}')

class Mutation(graphene.ObjectType):
    create_event = CreateEvent.Field()
    update_event = UpdateEvent.Field()
    delete_event = DeleteEvent.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)
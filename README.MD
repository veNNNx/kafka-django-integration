# Integration kafka with django events consumer in Docker

Project services:

- django

- postgres

- kafka

- graphql

## Deployment

- Setup kafka server:

download kafka tool (offset explorer)

connect to kafka server, advanced -> bootstrap server -> localhost:29092

add topic with name: events

- Setup docker
  docker-compose -d --build (all logs in docker)

- Test locally
  Docker run producer-api to send one event every 5 sec to kafka

## Authors

- [@Cwalina Piotr](https://github.com/veNNNx)

## Run Locally

```
- Graphql at 127.0.0.1/graphql

    All_events:
query {
  allEvents{
    name, uuid
  }
}

    Search for event by uuid:
query {
  eventByUuid(eventUuid:"111"){
    name
  }
}

    Search by fields:
query {
  filterEvents(name: "name_9") {
    edges {
      node {
        name
        description
        uuid,
        createdAt
        updatedAt
      }
    }
  }
}


- Events saved in DB:
127.0.0.1:5050
PGADMIN_DEFAULT_EMAIL:  admin@admin.com
PGADMIN_DEFAULT_PASSWORD: admin

hostname: postgres
Port: 5432
Maintenance db: postgres
username: postgres
password: postgres
```

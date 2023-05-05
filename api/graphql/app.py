from strawberry.fastapi import GraphQLRouter

from api.graphql.schema.types import schema

graphql = GraphQLRouter(schema)

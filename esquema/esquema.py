from peewee import PostgresqlDatabase, Model, CharField


db = PostgresqlDatabase('mybd', port=5432, user='postgres', password='152538')


class BaseModel(Model):
    class Meta:
        database = db


class Usuario(BaseModel):
    id = CharField(primary_key=True)
    nome = CharField(max_length=255, null=False)
    email = CharField(max_length=250, null=False, unique=True)
    profissao = CharField(max_length=250, null=False)


db.connect()
db.create_tables([Usuario])
db.close()
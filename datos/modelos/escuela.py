




class curso (BaseModel):
    id_curso = AutoField()
    nivel = CharField(max_length=20)
    nombre = CharField(max_length=30)


class Meta:
    table_name = 'curso'
    
from fastapi import FastAPI
from bd import students, courses
from prefix import course_not_find


app = FastAPI()


@app.get('/')
def index():
    return {'ola': 'Mundo'}

# Sempre que eu for usar uma rota fixa e eu quiser reaproveitar a rota para adicionar um parâmetro no final do
# endpoint, devo declarar a rota fixa antes
# exmplo nas 2 rotas a seguir
@app.get('/student/me')
async def get_loged_student():
    return {'id_student':'Estudante atual'}


@app.get('/student/{id_student}')
def get_student_by_id(id_student : int):
    return students[id_student]


#para deixar parametros pré-definidos para um end-point, basta criar uma subclasse de Enum, como em prefix.py
@app.get("/course/{name_course}")
async def get_course(name_course:course_not_find):
    if name_course == course_not_find.biologia: 
        return {
            "curso" : name_course,
            "message" : f"o curso de {name_course} ainda não foi adicionado! Previsão 15/09/2023"
        }
    elif name_course == course_not_find.matematica:
        return{
            "curso" : name_course,
            "message" : f"o curso de {name_course} ainda não foi adicionado! Previsão 05/08/2023"
        }
    else:
        return name_course



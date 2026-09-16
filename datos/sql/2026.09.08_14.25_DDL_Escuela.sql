create table Periodo_Academico (
    id_periodo_academico int not null auto_increment,
    nombre_periodo_academico varchar(50) not null,
    fecha_inicio date not null,
    fecha_fin date not null,
    primary key (id_periodo_academico)
);
--Crear tabla de Alumno
Create table Alumno (
    id_alumno int not null Primary key,
    nombre_alumno varchar(60) not null,
    correo_alumno varchar(50),
    telefono_alumno varchar(50),
    curso_alumno --completar luego
)



--Crear tabla de Nota
Create table Nota (
    id_nota varchar(50) not null primary key,
    calificacion int not null,
    fecha date not null,
    alumno ----(completar despues)
)



--Crear tabla de Asignatura
create table Asignatura (
    id_asignatura int not null primary key,
    nombre_asignatura varchar(40) not null,
    descripcion_asignatura varchar(100)
)



--Crear tabla de Profesor
Create table Profesor (
    id_profesor int not null primary key,
    nombre_profesor varchar(50) not null,
    correo_profesor varchar(60),
    telefono_profesor varchar(18),
    asigunatura_profesor --(Rellenar despues)
)



--Crear tabla de Asistencia
Create table Asistencia (
    id_asistencia int not null primary key,
    fecha_asistencia date not null,
    estado_asistencia varchar(30),
    alumno --(despues rellenar)
)



--Crear tabla de Curso
Create table Curso (
    id_curso int not null primary key,
    nombre_curso varchar(30) not null,
    nivel_curso varchar(20)
)



--Crear tabla de Apoderado
Create table Apoderado (
    id_apoderado int not null primary key,
    nombre_apoderado varchar(40) not null,
    correo_apoderado varchar(50) not null,
    telefono_apoderado, varchar(50) not null
)
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




--Crear tabla de Asignatura




--Crear tabla de Profesor




--Crear tabla de Asistencia




--Crear tabla de Curso




--Crear tabla de Apoderado

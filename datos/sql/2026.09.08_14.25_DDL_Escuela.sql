--Crear tabla de Apoderado            --Listo
Create table Apoderado (
    id_apoderado int primary key auto_increment not null,
    nombre varchar(40) not null,
    correo varchar(50) not null,
    telefono varchar(50) not null
);




--Crear tabla de Curso                 -Listo
Create table Curso (
    id_curso int primary key auto_increment not null,
    nombre varchar(30) not null,
    nivel varchar(20) not null
);




--Crear tabla de Profesor                --Listo
Create table Profesor (
    id_profesor int primary key auto_increment not null,
    nombre varchar(50) not null,
    correo varchar(60) not null,
    telefono varchar(18) not null
);




--Crear tabla de Asignatura              --Listo
Create table Asignatura (
    id_asignatura int primary key auto_increment not null,
    nombre varchar(40) not null,
    descripcion varchar(100),
    id_profesor int not null,
    foreign key(id_profesor)references Profesor(id_profesor)
);




--crear tabla de Contenido              --Listo
Create table Contenido (
    id_contenido int primary key auto_increment not null,
    nombre varchar(40) not null,
    numero_unidad int not null
);




--crear tablas de evaluaciones     -Listo
Create table Evaluaciones (
    id_evaluaciones int primary key auto_increment not null,
    nombre varchar(30) not null,
    fecha date not null,
    descripcion varchar(40) not null,
    id_contenido int not null,
    foreign key(id_contenido) references Contenido(id_contenido)
);




--Crear tabla de Seccion                 --Listo
Create table Seccion (
    id_seccion int primary key auto_increment not null,
    numero varchar(35) not null,
    cupos int not null,
    id_curso int not null,
    id_asignatura int not null,
    foreign key(id_curso)references Curso(id_curso),
    foreign key(id_asignatura)references Asignatura(id_asignatura)
);




--Crear tabla de Alumno                 --Listo
Create table Alumno (
    id_alumno int Primary key auto_increment not null,
    nombre varchar(60) not null,
    correo varchar(50) not null,
    telefono varchar(50) not null,
    id_seccion int not null,
    id_curso int not null,
    id_apoderado int not null,
    foreign key(id_curso)references Curso(id_curso),
    foreign key(id_apoderado)references Apoderado(id_apoderado),
    foreign key(id_seccion)references Seccion(id_seccion)
);




--Crear tabla de Registro Academico    --Listo
Create table Registro_academico (
    id_registro_academico int primary key auto_increment not null,
    fecha date not null,
    id_curso int not null,
    id_contenido int not null,
    foreign key(id_curso)references Curso(id_curso),
    foreign key(id_contenido)references Contenido(id_contenido)
);




--Crear tabla de clases programadas               --Listo
Create table Clases_programadas (
    id_clases_prog int primary key auto_increment not null,
    horario varchar(35) not null,
    fecha date not null,
    sala varchar(35) not null,
    id_asignatura int not null,
    id_seccion int not null,
    foreign key(id_asignatura)references Asignatura(id_asignatura),
    foreign key(id_seccion)references Seccion(id_seccion)
);




--Crear tabla de Nota                     --Listo
Create table Nota (
    id_nota int primary key auto_increment not null,
    calificacion float not null,
    fecha date not null,
    id_alumno int not null,
    id_evaluaciones int not null,
    foreign key(id_alumno)references Alumno(id_alumno),
    foreign key(id_evaluaciones)references Evaluaciones(id_evaluaciones)
);




--Crear tabla de Asistencia             --Listo
Create table Asistencia (
    id_asistencia int primary key auto_increment not null,
    fecha date not null,
    estado varchar(30) not null,
    id_alumno int not null,
    id_clases_prog int not null,
    foreign key(id_alumno)references Alumno(id_alumno),
    foreign key(id_clases_prog)references Clases_programadas(id_clases_prog)
);
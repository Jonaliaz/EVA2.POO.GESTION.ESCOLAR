--Crear tabla de Alumno                 --Listo
Create table Alumno (
    id_alumno int Primary key auto_increment not null,
    nombre_alumno varchar(60) not null,
    correo_alumno varchar(50) not null,
    telefono_alumno varchar(50) not null,
    id_curso int not null,
    id_apoderado int not null,
    foreign key (id_curso) references Curso(id_curso),
    foreign key (id_apoderado) references Apoderado(id_apoderado)
);



--Crear tabla de Nota                     --Listo
Create table Nota (
    id_nota int primary key auto_increment not null,
    calificacion int not null,
    fecha date not null,
    id_alumno int not null,
    id_asignatura int not null,
    foreign key (id_alumno) references Alumno(id_alumno),
    foreign key (id_asignatura) references Asignatura(id_asignatura)
);



--Crear tabla de Asignatura              --Listo
create table Asignatura (
    id_asignatura int primary key auto_increment not null,
    nombre_asignatura varchar(40) not null,
    descripcion_asignatura varchar(100)
);



--Crear tabla de Profesor                --Listo
Create table Profesor (
    id_profesor int primary key auto_increment not null,
    nombre_profesor varchar(50) not null,
    correo_profesor varchar(60) not null,
    telefono_profesor varchar(18) not null,
    id_asignatura int not null,
    foreign key(id_asignatura) references Asignatura(id_asignatura)
);



--Crear tabla de Asistencia             --Listo
Create table Asistencia (
    id_asistencia int primary key auto_increment not null,
    fecha_asistencia date not null,
    estado_asistencia varchar(30) not null,
    id_alumno int not null
    foreign key(id_alumno) references Alumno(id_alumno)
);



--Crear tabla de Curso                 -Listo
Create table Curso (
    id_curso int primary key auto_increment not null,
    nombre_curso varchar(30) not null,
    nivel_curso varchar(20) not null
);



--Crear tabla de Apoderado            --Listo
Create table Apoderado (
    id_apoderado int primary key auto_increment not null,
    nombre_apoderado varchar(40) not null,
    correo_apoderado varchar(50) not null,
    telefono_apoderado, varchar(50) not null,
);
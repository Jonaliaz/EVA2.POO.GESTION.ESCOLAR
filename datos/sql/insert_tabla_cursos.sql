--Ingresar datos a Curso
insert into Curso 
(nombre_curso, nivel_curso)
values 
('Analista programador','Primer año'),
('Desarrollador de software', 'Segundo año'),
('Ingenieria en Informatica','Tercer año');



--Ingresar datos a Apoderados
Insert into Apoderado
(nombre_apoderado, correo_apoderado, telefono_apoderado)
values
('Juan Perez', 'juan.perez@correo.cl', '911111111'),
('Maria Gonzalez', 'maria.gonzalez@correo.cl', '922222222'),
('Carlos Rojas', 'carlos.rojas@correo.cl', '933333333'),
('Patricia Torres', 'patricia.torres@correo.cl', '944444444'),
('Luis Silva', 'luis.silva@correo.cl', '955555555'),
('Ana Herrera', 'ana.herrera@correo.cl', '966666666'),
('Pedro Morales', 'pedro.morales@correo.cl', '977777777'),
('Claudia Reyes', 'claudia.reyes@correo.cl', '988888888'),
('Miguel Contreras', 'miguel.contreras@correo.cl', '999999999'),
('Veronica Fuentes', 'veronica.fuentes@correo.cl', '900000000');



--Ingresar datros a asignatura
Insert into Asignatura
(nombre_asignatura, descripcion_asignatura)
VALUES
('Base de Datos', 'Modelado y gestion de bases de datos'),
('Programacion', 'Desarrollo de aplicaciones'),
('Analisis de Sistemas', 'Levantamiento de requerimientos');



--Ingresar datos a Profesor
Insert into Profesor
(nombre_profesor, correo_profesor, telefono_profesor, id_asignatura)
values
('Rory Walter Alveal Lira', 'rory.alveal@correo.cl', '912345600', 1),
('Andrea Martinez', 'andrea.martinez@correo.cl', '912345601', 2),
('Rodrigo Paredes', 'rodrigo.paredes@correo.cl', '912345602', 3);



--Ingresar datos a Alumnos
Insert into Alumno
(nombre_alumno, correo_alumno, telefono_alumno, id_curso, id_apoderado)
values
('Leonardo Barriga', 'leonardo@correo.cl', '912345678', 1, 1),
('Matias Gonzalez', 'matias@correo.cl', '912345679', 1, 2),
('Vicente Rojas', 'vicente@correo.cl', '912345680', 1, 3),
('Benjamin Torres', 'benjamin@correo.cl', '912345681', 1, 4),
('Martin Silva', 'martin@correo.cl', '912345682', 1, 5),
('Joaquin Herrera', 'joaquin@correo.cl', '912345683', 1, 6),
('Diego Morales', 'diego@correo.cl', '912345684', 1, 7),
('Cristobal Reyes', 'cristobal@correo.cl', '912345685', 1, 8),
('Jona Aliaz', 'jona@correo.cl', '912345686', 1, 9),
('Nicolas Fuentes', 'nicolas@correo.cl', '912345687', 1, 10);



--Ingresar datos a Notas
Insert into Nota
(calificacion, fecha, id_alumno, id_asignatura)
values
(65, '2026-09-16', 1, 1),
(58, '2026-09-16', 2, 1),
(70, '2026-09-16', 3, 1),
(61, '2026-09-16', 4, 1),
(67, '2026-09-16', 5, 1),
(55, '2026-09-16', 6, 1),
(72, '2026-09-16', 7, 1),
(64, '2026-09-16', 8, 1),
(69, '2026-09-16', 9, 1),
(60, '2026-09-16', 10, 1);



--Ingresar datos a Asistencia
insert into Asistencia
(fecha_asistencia, estado_asistencia, id_alumno)
values
('2026-09-16', 'Presente', 1),
('2026-09-16', 'Presente', 2),
('2026-09-16', 'Ausente', 3),
('2026-09-16', 'Presente', 4),
('2026-09-16', 'Presente', 5),
('2026-09-16', 'Ausente', 6),
('2026-09-16', 'Presente', 7),
('2026-09-16', 'Presente', 8),
('2026-09-16', 'Presente', 9),
('2026-09-16', 'Presente', 10);




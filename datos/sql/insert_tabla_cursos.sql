--Insertar datos dentro de la tabla Apoderados
INSERT INTO Apoderado
(nombre, correo, telefono)
VALUES
('Carlos Gonzalez', 'carlos.gonzalez@correo.cl', '912345601'),
('Maria Rojas', 'maria.rojas@correo.cl', '912345602'),
('Pedro Silva', 'pedro.silva@correo.cl', '912345603'),
('Andrea Torres', 'andrea.torres@correo.cl', '912345604'),
('Luis Herrera', 'luis.herrera@correo.cl', '912345605'),
('Patricia Morales', 'patricia.morales@correo.cl', '912345606'),
('Jorge Reyes', 'jorge.reyes@correo.cl', '912345607'),
('Claudia Contreras', 'claudia.contreras@correo.cl', '912345608'),
('Miguel Fuentes', 'miguel.fuentes@correo.cl', '912345609'),
('Daniela Sepulveda', 'daniela.sepulveda@correo.cl', '912345610');




--Insertar datos dentro de la Curso
INSERT INTO Curso
(nombre, nivel)
VALUES
('Analista Programador', 'Primer Año'),
('Desarrollo de Software', 'Segundo Año'),
('Ingenieria', 'Tercer Año');




--Insertar datos dentro de la tabla Profesor
INSERT INTO Profesor
(nombre, correo, telefono)
VALUES
('Rory Alveal', 'rory.alveal@correo.cl', '923456701'),
('Andrea Martinez', 'andrea.martinez@correo.cl', '923456702'),
('Rodrigo Paredes', 'rodrigo.paredes@correo.cl', '923456703');




--Insertar datos dentro de la tabla Asignatura
INSERT INTO Asignatura
(nombre, descripcion, id_profesor)
VALUES
('Base de Datos', 'Fundamentos y gestion de bases de datos', 1),
('Programacion', 'Desarrollo y fundamentos de programacion', 2),
('Analisis de Sistemas', 'Analisis y modelado de sistemas', 3);




--Insertar datos dentro de la tabla Contenido
INSERT INTO Contenido
(nombre, numero_unidad)
VALUES
('Modelo Relacional', 1),
('Consultas SQL', 2),
('Normalizacion', 3),
('Integridad de Datos', 4);




--Insertar datos dentro de la tabla Evaluaciones
INSERT INTO Evaluaciones
(nombre, fecha, descripcion, id_contenido)
VALUES
('Prueba Relacional', '2026-09-10', 'Evaluacion del modelo relacional', 1),
('Trabajo SQL', '2026-09-17', 'Desarrollo de consultas SQL', 2),
('Control Normalizacion', '2026-09-24', 'Ejercicios de normalizacion', 3),
('Proyecto Integridad', '2026-10-01', 'Aplicacion de integridad de datos', 4);




--Insertar datos dentro de la tabla Seccion
INSERT INTO Seccion
(numero, cupos, id_curso, id_asignatura)
VALUES
('001', 30, 1, 1),
('002', 25, 2, 2),
('003', 35, 3, 3);




--Insertar datos dentro de la tabla Alumno
INSERT INTO Alumno
(nombre, correo, telefono, id_seccion, id_curso, id_apoderado)
VALUES
('Leonardo Barriga', 'leonardo@correo.cl', '934567801', 1, 1, 1),
('Matias Gonzalez', 'matias@correo.cl', '934567802', 1, 1, 2),
('Vicente Rojas', 'vicente@correo.cl', '934567803', 1, 1, 3),
('Benjamin Torres', 'benjamin@correo.cl', '934567804', 1, 1, 4),
('Martin Silva', 'martin@correo.cl', '934567805', 2, 2, 5),
('Joaquin Herrera', 'joaquin@correo.cl', '934567806', 2, 2, 6),
('Diego Morales', 'diego@correo.cl', '934567807', 2, 2, 7),
('Cristobal Reyes', 'cristobal@correo.cl', '934567808', 3, 3, 8),
('Jona Aliaz', 'jona@correo.cl', '934567809', 3, 3, 9),
('Nicolas Fuentes', 'nicolas@correo.cl', '934567810', 3, 3, 10);




--Insertar datos dentro de la tabla Registro Academico
INSERT INTO Registro_academico
(fecha, id_curso, id_contenido)
VALUES
('2026-09-01', 1, 1),
('2026-09-08', 1, 2),
('2026-09-15', 2, 3),
('2026-09-22', 3, 4);




--Insertar datos dentro de la tabla Clases Programadas
INSERT INTO Clases_Programadas
(horario, fecha, sala, id_asignatura, id_seccion)
VALUES
('08:30 - 10:00', '2026-09-21', 'Sala 101', 1, 1),
('10:15 - 11:45', '2026-09-22', 'Sala 204', 2, 2),
('12:00 - 13:30', '2026-09-23', 'Laboratorio 3', 3, 3);




--Insertar datos dentro de la tabla Nota
INSERT INTO Nota
(calificacion, fecha, id_alumno, id_evaluaciones)
VALUES
(6.5, '2026-09-10', 1, 1),
(5.8, '2026-09-10', 2, 1),
(6.2, '2026-09-10', 3, 1),
(5.4, '2026-09-10', 4, 1),
(6.8, '2026-09-17', 5, 2),
(4.9, '2026-09-17', 6, 2),
(6.0, '2026-09-17', 7, 2),
(5.7, '2026-09-24', 8, 3),
(6.9, '2026-09-24', 9, 3),
(6.3, '2026-09-24', 10, 3);




--Insertar datos dentro de la tabla Asistencia
INSERT INTO Asistencia
(fecha, estado, id_alumno, id_clases_prog)
VALUES
('2026-09-21', 'Presente', 1, 1),
('2026-09-21', 'Presente', 2, 1),
('2026-09-21', 'Ausente', 3, 1),
('2026-09-21', 'Presente', 4, 1),
('2026-09-22', 'Presente', 5, 2),
('2026-09-22', 'Ausente', 6, 2),
('2026-09-22', 'Presente', 7, 2),
('2026-09-23', 'Presente', 8, 3),
('2026-09-23', 'Presente', 9, 3),
('2026-09-23', 'Ausente', 10, 3);

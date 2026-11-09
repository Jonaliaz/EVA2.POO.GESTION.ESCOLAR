--creacion de tabla para la tabla alumno
CREATE TABLE `alumno` (
  `id_alumno` int(11) NOT NULL,
  `nombre` varchar(60) NOT NULL,
  `correo` varchar(50) NOT NULL,
  `telefono` varchar(50) NOT NULL,
  `id_seccion` int(11) NOT NULL,
  `id_curso` int(11) NOT NULL,
  `id_apoderado` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_uca1400_ai_ci;


--insert de datos para la tabla alumno

INSERT INTO `alumno` (`id_alumno`, `nombre`, `correo`, `telefono`, `id_seccion`, `id_curso`, `id_apoderado`) VALUES
(3, 'Matias Gonzalez', 'matias@correo.cl', '934567802', 1, 1, 2),
(4, 'Vicente Rojas', 'vicente@correo.cl', '934567803', 1, 1, 3),
(5, 'Benjamin Torres', 'benjamin@correo.cl', '934567804', 1, 1, 4),
(6, 'Martin Silva', 'martin@correo.cl', '934567805', 2, 2, 5),
(7, 'Joaquin Herrera', 'joaquin@correo.cl', '934567806', 2, 2, 6),
(8, 'Diego Morales', 'diego@correo.cl', '934567807', 2, 2, 7),
(9, 'Cristobal Reyes', 'cristobal@correo.cl', '934567808', 3, 3, 8),
(10, 'Jona Aliaz', 'jona@correo.cl', '934567809', 3, 3, 9),
(11, 'Nicolas Fuentes', 'nicolas@correo.cl', '934567810', 3, 3, 10),
(12, 'Leonardo Barriga', 'leonardo@correo.cl', '934567801', 1, 1, 1),
(13, 'Matias Gonzalez', 'matias@correo.cl', '934567802', 1, 1, 2),
(14, 'Vicente Rojas', 'vicente@correo.cl', '934567803', 1, 1, 3),
(15, 'Benjamin Torres', 'benjamin@correo.cl', '934567804', 1, 1, 4),
(16, 'Martin Silva', 'martin@correo.cl', '934567805', 2, 2, 5),
(17, 'Joaquin Herrera', 'joaquin@correo.cl', '934567806', 2, 2, 6),
(18, 'Diego Morales', 'diego@correo.cl', '934567807', 2, 2, 7),
(19, 'Cristobal Reyes', 'cristobal@correo.cl', '934567808', 3, 3, 8),
(20, 'Jona Aliaz', 'jona@correo.cl', '934567809', 3, 3, 9),
(21, 'Nicolas Fuentes', 'nicolas@correo.cl', '934567810', 3, 3, 10);



--creacion de tabla para la tabla apoderado

CREATE TABLE `apoderado` (
  `id_apoderado` int(11) NOT NULL,
  `nombre` varchar(40) NOT NULL,
  `correo` varchar(50) NOT NULL,
  `telefono` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_uca1400_ai_ci;


--insert de datos para la tabla apoderado

INSERT INTO `apoderado` (`id_apoderado`, `nombre`, `correo`, `telefono`) VALUES
(1, 'Carlos Gonzalez', 'carlos.gonzalez@correo.cl', '912345601'),
(2, 'Maria Rojas', 'maria.rojas@correo.cl', '912345602'),
(3, 'Pedro Silva', 'pedro.silva@correo.cl', '912345603'),
(4, 'Andrea Torres', 'andrea.torres@correo.cl', '912345604'),
(5, 'Luis Herrera', 'luis.herrera@correo.cl', '912345605'),
(6, 'Patricia Morales', 'patricia.morales@correo.cl', '912345606'),
(7, 'Jorge Reyes', 'jorge.reyes@correo.cl', '912345607'),
(8, 'Claudia Contreras', 'claudia.contreras@correo.cl', '912345608'),
(9, 'Miguel Fuentes', 'miguel.fuentes@correo.cl', '912345609'),
(10, 'Daniela Sepulveda', 'daniela.sepulveda@correo.cl', '912345610'),
(11, 'Carlos Gonzalez', 'carlos.gonzalez@correo.cl', '912345601'),
(12, 'Maria Rojas', 'maria.rojas@correo.cl', '912345602'),
(13, 'Pedro Silva', 'pedro.silva@correo.cl', '912345603'),
(14, 'Andrea Torres', 'andrea.torres@correo.cl', '912345604'),
(15, 'Luis Herrera', 'luis.herrera@correo.cl', '912345605'),
(16, 'Patricia Morales', 'patricia.morales@correo.cl', '912345606'),
(17, 'Jorge Reyes', 'jorge.reyes@correo.cl', '912345607'),
(18, 'Claudia Contreras', 'claudia.contreras@correo.cl', '912345608'),
(19, 'Miguel Fuentes', 'miguel.fuentes@correo.cl', '912345609'),
(20, 'Daniela Sepulveda', 'daniela.sepulveda@correo.cl', '912345610');


--Creacion de tabla para la tabla asignatura

CREATE TABLE `asignatura` (
  `id_asignatura` int(11) NOT NULL,
  `nombre` varchar(40) NOT NULL,
  `descripcion` varchar(100) DEFAULT NULL,
  `id_profesor` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_uca1400_ai_ci;


--Insert de datos para la tabla asignaturas

INSERT INTO `asignatura` (`id_asignatura`, `nombre`, `descripcion`, `id_profesor`) VALUES
(1, 'Base de Datos', 'Fundamentos y gestion de bases de datos', 1),
(2, 'Programacion', 'Desarrollo y fundamentos de programacion', 2),
(3, 'Analisis de Sistemas', 'Analisis y modelado de sistemas', 3);



--creacion de tabla para la tabla asistencia

CREATE TABLE `asistencia` (
  `id_asistencia` int(11) NOT NULL,
  `fecha` date NOT NULL,
  `estado` varchar(30) NOT NULL,
  `id_alumno` int(11) NOT NULL,
  `id_clases_prog` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_uca1400_ai_ci;


--Insert de datos para la tabla asistencia

INSERT INTO `asistencia` (`id_asistencia`, `fecha`, `estado`, `id_alumno`, `id_clases_prog`) VALUES
(1, '2026-09-21', 'Presente', 1, 1),
(3, '2026-09-21', 'Ausente', 3, 1),
(4, '2026-09-21', 'Presente', 4, 1),
(5, '2026-09-22', 'Presente', 5, 2),
(6, '2026-09-22', 'Ausente', 6, 2),
(7, '2026-09-22', 'Presente', 7, 2),
(8, '2026-09-23', 'Presente', 8, 3),
(9, '2026-09-23', 'Presente', 9, 3),
(10, '2026-09-23', 'Ausente', 10, 3);


--Creacion de tabla para la tabla clases_programadas

CREATE TABLE `clases_programadas` (
  `id_clases_prog` int(11) NOT NULL,
  `horario` varchar(35) NOT NULL,
  `fecha` date NOT NULL,
  `sala` varchar(35) NOT NULL,
  `id_asignatura` int(11) NOT NULL,
  `id_seccion` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_uca1400_ai_ci;


--Insert de datos para la tabla clases_programadas

INSERT INTO `clases_programadas` (`id_clases_prog`, `horario`, `fecha`, `sala`, `id_asignatura`, `id_seccion`) VALUES
(1, '08:30 - 10:00', '2026-09-21', 'Sala 101', 1, 1),
(2, '10:15 - 11:45', '2026-09-22', 'Sala 204', 2, 2),
(3, '12:00 - 13:30', '2026-09-23', 'Laboratorio 3', 3, 3);



--creacion de tabla para la tabla contenido

CREATE TABLE `contenido` (
  `id_contenido` int(11) NOT NULL,
  `nombre` varchar(40) NOT NULL,
  `numero_unidad` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_uca1400_ai_ci;


--insert de datos para la tabla contenido

INSERT INTO `contenido` (`id_contenido`, `nombre`, `numero_unidad`) VALUES
(1, 'Modelo Relacional', 1),
(2, 'Consultas SQL', 2),
(3, 'Normalizacion', 3),
(4, 'Integridad de Datos', 4);


--creacion de tabla para la tabla curso

CREATE TABLE `curso` (
  `id_curso` int(11) NOT NULL,
  `nombre` varchar(30) NOT NULL,
  `nivel` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_uca1400_ai_ci;


--insert de datos para la tabla curso

INSERT INTO `curso` (`id_curso`, `nombre`, `nivel`) VALUES
(1, 'Analista Programador', 'Primer Año'),
(2, 'Desarrollo de Software', 'Segundo Año'),
(3, 'Ingenieria', 'Tercer Año');


--creacion de tabla para la tabla evaluaciones

CREATE TABLE `evaluaciones` (
  `id_evaluaciones` int(11) NOT NULL,
  `nombre` varchar(30) NOT NULL,
  `fecha` date NOT NULL,
  `descripcion` varchar(40) NOT NULL,
  `id_contenido` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_uca1400_ai_ci;


--Insert de datos para la tabla evaluaciones

INSERT INTO `evaluaciones` (`id_evaluaciones`, `nombre`, `fecha`, `descripcion`, `id_contenido`) VALUES
(1, 'Prueba Relacional', '2026-09-10', 'Evaluacion del modelo relacional', 1),
(2, 'Trabajo SQL', '2026-09-17', 'Desarrollo de consultas SQL', 2),
(3, 'Control Normalizacion', '2026-09-24', 'Ejercicios de normalizacion', 3),
(4, 'Proyecto Integridad', '2026-10-01', 'Aplicacion de integridad de datos', 4);




--Estructura de tabla para la tabla `nota`


CREATE TABLE `nota` (
  `id_nota` int(11) NOT NULL,
  `calificacion` float NOT NULL,
  `fecha` date NOT NULL,
  `id_alumno` int(11) NOT NULL,
  `id_evaluaciones` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_uca1400_ai_ci;


--Volcado de datos para la tabla `nota`


INSERT INTO `nota` (`id_nota`, `calificacion`, `fecha`, `id_alumno`, `id_evaluaciones`) VALUES
(11, 6.5, '2026-09-10', 1, 1),
(13, 6.2, '2026-09-10', 3, 1),
(14, 5.4, '2026-09-10', 4, 1),
(15, 6.8, '2026-09-17', 5, 2),
(16, 4.9, '2026-09-17', 6, 2),
(17, 6, '2026-09-17', 7, 2),
(18, 5.7, '2026-09-24', 8, 3),
(19, 6.9, '2026-09-24', 9, 3),
(20, 6.3, '2026-09-24', 10, 3);



--Estructura de tabla para la tabla `profesor`


CREATE TABLE `profesor` (
  `id_profesor` int(11) NOT NULL,
  `nombre` varchar(50) NOT NULL,
  `correo` varchar(60) NOT NULL,
  `telefono` varchar(18) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_uca1400_ai_ci;


--Volcado de datos para la tabla `profesor`


INSERT INTO `profesor` (`id_profesor`, `nombre`, `correo`, `telefono`) VALUES
(1, '0', '0', '0'),
(2, 'Rory Alveal', 'rory.alveal@correo.cl', '923456701'),
(3, 'Andrea Martinez', 'andrea.martinez@correo.cl', '923456702'),
(4, 'Rodrigo Paredes', 'rodrigo.paredes@correo.cl', '923456703'),
(5, 'Rory Alveal', 'rory.alveal@correo.cl', '923456701'),
(6, 'Andrea Martinez', 'andrea.martinez@correo.cl', '923456702'),
(7, 'Rodrigo Paredes', 'rodrigo.paredes@correo.cl', '923456703');



--Estructura de tabla para la tabla `registro_academico`


CREATE TABLE `registro_academico` (
  `id_registro_academico` int(11) NOT NULL,
  `fecha` date NOT NULL,
  `id_curso` int(11) NOT NULL,
  `id_contenido` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_uca1400_ai_ci;


--Volcado de datos para la tabla `registro_academico`


INSERT INTO `registro_academico` (`id_registro_academico`, `fecha`, `id_curso`, `id_contenido`) VALUES
(1, '2026-09-01', 1, 1),
(2, '2026-09-08', 1, 2),
(3, '2026-09-15', 2, 3),
(4, '2026-09-22', 3, 4);



--Estructura de tabla para la tabla `seccion`


CREATE TABLE `seccion` (
  `id_seccion` int(11) NOT NULL,
  `numero` varchar(35) NOT NULL,
  `cupos` int(11) NOT NULL,
  `id_curso` int(11) NOT NULL,
  `id_asignatura` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_uca1400_ai_ci;


--Volcado de datos para la tabla `seccion`


INSERT INTO `seccion` (`id_seccion`, `numero`, `cupos`, `id_curso`, `id_asignatura`) VALUES
(1, '001', 30, 1, 1),
(2, '002', 25, 2, 2),
(3, '003', 35, 3, 3);




--Indices de la tabla `alumno`

ALTER TABLE `alumno`
  ADD PRIMARY KEY (`id_alumno`),
  ADD KEY `id_curso` (`id_curso`),
  ADD KEY `id_apoderado` (`id_apoderado`),
  ADD KEY `id_seccion` (`id_seccion`);


--Indices de la tabla `apoderado`

ALTER TABLE `apoderado`
  ADD PRIMARY KEY (`id_apoderado`);


--Indices de la tabla `asignatura`

ALTER TABLE `asignatura`
  ADD PRIMARY KEY (`id_asignatura`),
  ADD KEY `id_profesor` (`id_profesor`);


--Indices de la tabla `asistencia`

ALTER TABLE `asistencia`
  ADD PRIMARY KEY (`id_asistencia`),
  ADD KEY `id_alumno` (`id_alumno`),
  ADD KEY `id_clases_prog` (`id_clases_prog`);


--Indices de la tabla `clases_programadas`

ALTER TABLE `clases_programadas`
  ADD PRIMARY KEY (`id_clases_prog`),
  ADD KEY `id_asignatura` (`id_asignatura`),
  ADD KEY `id_seccion` (`id_seccion`);


--Indices de la tabla `contenido`

ALTER TABLE `contenido`
  ADD PRIMARY KEY (`id_contenido`);


--Indices de la tabla `curso`

ALTER TABLE `curso`
  ADD PRIMARY KEY (`id_curso`);


--Indices de la tabla `evaluaciones`

ALTER TABLE `evaluaciones`
  ADD PRIMARY KEY (`id_evaluaciones`),
  ADD KEY `id_contenido` (`id_contenido`);


--Indices de la tabla `nota`

ALTER TABLE `nota`
  ADD PRIMARY KEY (`id_nota`),
  ADD KEY `id_alumno` (`id_alumno`),
  ADD KEY `id_evaluaciones` (`id_evaluaciones`);


--Indices de la tabla `profesor`

ALTER TABLE `profesor`
  ADD PRIMARY KEY (`id_profesor`);


--Indices de la tabla `registro_academico`

ALTER TABLE `registro_academico`
  ADD PRIMARY KEY (`id_registro_academico`),
  ADD KEY `id_curso` (`id_curso`),
  ADD KEY `id_contenido` (`id_contenido`);


--Indices de la tabla `seccion`

ALTER TABLE `seccion`
  ADD PRIMARY KEY (`id_seccion`),
  ADD KEY `id_curso` (`id_curso`),
  ADD KEY `id_asignatura` (`id_asignatura`);





--AUTO_INCREMENT de la tabla `alumno`

ALTER TABLE `alumno`
  MODIFY `id_alumno` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=23;


--AUTO_INCREMENT de la tabla `apoderado`

ALTER TABLE `apoderado`
  MODIFY `id_apoderado` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=21;


--AUTO_INCREMENT de la tabla `asignatura`

ALTER TABLE `asignatura`
  MODIFY `id_asignatura` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;


--AUTO_INCREMENT de la tabla `asistencia`

ALTER TABLE `asistencia`
  MODIFY `id_asistencia` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;


--AUTO_INCREMENT de la tabla `clases_programadas`

ALTER TABLE `clases_programadas`
  MODIFY `id_clases_prog` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;


--AUTO_INCREMENT de la tabla `contenido`

ALTER TABLE `contenido`
  MODIFY `id_contenido` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;


--AUTO_INCREMENT de la tabla `curso`

ALTER TABLE `curso`
  MODIFY `id_curso` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;


--AUTO_INCREMENT de la tabla `evaluaciones`

ALTER TABLE `evaluaciones`
  MODIFY `id_evaluaciones` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;


--AUTO_INCREMENT de la tabla `nota`

ALTER TABLE `nota`
  MODIFY `id_nota` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=21;


--AUTO_INCREMENT de la tabla `profesor`

ALTER TABLE `profesor`
  MODIFY `id_profesor` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;


--AUTO_INCREMENT de la tabla `registro_academico`

ALTER TABLE `registro_academico`
  MODIFY `id_registro_academico` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;


--AUTO_INCREMENT de la tabla `seccion`

ALTER TABLE `seccion`
  MODIFY `id_seccion` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;



--Filtros para la tabla `alumno`

ALTER TABLE `alumno`
  ADD CONSTRAINT `alumno_ibfk_1` FOREIGN KEY (`id_curso`) REFERENCES `curso` (`id_curso`),
  ADD CONSTRAINT `alumno_ibfk_2` FOREIGN KEY (`id_apoderado`) REFERENCES `apoderado` (`id_apoderado`),
  ADD CONSTRAINT `alumno_ibfk_3` FOREIGN KEY (`id_seccion`) REFERENCES `seccion` (`id_seccion`);


--Filtros para la tabla `asignatura`

ALTER TABLE `asignatura`
  ADD CONSTRAINT `asignatura_ibfk_1` FOREIGN KEY (`id_profesor`) REFERENCES `profesor` (`id_profesor`);


--Filtros para la tabla `asistencia`

ALTER TABLE `asistencia`
  ADD CONSTRAINT `asistencia_ibfk_1` FOREIGN KEY (`id_alumno`) REFERENCES `alumno` (`id_alumno`),
  ADD CONSTRAINT `asistencia_ibfk_2` FOREIGN KEY (`id_clases_prog`) REFERENCES `clases_programadas` (`id_clases_prog`);


--Filtros para la tabla `clases_programadas`

ALTER TABLE `clases_programadas`
  ADD CONSTRAINT `clases_programadas_ibfk_1` FOREIGN KEY (`id_asignatura`) REFERENCES `asignatura` (`id_asignatura`),
  ADD CONSTRAINT `clases_programadas_ibfk_2` FOREIGN KEY (`id_seccion`) REFERENCES `seccion` (`id_seccion`);


--Filtros para la tabla `evaluaciones`

ALTER TABLE `evaluaciones`
  ADD CONSTRAINT `evaluaciones_ibfk_1` FOREIGN KEY (`id_contenido`) REFERENCES `contenido` (`id_contenido`);


--Filtros para la tabla `nota`

ALTER TABLE `nota`
  ADD CONSTRAINT `nota_ibfk_1` FOREIGN KEY (`id_alumno`) REFERENCES `alumno` (`id_alumno`),
  ADD CONSTRAINT `nota_ibfk_2` FOREIGN KEY (`id_evaluaciones`) REFERENCES `evaluaciones` (`id_evaluaciones`);


--Filtros para la tabla `registro_academico`

ALTER TABLE `registro_academico`
  ADD CONSTRAINT `registro_academico_ibfk_1` FOREIGN KEY (`id_curso`) REFERENCES `curso` (`id_curso`),
  ADD CONSTRAINT `registro_academico_ibfk_2` FOREIGN KEY (`id_contenido`) REFERENCES `contenido` (`id_contenido`);


--Filtros para la tabla `seccion`

ALTER TABLE `seccion`
  ADD CONSTRAINT `seccion_ibfk_1` FOREIGN KEY (`id_curso`) REFERENCES `curso` (`id_curso`),
  ADD CONSTRAINT `seccion_ibfk_2` FOREIGN KEY (`id_asignatura`) REFERENCES `asignatura` (`id_asignatura`);
COMMIT;


--Para las ñ, tildes, no rompa todo.
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;

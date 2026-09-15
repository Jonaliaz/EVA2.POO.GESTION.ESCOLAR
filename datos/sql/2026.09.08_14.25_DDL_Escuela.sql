create table Periodo_Academico (
    id_periodo_academico int not null auto_increment,
    nombre_periodo_academico varchar(50) not null,
    fecha_inicio date not null,
    fecha_fin date not null,
    primary key (id_periodo_academico)
);
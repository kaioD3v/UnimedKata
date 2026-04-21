CREATE TABLE paciente (
    id        INTEGER      NOT NULL, -- id do paciente
    nome      VARCHAR(120) NOT NULL, -- nome do paciente
    idade     SMALLINT     NOT NULL, -- idade do paciente
    PRIMARY KEY (id)
);

CREATE TABLE fila (
    id         INTEGER   NOT NULL, -- id da fila
    PRIMARY KEY (id)
);

CREATE TABLE paciente_fila (
    id               INTEGER  NOT NULL, -- id da entrada do paciente na fila
    paciente_id      INTEGER  NOT NULL, -- id do paciente
    fila_id          INTEGER  NOT NULL, -- id da fila
    urgencia         SMALLINT NOT NULL, -- urgência original
    urgencia_atualizada SMALLINT NOT NULL, -- urgência atualizada
    chegada          TIME     NOT NULL, -- horário de chegada
    PRIMARY KEY (id),
    UNIQUE (paciente_id, fila_id),
    FOREIGN KEY (paciente_id) REFERENCES paciente (id),
    FOREIGN KEY (fila_id)     REFERENCES fila (id)
);
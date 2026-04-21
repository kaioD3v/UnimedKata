DROP TABLE IF EXISTS `tarefa`; --  DROP TABLE para evitar erros caso a tabela já exista  --

CREATE TABLE `tarefa` (
  `idTarefa` int NOT NULL AUTO_INCREMENT, -- ID da tarefa, chave primária, auto-incrementável --
  `tituloTarefa` varchar(255) NOT NULL, -- Título da tarefa, obrigatório --
  `status` enum('a_fazer','concluida') DEFAULT 'a_fazer', -- Status da tarefa, com valores predefinidos --
  `prioridade` int DEFAULT NULL, -- Prioridade da tarefa, para uma futuro update--
  `criado_em` timestamp NULL DEFAULT CURRENT_TIMESTAMP, -- Data de criação, padrão é a data atual --
  `atualizado_em` timestamp NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Data de atualização, padrão é a data atual --
  PRIMARY KEY (`idTarefa`)
);
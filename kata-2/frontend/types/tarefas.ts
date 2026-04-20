export interface Task {
  idTarefa: number;
  tituloTarefa: string;
  status: string;
  prioridade: number | null;
  criado_em?: string;
  atualizado_em?: string;
}
import tkinter as tk
from tkinter import messagebox
import time
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime

class CronoanaliseTimeline:
    def __init__(self, root):
        self.root = root
        self.root.title("Cronoanálise Timeline")
        self.root.geometry("450x600")
        
        # Estrutura de dados
        self.etapas = ["Setup", "Processando", "Parada Motivo 1", "Parada Motivo 2"]
        self.historico = []  # Lista de dicionários: {'etapa': name, 'inicio': timestamp, 'fim': timestamp}
        self.inicio_atual = None
        self.etapa_atual = None

        # Interface
        tk.Label(root, text="OPERADOR:").pack(pady=2)
        self.ent_op_nome = tk.Entry(root)
        self.ent_op_nome.pack(pady=2)

        tk.Label(root, text="ORDEM DE PRODUÇÃO (OP):").pack(pady=2)
        self.ent_op_num = tk.Entry(root)
        self.ent_op_num.pack(pady=2)

        self.lbl_status = tk.Label(root, text="Status: Aguardando", font=("Arial", 10, "bold"), fg="gray")
        self.lbl_status.pack(pady=15)

        for e in self.etapas:
            btn = tk.Button(root, text=e, width=25, height=2, command=lambda o=e: self.registrar(o))
            btn.pack(pady=3)

        tk.Button(root, text="FINALIZAR E VER LINHA DO TEMPO", bg="blue", fg="white", 
                  font=("Arial", 10, "bold"), command=self.finalizar).pack(pady=20)

    def registrar(self, etapa):
        agora = time.time()
        
        # Se já havia algo rodando, finaliza o evento anterior
        if self.etapa_atual:
            self.historico.append({
                'etapa': self.etapa_atual,
                'inicio': self.inicio_atual,
                'fim': agora
            })
        
        # Se clicou no mesmo botão, ele para. Se clicou em outro, inicia o novo.
        if self.etapa_atual == etapa:
            self.etapa_atual = None
            self.lbl_status.config(text="Status: PAUSADO", fg="red")
        else:
            self.etapa_atual = etapa
            self.inicio_atual = agora
            self.lbl_status.config(text="Ativo: " + etapa.upper(), fg="green")

    def finalizar(self):
        if self.etapa_atual:
            self.historico.append({'etapa': self.etapa_atual, 'inicio': self.inicio_atual, 'fim': time.time()})
            self.etapa_atual = None

        if not self.historico:
            messagebox.showwarning("Aviso", "Nenhum dado registrado!")
            return

        self.salvar_txt()
        self.gerar_grafico_timeline()

    def salvar_txt(self):
        op = self.ent_op_num.get() or "SemOP"
        nome_arq = "Timeline_OP_" + op + ".txt"
        with open(nome_arq, "w") as f:
            f.write("RELATORIO DETALHADO DE EVENTOS\n")
            f.write("OP: " + op + " | Data: " + datetime.now().strftime("%d/%m/%Y") + "\n\n")
            for h in self.historico:
                ini = datetime.fromtimestamp(h['inicio']).strftime('%H:%M:%S')
                fim = datetime.fromtimestamp(h['fim']).strftime('%H:%M:%S')
                duracao = round((h['fim'] - h['inicio']), 2)
                f.write(ini + " ate " + fim + " | " + h['etapa'] + " (" + str(duracao) + "s)\n")
        messagebox.showinfo("Sucesso", "Relatorio salvo como " + nome_arq)

    def gerar_grafico_timeline(self):
        fig, ax = plt.subplots(figsize=(10, 5))
        
        cores = {"Setup": "blue", "Processando": "green", "Parada Motivo 1": "red", "Parada Motivo 2": "purple"}
        
        for i, h in enumerate(self.historico):
            ini = mdates.date2num(datetime.fromtimestamp(h['inicio']))
            fim = mdates.date2num(datetime.fromtimestamp(h['fim']))
            ax.barh(h['etapa'], fim - ini, left=ini, color=cores.get(h['etapa'], "gray"), edgecolor='black')

        # Formatação do eixo de tempo
        ax.xaxis_date()
        ax.xaxis.set_major_formatter(mdates.DateFormatter('%H:%M:%S'))
        plt.title("Linha do Tempo do Processo - OP: " + self.ent_op_num.get())
        plt.xlabel("Horário")
        plt.grid(axis='x', linestyle='--', alpha=0.6)
        plt.tight_layout()
        plt.show()

if __name__ == "__main__":
    root = tk.Tk()
    app = CronoanaliseTimeline(root)
    root.mainloop()

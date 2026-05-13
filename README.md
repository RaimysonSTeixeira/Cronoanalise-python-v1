# Cronoanálise Process Timeline (v1 - Python Desktop)

## 📋 Sobre o Projeto

Em ambientes industriais sem infraestrutura de TI, a cronoanálise de processo era feita com papel, caneta e planilha manual — sujeita a erro de anotação, perda de dado e ausência de visualização.

Este projeto nasceu para resolver isso: uma ferramenta desktop que o operador usa em tempo real para registrar cada etapa da produção (Setup, Processamento, Paradas), gerando automaticamente uma linha do tempo visual e um relatório exportável.

Desenvolvida para funcionar offline, sem dependência de servidor ou internet.

## ✨ Funcionalidades

- **Registro de Eventos:** Captura precisa de horários de início e fim por categoria
- **Visualização Gantt:** Linha do tempo gerada automaticamente com `Matplotlib`
- **Relatório Detalhado:** Exportação de log em `.txt` para análise posterior

## 🛠️ Tecnologias

- **Python** — lógica principal
- **Tkinter** — interface gráfica desktop
- **Matplotlib** — renderização do gráfico de Gantt

## 📸 Demonstração

![Screenshot do Sistema](assets/image_crono.png)

## 🚀 Evolução do Projeto

Esta versão desktop foi o ponto de partida. O problema que ela resolve — coletar e visualizar tempos de processo em campo — foi evoluindo em complexidade:

- **V1 (este repositório):** aplicação Python local, sem servidor, funciona offline
- **V2:** sistema embarcado em Raspberry Pi configurado como access point Wi-Fi, permitindo múltiplos operadores simultâneos sem internet
- **V3 (atual):** plataforma web com Next.js, Supabase e Vercel — operadores registram pelo navegador, gestor acessa os dados remotamente em tempo real

→ Repositório da versão web: (repositório privado — em revisão de segurança)

## ⚙️ Como executar

```bash
pip install -r requirements.txt
python cronoanalise.py
```

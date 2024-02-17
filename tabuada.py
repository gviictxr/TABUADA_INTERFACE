import tkinter as tk

def gerar_tabuada():
    num = int(entry.get())
    resultado_text.delete(1.0, tk.END)  

    resultado_text.insert(tk.END, f"Tabuada do {num}:\n\n")
    for i in range(1, 11):
        resultado = num * i
        resultado_text.insert(tk.END, f"{num} x {i} = {resultado}\n")

def limpar_resultado():
    entry.delete(0, tk.END)
    resultado_text.delete(1.0, tk.END)

janela = tk.Tk()
janela.title("Tabuada Generator")

label = tk.Label(janela, text="Informe um número inteiro:")
label.pack(pady=10)
entry = tk.Entry(janela)
entry.pack(pady=10)

botao_gerar = tk.Button(janela, text="Gerar Tabuada", command=gerar_tabuada)
botao_gerar.pack(pady=10)

botao_limpar = tk.Button(janela, text="Limpar", command=limpar_resultado)
botao_limpar.pack(pady=10)

resultado_text = tk.Text(janela, height=15, width=30)  # Aumentei o número de linhas visíveis
resultado_text.pack(pady=10)

entry.bind('<Return>', lambda event=None: gerar_tabuada())

janela.mainloop()

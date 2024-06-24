import tkinter as tk
import tkinter.font as font
import tkinter.ttk as ttk
import pandas as pd
import numpy as np
import xlsxwriter as sl
import subprocess
import sys

from tkinter import *

from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
from matplotlib.figure import Figure

data = pd.read_excel(r'DOCS/tabela_perfis.xlsx')
dada_numérico=data.values
dados=dada_numérico[2:120,2:24]


# =============================================================================
# =============================================================================
# # # =========================================================================
# # # # ############# ESCREVE A FRAME DOS TRECHOS NA DIREITA ##################
# # # =========================================================================
# =============================================================================
# =============================================================================

def FUNC_JANELA_ERRO(): 
    global texto_erro , texto_erro1 , texto_erro2 , texto_erro3 , texto_erro4 , texto_erro5 , texto_erro6 
   
    def  destroy_janela_erro():
        janela_erro.destroy()
        
       
    janela_erro= tk.Tk()
    
    font9 = "-family {Segoe UI} -size 12"
    janela_erro.geometry("500x200+500+300")
    janela_erro.minsize(148, 1)
    janela_erro.maxsize(1924, 1055)
    janela_erro.resizable(1, 1)
    janela_erro.title("Error")
    janela_erro.iconbitmap('icones/geral.ico')
    janela_erro.configure(background="#d9d9d9")
    janela_erro.configure(highlightbackground="#d9d9d9")
    janela_erro.configure(highlightcolor="black")

    btn_sair_janela_erro = tk.Button(janela_erro)
    btn_sair_janela_erro.place(relx=0.418, rely=0.7, height=50, width=100)
    btn_sair_janela_erro.configure(activebackground="#bd0000")
    btn_sair_janela_erro.configure(activeforeground="white")
    btn_sair_janela_erro.configure(activeforeground="#ff0000")
    btn_sair_janela_erro.configure(background="#ff0000")
    btn_sair_janela_erro.configure(disabledforeground="#a3a3a3")
    btn_sair_janela_erro.configure(font=font9)
    btn_sair_janela_erro.configure(foreground="#000000")
    btn_sair_janela_erro.configure(highlightbackground="#d9d9d9")
    btn_sair_janela_erro.configure(highlightcolor="black")
    btn_sair_janela_erro.configure(pady="0")
    btn_sair_janela_erro.configure(text='''Exit''')
    btn_sair_janela_erro.configure(command=destroy_janela_erro)
    

    txt_erro = tk.Text(janela_erro)
    txt_erro.place(relx=0.02, rely=0.05, relheight=0.6, relwidth=0.96)
    txt_erro.configure(background="#ff8a8a")
    txt_erro.configure(font="TkTextFont")
    txt_erro.configure(foreground="black")
    txt_erro.configure(highlightbackground="#d9d9d9")
    txt_erro.configure(highlightcolor="black")
    txt_erro.configure(insertbackground="black")
    txt_erro.configure(selectbackground="#c4c4c4")
    txt_erro.configure(selectforeground="black")
    txt_erro.configure(wrap="char")
    
    
    for n in range(len(texto_erro)):
        if (n>0):                                   # pula o primeiro pq é a descrição
            txt_erro.insert(END,"%d - "%(n))        # imprime o numeral 
        txt_erro.insert(END,texto_erro[n])

    janela_erro.mainloop()


def escreve_frame_trechos():
    # =============================================================================
    # FRAME 1- TRECHOS
    # =============================================================================
    _x_="<x<"
    

    Frame1 = tk.Frame(janela_geral)
    Frame1.place(relx=0.827, rely=0.013, relheight=0.975, relwidth=0.167)
    Frame1.configure(relief='groove')
    Frame1.configure(borderwidth="2")
    Frame1.configure(relief="groove")
    Frame1.configure(background="#d9d9d9")
    Frame1.configure(highlightbackground="#d9d9d9")
    Frame1.configure(highlightcolor="black")
    
    #       FRAME TRECHO 01
    
    msd_max_1=round(-1*MM[int(x_VV0[0]*100)],2)
    vsd_max_1=round(VV[0],2)
    
    Frame1_1 = tk.Frame(Frame1)
    Frame1_1.place(relx=0.02, rely=0.006, relheight=0.191, relwidth=0.96)
    Frame1_1.configure(relief='groove')
    Frame1_1.configure(borderwidth="2")
    Frame1_1.configure(relief="groove")
    Frame1_1.configure(background="#d9d9d9")
    Frame1_1.configure(highlightbackground="#d9d9d9")
    Frame1_1.configure(highlightcolor="black")
    
    la_trecho_01 = tk.Label(Frame1_1)
    la_trecho_01.place(relx=0.046, rely=0.067, height=22, width=103)
    la_trecho_01.configure(activebackground="#f9f9f9")
    la_trecho_01.configure(activeforeground="black")
    la_trecho_01.configure(background="#d9d9d9")
    la_trecho_01.configure(disabledforeground="#a3a3a3")
    la_trecho_01.configure(font="-family {Segoe UI} -size 10 -weight bold")
    la_trecho_01.configure(foreground="#000000")
    la_trecho_01.configure(highlightbackground="#d9d9d9")
    la_trecho_01.configure(highlightcolor="black")
    la_trecho_01.configure(text='''Region 01''')
    
    la_trecho_01_posicao = tk.Label(Frame1_1)
    la_trecho_01_posicao.place(relx=0.504, rely=0.054, height=22, width=83)
    la_trecho_01_posicao.configure(activebackground="#f9f9f9")
    la_trecho_01_posicao.configure(activeforeground="black")
    la_trecho_01_posicao.configure(background="#d9d9d9")
    la_trecho_01_posicao.configure(disabledforeground="#a3a3a3")
    la_trecho_01_posicao.configure(font="-family {Segoe UI} -size 10 -weight bold")
    la_trecho_01_posicao.configure(foreground="#000000")
    la_trecho_01_posicao.configure(highlightbackground="#d9d9d9")
    la_trecho_01_posicao.configure(highlightcolor="black")
    la_trecho_01_posicao.configure(text=(x_MM0[0],_x_,x_MM0[1]))
    
    la_trecho_01_n_con = tk.Label(Frame1_1)
    la_trecho_01_n_con.place(relx=0.042, rely=0.228, height=22, width=121)
    la_trecho_01_n_con.configure(activebackground="#f9f9f9")
    la_trecho_01_n_con.configure(activeforeground="black")
    la_trecho_01_n_con.configure(background="#d9d9d9")
    la_trecho_01_n_con.configure(disabledforeground="#a3a3a3")
    la_trecho_01_n_con.configure(foreground="#000000")
    la_trecho_01_n_con.configure(highlightbackground="#d9d9d9")
    la_trecho_01_n_con.configure(highlightcolor="black")
    la_trecho_01_n_con.configure(text='''Number of Studs=''')
    
    la_trecho_01_VA_n_con = tk.Label(Frame1_1)
    la_trecho_01_VA_n_con.place(relx=0.546, rely=0.228, height=22, width=46)
    la_trecho_01_VA_n_con.configure(activebackground="#f9f9f9")
    la_trecho_01_VA_n_con.configure(activeforeground="black")
    la_trecho_01_VA_n_con.configure(background="#f1f1f1")
    la_trecho_01_VA_n_con.configure(disabledforeground="#a3a3a3")
    la_trecho_01_VA_n_con.configure(foreground="#000000")
    la_trecho_01_VA_n_con.configure(highlightbackground="#d9d9d9")
    la_trecho_01_VA_n_con.configure(highlightcolor="black")
    la_trecho_01_VA_n_con.configure(text=n_con[0])
    
    la_trecho_01_esp = tk.Label(Frame1_1)
    la_trecho_01_esp.place(relx=0.042, rely=0.396, height=22, width=75)
    
    la_trecho_01_esp.configure(activebackground="#f9f9f9")
    la_trecho_01_esp.configure(activeforeground="black")
    la_trecho_01_esp.configure(background="#d9d9d9")
    la_trecho_01_esp.configure(disabledforeground="#a3a3a3")
    la_trecho_01_esp.configure(foreground="#000000")
    la_trecho_01_esp.configure(highlightbackground="#d9d9d9")
    la_trecho_01_esp.configure(highlightcolor="black")
    la_trecho_01_esp.configure(text='''Spacing=''')
    
    la_trecho_01_VA_esp = tk.Label(Frame1_1)
    la_trecho_01_VA_esp.place(relx=0.546, rely=0.396, height=22, width=46)
    la_trecho_01_VA_esp.configure(activebackground="#f9f9f9")
    la_trecho_01_VA_esp.configure(activeforeground="black")
    la_trecho_01_VA_esp.configure(background="#f1f1f1")
    la_trecho_01_VA_esp.configure(disabledforeground="#a3a3a3")
    la_trecho_01_VA_esp.configure(foreground="#000000")
    la_trecho_01_VA_esp.configure(highlightbackground="#d9d9d9")
    la_trecho_01_VA_esp.configure(highlightcolor="black")
    la_trecho_01_VA_esp.configure(text=round(espac[0],3))
    
    la_trecho_01_mrd = tk.Label(Frame1_1)
    la_trecho_01_mrd.place(relx=0.083, rely=0.564, height=22, width=48)
    la_trecho_01_mrd.configure(activebackground="#f9f9f9")
    la_trecho_01_mrd.configure(activeforeground="black")
    la_trecho_01_mrd.configure(background="#d9d9d9")
    la_trecho_01_mrd.configure(disabledforeground="#a3a3a3")
    la_trecho_01_mrd.configure(foreground="#000000")
    la_trecho_01_mrd.configure(highlightbackground="#d9d9d9")
    la_trecho_01_mrd.configure(highlightcolor="black")
    la_trecho_01_mrd.configure(text='''Mᵤ=''')
    
    la_trecho_01_VA_mrd = tk.Label(Frame1_1)
    la_trecho_01_VA_mrd.place(relx=0.279, rely=0.564, height=22, width=58)
    la_trecho_01_VA_mrd.configure(activebackground="#f9f9f9")
    la_trecho_01_VA_mrd.configure(activeforeground="black")
    la_trecho_01_VA_mrd.configure(background="#f1f1f1")
    la_trecho_01_VA_mrd.configure(disabledforeground="#a3a3a3")
    la_trecho_01_VA_mrd.configure(foreground="#000000")
    la_trecho_01_VA_mrd.configure(highlightbackground="#d9d9d9")
    la_trecho_01_VA_mrd.configure(highlightcolor="black")
    la_trecho_01_VA_mrd.configure(text=round(Mrd[0],1))
    
    la_trecho_01_msd = tk.Label(Frame1_1)
    la_trecho_01_msd.place(relx=0.508, rely=0.564, height=22, width=48)
    la_trecho_01_msd.configure(activebackground="#f9f9f9")
    la_trecho_01_msd.configure(activeforeground="black")
    la_trecho_01_msd.configure(background="#d9d9d9")
    la_trecho_01_msd.configure(disabledforeground="#a3a3a3")
    la_trecho_01_msd.configure(foreground="#000000")
    la_trecho_01_msd.configure(highlightbackground="#d9d9d9")
    la_trecho_01_msd.configure(highlightcolor="black")
    la_trecho_01_msd.configure(text='''Mᵣ=''')

    la_trecho_01_VA_msd = tk.Label(Frame1_1)
    la_trecho_01_VA_msd.place(relx=0.696, rely=0.564, height=22, width=46)
    la_trecho_01_VA_msd.configure(activebackground="#f9f9f9")
    la_trecho_01_VA_msd.configure(activeforeground="black")
    la_trecho_01_VA_msd.configure(background="#f1f1f1")
    la_trecho_01_VA_msd.configure(disabledforeground="#a3a3a3")
    la_trecho_01_VA_msd.configure(foreground="#000000")
    la_trecho_01_VA_msd.configure(highlightbackground="#d9d9d9")
    la_trecho_01_VA_msd.configure(highlightcolor="black")
    la_trecho_01_VA_msd.configure(text=msd_max_1)
    
    la_trecho_01_vrd = tk.Label(Frame1_1)
    la_trecho_01_vrd.place(relx=0.092, rely=0.732, height=22, width=41)
    la_trecho_01_vrd.configure(activebackground="#f9f9f9")
    la_trecho_01_vrd.configure(activeforeground="black")
    la_trecho_01_vrd.configure(background="#d9d9d9")
    la_trecho_01_vrd.configure(disabledforeground="#a3a3a3")
    la_trecho_01_vrd.configure(foreground="#000000")
    la_trecho_01_vrd.configure(highlightbackground="#d9d9d9")
    la_trecho_01_vrd.configure(highlightcolor="black")
    la_trecho_01_vrd.configure(text='''Vᵤ=''')
    
    la_trecho_01_vsd = tk.Label(Frame1_1)
    la_trecho_01_vsd.place(relx=0.533, rely=0.738, height=22, width=41)
    la_trecho_01_vsd.configure(activebackground="#f9f9f9")
    la_trecho_01_vsd.configure(activeforeground="black")
    la_trecho_01_vsd.configure(background="#d9d9d9")
    la_trecho_01_vsd.configure(disabledforeground="#a3a3a3")
    la_trecho_01_vsd.configure(foreground="#000000")
    la_trecho_01_vsd.configure(highlightbackground="#d9d9d9")
    la_trecho_01_vsd.configure(highlightcolor="black")
    la_trecho_01_vsd.configure(justify='left')
    la_trecho_01_vsd.configure(text='''Vᵣ=''')
    
    la_trecho_01_VA_vrd = tk.Label(Frame1_1)
    la_trecho_01_VA_vrd.place(relx=0.279, rely=0.732, height=22, width=54)
    la_trecho_01_VA_vrd.configure(activebackground="#f9f9f9")
    la_trecho_01_VA_vrd.configure(activeforeground="black")
    la_trecho_01_VA_vrd.configure(background="#f1f1f1")
    la_trecho_01_VA_vrd.configure(disabledforeground="#a3a3a3")
    la_trecho_01_VA_vrd.configure(foreground="#000000")
    la_trecho_01_VA_vrd.configure(highlightbackground="#d9d9d9")
    la_trecho_01_VA_vrd.configure(highlightcolor="black")
    la_trecho_01_VA_vrd.configure(text=round(Vrd,1))
    
    la_trecho_01_VA_vsd = tk.Label(Frame1_1)
    la_trecho_01_VA_vsd.place(relx=0.696, rely=0.732, height=22, width=46)
    la_trecho_01_VA_vsd.configure(activebackground="#f9f9f9")
    la_trecho_01_VA_vsd.configure(activeforeground="black")
    la_trecho_01_VA_vsd.configure(background="#f1f1f1")
    la_trecho_01_VA_vsd.configure(disabledforeground="#a3a3a3")
    la_trecho_01_VA_vsd.configure(foreground="#000000")
    la_trecho_01_VA_vsd.configure(highlightbackground="#d9d9d9")
    la_trecho_01_VA_vsd.configure(highlightcolor="black")
    la_trecho_01_VA_vsd.configure(text=vsd_max_1)
    
    #       FRAME TRECHO 02
    if (trechos>=2):
        
        msd_max_2=-round(MM[int(L[1]*100)],2)
        msd_max_3=-round(MM[int(x_VV0[1]*100)],2)
        
        
        vsd_max_2=round(max(abs((VV[int(L[1]*100-2):int(L[1]*100+1)]))),2)
        vsd_max_3=round(max(abs(VV[int(x_MM0[2]*100):int(x_MM0[3]*100)])),2)
        
        
        
        Frame1_2 = tk.Frame(Frame1)
        Frame1_2.place(relx=0.02, rely=0.205, relheight=0.191, relwidth=0.96)
        Frame1_2.configure(relief='groove')
        Frame1_2.configure(borderwidth="2")
        Frame1_2.configure(relief="groove")
        Frame1_2.configure(background="#d9d9d9")
        Frame1_2.configure(highlightbackground="#d9d9d9")
        Frame1_2.configure(highlightcolor="black")
        
        latrecho_2 = tk.Label(Frame1_2)
        latrecho_2.place(relx=0.042, rely=0.067, height=22, width=103)
        latrecho_2.configure(activebackground="#f9f9f9")
        latrecho_2.configure(activeforeground="black")
        latrecho_2.configure(background="#d9d9d9")
        latrecho_2.configure(disabledforeground="#a3a3a3")
        latrecho_2.configure(font="-family {Segoe UI} -size 10 -weight bold")
        latrecho_2.configure(foreground="#000000")
        latrecho_2.configure(highlightbackground="#d9d9d9")
        latrecho_2.configure(highlightcolor="black")
        latrecho_2.configure(text='''Region 02''')
        
        la_trecho_02_posicao = tk.Label(Frame1_2)
        la_trecho_02_posicao.place(relx=0.504, rely=0.054, height=22, width=83)
        la_trecho_02_posicao.configure(activebackground="#f9f9f9")
        la_trecho_02_posicao.configure(activeforeground="black")
        la_trecho_02_posicao.configure(background="#d9d9d9")
        la_trecho_02_posicao.configure(disabledforeground="#a3a3a3")
        la_trecho_02_posicao.configure(font="-family {Segoe UI} -size 10 -weight bold")
        la_trecho_02_posicao.configure(foreground="#000000")
        la_trecho_02_posicao.configure(highlightbackground="#d9d9d9")
        la_trecho_02_posicao.configure(highlightcolor="black")
        la_trecho_02_posicao.configure(text=(x_MM0[1],_x_,x_MM0[2]))
        
        la_trecho_02_n_con = tk.Label(Frame1_2)
        la_trecho_02_n_con.place(relx=0.042, rely=0.228, height=22, width=121)
        la_trecho_02_n_con.configure(activebackground="#f9f9f9")
        la_trecho_02_n_con.configure(activeforeground="black")
        la_trecho_02_n_con.configure(background="#d9d9d9")
        la_trecho_02_n_con.configure(disabledforeground="#a3a3a3")
        la_trecho_02_n_con.configure(foreground="#000000")
        la_trecho_02_n_con.configure(highlightbackground="#d9d9d9")
        la_trecho_02_n_con.configure(highlightcolor="black")
        la_trecho_02_n_con.configure(text='''Number of Studs=''')
        
        la_trecho_02_VA_n_con = tk.Label(Frame1_2)
        la_trecho_02_VA_n_con.place(relx=0.546, rely=0.228, height=22, width=46)
        la_trecho_02_VA_n_con.configure(activebackground="#f9f9f9")
        la_trecho_02_VA_n_con.configure(activeforeground="black")
        la_trecho_02_VA_n_con.configure(background="#f1f1f1")
        la_trecho_02_VA_n_con.configure(disabledforeground="#a3a3a3")
        la_trecho_02_VA_n_con.configure(foreground="#000000")
        la_trecho_02_VA_n_con.configure(highlightbackground="#d9d9d9")
        la_trecho_02_VA_n_con.configure(highlightcolor="black")
        la_trecho_02_VA_n_con.configure(text=n_con[1])
        
        la_trecho_02_esp = tk.Label(Frame1_2)
        la_trecho_02_esp.place(relx=0.000, rely=0.396, height=22, width=75)
        
        la_trecho_02_esp.configure(activebackground="#f9f9f9")
        la_trecho_02_esp.configure(activeforeground="black")
        la_trecho_02_esp.configure(background="#d9d9d9")
        la_trecho_02_esp.configure(disabledforeground="#a3a3a3")
        la_trecho_02_esp.configure(foreground="#000000")
        la_trecho_02_esp.configure(highlightbackground="#d9d9d9")
        la_trecho_02_esp.configure(highlightcolor="black")
        la_trecho_02_esp.configure(text='''Spacing=''')
        
        la_trecho_02_VA_esp = tk.Label(Frame1_2)
        la_trecho_02_VA_esp.place(relx=0.546, rely=0.396, height=22, width=46)
        la_trecho_02_VA_esp.configure(activebackground="#f9f9f9")
        la_trecho_02_VA_esp.configure(activeforeground="black")
        la_trecho_02_VA_esp.configure(background="#f1f1f1")
        la_trecho_02_VA_esp.configure(disabledforeground="#a3a3a3")
        la_trecho_02_VA_esp.configure(foreground="#000000")
        la_trecho_02_VA_esp.configure(highlightbackground="#d9d9d9")
        la_trecho_02_VA_esp.configure(highlightcolor="black")
        la_trecho_02_VA_esp.configure(text=round(espac[1],3))
        
        la_trecho_02_mrd = tk.Label(Frame1_2)
        la_trecho_02_mrd.place(relx=0.083, rely=0.564, height=22, width=48)
        la_trecho_02_mrd.configure(activebackground="#f9f9f9")
        la_trecho_02_mrd.configure(activeforeground="black")
        la_trecho_02_mrd.configure(background="#d9d9d9")
        la_trecho_02_mrd.configure(disabledforeground="#a3a3a3")
        la_trecho_02_mrd.configure(foreground="#000000")
        la_trecho_02_mrd.configure(highlightbackground="#d9d9d9")
        la_trecho_02_mrd.configure(highlightcolor="black")
        la_trecho_02_mrd.configure(text='''Mᵤ=''')
        
        la_trecho_02_VA_mrd = tk.Label(Frame1_2)
        la_trecho_02_VA_mrd.place(relx=0.279, rely=0.564, height=22, width=58)
        la_trecho_02_VA_mrd.configure(activebackground="#f9f9f9")
        la_trecho_02_VA_mrd.configure(activeforeground="black")
        la_trecho_02_VA_mrd.configure(background="#f1f1f1")
        la_trecho_02_VA_mrd.configure(disabledforeground="#a3a3a3")
        la_trecho_02_VA_mrd.configure(foreground="#000000")
        la_trecho_02_VA_mrd.configure(highlightbackground="#d9d9d9")
        la_trecho_02_VA_mrd.configure(highlightcolor="black")
        la_trecho_02_VA_mrd.configure(text=round(Mrd[1],1))
        
        la_trecho_02_msd = tk.Label(Frame1_2)
        la_trecho_02_msd.place(relx=0.508, rely=0.564, height=22, width=48)
        la_trecho_02_msd.configure(activebackground="#f9f9f9")
        la_trecho_02_msd.configure(activeforeground="black")
        la_trecho_02_msd.configure(background="#d9d9d9")
        la_trecho_02_msd.configure(disabledforeground="#a3a3a3")
        la_trecho_02_msd.configure(foreground="#000000")
        la_trecho_02_msd.configure(highlightbackground="#d9d9d9")
        la_trecho_02_msd.configure(highlightcolor="black")
        la_trecho_02_msd.configure(text='''Mᵣ=''')
        
        la_trecho_02_VA_msd = tk.Label(Frame1_2)
        la_trecho_02_VA_msd.place(relx=0.696, rely=0.564, height=22, width=46)
        la_trecho_02_VA_msd.configure(activebackground="#f9f9f9")
        la_trecho_02_VA_msd.configure(activeforeground="black")
        la_trecho_02_VA_msd.configure(background="#f1f1f1")
        la_trecho_02_VA_msd.configure(disabledforeground="#a3a3a3")
        la_trecho_02_VA_msd.configure(foreground="#000000")
        la_trecho_02_VA_msd.configure(highlightbackground="#d9d9d9")
        la_trecho_02_VA_msd.configure(highlightcolor="black")
        la_trecho_02_VA_msd.configure(text=msd_max_2)
        
        la_trecho_02_vrd = tk.Label(Frame1_2)
        la_trecho_02_vrd.place(relx=0.092, rely=0.732, height=22, width=41)
        la_trecho_02_vrd.configure(activebackground="#f9f9f9")
        la_trecho_02_vrd.configure(activeforeground="black")
        la_trecho_02_vrd.configure(background="#d9d9d9")
        la_trecho_02_vrd.configure(disabledforeground="#a3a3a3")
        la_trecho_02_vrd.configure(foreground="#000000")
        la_trecho_02_vrd.configure(highlightbackground="#d9d9d9")
        la_trecho_02_vrd.configure(highlightcolor="black")
        la_trecho_02_vrd.configure(text='''Vᵤ=''')
        
        la_trecho_02_vsd = tk.Label(Frame1_2)
        la_trecho_02_vsd.place(relx=0.533, rely=0.738, height=22, width=41)
        la_trecho_02_vsd.configure(activebackground="#f9f9f9")
        la_trecho_02_vsd.configure(activeforeground="black")
        la_trecho_02_vsd.configure(background="#d9d9d9")
        la_trecho_02_vsd.configure(disabledforeground="#a3a3a3")
        la_trecho_02_vsd.configure(foreground="#000000")
        la_trecho_02_vsd.configure(highlightbackground="#d9d9d9")
        la_trecho_02_vsd.configure(highlightcolor="black")
        la_trecho_02_vsd.configure(justify='left')
        la_trecho_02_vsd.configure(text='''Vᵣ=''')
        
        la_trecho_02_VA_vrd = tk.Label(Frame1_2)
        la_trecho_02_VA_vrd.place(relx=0.279, rely=0.732, height=22, width=54)
        la_trecho_02_VA_vrd.configure(activebackground="#f9f9f9")
        la_trecho_02_VA_vrd.configure(activeforeground="black")
        la_trecho_02_VA_vrd.configure(background="#f1f1f1")
        la_trecho_02_VA_vrd.configure(disabledforeground="#a3a3a3")
        la_trecho_02_VA_vrd.configure(foreground="#000000")
        la_trecho_02_VA_vrd.configure(highlightbackground="#d9d9d9")
        la_trecho_02_VA_vrd.configure(highlightcolor="black")
        la_trecho_02_VA_vrd.configure(text=round(Vrd,1))
        
        la_trecho_02_VA_vsd = tk.Label(Frame1_2)
        la_trecho_02_VA_vsd.place(relx=0.696, rely=0.732, height=22, width=46)
        la_trecho_02_VA_vsd.configure(activebackground="#f9f9f9")
        la_trecho_02_VA_vsd.configure(activeforeground="black")
        la_trecho_02_VA_vsd.configure(background="#f1f1f1")
        la_trecho_02_VA_vsd.configure(disabledforeground="#a3a3a3")
        la_trecho_02_VA_vsd.configure(foreground="#000000")
        la_trecho_02_VA_vsd.configure(highlightbackground="#d9d9d9")
        la_trecho_02_VA_vsd.configure(highlightcolor="black")
        la_trecho_02_VA_vsd.configure(text=vsd_max_2)
    
    #       FRAME TRECHO 03

        Frame1_3 = tk.Frame(Frame1)
        Frame1_3.place(relx=0.02, rely=0.404, relheight=0.191, relwidth=0.96)
        Frame1_3.configure(relief='groove')
        Frame1_3.configure(borderwidth="2")
        Frame1_3.configure(relief="groove")
        Frame1_3.configure(background="#d9d9d9")
        Frame1_3.configure(highlightbackground="#d9d9d9")
        Frame1_3.configure(highlightcolor="black")
        
        latrecho_3 = tk.Label(Frame1_3)
        latrecho_3.place(relx=0.046, rely=0.067, height=22, width=103)
        latrecho_3.configure(activebackground="#f9f9f9")
        latrecho_3.configure(activeforeground="black")
        latrecho_3.configure(background="#d9d9d9")
        latrecho_3.configure(disabledforeground="#a3a3a3")
        latrecho_3.configure(font="-family {Segoe UI} -size 10 -weight bold")
        latrecho_3.configure(foreground="#000000")
        latrecho_3.configure(highlightbackground="#d9d9d9")
        latrecho_3.configure(highlightcolor="black")
        latrecho_3.configure(text='''Region 03''')
        
        la_trecho_03_posicao = tk.Label(Frame1_3)
        la_trecho_03_posicao.place(relx=0.504, rely=0.054, height=22, width=83)
        la_trecho_03_posicao.configure(activebackground="#f9f9f9")
        la_trecho_03_posicao.configure(activeforeground="black")
        la_trecho_03_posicao.configure(background="#d9d9d9")
        la_trecho_03_posicao.configure(disabledforeground="#a3a3a3")
        la_trecho_03_posicao.configure(font="-family {Segoe UI} -size 10 -weight bold")
        la_trecho_03_posicao.configure(foreground="#000000")
        la_trecho_03_posicao.configure(highlightbackground="#d9d9d9")
        la_trecho_03_posicao.configure(highlightcolor="black")
        la_trecho_03_posicao.configure(text=(x_MM0[2],_x_,x_MM0[3]))
        
        la_trecho_03_n_con = tk.Label(Frame1_3)
        la_trecho_03_n_con.place(relx=0.042, rely=0.228, height=22, width=121)
        la_trecho_03_n_con.configure(activebackground="#f9f9f9")
        la_trecho_03_n_con.configure(activeforeground="black")
        la_trecho_03_n_con.configure(background="#d9d9d9")
        la_trecho_03_n_con.configure(disabledforeground="#a3a3a3")
        la_trecho_03_n_con.configure(foreground="#000000")
        la_trecho_03_n_con.configure(highlightbackground="#d9d9d9")
        la_trecho_03_n_con.configure(highlightcolor="black")
        la_trecho_03_n_con.configure(text='''Number of Studs=''')
        
        la_trecho_03_VA_n_con = tk.Label(Frame1_3)
        la_trecho_03_VA_n_con.place(relx=0.546, rely=0.228, height=22, width=46)
        la_trecho_03_VA_n_con.configure(activebackground="#f9f9f9")
        la_trecho_03_VA_n_con.configure(activeforeground="black")
        la_trecho_03_VA_n_con.configure(background="#f1f1f1")
        la_trecho_03_VA_n_con.configure(disabledforeground="#a3a3a3")
        la_trecho_03_VA_n_con.configure(foreground="#000000")
        la_trecho_03_VA_n_con.configure(highlightbackground="#d9d9d9")
        la_trecho_03_VA_n_con.configure(highlightcolor="black")
        la_trecho_03_VA_n_con.configure(text=n_con[2])
        
        la_trecho_03_esp = tk.Label(Frame1_3)
        la_trecho_03_esp.place(relx=0.042, rely=0.396, height=22, width=75)
        
        la_trecho_03_esp.configure(activebackground="#f9f9f9")
        la_trecho_03_esp.configure(activeforeground="black")
        la_trecho_03_esp.configure(background="#d9d9d9")
        la_trecho_03_esp.configure(disabledforeground="#a3a3a3")
        la_trecho_03_esp.configure(foreground="#000000")
        la_trecho_03_esp.configure(highlightbackground="#d9d9d9")
        la_trecho_03_esp.configure(highlightcolor="black")
        la_trecho_03_esp.configure(text='''Spacing=''')
        
        la_trecho_03_VA_esp = tk.Label(Frame1_3)
        la_trecho_03_VA_esp.place(relx=0.546, rely=0.396, height=22, width=46)
        la_trecho_03_VA_esp.configure(activebackground="#f9f9f9")
        la_trecho_03_VA_esp.configure(activeforeground="black")
        la_trecho_03_VA_esp.configure(background="#f1f1f1")
        la_trecho_03_VA_esp.configure(disabledforeground="#a3a3a3")
        la_trecho_03_VA_esp.configure(foreground="#000000")
        la_trecho_03_VA_esp.configure(highlightbackground="#d9d9d9")
        la_trecho_03_VA_esp.configure(highlightcolor="black")
        la_trecho_03_VA_esp.configure(text=round(espac[2],3))
        
        la_trecho_03_mrd = tk.Label(Frame1_3)
        la_trecho_03_mrd.place(relx=0.083, rely=0.564, height=22, width=48)
        la_trecho_03_mrd.configure(activebackground="#f9f9f9")
        la_trecho_03_mrd.configure(activeforeground="black")
        la_trecho_03_mrd.configure(background="#d9d9d9")
        la_trecho_03_mrd.configure(disabledforeground="#a3a3a3")
        la_trecho_03_mrd.configure(foreground="#000000")
        la_trecho_03_mrd.configure(highlightbackground="#d9d9d9")
        la_trecho_03_mrd.configure(highlightcolor="black")
        la_trecho_03_mrd.configure(text='''Mᵤ=''')
        
        la_trecho_03_VA_mrd = tk.Label(Frame1_3)
        la_trecho_03_VA_mrd.place(relx=0.279, rely=0.564, height=22, width=58)
        la_trecho_03_VA_mrd.configure(activebackground="#f9f9f9")
        la_trecho_03_VA_mrd.configure(activeforeground="black")
        la_trecho_03_VA_mrd.configure(background="#f1f1f1")
        la_trecho_03_VA_mrd.configure(disabledforeground="#a3a3a3")
        la_trecho_03_VA_mrd.configure(foreground="#000000")
        la_trecho_03_VA_mrd.configure(highlightbackground="#d9d9d9")
        la_trecho_03_VA_mrd.configure(highlightcolor="black")
        la_trecho_03_VA_mrd.configure(text=round(Mrd[2],1))
        
        la_trecho_03_msd = tk.Label(Frame1_3)
        la_trecho_03_msd.place(relx=0.508, rely=0.564, height=22, width=48)
        la_trecho_03_msd.configure(activebackground="#f9f9f9")
        la_trecho_03_msd.configure(activeforeground="black")
        la_trecho_03_msd.configure(background="#d9d9d9")
        la_trecho_03_msd.configure(disabledforeground="#a3a3a3")
        la_trecho_03_msd.configure(foreground="#000000")
        la_trecho_03_msd.configure(highlightbackground="#d9d9d9")
        la_trecho_03_msd.configure(highlightcolor="black")
        la_trecho_03_msd.configure(text='''Mᵣ=''')
        
        la_trecho_03_VA_msd = tk.Label(Frame1_3)
        la_trecho_03_VA_msd.place(relx=0.696, rely=0.564, height=22, width=46)
        la_trecho_03_VA_msd.configure(activebackground="#f9f9f9")
        la_trecho_03_VA_msd.configure(activeforeground="black")
        la_trecho_03_VA_msd.configure(background="#f1f1f1")
        la_trecho_03_VA_msd.configure(disabledforeground="#a3a3a3")
        la_trecho_03_VA_msd.configure(foreground="#000000")
        la_trecho_03_VA_msd.configure(highlightbackground="#d9d9d9")
        la_trecho_03_VA_msd.configure(highlightcolor="black")
        la_trecho_03_VA_msd.configure(text=msd_max_3)
        
        la_trecho_03_vrd = tk.Label(Frame1_3)
        la_trecho_03_vrd.place(relx=0.092, rely=0.732, height=22, width=41)
        la_trecho_03_vrd.configure(activebackground="#f9f9f9")
        la_trecho_03_vrd.configure(activeforeground="black")
        la_trecho_03_vrd.configure(background="#d9d9d9")
        la_trecho_03_vrd.configure(disabledforeground="#a3a3a3")
        la_trecho_03_vrd.configure(foreground="#000000")
        la_trecho_03_vrd.configure(highlightbackground="#d9d9d9")
        la_trecho_03_vrd.configure(highlightcolor="black")
        la_trecho_03_vrd.configure(text='''Vᵤ=''')

        la_trecho_03_vsd = tk.Label(Frame1_3)
        la_trecho_03_vsd.place(relx=0.533, rely=0.738, height=22, width=41)
        la_trecho_03_vsd.configure(activebackground="#f9f9f9")
        la_trecho_03_vsd.configure(activeforeground="black")
        la_trecho_03_vsd.configure(background="#d9d9d9")
        la_trecho_03_vsd.configure(disabledforeground="#a3a3a3")
        la_trecho_03_vsd.configure(foreground="#000000")
        la_trecho_03_vsd.configure(highlightbackground="#d9d9d9")
        la_trecho_03_vsd.configure(highlightcolor="black")
        la_trecho_03_vsd.configure(justify='left')
        la_trecho_03_vsd.configure(text='''Vᵣ=''')
        
        la_trecho_03_VA_vrd = tk.Label(Frame1_3)
        la_trecho_03_VA_vrd.place(relx=0.279, rely=0.732, height=22, width=54)
        la_trecho_03_VA_vrd.configure(activebackground="#f9f9f9")
        la_trecho_03_VA_vrd.configure(activeforeground="black")
        la_trecho_03_VA_vrd.configure(background="#f1f1f1")
        la_trecho_03_VA_vrd.configure(disabledforeground="#a3a3a3")
        la_trecho_03_VA_vrd.configure(foreground="#000000")
        la_trecho_03_VA_vrd.configure(highlightbackground="#d9d9d9")
        la_trecho_03_VA_vrd.configure(highlightcolor="black")
        la_trecho_03_VA_vrd.configure(text=round(Vrd,1))
        
        la_trecho_03_VA_vsd = tk.Label(Frame1_3)
        la_trecho_03_VA_vsd.place(relx=0.696, rely=0.732, height=22, width=46)
        la_trecho_03_VA_vsd.configure(activebackground="#f9f9f9")
        la_trecho_03_VA_vsd.configure(activeforeground="black")
        la_trecho_03_VA_vsd.configure(background="#f1f1f1")
        la_trecho_03_VA_vsd.configure(disabledforeground="#a3a3a3")
        la_trecho_03_VA_vsd.configure(foreground="#000000")
        la_trecho_03_VA_vsd.configure(highlightbackground="#d9d9d9")
        la_trecho_03_VA_vsd.configure(highlightcolor="black")
        la_trecho_03_VA_vsd.configure(text=vsd_max_3)
    
    
    if (trechos>=3):
        
        
        msd_max_4=-round(MM[int(L[2]*100)],2)
        msd_max_5=-round(MM[int(x_VV0[2]*100)],2)
        
        vsd_max_4=round(max(abs((VV[int(L[2]*100-2):int(L[2]*100+1)]))),2)
        vsd_max_5=round(max(abs(VV[int(x_MM0[4]*100):int(x_MM0[5]*100)])),2)
        
        # vsd_max5=10
        
        #       FRAME TRECHO 04
        Frame1_4 = tk.Frame(Frame1)
        Frame1_4.place(relx=0.02, rely=0.603, relheight=0.191, relwidth=0.96)
        Frame1_4.configure(relief='groove')
        Frame1_4.configure(borderwidth="2")
        Frame1_4.configure(relief="groove")
        Frame1_4.configure(background="#d9d9d9")
        Frame1_4.configure(highlightbackground="#d9d9d9")
        Frame1_4.configure(highlightcolor="black")
        
        latrecho_4 = tk.Label(Frame1_4)
        latrecho_4.place(relx=0.046, rely=0.067, height=22, width=103)
        latrecho_4.configure(activebackground="#f9f9f9")
        latrecho_4.configure(activeforeground="black")
        latrecho_4.configure(background="#d9d9d9")
        latrecho_4.configure(disabledforeground="#a3a3a3")
        latrecho_4.configure(font="-family {Segoe UI} -size 10 -weight bold")
        latrecho_4.configure(foreground="#000000")
        latrecho_4.configure(highlightbackground="#d9d9d9")
        latrecho_4.configure(highlightcolor="black")
        latrecho_4.configure(text='''Region 04''')
        
        la_trecho_04_posicao = tk.Label(Frame1_4)
        la_trecho_04_posicao.place(relx=0.504, rely=0.054, height=22, width=83)
        la_trecho_04_posicao.configure(activebackground="#f9f9f9")
        la_trecho_04_posicao.configure(activeforeground="black")
        la_trecho_04_posicao.configure(background="#d9d9d9")
        la_trecho_04_posicao.configure(disabledforeground="#a3a3a3")
        la_trecho_04_posicao.configure(font="-family {Segoe UI} -size 10 -weight bold")
        la_trecho_04_posicao.configure(foreground="#000000")
        la_trecho_04_posicao.configure(highlightbackground="#d9d9d9")
        la_trecho_04_posicao.configure(highlightcolor="black")
        la_trecho_04_posicao.configure(text=(x_MM0[3],_x_,x_MM0[4]))
        
        la_trecho_04_n_con = tk.Label(Frame1_4)
        la_trecho_04_n_con.place(relx=0.042, rely=0.228, height=22, width=121)
        la_trecho_04_n_con.configure(activebackground="#f9f9f9")
        la_trecho_04_n_con.configure(activeforeground="black")
        la_trecho_04_n_con.configure(background="#d9d9d9")
        la_trecho_04_n_con.configure(disabledforeground="#a3a3a3")
        la_trecho_04_n_con.configure(foreground="#000000")
        la_trecho_04_n_con.configure(highlightbackground="#d9d9d9")
        la_trecho_04_n_con.configure(highlightcolor="black")
        la_trecho_04_n_con.configure(text='''Number of Studs=''')
        
        la_trecho_04_VA_n_con = tk.Label(Frame1_4)
        la_trecho_04_VA_n_con.place(relx=0.546, rely=0.228, height=22, width=46)
        la_trecho_04_VA_n_con.configure(activebackground="#f9f9f9")
        la_trecho_04_VA_n_con.configure(activeforeground="black")
        la_trecho_04_VA_n_con.configure(background="#f1f1f1")
        la_trecho_04_VA_n_con.configure(disabledforeground="#a3a3a3")
        la_trecho_04_VA_n_con.configure(foreground="#000000")
        la_trecho_04_VA_n_con.configure(highlightbackground="#d9d9d9")
        la_trecho_04_VA_n_con.configure(highlightcolor="black")
        la_trecho_04_VA_n_con.configure(text=n_con[3])
        
        la_trecho_04_esp = tk.Label(Frame1_4)
        la_trecho_04_esp.place(relx=0.042, rely=0.396, height=22, width=75)
        
        la_trecho_04_esp.configure(activebackground="#f9f9f9")
        la_trecho_04_esp.configure(activeforeground="black")
        la_trecho_04_esp.configure(background="#d9d9d9")
        la_trecho_04_esp.configure(disabledforeground="#a3a3a3")
        la_trecho_04_esp.configure(foreground="#000000")
        la_trecho_04_esp.configure(highlightbackground="#d9d9d9")
        la_trecho_04_esp.configure(highlightcolor="black")
        la_trecho_04_esp.configure(text='''Spacing=''')
        
        la_trecho_04_VA_esp = tk.Label(Frame1_4)
        la_trecho_04_VA_esp.place(relx=0.546, rely=0.396, height=22, width=46)
        la_trecho_04_VA_esp.configure(activebackground="#f9f9f9")
        la_trecho_04_VA_esp.configure(activeforeground="black")
        la_trecho_04_VA_esp.configure(background="#f1f1f1")
        la_trecho_04_VA_esp.configure(disabledforeground="#a3a3a3")
        la_trecho_04_VA_esp.configure(foreground="#000000")
        la_trecho_04_VA_esp.configure(highlightbackground="#d9d9d9")
        la_trecho_04_VA_esp.configure(highlightcolor="black")
        la_trecho_04_VA_esp.configure(text=round(espac[3],3))
        
        la_trecho_04_mrd = tk.Label(Frame1_4)
        la_trecho_04_mrd.place(relx=0.083, rely=0.564, height=22, width=48)
        la_trecho_04_mrd.configure(activebackground="#f9f9f9")
        la_trecho_04_mrd.configure(activeforeground="black")
        la_trecho_04_mrd.configure(background="#d9d9d9")
        la_trecho_04_mrd.configure(disabledforeground="#a3a3a3")
        la_trecho_04_mrd.configure(foreground="#000000")
        la_trecho_04_mrd.configure(highlightbackground="#d9d9d9")
        la_trecho_04_mrd.configure(highlightcolor="black")
        la_trecho_04_mrd.configure(text='''Mᵤ=''')
        
        la_trecho_04_VA_mrd = tk.Label(Frame1_4)
        la_trecho_04_VA_mrd.place(relx=0.279, rely=0.564, height=22, width=58)
        la_trecho_04_VA_mrd.configure(activebackground="#f9f9f9")
        la_trecho_04_VA_mrd.configure(activeforeground="black")
        la_trecho_04_VA_mrd.configure(background="#f1f1f1")
        la_trecho_04_VA_mrd.configure(disabledforeground="#a3a3a3")
        la_trecho_04_VA_mrd.configure(foreground="#000000")
        la_trecho_04_VA_mrd.configure(highlightbackground="#d9d9d9")
        la_trecho_04_VA_mrd.configure(highlightcolor="black")
        la_trecho_04_VA_mrd.configure(text=round(Mrd[3],1))
        
        la_trecho_04_msd = tk.Label(Frame1_4)
        la_trecho_04_msd.place(relx=0.508, rely=0.564, height=22, width=48)
        la_trecho_04_msd.configure(activebackground="#f9f9f9")
        la_trecho_04_msd.configure(activeforeground="black")
        la_trecho_04_msd.configure(background="#d9d9d9")
        la_trecho_04_msd.configure(disabledforeground="#a3a3a3")
        la_trecho_04_msd.configure(foreground="#000000")
        la_trecho_04_msd.configure(highlightbackground="#d9d9d9")
        la_trecho_04_msd.configure(highlightcolor="black")
        la_trecho_04_msd.configure(text='''Mᵣ=''')
        
        la_trecho_04_VA_msd = tk.Label(Frame1_4)
        la_trecho_04_VA_msd.place(relx=0.696, rely=0.564, height=22, width=46)
        la_trecho_04_VA_msd.configure(activebackground="#f9f9f9")
        la_trecho_04_VA_msd.configure(activeforeground="black")
        la_trecho_04_VA_msd.configure(background="#f1f1f1")
        la_trecho_04_VA_msd.configure(disabledforeground="#a3a3a3")
        la_trecho_04_VA_msd.configure(foreground="#000000")
        la_trecho_04_VA_msd.configure(highlightbackground="#d9d9d9")
        la_trecho_04_VA_msd.configure(highlightcolor="black")
        la_trecho_04_VA_msd.configure(text=msd_max_4)
        
        la_trecho_04_vrd = tk.Label(Frame1_4)
        la_trecho_04_vrd.place(relx=0.092, rely=0.732, height=22, width=41)
        la_trecho_04_vrd.configure(activebackground="#f9f9f9")
        la_trecho_04_vrd.configure(activeforeground="black")
        la_trecho_04_vrd.configure(background="#d9d9d9")
        la_trecho_04_vrd.configure(disabledforeground="#a3a3a3")
        la_trecho_04_vrd.configure(foreground="#000000")
        la_trecho_04_vrd.configure(highlightbackground="#d9d9d9")
        la_trecho_04_vrd.configure(highlightcolor="black")
        la_trecho_04_vrd.configure(text='''Vᵤ=''')
        
        la_trecho_04_vsd = tk.Label(Frame1_4)
        la_trecho_04_vsd.place(relx=0.533, rely=0.738, height=22, width=41)
        la_trecho_04_vsd.configure(activebackground="#f9f9f9")
        la_trecho_04_vsd.configure(activeforeground="black")
        la_trecho_04_vsd.configure(background="#d9d9d9")
        la_trecho_04_vsd.configure(disabledforeground="#a3a3a3")
        la_trecho_04_vsd.configure(foreground="#000000")
        la_trecho_04_vsd.configure(highlightbackground="#d9d9d9")
        la_trecho_04_vsd.configure(highlightcolor="black")
        la_trecho_04_vsd.configure(justify='left')
        la_trecho_04_vsd.configure(text='''Vᵣ=''')
        
        la_trecho_04_VA_vrd = tk.Label(Frame1_4)
        la_trecho_04_VA_vrd.place(relx=0.279, rely=0.732, height=22, width=54)
        la_trecho_04_VA_vrd.configure(activebackground="#f9f9f9")
        la_trecho_04_VA_vrd.configure(activeforeground="black")
        la_trecho_04_VA_vrd.configure(background="#f1f1f1")
        la_trecho_04_VA_vrd.configure(disabledforeground="#a3a3a3")
        la_trecho_04_VA_vrd.configure(foreground="#000000")
        la_trecho_04_VA_vrd.configure(highlightbackground="#d9d9d9")
        la_trecho_04_VA_vrd.configure(highlightcolor="black")
        la_trecho_04_VA_vrd.configure(text=round(Vrd,1))
        
        la_trecho_04_VA_vsd = tk.Label(Frame1_4)
        la_trecho_04_VA_vsd.place(relx=0.696, rely=0.732, height=22, width=46)
        la_trecho_04_VA_vsd.configure(activebackground="#f9f9f9")
        la_trecho_04_VA_vsd.configure(activeforeground="black")
        la_trecho_04_VA_vsd.configure(background="#f1f1f1")
        la_trecho_04_VA_vsd.configure(disabledforeground="#a3a3a3")
        la_trecho_04_VA_vsd.configure(foreground="#000000")
        la_trecho_04_VA_vsd.configure(highlightbackground="#d9d9d9")
        la_trecho_04_VA_vsd.configure(highlightcolor="black")
        la_trecho_04_VA_vsd.configure(text=vsd_max_4)
        
        #       FRAME TRECHO 05
        
        Frame1_5 = tk.Frame(Frame1)
        Frame1_5.place(relx=0.02, rely=0.801, relheight=0.191, relwidth=0.96)
        Frame1_5.configure(relief='groove')
        Frame1_5.configure(borderwidth="2")
        Frame1_5.configure(relief="groove")
        Frame1_5.configure(background="#d9d9d9")
        Frame1_5.configure(highlightbackground="#d9d9d9")
        Frame1_5.configure(highlightcolor="black")
        
        latrecho_5 = tk.Label(Frame1_5)
        latrecho_5.place(relx=0.046, rely=0.067, height=22, width=103)
        latrecho_5.configure(activebackground="#f9f9f9")
        latrecho_5.configure(activeforeground="black")
        latrecho_5.configure(background="#d9d9d9")
        latrecho_5.configure(disabledforeground="#a3a3a3")
        latrecho_5.configure(font="-family {Segoe UI} -size 10 -weight bold")
        latrecho_5.configure(foreground="#000000")
        latrecho_5.configure(highlightbackground="#d9d9d9")
        latrecho_5.configure(highlightcolor="black")
        latrecho_5.configure(text='''Region 05''')
        
        la_trecho_05_posicao = tk.Label(Frame1_5)
        la_trecho_05_posicao.place(relx=0.504, rely=0.054, height=22, width=83)
        la_trecho_05_posicao.configure(activebackground="#f9f9f9")
        la_trecho_05_posicao.configure(activeforeground="black")
        la_trecho_05_posicao.configure(background="#d9d9d9")
        la_trecho_05_posicao.configure(disabledforeground="#a3a3a3")
        la_trecho_05_posicao.configure(font="-family {Segoe UI} -size 10 -weight bold")
        la_trecho_05_posicao.configure(foreground="#000000")
        la_trecho_05_posicao.configure(highlightbackground="#d9d9d9")
        la_trecho_05_posicao.configure(highlightcolor="black")
        la_trecho_05_posicao.configure(text=(x_MM0[4],_x_,x_MM0[5]))
        
        la_trecho_05_n_con = tk.Label(Frame1_5)
        la_trecho_05_n_con.place(relx=0.042, rely=0.228, height=22, width=121)
        la_trecho_05_n_con.configure(activebackground="#f9f9f9")
        la_trecho_05_n_con.configure(activeforeground="black")
        la_trecho_05_n_con.configure(background="#d9d9d9")
        la_trecho_05_n_con.configure(disabledforeground="#a3a3a3")
        la_trecho_05_n_con.configure(foreground="#000000")
        la_trecho_05_n_con.configure(highlightbackground="#d9d9d9")
        la_trecho_05_n_con.configure(highlightcolor="black")
        la_trecho_05_n_con.configure(text='''Number of Studs=''')
        
        la_trecho_05_VA_n_con = tk.Label(Frame1_5)
        la_trecho_05_VA_n_con.place(relx=0.546, rely=0.228, height=22, width=46)
        la_trecho_05_VA_n_con.configure(activebackground="#f9f9f9")
        la_trecho_05_VA_n_con.configure(activeforeground="black")
        la_trecho_05_VA_n_con.configure(background="#f1f1f1")
        la_trecho_05_VA_n_con.configure(disabledforeground="#a3a3a3")
        la_trecho_05_VA_n_con.configure(foreground="#000000")
        la_trecho_05_VA_n_con.configure(highlightbackground="#d9d9d9")
        la_trecho_05_VA_n_con.configure(highlightcolor="black")
        la_trecho_05_VA_n_con.configure(text=n_con[4])
        
        la_trecho_05_esp = tk.Label(Frame1_5)
        la_trecho_05_esp.place(relx=0.042, rely=0.396, height=22, width=75)
        
        la_trecho_05_esp.configure(activebackground="#f9f9f9")
        la_trecho_05_esp.configure(activeforeground="black")
        la_trecho_05_esp.configure(background="#d9d9d9")
        la_trecho_05_esp.configure(disabledforeground="#a3a3a3")
        la_trecho_05_esp.configure(foreground="#000000")
        la_trecho_05_esp.configure(highlightbackground="#d9d9d9")
        la_trecho_05_esp.configure(highlightcolor="black")
        la_trecho_05_esp.configure(text='''Spacing=''')
        
        la_trecho_05_VA_esp = tk.Label(Frame1_5)
        la_trecho_05_VA_esp.place(relx=0.546, rely=0.396, height=22, width=46)
        la_trecho_05_VA_esp.configure(activebackground="#f9f9f9")
        la_trecho_05_VA_esp.configure(activeforeground="black")
        la_trecho_05_VA_esp.configure(background="#f1f1f1")
        la_trecho_05_VA_esp.configure(disabledforeground="#a3a3a3")
        la_trecho_05_VA_esp.configure(foreground="#000000")
        la_trecho_05_VA_esp.configure(highlightbackground="#d9d9d9")
        la_trecho_05_VA_esp.configure(highlightcolor="black")
        la_trecho_05_VA_esp.configure(text=round(espac[4],3))
        
        la_trecho_05_mrd = tk.Label(Frame1_5)
        la_trecho_05_mrd.place(relx=0.083, rely=0.564, height=22, width=48)
        la_trecho_05_mrd.configure(activebackground="#f9f9f9")
        la_trecho_05_mrd.configure(activeforeground="black")
        la_trecho_05_mrd.configure(background="#d9d9d9")
        la_trecho_05_mrd.configure(disabledforeground="#a3a3a3")
        la_trecho_05_mrd.configure(foreground="#000000")
        la_trecho_05_mrd.configure(highlightbackground="#d9d9d9")
        la_trecho_05_mrd.configure(highlightcolor="black")
        la_trecho_05_mrd.configure(text='Mᵤ=')
        
        la_trecho_05_VA_mrd = tk.Label(Frame1_5)
        la_trecho_05_VA_mrd.place(relx=0.279, rely=0.564, height=22, width=58)
        la_trecho_05_VA_mrd.configure(activebackground="#f9f9f9")
        la_trecho_05_VA_mrd.configure(activeforeground="black")
        la_trecho_05_VA_mrd.configure(background="#f1f1f1")
        la_trecho_05_VA_mrd.configure(disabledforeground="#a3a3a3")
        la_trecho_05_VA_mrd.configure(foreground="#000000")
        la_trecho_05_VA_mrd.configure(highlightbackground="#d9d9d9")
        la_trecho_05_VA_mrd.configure(highlightcolor="black")
        la_trecho_05_VA_mrd.configure(text=round(Mrd[4],1))
        
        la_trecho_05_msd = tk.Label(Frame1_5)
        la_trecho_05_msd.place(relx=0.508, rely=0.564, height=22, width=48)
        la_trecho_05_msd.configure(activebackground="#f9f9f9")
        la_trecho_05_msd.configure(activeforeground="black")
        la_trecho_05_msd.configure(background="#d9d9d9")
        la_trecho_05_msd.configure(disabledforeground="#a3a3a3")
        la_trecho_05_msd.configure(foreground="#000000")
        la_trecho_05_msd.configure(highlightbackground="#d9d9d9")
        la_trecho_05_msd.configure(highlightcolor="black")
        la_trecho_05_msd.configure(text='''Mᵣ=''')
        
        la_trecho_05_VA_msd = tk.Label(Frame1_5)
        la_trecho_05_VA_msd.place(relx=0.696, rely=0.564, height=22, width=46)
        la_trecho_05_VA_msd.configure(activebackground="#f9f9f9")
        la_trecho_05_VA_msd.configure(activeforeground="black")
        la_trecho_05_VA_msd.configure(background="#f1f1f1")
        la_trecho_05_VA_msd.configure(disabledforeground="#a3a3a3")
        la_trecho_05_VA_msd.configure(foreground="#000000")
        la_trecho_05_VA_msd.configure(highlightbackground="#d9d9d9")
        la_trecho_05_VA_msd.configure(highlightcolor="black")
        la_trecho_05_VA_msd.configure(text=msd_max_5)
        
        la_trecho_05_vrd = tk.Label(Frame1_5)
        la_trecho_05_vrd.place(relx=0.092, rely=0.732, height=22, width=41)
        la_trecho_05_vrd.configure(activebackground="#f9f9f9")
        la_trecho_05_vrd.configure(activeforeground="black")
        la_trecho_05_vrd.configure(background="#d9d9d9")
        la_trecho_05_vrd.configure(disabledforeground="#a3a3a3")
        la_trecho_05_vrd.configure(foreground="#000000")
        la_trecho_05_vrd.configure(highlightbackground="#d9d9d9")
        la_trecho_05_vrd.configure(highlightcolor="black")
        la_trecho_05_vrd.configure(text='''Vᵤ=''')
        
        la_trecho_05_vsd = tk.Label(Frame1_5)
        la_trecho_05_vsd.place(relx=0.533, rely=0.738, height=22, width=41)
        la_trecho_05_vsd.configure(activebackground="#f9f9f9")
        la_trecho_05_vsd.configure(activeforeground="black")
        la_trecho_05_vsd.configure(background="#d9d9d9")
        la_trecho_05_vsd.configure(disabledforeground="#a3a3a3")
        la_trecho_05_vsd.configure(foreground="#000000")
        la_trecho_05_vsd.configure(highlightbackground="#d9d9d9")
        la_trecho_05_vsd.configure(highlightcolor="black")
        la_trecho_05_vsd.configure(justify='left')
        la_trecho_05_vsd.configure(text='''Vᵣ=''')
        
        la_trecho_05_VA_vrd = tk.Label(Frame1_5)
        la_trecho_05_VA_vrd.place(relx=0.279, rely=0.732, height=22, width=54)
        la_trecho_05_VA_vrd.configure(activebackground="#f9f9f9")
        la_trecho_05_VA_vrd.configure(activeforeground="black")
        la_trecho_05_VA_vrd.configure(background="#f1f1f1")
        la_trecho_05_VA_vrd.configure(disabledforeground="#a3a3a3")
        la_trecho_05_VA_vrd.configure(foreground="#000000")
        la_trecho_05_VA_vrd.configure(highlightbackground="#d9d9d9")
        la_trecho_05_VA_vrd.configure(highlightcolor="black")
        la_trecho_05_VA_vrd.configure(text=round(Vrd,1))
        
        la_trecho_05_VA_vsd = tk.Label(Frame1_5)
        la_trecho_05_VA_vsd.place(relx=0.696, rely=0.732, height=22, width=46)
        la_trecho_05_VA_vsd.configure(activebackground="#f9f9f9")
        la_trecho_05_VA_vsd.configure(activeforeground="black")
        la_trecho_05_VA_vsd.configure(background="#f1f1f1")
        la_trecho_05_VA_vsd.configure(disabledforeground="#a3a3a3")
        la_trecho_05_VA_vsd.configure(foreground="#000000")
        la_trecho_05_VA_vsd.configure(highlightbackground="#d9d9d9")
        la_trecho_05_VA_vsd.configure(highlightcolor="black")
        la_trecho_05_VA_vsd.configure(text=vsd_max_5)


# =============================================================================
# =============================================================================
# # # =========================================================================
# # # # ###############   FUNÇÕES QUE CRIAM AS PLOTAGENS   ####################
# # # =========================================================================
# =============================================================================
# =============================================================================
        
        
        
# =============================================================================
# FUNÇÃO QUE CRIA A LINHA DA VIGAS E OS APOIOS    
# =============================================================================
        
def CRIA_VIGA_APOIOS(fig):

#    CRIA A LINHA DA VIGA
    #print(L)
    v    = np.zeros(int(sum(L)/0.01))             # VETOR VERTICAL PARA LINHA D VIGA
    h    = np.arange(0, sum(L),0.01)              # VETOR HORIZONTAL PARA LINHA DA VIGA 
    viga = fig.add_subplot(111)                   # CRIANDO UMA VARIAVEL COM OS DADOS DESSE GRAFICO
    viga.plot(h,v,'black',linewidth=2)            # PLOTANDO OS DADOS DA viga

#    CRIA OS APOIOS    
    aux=0
    for kk in range(trechos+1):
        apoio_base=0
        apoio_lat_esq=0
        apoio_lat_dir=0
        apoiox=0
        apoioy=0

        apoiox         =np.arange((aux-0.2),(aux+0.2),0.01)
        apoioy         =np.zeros(len(apoiox))-0.28
        
        #apoio_base     =fig.add_subplot(111)
        viga.plot(apoiox,apoioy,'green',linewidth=1.6)
        
        apoiox         =np.arange((aux-0.2),(aux),0.01)
        apoioy         =np.linspace(-0.27,-0.03,len(apoiox))
        
        #apoio_lat_esq  =fig.add_subplot(111)
        viga.plot(apoiox,apoioy,'green',linewidth=1.6)
    
        apoiox         =np.arange(aux,aux+0.2,0.01)
        apoioy         =np.linspace(-0.03,-0.27,len(apoiox))
        
        #apoio_lat_dir  =fig.add_subplot(111)
        viga.plot(apoiox,apoioy,'green',linewidth=1.6)
   

        if (kk<trechos):
            aux=aux+L[kk]
            
#    RETIRANDO A MOLDURA
    viga.spines['right'].set_color('white')
    viga.spines['top'].set_color('white')
    viga.spines['left'].set_color('white')
    viga.spines['bottom'].set_color('white')
    
#    CONFIGURANDO A ALTURA DA JANELA DO GRAFICO
    viga.axis([-1,sum(L)+1,-2.5,2.5])
    
#    DESLIGANDO OS EIXOS
    
    fig.gca().axes.get_yaxis().set_visible(False)               # REMOVE OS EIXOS DO GRAFICO
    fig.gca().axes.get_xaxis().set_visible(False)
    
    return viga
    
#=============================================================================#
    
    
    
    
    
         
# =============================================================================
# FUNÇÃO QUE CRIA A PLOTAGEM DO GRAFICO DE CORTE ATUANTE    
# =============================================================================
    
def GRAFICO_CORTE_ATUANTE():
    global fig
    
    Frame4_solicitante = tk.Frame(janela_geral)
    Frame4_solicitante.place(relx=0.24, rely=0.088, relheight=0.315, relwidth=0.58)
    Frame4_solicitante.configure(relief='groove')
    Frame4_solicitante.configure(borderwidth="2")
    Frame4_solicitante.configure(relief="groove")
    Frame4_solicitante.configure(background="#d9d9d9")
    Frame4_solicitante.configure(highlightbackground="#d9d9d9")
    Frame4_solicitante.configure(highlightcolor="black")

    fig = Figure(figsize=(1, 1), dpi=100)           # CRIA A FIGURA 
    
    corte = CRIA_VIGA_APOIOS(fig)
    
#    CONFIGURA A PROPORÇAO DA TELA
    max_abs=  max(np.abs(VV))
    rel_tela= max_abs/2

#    PLOTANDO O GRAFICO DE CORTE
    
    #corte = fig.add_subplot(111)
    corte.plot(xx,VV/rel_tela,'blue',linewidth=0.5)   

#    CRIANDO A LINHA INICIAL E A FINAL DO DIAGRAMA

    v = np.arange(0,VV[0]/rel_tela, .01)                # VETOR VERTICAL PARA A LINHA RETA DO APOIO 1 DO CORTE
    h = np.zeros(len(v))                                # VETOR HORIZONTAL PARA A LINHA RETA DO APOIO 1 DO CORTE
    #linha_corte = fig.add_subplot(111)                    
    corte.plot(h,v,'blue',linewidth=0.5)         
    
    v = np.arange(VV[len(VV)-1]/rel_tela,0, .01)        # VETOR VERTICAL PARA A LINHA RETA DO APOIO FINAL DO CORTE
    h = np.zeros(len(v)) + Lt                           # VETOR HORIZONTAL PARA A LINHA RETA DO APOIO FINAL DO CORTE
    #linha_corte=fig.add_subplot(111)                   
    corte.plot(h,v,'blue',linewidth=0.5)   

    corte.annotate("CALCULATED REQUIRED SHEAR FORCE", xy=(2, 1), xytext=(-3, 2.8))       

#    COLOCANDO OS TEXTOS NOS PONTOS DE MAXIMO

    for jj in range(2):
        aux_x=0
        if(jj==1):aux_x=L[0]
        for kk in range(trechos):
            aa=jj 
            #corte_max=fig.add_subplot(111)
            if(jj==1 and kk==(trechos-1)):aa=-1
            a=round(VV[int(aux_x*100+aa)],0)
            posx=aux_x+0.1
            corte.annotate(a, xy=(2, 1), xytext=(posx, 1.2*(a/rel_tela)))
            aux_x =(aux_x+L[kk])
    
    canvas = FigureCanvasTkAgg(fig, master = Frame4_solicitante)  # A tk.DrawingArea.
    canvas.draw()
    toolbar = NavigationToolbar2Tk(canvas, Frame4_solicitante)
    toolbar.update()
    canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)    # POSICIONA O GRAFICO NA FRAME
    
#=============================================================================#
    
    
    
    

    
# =============================================================================
# FUNÇÃO QUE CRIA A PLOTAGEM DO GRAFICO DE CORTE RESISTENTE  
# =============================================================================
    
def GRAFICO_CORTE_RESISTENTE():
    global fig
    
    Frame5_resistente = tk.Frame(janela_geral)
    Frame5_resistente.place(relx=0.24, rely=0.413, relheight=0.315, relwidth=0.58)
    Frame5_resistente.configure(relief='groove')
    Frame5_resistente.configure(borderwidth="2")
    Frame5_resistente.configure(relief="groove")
    Frame5_resistente.configure(background="#d9d9d9")
    Frame5_resistente.configure(highlightbackground="#d9d9d9")
    Frame5_resistente.configure(highlightcolor="black")


    fig = Figure(figsize=(1, 1), dpi=100)           # CRIA A FIGURA 
    
    corte = CRIA_VIGA_APOIOS(fig)
    
    #    CONFIGURA A PROPORÇAO DA TELA
    rel_tela=Vrd/2
    
    #    CRIANDO A LINHA INICIAL E A FINAL DO DIAGRAMA
    ini=0
    fim=Vrd/rel_tela
    Ltotal=0
    altura=Vrd/rel_tela
    for k in range (2):
        Ltotal=0
        
        for j in range(2):  
            if(k==1):ini=-Vrd/rel_tela ;fim=0
            if(j==1):Ltotal=Lt
            v = np.arange(ini , fim , .01)                # VETOR VERTICAL PARA A LINHA RETA DO APOIO 1 DO CORTE
            h = np.zeros(len(v))  + Ltotal                           # VETOR HORIZONTAL PARA A LINHA RETA DO APOIO 1 DO CORTE
           #linha_vert=fig.add_subplot(111)                    
            corte.plot(h,v,'blue',linewidth=0.5)  
            
        if(k==1):altura=-Vrd/rel_tela
        h = np.arange(0 , Lt , .01)                # VETOR VERTICAL PARA A LINHA RETA DO APOIO 1 DO CORTE
        v = np.zeros(len(h))  + altura                           # VETOR HORIZONTAL PARA A LINHA RETA DO APOIO 1 DO CORTE
        #linha_vert=fig.add_subplot(111)                    
        corte.plot(h,v,'blue',linewidth=0.5)  
        
        corte.annotate(round( Vrd,1), xy=(2, 1), xytext=(Lt/2-0.4, (Vrd/rel_tela)))
        corte.annotate(round(-Vrd,1), xy=(2, 1), xytext=(Lt/2-0.4, (-Vrd/rel_tela)))
        corte.annotate("CALCULATED SHEAR CAPACITY", xy=(2, 1), xytext=(-3, 2.8))
    
    canvas = FigureCanvasTkAgg(fig, master=Frame5_resistente)  # A tk.DrawingArea.
    canvas.draw()
    toolbar = NavigationToolbar2Tk(canvas, Frame5_resistente)
    toolbar.update()
    canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)    # POSICIONA O GRAFICO NA FRAME
    
#=============================================================================#
    
    
    
    
    
         
    
    
# =============================================================================
# FUNÇÃO QUE CRIA A PLOTAGEM DO GRAFICO DE MOMENTO RESISTENTE     
# =============================================================================
    
def GRAFICO_MOMENTO_RESISTENTE():
    global fig
    
    Frame5_resistente = tk.Frame(janela_geral)
    Frame5_resistente.place(relx=0.24, rely=0.413, relheight=0.315, relwidth=0.58)
    Frame5_resistente.configure(relief='groove')
    Frame5_resistente.configure(borderwidth="2")
    Frame5_resistente.configure(relief="groove")
    Frame5_resistente.configure(background="#d9d9d9")
    Frame5_resistente.configure(highlightbackground="#d9d9d9")
    Frame5_resistente.configure(highlightcolor="black")

    fig = Figure(figsize=(1, 1), dpi=100)           # CRIA A FIGURA 
    
    mom = CRIA_VIGA_APOIOS(fig)
    
    #    CONFIGURA A PROPORÇAO DA TELA
    max_abs = max(np.abs(Mrd))
    rel_tela= max_abs/2
    
    #    CRIANDO A LINHA INICIAL E A FINAL DO DIAGRAMA
    for k in range (len(Mrd)):
        for j in range(2):
            if (Mrd[k]>=0):
                aux_v_i=-Mrd[k]/rel_tela
                aux_v_f=0
                
            elif (Mrd[k]<0):
                aux_v_i=0
                aux_v_f=-Mrd[k]/rel_tela
                
            v = np.arange(aux_v_i , aux_v_f , .01)                             # VETOR VERTICAL PARA A LINHA RETA DO APOIO 1 DO CORTE
            h = np.zeros(len(v))   + (x_MM0[k+j])                              # VETOR HORIZONTAL PARA A LINHA RETA DO APOIO 1 DO CORTE                 
            mom.plot(h,v,'blue',linewidth=0.5)         
            
        h = np.arange(x_MM0[k],x_MM0[k+1], .01)                                # VETOR VERTICAL PARA A LINHA RETA DO APOIO FINAL DO CORTE
        v = (np.zeros(len(h))) - (Mrd[k]/rel_tela)                             # VETOR HORIZONTAL PARA A LINHA RETA DO APOIO FINAL DO CORTE            
        mom.plot(h,v,'blue',linewidth=0.5)   
        
        #ano_mom=fig.add_subplot(111)
        posx=(x_MM0[k]+x_MM0[k+1])/2
        a=round(Mrd[k],1)
        mom.annotate(a, xy=(2, 1), xytext=(posx-0.4, (-a/rel_tela)))
        mom.annotate("CALCULATED BENDING MOMENT CAPACITY", xy=(2, 1), xytext=(-3, 2.8))
    
    canvas = FigureCanvasTkAgg(fig, master=Frame5_resistente)  # A tk.DrawingArea.
    canvas.draw()
    
    toolbar = NavigationToolbar2Tk(canvas, Frame5_resistente)
    toolbar.update()
    
    canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)    # POSICIONA O GRAFICO NA FRAME

#=============================================================================#
    
    
    
    
    
         

# =============================================================================
# FUNÇÃO QUE CRIA A PLOTAGEM DO GRAFICO DE MOMENTO ATUANTE    
# =============================================================================
    

def GRAFICO_MOMENTO_ATUANTE():
    global fig
    
    Frame4_solicitante = tk.Frame(janela_geral)
    Frame4_solicitante.place(relx=0.24, rely=0.088, relheight=0.315, relwidth=0.58)
    Frame4_solicitante.configure(relief='groove')
    Frame4_solicitante.configure(borderwidth="2")
    Frame4_solicitante.configure(relief="groove")
    Frame4_solicitante.configure(background="#d9d9d9")
    Frame4_solicitante.configure(highlightbackground="#d9d9d9")
    Frame4_solicitante.configure(highlightcolor="black")

    fig = Figure(figsize=(1, 1), dpi=100)           # CRIA A FIGURA 
    
    mom = CRIA_VIGA_APOIOS(fig)
    
#    CONFIGURA A PROPORÇAO DA TELA
    max_abs=max(np.abs(MM))
    rel_tela=max_abs/2

#    PLOTANDO O GRAFICO DE CORTE
    
    # momento=fig.add_subplot(111)
    mom.plot(xx,MM/rel_tela,'blue',linewidth=0.5)   

    for jj in range(trechos):
        a=round(MM[int(x_VV0[jj]*100)],3)
        posx=x_VV0[jj]
        
        v = np.arange(MM[int(x_VV0[jj]*100)]/rel_tela,0, .01)   # VETOR VERTICAL PARA A LINHA RETA DO APOIO 1 DO CORTE
        h = np.zeros(len(v))+posx                               # VETOR HORIZONTAL PARA A LINHA RETA DO APOIO 1 DO CORTE
        # linha_mom=fig.add_subplot(111)                    
        mom.plot(h,v,'blue',linewidth=0.5)    
        
        # mom_max=fig.add_subplot(111)
        mom.annotate(-1*a, xy=(2, 1), xytext=(posx-0.2, -0.5+(a/rel_tela)))
        
    posx=0
    for jj in range (trechos-1):
        posx=posx+L[jj]
        a=round(MM[int(posx*100)],1)
        
        v = np.arange(0 , MM[int(posx*100)]/rel_tela , .01)                # VETOR VERTICAL PARA A LINHA RETA DO APOIO 1 DO CORTE
        h = np.zeros(len(v))+posx                               # VETOR HORIZONTAL PARA A LINHA RETA DO APOIO 1 DO CORTE
        # linha_mom=fig.add_subplot(111)                    
        mom.plot(h,v,'blue',linewidth=0.5)  
        
        # mom_min=fig.add_subplot(111)
        mom.annotate(-1*a, xy=(2, 1), xytext=(posx-0.2, +0.5+(a/rel_tela)))
        mom.annotate("CALCULATED REQUIRED BENDING MOMENT", xy=(2, 1), xytext=(-3, 2.8))
    

    canvas = FigureCanvasTkAgg(fig, master=Frame4_solicitante)  # A tk.DrawingArea.
    canvas.draw()
    
    toolbar = NavigationToolbar2Tk(canvas, Frame4_solicitante)
    toolbar.update()
    
    canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)    # POSICIONA O GRAFICO NA FRAME

#=============================================================================#
    
    
    
    
    


# =============================================================================
# FUNÇÃO QUE CRIA A PLOTAGEM DO RESULTADO PARA EFEITO DE CORTE    
# =============================================================================


def GRAFICO_RESULTADO_CORTE():
    global fig
    
    Frame6_conectores = tk.Frame(janela_geral)
    Frame6_conectores.place(relx=0.24, rely=0.738, relheight=0.25, relwidth=0.58)
    Frame6_conectores.configure(relief='groove')
    Frame6_conectores.configure(borderwidth="2")
    Frame6_conectores.configure(relief="groove")
    Frame6_conectores.configure(background="#d9d9d9")
    Frame6_conectores.configure(highlightbackground="#d9d9d9")
    Frame6_conectores.configure(highlightcolor="black")

    fig = Figure(figsize=(1, 1), dpi=100)           # CRIA A FIGURA 
    
    corte = CRIA_VIGA_APOIOS(fig)

#    CONFIGURA A PROPORÇAO DA TELA
    max_abs=max(np.abs(VV))
    rel_tela=max_abs/2

#    PLOTANDO O GRAFICO DE CORTE ATUANTE
    
    #corte=fig.add_subplot(111)
    corte.plot(xx,VV/rel_tela,'Red',linewidth=0.3)   
    
#    CRIANDO A LINHA INICIAL E A FINAL DO DIAGRAMA

    v = np.arange(0,VV[0]/rel_tela, .01)                # VETOR VERTICAL PARA A LINHA RETA DO APOIO 1 DO CORTE
    h = np.zeros(len(v))                                # VETOR HORIZONTAL PARA A LINHA RETA DO APOIO 1 DO CORTE
    #linha_corte=fig.add_subplot(111)                    
    corte.plot(h,v,'green',linewidth=0.3)         
    
    v = np.arange(VV[len(VV)-1]/rel_tela,0, .01)        # VETOR VERTICAL PARA A LINHA RETA DO APOIO FINAL DO CORTE
    h = np.zeros(len(v)) + Lt                           # VETOR HORIZONTAL PARA A LINHA RETA DO APOIO FINAL DO CORTE
    # linha_corte=fig.add_subplot(111)                   
    corte.plot(h,v,'green',linewidth=0.3)   

#    PLOTANDO O GRAFICO DE CORTE RESISTENTE
    
    ini=0
    fim=Vrd/rel_tela
    Ltotal=0
    altura=Vrd/rel_tela
    for k in range (2):
        Ltotal=0
        
        for j in range(2):  
            if(k==1):ini=-Vrd/rel_tela ;fim=0
            if(j==1):Ltotal=Lt
            v = np.arange(ini , fim , .01)                # VETOR VERTICAL PARA A LINHA RETA DO APOIO 1 DO CORTE
            h = np.zeros(len(v))  + Ltotal                           # VETOR HORIZONTAL PARA A LINHA RETA DO APOIO 1 DO CORTE
            #linha_vert=fig.add_subplot(111)                    
            corte.plot(h,v,'green',linewidth=0.3)  
            
        if(k==1):altura=-Vrd/rel_tela
        h = np.arange(0 , Lt , .01)                # VETOR VERTICAL PARA A LINHA RETA DO APOIO 1 DO CORTE
        v = np.zeros(len(h))  + altura                           # VETOR HORIZONTAL PARA A LINHA RETA DO APOIO 1 DO CORTE
        # linha_vert=fig.add_subplot(111)                    
        corte.plot(h,v,'green',linewidth=0.3)  

#CRIA AS LINHAS QUE SEPARAM OS TRECHOS DE MOMENTO NULO
    if (trechos==1): j=0 
    if (trechos==2): j=2
    if (trechos==3): j=4
    for k in range(j):
        v = np.arange(-10 , 10 , .01)
        h = np.zeros(len(v))  + x_MM0[k+1]
        #linha_cone=fig.add_subplot(111)                    
        corte.plot(h,v,'gray',linewidth=1)
        
    for k in range(len(Mrd)):
        b=((x_MM0[k+1]-x_MM0[k])/2)+x_MM0[k]
        corte.annotate(k+1, xy=(2, 1), xytext=(b,-3))  

    a=0
    
#CRIANDO A APARENCIA DOS CONECTORES
    for k in range (len(Mrd)):
        if (k==0):
            xcon=cobrimento
        elif(k>=1):
            xcon=x_MM0[k]
        a=0  
         
        for j in range (int(n_con[k])):
            
            if (trechos==1):
                xcon=xcon+a
                v = np.arange(0 , 0.3 , .01)
                h = np.zeros(len(v))  + xcon
                #linha_cone=fig.add_subplot(111)                    
                corte.plot(h,v,'black',linewidth=1.5)
                
                h = np.arange(xcon-0.02 , xcon+0.02 , .01)
                v = np.zeros(len(h))  + 0.3
                #linha_sup_cone=fig.add_subplot(111)
                corte.plot(h,v,'black',linewidth=1.5)
                
                a=espac[k]
                
            elif(trechos>=2 and k==0):
                xcon=xcon+a
                v = np.arange(0 , 0.3 , .01)
                h = np.zeros(len(v))  + xcon
                #linha_cone=fig.add_subplot(111)                    
                corte.plot(h,v,'black',linewidth=1.5)
                
                h = np.arange(xcon-0.02 , xcon+0.02 , .01)
                v = np.zeros(len(h))  + 0.3
               # linha_sup_cone=fig.add_subplot(111)
                corte.plot(h,v,'black',linewidth=1.5)
                
                a=espac[k]
                
            elif((trechos>=2 and k==1) or (trechos==3 and k==1) or (trechos==3 and k==2) or (trechos==3 and k==3)):
                if(j==0): b=espac[k]/2
                else: b=0 
                xcon=xcon+a+b
                v = np.arange(0 , 0.3 , .01)
                h = np.zeros(len(v))  + xcon
                #linha_cone=fig.add_subplot(111)                    
                corte.plot(h,v,'black',linewidth=1.5)
                
                h = np.arange(xcon-0.02 , xcon+0.02 , .01)
                v = np.zeros(len(h))  + 0.3
                #linha_sup_cone=fig.add_subplot(111)
                corte.plot(h,v,'black',linewidth=1.5)
                
                a=espac[k]
                
            elif((trechos==2 and k==2) or (trechos==3 and k==4)):
                a=espac[k]
                xcon=xcon+a
                v = np.arange(0 , 0.3 , .01)
                h = np.zeros(len(v))  + xcon
                #linha_cone=fig.add_subplot(111)                    
                corte.plot(h,v,'black',linewidth=1.5)
                
                h = np.arange(xcon-0.02 , xcon+0.02 , .01)
                v = np.zeros(len(h))  + 0.3
                #linha_sup_cone=fig.add_subplot(111)
                corte.plot(h,v,'black',linewidth=1.5)
                
                
    
    
    canvas = FigureCanvasTkAgg(fig, master=Frame6_conectores)  # A tk.DrawingArea.
    canvas.draw()
    
    toolbar = NavigationToolbar2Tk(canvas, Frame6_conectores)
    toolbar.update()
    
    canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)    # POSICIONA O GRAFICO NA FRAME
    
#=============================================================================#
    
    
    
    
    
         

# =============================================================================
# FUNÇÃO QUE CRIA A PLOTAGEM DO RESULTADO PARA MOMENTO FLETOR  
# ============================================================================

def GRAFICO_RESULTADO_MOMENTO():
    global fig
    
    Frame6_conectores = tk.Frame(janela_geral)
    Frame6_conectores.place(relx=0.24, rely=0.738, relheight=0.25, relwidth=0.58)
    Frame6_conectores.configure(relief='groove')
    Frame6_conectores.configure(borderwidth="2")
    Frame6_conectores.configure(relief="groove")
    Frame6_conectores.configure(background="#d9d9d9")
    Frame6_conectores.configure(highlightbackground="#d9d9d9")
    Frame6_conectores.configure(highlightcolor="black")


    fig = Figure(figsize=(1, 1), dpi=100)           # CRIA A FIGURA 
    
    mom = CRIA_VIGA_APOIOS(fig)

#    CONFIGURA A PROPORÇAO DA TELA
    max_abs=max(np.abs(VV))
    rel_tela=max_abs/2

#    PLOTANDO O GRAFICO DE MOMENTO ATUANTE
    
    # mom=fig.add_subplot(111)
    mom.plot(xx,MM/rel_tela,'Red',linewidth=0.3)   
    
        #    CRIANDO A LINHA INICIAL E A FINAL DO DIAGRAMA
    for k in range (len(Mrd)):
        for j in range(2):
            if (Mrd[k]>=0):
                aux_v_i=-Mrd[k]/rel_tela
                aux_v_f=0
                
            elif (Mrd[k]<0):
                aux_v_i=0
                aux_v_f=-Mrd[k]/rel_tela
                
            v = np.arange(aux_v_i , aux_v_f , .01)                # VETOR VERTICAL PARA A LINHA RETA DO APOIO 1 DO CORTE
            h = np.zeros(len(v))   + (x_MM0[k+j])                 # VETOR HORIZONTAL PARA A LINHA RETA DO APOIO 1 DO CORTE            
            mom.plot(h,v,'green',linewidth=0.3)         
            
        h = np.arange(x_MM0[k],x_MM0[k+1], .01)        # VETOR VERTICAL PARA A LINHA RETA DO APOIO FINAL DO CORTE
        v = (np.zeros(len(h))) - (Mrd[k]/rel_tela)     # VETOR HORIZONTAL PARA A LINHA RETA DO APOIO FINAL DO CORTE                
        mom.plot(h,v,'green',linewidth=0.3)   

#CRIA AS LINHAS QUE SEPARAM OS TRECHOS DE MOMENTO NULO
    for k in range(len(Mrd)):
        b=((x_MM0[k+1]-x_MM0[k])/2)+x_MM0[k]
        mom.annotate(k+1, xy=(2, 1), xytext=(b,-3))  
    
    a=0
#CRIANDO A APARENCIA DOS CONECTORES
    for k in range (len(Mrd)):
        if (k==0):
            xcon=cobrimento
        elif(k>=1):
            xcon=x_MM0[k]
        a=0  
         
        for j in range (int(n_con[k])):
            
            if (trechos==1):
                xcon=xcon+a
                v = np.arange(0 , 0.3 , .01)
                h = np.zeros(len(v))  + xcon
                # linha_cone=fig.add_subplot(111)                    
                mom.plot(h,v,'black',linewidth=1.5)
                
                h = np.arange(xcon-0.02 , xcon+0.02 , .01)
                v = np.zeros(len(h))  + 0.3
                # linha_sup_cone=fig.add_subplot(111)
                mom.plot(h,v,'black',linewidth=1.5)
                
                a=espac[k]
                
            elif(trechos>=2 and k==0):
                xcon=xcon+a
                v = np.arange(0 , 0.3 , .01)
                h = np.zeros(len(v))  + xcon
                # linha_cone=fig.add_subplot(111)                    
                mom.plot(h,v,'black',linewidth=1.5)
                
                h = np.arange(xcon-0.02 , xcon+0.02 , .01)
                v = np.zeros(len(h))  + 0.3
                # linha_sup_cone=fig.add_subplot(111)
                mom.plot(h,v,'black',linewidth=1.5)
                
                a=espac[k]
                
            elif((trechos>=2 and k==1) or (trechos==3 and k==1) or (trechos==3 and k==2) or (trechos==3 and k==3)):
                if(j==0): b=espac[k]/2
                else: b=0 
                xcon=xcon+a+b
                v = np.arange(0 , 0.3 , .01)
                h = np.zeros(len(v))  + xcon
                # linha_cone=fig.add_subplot(111)                    
                mom.plot(h,v,'black',linewidth=1.5)
                
                h = np.arange(xcon-0.02 , xcon+0.02 , .01)
                v = np.zeros(len(h))  + 0.3
                # linha_sup_cone=fig.add_subplot(111)
                mom.plot(h,v,'black',linewidth=1.5)
                
                a=espac[k]
                
            elif((trechos==2 and k==2) or (trechos==3 and k==4)):
                a=espac[k]
                xcon=xcon+a
                v = np.arange(0 , 0.3 , .01)
                h = np.zeros(len(v))  + xcon
                # linha_cone=fig.add_subplot(111)                    
                mom.plot(h,v,'black',linewidth=1.5)
                
                h = np.arange(xcon-0.02 , xcon+0.02 , .01)
                v = np.zeros(len(h))  + 0.3
                # linha_sup_cone=fig.add_subplot(111)
                mom.plot(h,v,'black',linewidth=1.5)
                
                
    
    canvas = FigureCanvasTkAgg(fig, master=Frame6_conectores)  # A tk.DrawingArea.
    canvas.draw()
    
    toolbar = NavigationToolbar2Tk(canvas, Frame6_conectores)
    toolbar.update()
    
    canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)    # POSICIONA O GRAFICO NA FRAME
    
#=============================================================================#
    
    
    
    
# # # =========================================================================
# # # # #######################      LEITURA EXCEL      ######################
# # # =========================================================================
 
def FUNC_DATA_IN():
    global trechos , L , q
    global bf , bs , tf , h , d , d_ , tw , ry , Wx , I_p , area_p
    global norma , interacao , Lb_max , tc , n_barras , diametro_barras , cobrimento , fucs , ycs , diametro_conector, DoC
    global fck , yc , E_a , fy , ya , E_as , fs , ys   
    
    # print(nome_arquivo)
    
    base = pd.read_excel(nome_arquivo)
    base_numérico=base.values
    
    
        
    # =============================================================================
    # COLETA DE CARGA E VÃOS
    # =============================================================================
    
    trechos=int(base_numérico[0,1])
    
    L   =np.zeros(trechos)
    q   =np.zeros(trechos)
    
    for read in range(trechos):
        L[read]=base_numérico[2+read,1]
        q[read]=base_numérico[5+read,1]
        
        
    
    # =============================================================================
    # COLETA DE DADOS DO PERFIL
    # =============================================================================
    
                                         
    bf     =       base_numérico[3,4]
    bs     =       base_numérico[3,4]
    tf     =       base_numérico[4,4]
    h      =       round(base_numérico[5,4],6)
    d      =       base_numérico[6,4]
    d_     =       base_numérico[7,4]           
    
    tw     =       base_numérico[3,7]
    ry     =       base_numérico[4,7]
    Wx     =       base_numérico[5,7]
    I_p    =       base_numérico[6,7]
    area_p =       base_numérico[7,7]           
    
    
    # =============================================================================
    # COLETA DE DADOS GERAIS
    # =============================================================================
    
    
    norma             =    base_numérico[1 ,5]
    interacao         =    base_numérico[10,7]
    Lb_max            =    base_numérico[11,7]
    tc                =    base_numérico[12,7]
    n_barras          =    base_numérico[13,7]
    diametro_barras   =    base_numérico[14,7]
    cobrimento        =    base_numérico[15,7]
    fucs              =    base_numérico[16,7]
    diametro_conector =    base_numérico[17,7]
    ycs               =    base_numérico[18,7]
    DoC               =    base_numérico[19,7]
    
    # =============================================================================
    # COLETA DE DADOS DOS MATERIAIS
    # =============================================================================
    
    fck    =    base_numérico[21,7]
    yc     =    base_numérico[22,7]
    
    E_a    =    base_numérico[23,7]
    fy     =    base_numérico[24,7]
    ya     =    base_numérico[25,7]
    
    E_as   =    base_numérico[26,7]
    fs     =    base_numérico[27,7]
    ys     =    base_numérico[28,7]
    
    
    Reescreve_labels_frame1()
    
def janela_nome(): 
    def take_nome():
        global nome_arquivo
        nome_arquivo      =   box_take_nomes   .get()
        janela_carregar.destroy()
        FUNC_DATA_IN()
        # print (fy)
    
    janela_carregar=tk.Tk()
    
    style = ttk.Style()
    style.configure('.',background=_bgcolor)
    style.configure('.',foreground=_fgcolor)
    style.configure('.',font="TkDefaultFont")
    style.map('.',background=[('selected', _compcolor), ('active',_ana2color)])
    
    janela_carregar.geometry("300x150+561+192")
    janela_carregar.minsize(148, 1)
    janela_carregar.maxsize(1924, 1055)
    janela_carregar.resizable(1, 1)
    janela_carregar.iconbitmap('icones/geral.ico')
    janela_carregar.title("File Selection")
    janela_carregar.configure(background="#d9d9d9")
    janela_carregar.configure(highlightbackground="#d9d9d9")
    janela_carregar.configure(highlightcolor="black")
    
    la_normas = tk.Label(janela_carregar)
    la_normas.place(relx=0.083, rely=0.1, height=33, width=250)
    la_normas.configure(activebackground="#f9f9f9")
    la_normas.configure(activeforeground="black")
    la_normas.configure(background="#d9d9d9")
    la_normas.configure(disabledforeground="#a3a3a3")
    la_normas.configure(font="-family {Segoe UI} -size 11 -weight bold -slant italic")
    la_normas.configure(foreground="#000000")
    la_normas.configure(highlightbackground="#d9d9d9")
    la_normas.configure(highlightcolor="black")
    la_normas.configure(text='''File Name (.xlsx)''')
    
    box_take_nomes = tk.Entry(janela_carregar)
    box_take_nomes.place(relx=0.2, rely=0.4, relheight=0.173, relwidth=0.623)
    box_take_nomes.configure(background="white")
    box_take_nomes.configure(disabledforeground="#a3a3a3")
    box_take_nomes.configure(font="TkFixedFont")
    box_take_nomes.configure(foreground="#000000")
    box_take_nomes.configure(highlightbackground="#d9d9d9")
    box_take_nomes.configure(highlightcolor="black")
    box_take_nomes.configure(insertbackground="black")
    box_take_nomes.configure(selectbackground="#c4c4c4")
    box_take_nomes.configure(selectforeground="black")
    
    btn_take_nomes = tk.Button(janela_carregar)
    btn_take_nomes.place(relx=0.4, rely=0.667, height=43, width=56)
    btn_take_nomes.configure(activebackground="#ececec")
    btn_take_nomes.configure(activeforeground="#000000")
    btn_take_nomes.configure(background="#0000ff")
    btn_take_nomes.configure(disabledforeground="#a3a3a3")
    btn_take_nomes.configure(foreground="#ffffff")
    btn_take_nomes.configure(highlightbackground="#d9d9d9")
    btn_take_nomes.configure(highlightcolor="black")
    btn_take_nomes.configure(pady="0")
    btn_take_nomes.configure(text='''>>>''')
    btn_take_nomes.configure(command=take_nome)
    
    
    
    janela_carregar.mainloop()
    
    
def close():
    janela_geral.destroy()
    
entry_text = None    

def reset_program():
    # Feche o programa atual
    janela_geral.destroy()

    # Reinicie o programa atual
    subprocess.Popen([sys.executable] + sys.argv)


# =============================================================================
# =============================================================================
# # # =========================================================================
# # # # ##########   FUNÇÕES QUE REALIZAM OS CALCULOS NBR8800  ################
# # # =========================================================================
# =============================================================================
# =============================================================================        



# =============================================================================
# FUNÇÃO QUE CÁLCULA A MATRIZ DE RIGIDEZ, ESFORÇOS ATUANTES E REAÇÕES
# =============================================================================
    
    
def ESFORCOS_ATUANTES():
    global xx , MM , VV , x_VV0 , x_MM0 , texto_erro , msd_max_ , vsd_max_
    KG   =np.zeros((4+(trechos*2-2),4+(trechos*2-2)))
    KG_a =np.zeros((trechos+1,trechos+1))
    KG_aa=np.zeros((trechos+1,trechos+1))
    cont_1=0
    for n in range (trechos):       #   Cria a matriz de rigidez global
        
        a=cont_1
        b=cont_1+1
        c=cont_1+2
        d=cont_1+3
        
        k12=12/L[n]**3 
        k06=6/L[n]**2
        k04=4/L[n]
        k02=2/L[n]
        
        KG[a,a]=KG[a,a]+k12     ;   
        KG[b,a]=KG[b,a]+k06     ;   KG[b,b]=KG[b,b]+k04
        KG[c,a]=KG[c,a]-k12     ;   KG[c,b]=KG[c,b]-k06     ;   KG[c,c]=KG[c,c]+k12
        KG[d,a]=KG[d,a]+k06     ;   KG[d,b]=KG[d,b]+k02     ;   KG[d,c]=KG[d,c]-k06     ;   KG[d,d]=KG[d,d]+k04
        
        KG[a,b]=KG[b,a]
        KG[a,c]=KG[c,a]
        KG[a,d]=KG[d,a]
        KG[b,c]=KG[c,b]
        KG[b,d]=KG[d,b]
        KG[c,d]=KG[d,c]
        
        
        cont_1=cont_1+2
    #ENDFOR
    for l in range (trechos+1):
        for c in range(trechos+1):
            KG_aa[l,c]=KG[l*2+1,c*2+1]      #   Cria a matriz de rigidez reduzida
        #ENDFOR
    #ENDFOR
    KG_a=np.linalg.inv(KG_aa)               #   Inverte a matriz reduzida
    
    if (trechos==1):                        #   Cálcula as reações se a viga tiver 1 trecho
        aux2= (q*L)/2
        M   = [0,0]
        U   = np.matmul(KG_a,M)
        Ug  = [0,U[0],0,U[1]]
        R   = [aux2[0],0,aux2[0],0]
        R   = R+np.matmul(KG,Ug)
        
    elif (trechos==2):                      #   Cálcula as reações se a viga tiver 2 trechos
        aux = (q*L**2)/8
        aux2= (q*L)/8
        Mb  = aux[0]-aux[1]
        M   = [0,Mb,0]
        U   = np.matmul(KG_a,M)
        Ug  = [0,U[0],0,U[1],0,U[2]]
        R   = [3*aux2[0],0,(5*aux2[0]+5*aux2[1]),0,3*aux2[1],0]
        R   = R+np.matmul(KG,Ug)
    
    elif (trechos==3):                      #   Cálcula as reações se a viga tiver 3 trechos
        aux = (q*L**2)/8
        aux2= (q*L)/8
        Mb  = aux[0]-(2*aux[1]/3)
        Mc  = (2*aux[1]/3)-aux[2]
        M   = [0,Mb,Mc,0]
        U   = np.matmul(KG_a,M)
        Ug  = [0,U[0],0,U[1],0,U[2],0,U[3]]
        R   = [3*aux2[0],0,(5*aux2[0]+4*aux2[1]),0,(4*aux2[1]+5*aux2[2]),0,3*aux2[2],0]
        R   = R+np.matmul(KG,Ug)


    # CRIA OS VETORES DE MOMENTO E ESFORÇO CORTANTE EM RELAÇÃO DO VETOR xx
    for k in range(len(xx)):
        if(k<=(100*L[0])):
            MM[k]=(-R[0]*xx[k]+(q[0]*xx[k]**2)/2)       
            VV[k]=( R[0]-(xx[k]*q[0]))
            x_VV0[0]=R[0]/q[0]                      # DEFINE O PONTO DE MOMENTO POSITIVO MAXIMO DE CADA TRECHO, O MOMENTO MAXIMO NEGATIVO É EM CIMA DO APOIO

        elif(k>=(100*L[0]) and k<=(100*L[0]+100*L[1]) and (trechos>=2)):
            MM[k]=(-R[0]*xx[k]+(q[0]*L[0]*(xx[k]-L[0]/2))-(R[2]*(xx[k]-L[0]))+(q[1]*(xx[k]-L[0])*((xx[k]-L[0])/2)))
            VV[k]=( R[0]-(L[0]*q[0])+R[2]-((xx[k]-L[0])*q[1]))
            x_VV0[1]=((R[0]+R[2]-(L[0]*q[0]))/q[1])+L[0]

        elif(k>=(100*L[0]+100*L[1]) and (trechos==3)):
            MM[k]=(-R[0]*xx[k] + (q[0]*L[0]*(xx[k]-L[0]/2)) - (R[2]*(xx[k]-L[0])) + (q[1]*L[1]*(xx[k]-L[0]-L[1]/2)) - (R[4]*(xx[k]-L[0]-L[1])) + (q[2]*(xx[k]-L[0]-L[1])*((xx[k]-L[0]-L[1])/2)))                            
            VV[k]=( R[0]-(L[0]*q[0])+R[2]-(L[1]*q[1])+R[4]-((xx[k]-L[0]-L[1])*q[2]))
            x_VV0[2]=((R[0]+R[2]+R[4]-(L[0]*q[0])-(L[1]*q[1]))/q[2])+L[0]+L[1]
            
    MM=MM*1
    VV=VV*1
#       SOLUCIONA A EQ DE 2º GRAU E DESCOBRE AONDE O MOMENTO É NULO
    
    for k in range(trechos):
        if (k==0):
            a=q[0]/2
            b=-R[0]
            c=0
        elif(k==1):
            a=q[1]/2
            b=-R[0]+q[0]*L[0]-R[2]-q[1]*L[0]
            c=-((q[0]*L[0]**2)/2) + ((q[1]*L[0]**2)/2) + R[2]*L[0]
        elif(k==2):
            a=q[2]/2
            b=-R[6]
            c=0
            
        x=(b**2)-(4*a*c)
        
        if (x>=0):
            x=np.sqrt(x)
            x1=(-b+x)/(2*a)
            x2=(-b-x)/(2*a)
            if (k==2):
                a=x1
                x1=Lt-x2
                x2=Lt-a
        else:
            texto_erro+=["NO REAL ROOTS FOUND! \n(provavel que nenhum x passe pelo eixo das abscissas)"]
            FUNC_JANELA_ERRO()
            print("NO REAL ROOTS FOUND! (provavel que nenhum x passe pelo eixo das abscissas)")


        x_MM0[k*2      ]=round(x2,2)
        x_MM0[(k+1)*2-1]=round(x1,2)
        
        
        

    #LAÇO QUE DEFINE O MOMENTO E ESFORÇO CORTANTE MÁXIMO EM CADA TRECHO
    
    if(trechos>=1):
        msd_max_[0]=round(-1*MM[int(x_VV0[0]*100)],2)
        vsd_max_[0]=round(VV[0],2)
        
        if (trechos>=2):
            msd_max_[1]=-round(MM[int(L[1]*100)],2)
            msd_max_[2]=-round(MM[int(x_VV0[1]*100)],2)
            
            vsd_max_[1]=round(max(abs((VV[int(L[1]*100-2):int(L[1]*100+1)]))),2)
            vsd_max_[2]=round(max(abs(VV[int(x_MM0[2]*100):int(x_MM0[3]*100)])),2)
            
            if (trechos>=3):
                msd_max_[3]=-round(MM[int(L[2]*100)],2)
                msd_max_[4]=-round(MM[int(x_VV0[2]*100)],2)
                
                vsd_max_[3]=round(max(abs((VV[int(L[2]*100-2):int(L[2]*100+1)]))),2)
                vsd_max_[4]=round(max(abs(VV[int(x_MM0[4]*100):int(x_MM0[5]*100)])),2)
                
    
        
    #xx     -   Vetor de posição x discretizado em 100*Lt
    #MM     -   Vetor com os momentos de cada posição xx
    #VV     -   Vetor com os cortantes de cada posição xx
    #x_VV0  -   Vetor com os "x" dos zeros no diagrama de corte 
    #x_MM0  -   Vetor com a posiçao dos zeros no diagrama de momento 
    
#=============================================================================#    
    
    
    
    
    
    
# =============================================================================
# FUNÇÃO QUE CRIA OS VETORES
# =============================================================================
    
    
def CRIA_VETORES():
    global size_vetor , lb , Ccd , Tad , Mrd , Vrd , a , Lt , xx , MM , VV , x_VV0 , x_MM0 , MdistRd , LN , Msd , n_con , espac , tex , tex_1
    global texto_erro , msd_max_ , vsd_max_ , erros , pos_err , LN , a_ln , ws_vetor , wi_vetor , limitador
    global d3 , d4 , d5
    
    
    for n in range (trechos):
        if (n==0):
            size_vetor=1
        else:
            size_vetor=size_vetor+2
            
           
    lb = np.zeros(size_vetor)            # VETOR DE LARGURA DE MESA
    Ccd= np.zeros(size_vetor)
    Tad= np.zeros(size_vetor)
    Mrd= np.zeros(size_vetor)
    Msd= np.zeros(size_vetor)
    Vrd= np.zeros(size_vetor)
    n_con=np.zeros(size_vetor)
    espac=np.zeros(size_vetor)
    a_ln = np.zeros(size_vetor)
    
    
    d3=np.zeros(size_vetor)
    d4=np.zeros(size_vetor)
    d5=np.zeros(size_vetor)
    
    msd_max_=np.zeros(size_vetor)
    vsd_max_=np.zeros(size_vetor)
    
    LN=["---","---","---","---","---"]
    texto_erro =["Error Check\n\n"]
    limitador=["----","----","----","----","----",]
    

    
    # CRIA OS VETORES PARA DEFINIÇÃO DOS ESFORÇOS ATUANTES
    Lt=sum(L)
    xx=np.linspace(0,Lt,int(100*Lt))
    MM=np.zeros(len(xx))
    VV=np.zeros(len(xx))
    
    x_VV0=np.zeros(trechos)
    x_MM0=np.zeros(trechos*2)
    MdistRd=[0,0]
    
    
    
    
    ws_vetor=np.zeros(size_vetor)
    wi_vetor=np.zeros(size_vetor)

#=============================================================================# 

    
    
    
    
    
# =============================================================================
# # ===========================================================================
# # FUNÇÕES PARA O DIMENSIONAMENTO PELA A NBR8800
# # ===========================================================================
# =============================================================================
    
    

    
####################################################
#####              LARGURA EFETIVA          ########
####################################################
def LARGURA():
    global lb
    if (trechos==1):
        lb[0]=min(2*L[0]/8,Lb_max)
    elif (trechos==2):
        lb[0]=min((2*(4*L[0]/5))/8,Lb_max)
        lb[1]=min((2*(L[0]+L[1])/4)/8,Lb_max)
        lb[2]=min((2*(4*L[1]/5))/8,Lb_max)
    elif(trechos==3):
        lb[0]=min((2*(4*L[0]/5))/8,Lb_max)
        lb[1]=min((2*(L[0]+L[1])/4)/8,Lb_max)
        lb[2]=min((2*7*L[1]/10)/8,Lb_max)
        lb[3]=min((2*(L[1]+L[2])/4)/8,Lb_max)
        lb[4]=min((2*(4*L[2]/5))/8,Lb_max)


####################################################
#####  classificacao DA SEÇÃO TRANSVERSAL   ########
####################################################
def CLASSIFICA():
    global classificacao , texto_erro , lambda_ , lambda_p , lambda_r
    bs=bf
    if(bf==bs):
        #print("seção é duplamente simetrica")
        lambda_    = d_/tw
        lambda_p   = 3.76*np.sqrt((E_a/fy))
        lambda_r   = 5.70*np.sqrt((E_a/fy))

        if     (lambda_<=lambda_p):
            
            classificacao="compacta"
            
        elif   (lambda_p<=lambda_<=lambda_r):
            
            classificacao="semicompacta"
            
        elif   (lambda_r<=lambda_):
            
            classificacao="semicompacta"
    else:
        texto_erro+=["The section is not doubly symmetric."]
        FUNC_JANELA_ERRO()
        exit()
        print("The section is not doubly symmetric.")
        #ENDIF
    #ENDIF
#END_CLASSIFICA





####################################################
#####                   OUTROS              ########
####################################################

def PROPRIEDADES():
    global Tad , Ccd , ws , wi , ws_vetor , wi_vetor
    
    Tad     = area_p*fyd                       #Tensão máxima admitida pelo perfil metálico. (área * tensão/área).
    Ccd[kk]     = 0.85*fcd*lb[kk]*tc           #Força resistente de cálculo da espessura comprimida da laje de concreto; O 0.85 é responsável pela minoração da resistência devido ao efeito de Rüsch (efeitos de longa duração)
    #    ####   PROPRIEDADES DA SEÇÃO HOMOGENEIZADA   #######
    
    # =============================================================================
    # PROPRIEDADES DA LAJE
    # =============================================================================
    
    area_c     = lb[kk]*tc/alpha_e              # Área equivalenete de concreto
    yc         = tc/2                           # CG_y= Centro de gravidade y
    ayc        = yc*area_c                      #
    ayc2       = (yc**2)*area_c                 #
    I_c        = ((area_c/tc)*tc**3)/12         # Inércia
    
    # =============================================================================
    # PROPRIEDADES DO PERFIL
    # =============================================================================
    
    yp     = (d/2)+tc                       # CG_y= Centro de gravidade y
    ayp    = yp*area_p                      #
    ayp2   = (yp**2)*area_p                 #
    
    # =============================================================================
    # PROPRIEDADES DA SEÇÃO MISTA
    # =============================================================================
     
    area_t = area_c+area_p                  # Área total da seção
    ayt    = ayc+ayp                        #
    ayt2   = ayp2+ayc2                      #
    I_t    = I_c+I_p                        # 
    
    ys     = ayt/area_t                     # Distância da borda superior da laje até o GC da seção mista.
    yi     = (d+tc)-ys                      # Distância da borda inferior do perfil até o CG da seção mista.
    I      = I_t+ayt2-(area_t*ys**2)        # Inércia da seção mista
    
    ws     = I/ys                           # Módulo de resistência elástico da seção transversal mista em relação ao eixo de flexão superior ao CG.
    wi     = I/yi                           # Módulo de resistência elástico da seção transversal mista em relação ao eixo de flexão inferior ao CG.

    ws_vetor[kk]= ws
    wi_vetor[kk]= wi
    # =============================================================================
    # LINHA NEUTRA ELASTICA
    # =============================================================================
    #y_elastica=((bf*tf*)bf/2)+((tw*h))



# =============================================================================
#           #####################################################
#           ######      VERIFICAÇÃO À FORÇA CORTANTE       ######
#           #####################################################
# =============================================================================
def CORTANTE():   

    global kv , Vpl , lambda_corte , lambda_p_corte  , lambda_r_corte , Vrd
        
    kv         = 5                                          # Sem enrijecedores transversais
    Vpl        = 0.60*(d*tw)*fy                             # Força cortante correspondente à plastificação da alma por cisalhamento;
    
    lambda_corte    = d/tw
    lambda_p_corte  = 1.10*np.sqrt(((E_a*kv)/fy))
    lambda_r_corte   = 1.37*np.sqrt(((E_a*kv)/fy))
    
    if     (lambda_corte<=lambda_p_corte):
        Vrd=Vpl/ya
        
    elif   (lambda_p_corte<=lambda_<=lambda_r_corte):
        Vrd=(lambda_p_corte/lambda_corte)*(Vpl/ya)
        
    elif   (lambda_r_corte<=lambda_corte):
        Vrd=1.24*((lambda_p_corte/lambda_corte)**2)*(Vpl/ya)
        
    Vrd=round(Vrd,2) 






# =============================================================================
#           #####################################################
#           ######  VERIFICAÇÃO DO MOMENTO FLETOR POSITIVO ######
#           #####################################################
# =============================================================================
    

def MOMENTO_POSITIVO():
    
    global Mrd , a , LN , yp , texto_erro , LN , a_ln

    if(classificacao=="compacta"):
    # =============================================================================
    #     ##   SEÇÃO COMPACTA    ##
    # =============================================================================
        if(interacao=="Complete"):
        # =============================================================================
        #         ## INTERAÇÃO COMPLETA  ##
        # =============================================================================
            if(Ccd[kk]>=Tad):                                      # Linha neutra na laje de concreto;
            # =============================================================================
            #                ## L-N NA LAJE ##
            # =============================================================================
                LN[kk]="laje"
#                print("A linha neutra se encontra na laje de concreto")
                a_ln[kk]=(Tad)/(0.85*fcd*lb[kk])                          # Espessura da região comprimida da laje;
                S_Qrd=Tad
                if(a_ln[kk]>tc):
                    #print("erro-  a<tc")
                    exit()
                Mrd[kk]=1*Tad*(d1+hf+tc-(a_ln[kk]/2))
                yp=0
            else:                                              # Linha neutra no perfil metálico;
            # =============================================================================
                #             # L-N NO PERFIL #
            # =============================================================================
#                print("A linha neutra se encontra no perfil metalico")
                a_ln[kk]=tc
                Cad=(Tad-Ccd[kk])*0.5
                S_Qrd=Ccd[kk]
                if(Cad<(fyd*bf*tf)):   
                    LN[kk]="Mesa"
                    ######
                    # Linha neutra na MESA do perfil metálico;
                    ######                  
#                    print("A linha neutra se encontra na MESA do perfil metalico")
                    yp=(Cad/(fyd*bf*tf))*tf                     # Espessura comprimida do perfil
                    yt=((tf/2)*(bf*tf)+(tf+h/2)*(h*tw)+((tf-yp)/2+h+tf)*((tf-yp)*bf))/((bf*tf)+(h*tw)+(tf-yp)*bf)
                                                                # Centro de gravidade da seção tracionada do perfil
                    yc=yp/2                                     # Centro de gravidade da seção comprimida do perfil
                    a_ln[kk]=a_ln[kk]+yp
                else:       
                    ######
                    # Linha neutra na ALMA do perfil metálico;
                    ######
                    LN[kk]="Alma"
#                    print("A linha neutra se encontra na ALMA do perfil metalico")
                    yp=tf+(h*((Cad-(fyd*bf*tf))/(fyd*tw*h)))    # Espessura comprimida do perfil
                    yt=((tf/2)*(bf*tf)+((d-yp+tf)/2)*((h+tf-yp)*tw))/((bf*tf)+((h+tf-yp)*tw))    
                                                                # Centro de gravidade da seção tracionada do perfil
                    yc=((tf/2)*(bf*tf)+(((yp-tf)/2)+tf)*(tw*(yp-tf)))/((bf*tf)+(tw*(yp-tf)))          
                                                                # Centro de gravidade da seção comprimida do perfil
                    a_ln[kk]=a_ln[kk]+yp
  
                Mrd[kk]=1*(Cad*(d-yt-yc)+Ccd[kk]*((tc/2)+hf+d-yt))
                
        
        elif(interacao=="Partial"):
        # =============================================================================
        #         ##  INTERAÇÃO PARCIAL  ##
        # =============================================================================
        
        # Neste caso existem duas linhas neutras no conjunto.
            if(L[c]>25):
                texto_erro+=["Beam with a span greater than 25 meters. Partial interaction not allowed"]
                FUNC_JANELA_ERRO()
                print("Beam with a span greater than 25 meters. Partial interaction not allowed")
                exit()
            Le=4*L[c]/5
            ni=1-((E_a/(578*fy))*(0.75-0.03*Le))
            if (ni<0.4):
                ni=0.4

            if(Tad<Ccd[kk]):
                aux1=Tad
            else:
                aux1=Ccd[kk]
                
            S_Qrd=aux1*ni
            Ccd[kk]=S_Qrd
            Cad=(Tad-Ccd[kk])*0.5
            a_ln[kk]=Ccd[kk]/(0.85*fcd*bf)                             # Profundidade da linha neutra na laje de concreto
            if(Cad<(fyd*bf*tf)):   
                ######
                # Linha neutra do perfil metálico na MESA;
                ######                  
#                print("A linha neutra se encontra na MESA do perfil metalico")
                yp=(Cad/(fyd*bf*tf))*tf                     # Espessura comprimida do perfil
                yt=((tf/2)*(bf*tf)+(tf+h/2)*(h*tw)+((tf-yp)/2+h+tf)*((tf-yp)*bf))/((bf*tf)+(h*tw)+(tf-yp)*bf)
                                                            # Centro de gravidade da seção tracionada do perfil
                yc=yp/2                                     # Centro de gravidade da seção comprimida do perfil
                
            else:       
                ######
                # Linha neutra do perfil metálico na ALMA;
                ######
#                print("A linha neutra se encontra na ALMA do perfil metalico")
                yp=tf+(h*((Cad-(fyd*bf*tf))/(fyd*tw*h)))    # Espessura comprimida do perfil
                yt=((tf/2)*(bf*tf)+((d-yp+tf)/2)*((h+tf-yp)*tw))/((bf*tf)+((h+tf-yp)*tw))    
                                                            # Centro de gravidade da seção tracionada do perfil
                yc=((tf/2)*(bf*tf)+(((yp-tf)/2)+tf)*(tw*(yp-tf)))/((bf*tf)+(tw*(yp-tf)))          
                                                            # Centro de gravidade da seção comprimida do perfil
                                
            Mrd[kk]=1*(Cad*(d-yt-yc)+Ccd[kk]*(tc-(a_ln[kk]/2)+hf+d-yt))
    
    elif(classificacao=="semicompacta"):
    # =============================================================================
    #     ## SEÇÃO SEMICOMPACTA  ##
    # =============================================================================
        if(interacao=="Complete"):
    # =============================================================================
    #         ## INTERAÇÃO COMPLETA  ##
    # =============================================================================
            if(Tad<Ccd[kk]):
                aux1=Tad
            else:
                aux1=Ccd[kk]
                    
            S_Qrd=aux1
            Mrdt=fyd*wi
            Mrdc=0.85*fcd*ws*alpha_e
            if(Mrdt<Mrdc):
                aux2=Mrdt
            else:
                aux2=Mrdc
            Mrd[kk]=aux2
            
        elif(interacao=="Partial"):
    # =============================================================================
    #         ## INTERAÇÃO PARCIAL  ##
    # =============================================================================
            
              # Neste caso existem duas linhas neutras no conjunto.
            
            if(L[c]>25):
                texto_erro+=["Beam with a span greater than 25 meters. Partial interaction not allowed"]
                FUNC_JANELA_ERRO()
                print("Beam with a span greater than 25 meters. Partial interaction not allowed")
                exit()
            ni=1-(E_a/(578*fy))*(0.75-0.03*L[c])
            if (ni<0.4):
                ni=0.4
                
            if(Tad<Ccd[kk]):
                Fhd=Tad
            else:
                Fhd=Ccd[kk]   
            S_Qrd=Fhd*ni
            
            wef=wa+np.sqrt(S_Qrd/Fhd)*(wi-wa)
            
            Mrdt=fyd*wef
            Mrdc=0.85*fcd*ws*alpha_e
            if(Mrdt<Mrdc):
                aux2=Mrdt
            else:
                aux2=Mrdc
            Mrd[kk]=aux2





# =============================================================================
#           #####################################################
#           ######  VERIFICAÇÃO DO MOMENTO FLETOR NEGATIVO ######
#           #####################################################
# =============================================================================


def MOMENTO_NEGATIVO():
    global MdistRd , Tds , texto_erro , d3 , d4 , d5
######    DEFINIÇÃO DA LINHA NEUTRA  

    Asl_e=Asl*alpha_f
    A_mesa_s=bs*tf
    A_mesa_i=bf*tf
    A_alma  =h*tw
    

    A_total=Asl_e + A_mesa_s + A_mesa_i + A_alma
    
    y_=((A_mesa_i*tf/2)+(A_alma*(tf+h/2))+(A_mesa_s*(tf+h+tf/2))+(Asl_e*(d+tc-cobrimento-diametro_barras/2)))/A_total
    a_ln[nn]=y_
    
    #print(y_)
            
    
######    VERIFICAÇÕES INICIAIS
    
    if((bf/tf)>(0.38*(np.sqrt(E_a/fy)))): ########################################################################################################################################################################
        texto_erro+=["The flange will suffer local buckling, please increase the thickness of the compressed table!"]
        # FUNC_JANELA_ERRO()
        print("\nThe flange will suffer local buckling, please increase the thickness of the compressed table!\n")
        # exit()
    aux =(2*(y_-tf)-2*ry)/tw

    if(3.76*np.sqrt(E_a/fy)<aux):
        texto_erro+=["The web section will suffer local buckling, please increase the slab thickness or change the profile"]
        FUNC_JANELA_ERRO()
        print("The web section will suffer local buckling, please increase the slab thickness or change the profile!")
        exit()
#######    RESISTÊNCIA DA SEÇÃO TRANSVERSAL    


    Tds=Asl*fsd                 # tensão de escoamento da armadura
    Tds_e=Tds*alpha_f           # tensão de escoamento da armadura equivalente
    
    if(classificacao=="compacta"):
    #     ##   SEÇÃO COMPACTA    ##
        if(y_>=(tf+h)):  
            LN[nn]="mesa superior"
                            # Linha neutra na mesa superior;
            Aac=(bf*tf)+(h*tw)+((y_-h-tf)*bs)
            Aat=( A_mesa_s + A_mesa_i + A_alma) -Aac
            cg_ac=(  (A_mesa_i*tf/2)  +   (A_alma*(tf+h/2))  +  (((y_-tf-h)*bs)*(((y_-tf-h)/2)+h+tf))  )  / (A_mesa_i+A_alma+((y_-tf-h)*bs))
                            
            cg_at=(  (d-y_)*bf*(((d-y_)/2)+(y_))   )  /  ((d-y_)*bf)
            
                            # Linha neutra na alma do perfil;     
        else:
            LN[nn]="alma"
            Aac=((bf*tf)+((y_-tf)*tw))
            Aat=area_p-Aac
            cg_ac=(  (A_mesa_i*tf/2)  +   (((y_-tf)*tw)*(((y_-tf)/2)+tf))  )  / (A_mesa_i+((y_-tf)*tw))
            cg_at=(  ((h+tf-y_)*tw)*(((h+tf-y_)/2)+y_)  +  (bs*tf)*(d-tf/2)  )  / (((h+tf-y_)*tw)  +  (bs*tf) )
            
        #ENDIF
        d3[nn]=(d+tc-cobrimento-diametro_barras/2)-y_
        d4[nn]=cg_at-y_
        d5[nn]=y_-cg_ac

        Mrd[nn]=-1*(Tds*d3[nn]+Aat*fyd*d4[nn]+Aac*fyd*d5[nn])
        
        Mrk  =Tds*d3[nn]*ya + Aat*fyd*d4[nn]*ya + Aac*fyd*d5[nn]*ya
    else:
        #     ##   SEÇÃO NÃO COMPACTA    ##
        texto_erro+=["NBR 8800 only allows compact continuous beams!"]
        FUNC_JANELA_ERRO()
        print("NBR 8800 only allows compact continuous beams!")
        exit()

######    VERIFICAÇÃO DA FLAMBAGEM LATERAL COM DISTORÇÃO DA SEÇÃO TRANSVERSAL
    Cbdist=1
    ho=h+tf
    lambda_dist=5*(1+(tw*(h+tf)/(4*bf*tf)))*((fy**2/(E_a*Cbdist)**2)*((ho/tw)**3)*(tf/bf))**0.25

    if (lambda_dist<0.4):
        Xdist=1
    elif(lambda_dist<=1.5):
        Xdist=0.658**(lambda_dist**2)
    elif(lambda_dist>1.5):
        Xdist=0.877/(lambda_dist**2)
        

    MdistRd[c]=Xdist*Mrd[nn]
    Mrd[nn]=MdistRd[c]
    
    
#=============================================================================#









# =============================================================================
#           ##########################################################
#           ## DIMENSIONAMENTO DA QUANTIA E POSIÇÃO DOS CONECTORES ###
#           ##########################################################
# =============================================================================
    
    
def CONECTORES():

    global Qrd , pos_err , erros , n_con , espac , limitador
    area_secao_con= np.pi * (diametro_conector/2)**2
    
    aux_1_qrd=(area_secao_con * np.sqrt(fck*E_c))/(2)
    aux_2_qrd= (1 * 1 * area_secao_con * fucs)/ycs
    
    
    if (aux_1_qrd>=aux_2_qrd):
        Qrd=aux_2_qrd
    else:
        Qrd=aux_1_qrd
    
    
    c=0
    for k in range (trechos):
        Msd[c]=-MM[int(x_VV0[k]*100)]
        
        if (interacao=="Complete" or "complete"):
            if(LN[c]=="laje"):
                n_con[c]=2*(int((Tad/Qrd))+1)     # Nº de conectores no trecho inteiro(por isso vezes 2)
                limitador[c]="Plastification of steel section"
                
            else:
                n_con[c]=2*(int((Ccd[c]/Qrd))+1)
                limitador[c]="Concrete slab crushing"
        else:
            Fsh      = np.min(Ccd[c],Tad)*(DoC/100)
            n_con[c] = 2*(int((Fsh/Qrd)+1))
            #n_con[c]=2*(int((Ccd[c]/Qrd))+1)
            
            # else Tds=Asl*fsd   (VERIFICAR ESSA PARTE - FUNCIONA PARA FLEXÃO NEGATIVA)     
            
        L_=round( x_MM0[c+1]-x_MM0[c],2)
        
        if (trechos==1):     # A
            recuo=cobrimento*2

            espac[c]=round((L_-recuo-diametro_conector)/(n_con[c]-1)-0.0004,3)
            recuo_considerado=100*((L_-(espac[c]*(n_con[c]-1)))/2)
            # print("recuo_considerado=",recuo_considerado)
            
            
        elif ((trechos>=2 and k==0) or (trechos==2 and k==1) or (trechos==3 and k==2)):   # B ou D
            recuo=cobrimento
            espac[c]=round((L_-recuo)/(n_con[c]),3)
        
        else:
            recuo=0
            espac[c]=round((L_)/(n_con[c]),3)

        if(espac[c]<(6*diametro_conector)):         # VERIFICAÇÃO DA DISTANCIA MINIMA
            espac[c]=round((6*diametro_conector),3)
            n_con[c]=int((L_-recuo)/espac[c])
            espac[c]=round((L_-recuo)/(n_con[c]),3)
            #print("espac6dia=",espac)
            
            
            
        if(espac[c]>(8*tc)):                        # VERIFICAÇÃO DA DISTANCIA MAXIMA
            espac[c]=(8*tc)
            n_con[c]=int((L_-recuo)/espac[c])
            espac[c]=(L_-recuo)/(n_con[c])
           # print("espac8tc=",espac)
        
            
        c=c+2
        
        
    c=1   
    a=0
    for k in range (trechos-1):
        limitador[c]="Plastification of steel bars"
        a=a+L[k]
        Msd[c]=-MM[int(a*100)]
        
        n_con[c]=2*(int(Tds/Qrd)+1)
            
        L_= x_MM0[c+1]-x_MM0[c]
        
        
        espac[c]=L_/(n_con[c])
        
        
        
        if(espac[c]<(6*diametro_conector)):         # VERIFICAÇÃO DA DISTANCIA MINIMA
            espac[c]=round((6*diametro_conector),3)
            n_con[c]=int((L_)/espac[c])
            espac[c]=round((L_)/(n_con[c]),3)

        if(espac[c]>(8*tc)):                        # VERIFICAÇÃO DA DISTANCIA MAXIMA
            espac[c]=(8*tc)
            n_con[c]=int((L_)/espac[c])
            espac[c]=round((L_)/(n_con[c]),3)
        c=c+2
    
#=============================================================================#








# =============================================================================
# # ===========================================================================
# # FUNÇÃO QUE REÚNE AS FUNÇÕES DA NBR 8800
# # ===========================================================================
# =============================================================================

def ESFORCOS_RESISTENTES():  
    global kk , nn , c 

    LARGURA()
    CLASSIFICA()
    CORTANTE()
    
    
    
#    LOOP PARA CALCULO DO MOMENTO POSITIVO DE CADA TRECHO
    kk=0
    for c in range (trechos):                   # MOMENTO POSITIVO RESISTENTE /// ESFORÇO CORTANTE RESISTENTE
        PROPRIEDADES()                          # Tad ; Ccd ; wi ; ws
        MOMENTO_POSITIVO()
        kk=kk+2
    
    
#    LOOP PARA CALCULO DO MOMENTO NEGATIVO DE CADA TRECHO
    nn=1
    for c in range (trechos-1):
        MOMENTO_NEGATIVO()
        nn=nn+2
        
        
#    CHAMA A FUNÇÃO QUE DIMENSIONA OS CONECTORES
    CONECTORES()



def CALCULO_GERAL():
    global fs , E_a , fy , ya , fck , yc , tc , hf , cobrimento , d1 , fyd , fcd , fsd , E_c , alpha_e
    global alpha_f , massa , d , bf , bs , tw , tf , h , d_ , area_p , I_p , wa , ry , Asl , diametro_barras
    global interacao 
    
                                                  
    hf=0                                # Espessura da pré laje                                             (m);
    d1=d/2               # Distância do centro geométrico até a face superior desse perfil   (m);
    fyd=fy/ya                           # Tensão de escoamento de calculo do aço estrutural                    ;
    fcd=fck/yc                          # Resistência de calculo do concreto                                   ;
    fsd=fs/ya                           # Resistência de cálculo ao escoamento do aço da armadura       (KN/m²);
    E_c=4760*(np.sqrt(fck/1000))*1000   # Modulo de elasticidade do concreto(KN/m²)                            ;
    alpha_e=E_a/E_c                     # Razão modular                                                        ;
    alpha_f=fsd/fyd                     # Razão da tensão de escoamento entre aço do perfil e armadura         ;
    Asl=n_barras*(np.pi *(diametro_barras/2)**2)         



    CRIA_VETORES()
    ESFORCOS_ATUANTES()
    ESFORCOS_RESISTENTES()

    

def VERIFICACAO_MOMENTO():
    global texto_erro , texto_erro1 , texto_erro2 , texto_erro3 , texto_erro4 , texto_erro5 , texto_erro6 
    for k in range(len(Mrd)):
        if (abs(Msd[k])>abs(Mrd[k])):
            texto_erro+=["Error in region"]
            texto_erro+=[k+1]
            texto_erro+=["\nRequired moment > Moment capacity!"]
            texto_erro+=["\n\nRequired moment in the region:  "]
            texto_erro+=[round(Msd[k],2)]
            texto_erro+=["\nMoment capacity in the region:   "]
            texto_erro+=[round(Mrd[k],2)]
            FUNC_JANELA_ERRO()
            
def VERIFICACAO_CORTANTE():
    global texto_erro , texto_erro1 , texto_erro2 , texto_erro3 , texto_erro4 , texto_erro5 , texto_erro6 
      
    if (abs(max(VV))>abs(Vrd)):
        texto_erro+=["Error...."]
        texto_erro+=["\n!Required shear > Shear capacity"]
        texto_erro+=["\n\nRequired Shear in the region:  "]
        texto_erro+=[round(abs(max(VV)),2)]
        texto_erro+=["\nShear capacity in the region:   "]
        texto_erro+=[round(Vrd,2)]
        FUNC_JANELA_ERRO()

def CALCULO_CORTE_NBR():
    CALCULO_GERAL()
    GRAFICO_CORTE_ATUANTE()
    GRAFICO_CORTE_RESISTENTE()
    GRAFICO_RESULTADO_CORTE()
    escreve_frame_trechos()
    VERIFICACAO_CORTANTE()
    
def CALCULO_MOMENTO_NBR():
    CALCULO_GERAL()
    GRAFICO_MOMENTO_ATUANTE()
    GRAFICO_MOMENTO_RESISTENTE()
    GRAFICO_RESULTADO_MOMENTO()
    escreve_frame_trechos()
    VERIFICACAO_MOMENTO()

# # # # =========================================================================
# # # # # #######################      RELATÓRIO EXCEL     ######################
# # # # =========================================================================

def FUNC_RELATORIO():

    outexcel = sl.Workbook("Report_COMBEAMS.xlsx")
    outsheet = outexcel.add_worksheet()
    outsheet.hide_gridlines(2)
    
    outsheet.set_column(0,8,10)
    
    formato_subtitulos= outexcel.add_format({
        'bold':1,
        'align':'center',
        'valign': 'vcenter',
        'border':1
        })
    
    formato_c= outexcel.add_format({
        'align':'center',
        'valign': 'vcenter',
        })
    
    formato_c_b= outexcel.add_format({
        'align':'center',
        'bold':1,
        'valign': 'vcenter',
        'text_wrap':'true',
        })
    
    formato_correto= outexcel.add_format({
        'align':'center',
        'valign': 'vcenter',
        'text_wrap':'true',
        'bg_color':'green'
        })
    
    formato_erro= outexcel.add_format({
        'align':'center',
        'valign': 'vcenter',
        'text_wrap':'true',
        'bg_color':'red'
        })

    linha=1
    # =============================================================================
    # DADOS LINEARES
    # =============================================================================
    outsheet.merge_range(0,0,0,1,'LINEAR DATA',formato_subtitulos)
    
    outsheet.write(linha,0,"regions=",formato_c_b)   ;    outsheet.write(linha,1,trechos,formato_c)
    
    for n in range(trechos):
        outsheet.write(linha+n+2,0,"L%d="%(n+1),formato_c_b)
        outsheet.write(linha+n+2,1,L[n],formato_c)
        
        outsheet.write(linha+n+5,0,"q%d="%(n+1),formato_c_b)
        outsheet.write(linha+n+5,1,q[n],formato_c)
    
    linha=2
    # =============================================================================
    # DADOS DO PERFIL
    # =============================================================================
    
    outsheet.merge_range('C1:H1','SECTION DATA',formato_subtitulos)
    
    outsheet.write(linha+2,3,'bf=',formato_c_b)    ;   outsheet.write(linha+2,4,bf,formato_c)
    outsheet.write(linha+3,3,'tf=',formato_c_b)    ;   outsheet.write(linha+3,4,tf,formato_c)
    outsheet.write(linha+4,3,'h=',formato_c_b)     ;   outsheet.write(linha+4,4,h,formato_c)
    outsheet.write(linha+5,3,'d=',formato_c_b)     ;   outsheet.write(linha+5,4,d,formato_c)
    outsheet.write(linha+6,3,"d'=",formato_c_b)    ;   outsheet.write(linha+6,4,d_,formato_c)
    
    outsheet.write(linha+2,6,'tw=',formato_c_b)      ;   outsheet.write(linha+2,7,tw,formato_c)
    outsheet.write(linha+3,6,'ry=',formato_c_b)      ;   outsheet.write(linha+3,7,ry,formato_c)
    outsheet.write(linha+4,6,'Wx=',formato_c_b)      ;   outsheet.write(linha+4,7,Wx,formato_c)
    outsheet.write(linha+5,6,'Ix=',formato_c_b)      ;   outsheet.write(linha+5,7,I_p,formato_c)
    outsheet.write(linha+6,6,"Área=",formato_c_b)    ;   outsheet.write(linha+6,7,area_p,formato_c)
    
    outsheet.insert_image(linha+8,1,"imagens\SECAO_330x344.png")
    # =============================================================================
    # DADOS GERAIS
    # =============================================================================
    linha=10

    outsheet.merge_range(linha,6,linha,7,'GENERAL DATA',formato_subtitulos)
    
    outsheet.write(linha+1,6,'Interação=',formato_c_b)      ;   outsheet.write(linha+1,7,interacao,formato_c)
    outsheet.write(linha+2,6,'Lb_máx=',formato_c_b)         ;   outsheet.write(linha+2,7,Lb_max,formato_c)
    outsheet.write(linha+3,6,'tc=',formato_c_b)             ;   outsheet.write(linha+3,7,tc,formato_c)
    outsheet.write(linha+4,6,'Nº barras=',formato_c_b)      ;   outsheet.write(linha+4,7,n_barras,formato_c)
    outsheet.write(linha+5,6,'Ø barras=',formato_c_b)       ;   outsheet.write(linha+5,7,diametro_barras,formato_c)
    outsheet.write(linha+6,6,"c=",formato_c_b)              ;   outsheet.write(linha+6,7,cobrimento,formato_c)
    outsheet.write(linha+7,6,"fucs=",formato_c_b)           ;   outsheet.write(linha+7,7,fucs,formato_c)
    outsheet.write(linha+8,6,"Ø conector=",formato_c_b)     ;   outsheet.write(linha+8,7,diametro_conector,formato_c)
    outsheet.write(linha+9,6,"y conector=",formato_c_b)     ;   outsheet.write(linha+9,7,ycs,formato_c) 
    if interacao == 'Partial':
        outsheet.write(linha+10,6,"DoC=",formato_c_b)           ;   outsheet.write(linha+10,7,DoC,formato_c) 
    
    # =============================================================================
    # MATERIAIS
    # =============================================================================
    linha=21
    
    outsheet.merge_range(linha,6,linha,7,'MATERIALS',formato_subtitulos)
    
    outsheet.write(linha+1,6,'fck=',formato_c_b)         ;   outsheet.write(linha+1,7,fck,formato_c)
    outsheet.write(linha+2,6,'yc=',formato_c_b)          ;   outsheet.write(linha+2,7,yc,formato_c)
    outsheet.write(linha+3,6,'E aço=',formato_c_b)       ;   outsheet.write(linha+3,7,E_a,formato_c)
    outsheet.write(linha+4,6,'fy=',formato_c_b)          ;   outsheet.write(linha+4,7,fy,formato_c)
    outsheet.write(linha+5,6,"ya=",formato_c_b)          ;   outsheet.write(linha+5,7,ya,formato_c)
    outsheet.write(linha+6,6,"E armadura=",formato_c_b)  ;   outsheet.write(linha+6,7,E_as,formato_c)
    outsheet.write(linha+7,6,"fs=",formato_c_b)          ;   outsheet.write(linha+7,7,fs,formato_c)
    outsheet.write(linha+8,6,"ys=",formato_c_b)          ;   outsheet.write(linha+8,7,ys,formato_c)
    
    
    # =============================================================================
    # OUTROS
    # =============================================================================
    linha=31
    outsheet.merge_range(linha,0,linha,7,'OTHERS',formato_subtitulos)
    
    
    outsheet.write(linha+1,0,'hf=',formato_c_b)          ;   outsheet.write(linha+1,1,hf,formato_c)
    outsheet.write(linha+2,0,'fyd=',formato_c_b)         ;   outsheet.write(linha+2,1,fyd,formato_c)
    
    outsheet.write(linha+1,2,'fcd=',formato_c_b)         ;   outsheet.write(linha+1,3,fcd,formato_c)
    outsheet.write(linha+2,2,'fsd=',formato_c_b)         ;   outsheet.write(linha+2,3,fsd,formato_c)
    
    outsheet.write(linha+1,4,'E concreto=',formato_c_b)  ;   outsheet.write(linha+1,5,E_c,formato_c)
    outsheet.write(linha+2,4,'Asl=',formato_c_b)         ;   outsheet.write(linha+2,5,Asl,formato_c)
    
    outsheet.write(linha+1,6,'alpha e=',formato_c_b)     ;   outsheet.write(linha+1,7,alpha_e,formato_c)
    outsheet.write(linha+2,6,'alpha f=',formato_c_b)     ;   outsheet.write(linha+2,7,alpha_f,formato_c)
    
    # =============================================================================
    # # ===========================================================================
    # # NBR 8800
    # # ===========================================================================
    # =============================================================================

    
    # =============================================================================
    # LARGURA EFETIVA
    # =============================================================================
    linha=36
    
    outsheet.merge_range(linha,0,linha,7,'EFFECTIVE WIDTH',formato_subtitulos)
    
    if (trechos==1):
        outsheet.insert_image(linha+2,0,"imagens\a_trecho.jpeg",{'x_scale': 0.65, 'y_scale': 0.65})
    elif(trechos==2):
        outsheet.insert_image(linha+2,0,"imagens\b_trecho.png",{'x_scale': 0.3, 'y_scale': 0.3})
    else:
        outsheet.insert_image(linha+2,0,"imagens\c_trecho.png",{'x_scale': 0.3, 'y_scale': 0.3})
    l=45
    c=0
    for n in range (size_vetor):
        l=l+0.3
        outsheet.write(int(l),c,"Lb %d ="%(n+1),formato_c_b) ; outsheet.write(int(l),c+1,lb[n],formato_c_b)
        outsheet.write(int(l)-5+n,6,"L%d efetivo="%(n+1),formato_c) ; outsheet.write(int(l)-5+n,7,x_MM0[n+1]-x_MM0[n],formato_c)
        c=c+3
        if (c==9):
            c=0

    # =============================================================================
    # CLASSIFICAÇÃO DA SEÇÃO
    # =============================================================================
    
    outsheet.merge_range('A48:H48','CLASSIFICATION',formato_subtitulos)
    
    outsheet.merge_range('A49:H49',classificacao,formato_c_b)
    
    linha=50
    
    outsheet.write(linha-1,1,"λ=%d"%lambda_,formato_c_b)
    outsheet.write(linha-1,3,"λp= %d"%lambda_p,formato_c_b)
    outsheet.write(linha-1,5,"λr= %d"%lambda_r,formato_c_b)
    
    # =============================================================================
    # PROPRIEDADES
    # =============================================================================
    
    outsheet.merge_range('A52:H52','PROPERTIES',formato_subtitulos)
    
    # Força resistente de cálculo da laje de concreto
    
    outsheet.merge_range('A54:D54','Strength of Concrete Slab',formato_subtitulos)
    linha=linha+5
    for n in range(size_vetor):
        
        outsheet.write(linha+n,1,"Ccd%d="%(n+1),formato_c_b)
        if (n==1 or n==3):
            outsheet.write(linha+n,2,'tensile',formato_c)
        else:
            outsheet.write(linha+n,2,Ccd[n],formato_c)
    
    # Força resistente de cálculo do perfil
    
    outsheet.merge_range('E54:H54','Strength of steel section',formato_subtitulos)

    outsheet.write(linha,5,"Tad=",formato_c_b)
    outsheet.write(linha,6,Tad,formato_c)
    
    # Módulo de resistência elástico da seção
    
    outsheet.merge_range('A63:D65','Section elastic modulus of resistance \n mixed transverse in relation to the bending axis \n higher than CG.',formato_c_b)
    outsheet.merge_range('E63:H65','Section elastic modulus of resistance \n mixed transverse in relation to the bending axis \n lower than CG.',formato_c_b)
    linha=linha+12
    for n in range(size_vetor):
        
        outsheet.write(linha+n,1,"ws %d="%(n+1),formato_c_b)
        outsheet.write(linha+n,2,ws_vetor[n],formato_c)  
            
        outsheet.write(linha+n,5,"wi %d="%(n+1),formato_c_b)
        outsheet.write(linha+n,6,wi_vetor[n],formato_c)
    
    # =============================================================================
    # VERIFICAÇÃO A FORÇA CORTANTE
    # =============================================================================
    # linha=67
    linha=linha+12
    outsheet.merge_range('A75:H75','REQUIRED SHEAR',formato_subtitulos)
    
    outsheet.merge_range('A77:H77','The required shear is given considering the resistance of the steel section!',formato_c_b)
    
    outsheet.write(linha,1,"k=",formato_c_b)            ;   outsheet.write(linha,2,5,formato_c)  
    outsheet.write(linha+1,1,"Vpl=",formato_c_b)        ;   outsheet.write(linha+1,2,Vpl,formato_c)  
    outsheet.write(linha+2,1,"Vrd=",formato_subtitulos) ;   outsheet.write(linha+2,2,Vrd,formato_c_b)  
    
    outsheet.write(linha,5,"λ=",formato_c_b)     ;   outsheet.write(linha  ,6,round(lambda_corte ,2),formato_c)  
    outsheet.write(linha+1,5,"λp=",formato_c_b)  ;   outsheet.write(linha+1,6,round(lambda_p_corte,2),formato_c)      
    outsheet.write(linha+2,5,"λr=",formato_c_b)  ;   outsheet.write(linha+2,6,round(lambda_r_corte,2),formato_c)  
    
    # =============================================================================
    # MOMENTO POSITIVO
    # =============================================================================
    # linha=79
    
    linha=linha+4
    outsheet.merge_range(linha,0,linha,7,'POSITIVE MOMENT',formato_subtitulos)
    
    xlsx1=0
    xlsx2=0
    # if(interacao=="Complete" or "Partial"):
    outsheet.merge_range(linha+2,0,linha+2,4,'Compressed section thickness',formato_subtitulos)
        
    linha=linha+3
        
    for n in range(size_vetor):
        outsheet.write(linha+n,0,"Trecho %d"%(n+1),formato_c_b)
        if (n==1 or n==3):
            outsheet.merge_range(linha+n,1,linha+n,4,'Negative Moment',formato_c)
        else:
            outsheet.merge_range(linha+n,1,linha+n,2,'Neutral line in %s'%LN[n],formato_c)
            outsheet.write(linha+n,3,"Hc=",formato_c_b)  ;   outsheet.write(linha+n,4,round(a_ln[n],4),formato_c)  
        
        linha=linha+8
        xlsx1=8
        xlsx2=11
        
    outsheet.merge_range(linha+2-xlsx2,6,linha+2-xlsx2,7,'Moment Capacity',formato_subtitulos)
    for n in range(size_vetor):
        if (n==1 or n==3):
            outsheet.merge_range(linha+n-xlsx1,6,linha+n-8,7,'Negative Moment',formato_c)
        else:
            outsheet.write(linha+n-xlsx1,6,"Mrd %d="%(n+1),formato_c_b)  ;   outsheet.write(linha+n-xlsx1,7,round(Mrd[n],2),formato_c_b) 
    linha=linha +8
    linha=linha-xlsx1   
    
    # =============================================================================
    # MOMENTO NEGATIVO
    # =============================================================================
    # linha=87
    outsheet.merge_range(linha,0,linha,7,'NEGATIVE MOMENT',formato_subtitulos)
    
    xlsx1=0
    
    for n in range(size_vetor):
        if (n==1 or n==3):
            outsheet.merge_range(linha+2,1,linha+2,6,'REGION %d'%(n+1),formato_subtitulos)
            
            
            outsheet.merge_range(linha+3,1,linha+3,5,'Compressed section thickness =')
            outsheet.write(linha+3+xlsx1,6,round(a_ln[n],5),formato_c_b)
            
            outsheet.merge_range(linha+4,1,linha+4,5,'d3 = distancia do CG da armadura à linha neutra =')
            outsheet.write(linha+4+xlsx1,6,round(d3[n],2),formato_c_b)
            
            outsheet.merge_range(linha+5,1,linha+5,5,'d4 = distance from the CG of the armature to the neutral axis =')
            outsheet.write(linha+5+xlsx1,6,round(d4[n],2),formato_c_b)
            
            outsheet.merge_range(linha+6,1,linha+6,5,'d5 = distance from the CG of the compressed area to the neutral axis =')
            outsheet.write(linha+6+xlsx1,6,round(d5[n],2),formato_c_b)
            
            outsheet.merge_range(linha+7,1,linha+7,5,'bending moment capacity =')
            outsheet.write(linha+7+xlsx1,6,round(Mrd[n],2),formato_c_b)
    
            
            linha=linha+7
    
    # =============================================================================
    # VERIFICAÇÃO DOS MOMENTOS
    # =============================================================================
    # linha=87
    
    linha = linha +3
    outsheet.merge_range(linha,0,linha,7,'CHECKS',formato_subtitulos) 
    
    linha = linha +2
    
    # VERIFICAÇÃO MOMENTO
    
    outsheet.merge_range(linha,2,linha,5,'Bending Moment',formato_subtitulos)
    outsheet.write(linha+1,2,'Regions',formato_subtitulos)
    outsheet.write(linha+1,3,'Mrd',formato_subtitulos)
    outsheet.write(linha+1,4,'Msd',formato_subtitulos)
    outsheet.write(linha+1,5,'Status',formato_subtitulos)
    
    linha = linha +2
        
    for n in range (size_vetor):
        
        if(np.sqrt(Mrd[n]**2)>=np.sqrt(msd_max_[n]**2)):
            outsheet.write(linha+n,2,  'Region %d'%n       ,formato_c)
            outsheet.write(linha+n,3,  round(Mrd[n]     ,2),formato_c)
            outsheet.write(linha+n,4,  round(msd_max_[n],2),formato_c)
            outsheet.write(linha+n,5,  'OK!'               ,formato_correto)
        else:
            outsheet.write(linha+n,2,  'Region %d'%n       ,formato_c)
            outsheet.write(linha+n,3,  round(Mrd[n]     ,2),formato_c)
            outsheet.write(linha+n,4,  round(msd_max_[n],2),formato_c)
            outsheet.write(linha+n,5,  'FAILURE!'          ,formato_erro)
      
    # VERIFICAÇÃO CORTANTE
    
    linha = linha +6
    
    outsheet.merge_range(linha,2,linha,5,'Shear required',formato_subtitulos)
    outsheet.write(linha+1,2,'Region',formato_subtitulos)
    outsheet.write(linha+1,3,'Vrd',formato_subtitulos)
    outsheet.write(linha+1,4,'Vsd',formato_subtitulos)
    outsheet.write(linha+1,5,'Status',formato_subtitulos)
    
    linha = linha +2
    for n in range (size_vetor):
        
        if(Vrd>=vsd_max_[n]):
            outsheet.write(linha+n,2,  'Region %d'%n       ,formato_c)
            outsheet.write(linha+n,3,  round(Vrd        ,2),formato_c)
            outsheet.write(linha+n,4,  round(vsd_max_[n],2),formato_c)
            outsheet.write(linha+n,5,  'OK!'               ,formato_correto)
        else:
            outsheet.write(linha+n,2,  'Region %d'%n       ,formato_c)
            outsheet.write(linha+n,3,  round(Vrd        ,2),formato_c)
            outsheet.write(linha+n,4,  round(vsd_max_[n],2),formato_c)
            outsheet.write(linha+n,5,  'FAILURE!'            ,formato_erro)

    # =============================================================================
    # CONECTORES
    # =============================================================================
    # linha=87
    linha = linha +7
    outsheet.merge_range(linha,0,linha,7,'SHEAR STUDS',formato_subtitulos)
    
    outsheet.write(linha+2,1,'Regions'    ,formato_subtitulos)
    outsheet.write(linha+2,2,'Qrd'    ,formato_subtitulos)
    outsheet.write(linha+2,3,'Nº con.'    ,formato_subtitulos)
    outsheet.write(linha+2,4,'Pitch',formato_subtitulos)
    outsheet.merge_range(linha+2,5,linha+2,7,'STUDS LIMATITION',formato_subtitulos)
    
    linha = linha +3
    for n in range (size_vetor):
        
        outsheet.write(linha+n,1,  'Region %d'%n       ,formato_c)
        outsheet.write(linha+n,2,  round(Qrd,3)        ,formato_c)
        outsheet.write(linha+n,3,  n_con[n]            ,formato_c)
        outsheet.write(linha+n,4,  round(espac[n],3)   ,formato_c)
        outsheet.merge_range(linha+n,5,linha+n,7,limitador[n],formato_c)
    
    outexcel.close()
    
cont1=0
contador=(len(dados[:,1]))-1
teste_insere_perfil=0
#=============================================================================
# =============================================================================
# =============================================================================
# # # =========================================================================
# # # # ####################### GRAPHICAL USER INTERFACE ######################
# # # =========================================================================
# =============================================================================
# =============================================================================

def Reescreve_labels_frame1():

    la_VA_bf = tk.Label(Frame2)
    la_VA_bf.place(relx=0.176, rely=0.487, height=26, width=72)
    la_VA_bf.configure(activebackground="#f9f9f9")
    la_VA_bf.configure(activeforeground="black")
    la_VA_bf.configure(background="#fbfbfb")
    la_VA_bf.configure(disabledforeground="#a3a3a3")
    la_VA_bf.configure(foreground="#000000")
    la_VA_bf.configure(highlightbackground="#d9d9d9")
    la_VA_bf.configure(highlightcolor="black")
    la_VA_bf.configure(text=bf)
        
    la_VA_tf = tk.Label(Frame2)
    la_VA_tf.place(relx=0.176, rely=0.526, height=26, width=72)
    la_VA_tf.configure(activebackground="#f9f9f9")
    la_VA_tf.configure(activeforeground="black")
    la_VA_tf.configure(background="#fbfbfb")
    la_VA_tf.configure(disabledforeground="#a3a3a3")
    la_VA_tf.configure(foreground="#000000")
    la_VA_tf.configure(highlightbackground="#d9d9d9")
    la_VA_tf.configure(highlightcolor="black")
    la_VA_tf.configure(text=tf)
    
    la_VA_h = tk.Label(Frame2)
    la_VA_h.place(relx=0.176, rely=0.564, height=26, width=72)
    la_VA_h.configure(activebackground="#f9f9f9")
    la_VA_h.configure(activeforeground="black")
    la_VA_h.configure(background="#fbfbfb")
    la_VA_h.configure(disabledforeground="#a3a3a3")
    la_VA_h.configure(foreground="#000000")
    la_VA_h.configure(highlightbackground="#d9d9d9")
    la_VA_h.configure(highlightcolor="black")
    la_VA_h.configure(text=h)
    
    la_VA_d = tk.Label(Frame2)
    la_VA_d.place(relx=0.176, rely=0.603, height=25, width=72)
    la_VA_d.configure(activebackground="#f9f9f9")
    la_VA_d.configure(activeforeground="black")
    la_VA_d.configure(background="#fbfbfb")
    la_VA_d.configure(disabledforeground="#a3a3a3")
    la_VA_d.configure(foreground="#000000")
    la_VA_d.configure(highlightbackground="#d9d9d9")
    la_VA_d.configure(highlightcolor="black")
    la_VA_d.configure(text=d)
    
    la_VA_d_ = tk.Label(Frame2)
    la_VA_d_.place(relx=0.176, rely=0.641, height=26, width=72)
    la_VA_d_.configure(activebackground="#f9f9f9")
    la_VA_d_.configure(activeforeground="black")
    la_VA_d_.configure(background="#fbfbfb")
    la_VA_d_.configure(disabledforeground="#a3a3a3")
    la_VA_d_.configure(foreground="#000000")
    la_VA_d_.configure(highlightbackground="#d9d9d9")
    la_VA_d_.configure(highlightcolor="black")
    la_VA_d_.configure(text=d_)
    
    la_VA_tw = tk.Label(Frame2)
    la_VA_tw.place(relx=0.618, rely=0.487, height=26, width=72)
    la_VA_tw.configure(activebackground="#f9f9f9")
    la_VA_tw.configure(activeforeground="black")
    la_VA_tw.configure(background="#fbfbfb")
    la_VA_tw.configure(disabledforeground="#a3a3a3")
    la_VA_tw.configure(foreground="#000000")
    la_VA_tw.configure(highlightbackground="#d9d9d9")
    la_VA_tw.configure(highlightcolor="black")
    la_VA_tw.configure(text=tw)
    
    la_VA_ry = tk.Label(Frame2)
    la_VA_ry.place(relx=0.618, rely=0.526, height=26, width=72)
    la_VA_ry.configure(activebackground="#f9f9f9")
    la_VA_ry.configure(activeforeground="black")
    la_VA_ry.configure(background="#fbfbfb")
    la_VA_ry.configure(disabledforeground="#a3a3a3")
    la_VA_ry.configure(foreground="#000000")
    la_VA_ry.configure(highlightbackground="#d9d9d9")
    la_VA_ry.configure(highlightcolor="black")
    la_VA_ry.configure(text=ry)
    
    la_VA_wx = tk.Label(Frame2)
    la_VA_wx.place(relx=0.618, rely=0.564, height=26, width=72)
    la_VA_wx.configure(activebackground="#f9f9f9")
    la_VA_wx.configure(activeforeground="black")
    la_VA_wx.configure(background="#fbfbfb")
    la_VA_wx.configure(disabledforeground="#a3a3a3")
    la_VA_wx.configure(foreground="#000000")
    la_VA_wx.configure(highlightbackground="#d9d9d9")
    la_VA_wx.configure(highlightcolor="black")
    la_VA_wx.configure(text=Wx)
    
    la_VA_ix = tk.Label(Frame2)
    la_VA_ix.place(relx=0.618, rely=0.603, height=26, width=72)
    la_VA_ix.configure(activebackground="#f9f9f9")
    la_VA_ix.configure(activeforeground="black")
    la_VA_ix.configure(background="#fbfbfb")
    la_VA_ix.configure(disabledforeground="#a3a3a3")
    la_VA_ix.configure(foreground="#000000")
    la_VA_ix.configure(highlightbackground="#d9d9d9")
    la_VA_ix.configure(highlightcolor="black")
    la_VA_ix.configure(text=I_p)
    
    la_VA_area = tk.Label(Frame2)
    la_VA_area.place(relx=0.618, rely=0.641, height=25, width=72)
    la_VA_area.configure(activebackground="#f9f9f9")
    la_VA_area.configure(activeforeground="black")
    la_VA_area.configure(background="#fbfbfb")
    la_VA_area.configure(disabledforeground="#a3a3a3")
    la_VA_area.configure(foreground="#000000")
    la_VA_area.configure(highlightbackground="#d9d9d9")
    la_VA_area.configure(highlightcolor="black")
    la_VA_area.configure(text=area_p)
    
    la_VA_tc = tk.Label(Frame2)
    la_VA_tc.place(relx=0.176, rely=0.731, height=25, width=72)
    la_VA_tc.configure(activebackground="#f9f9f9")
    la_VA_tc.configure(activeforeground="black")
    la_VA_tc.configure(background="#fbfbfb")
    la_VA_tc.configure(disabledforeground="#a3a3a3")
    la_VA_tc.configure(foreground="#000000")
    la_VA_tc.configure(highlightbackground="#d9d9d9")
    la_VA_tc.configure(highlightcolor="black")
    la_VA_tc.configure(text=tc)
    
    la_VA_n_barras = tk.Label(Frame2)
    la_VA_n_barras.place(relx=0.162, rely=0.821, height=25, width=52)
    la_VA_n_barras.configure(activebackground="#f9f9f9")
    la_VA_n_barras.configure(activeforeground="black")
    la_VA_n_barras.configure(background="#fbfbfb")
    la_VA_n_barras.configure(disabledforeground="#a3a3a3")
    la_VA_n_barras.configure(foreground="#000000")
    la_VA_n_barras.configure(highlightbackground="#d9d9d9")
    la_VA_n_barras.configure(highlightcolor="black")
    la_VA_n_barras.configure(text=n_barras)
    
    la_VA_diametro_barras = tk.Label(Frame2)
    la_VA_diametro_barras.place(relx=0.471, rely=0.821, height=25, width=52)
    la_VA_diametro_barras.configure(activebackground="#f9f9f9")
    la_VA_diametro_barras.configure(activeforeground="black")
    la_VA_diametro_barras.configure(background="#fbfbfb")
    la_VA_diametro_barras.configure(disabledforeground="#a3a3a3")
    la_VA_diametro_barras.configure(foreground="#000000")
    la_VA_diametro_barras.configure(highlightbackground="#d9d9d9")
    la_VA_diametro_barras.configure(highlightcolor="black")
    la_VA_diametro_barras.configure(text=diametro_barras)
    
    la_VA_cobri = tk.Label(Frame2)
    la_VA_cobri.place(relx=0.765, rely=0.821, height=25, width=52)
    la_VA_cobri.configure(activebackground="#f9f9f9")
    la_VA_cobri.configure(activeforeground="black")
    la_VA_cobri.configure(background="#fbfbfb")
    la_VA_cobri.configure(disabledforeground="#a3a3a3")
    la_VA_cobri.configure(foreground="#000000")
    la_VA_cobri.configure(highlightbackground="#d9d9d9")
    la_VA_cobri.configure(highlightcolor="black")
    la_VA_cobri.configure(text=cobrimento)
    
    la_VA_fucs = tk.Label(Frame2)
    la_VA_fucs.place(relx=0.176, rely=0.91, height=26, width=72)
    la_VA_fucs.configure(activebackground="#f9f9f9")
    la_VA_fucs.configure(activeforeground="black")
    la_VA_fucs.configure(background="#fbfbfb")
    la_VA_fucs.configure(disabledforeground="#a3a3a3")
    la_VA_fucs.configure(foreground="#000000")
    la_VA_fucs.configure(highlightbackground="#d9d9d9")
    la_VA_fucs.configure(highlightcolor="black")
    la_VA_fucs.configure(text=fucs)
    
    la_VA_γc = tk.Label(Frame2)
    la_VA_γc.place(relx=0.588, rely=0.91, height=26, width=72)
    la_VA_γc.configure(activebackground="#f9f9f9")
    la_VA_γc.configure(activeforeground="black")
    la_VA_γc.configure(background="#fbfbfb")
    la_VA_γc.configure(disabledforeground="#a3a3a3")
    la_VA_γc.configure(foreground="#000000")
    la_VA_γc.configure(highlightbackground="#d9d9d9")
    la_VA_γc.configure(highlightcolor="black")
    la_VA_γc.configure(text=ycs)
    
    la_VA_Ø = tk.Label(Frame2)
    la_VA_Ø.place(relx=0.176, rely=0.949, height=25, width=72)
    la_VA_Ø.configure(activebackground="#f9f9f9")
    la_VA_Ø.configure(activeforeground="black")
    la_VA_Ø.configure(background="#fbfbfb")
    la_VA_Ø.configure(disabledforeground="#a3a3a3")
    la_VA_Ø.configure(foreground="#000000")
    la_VA_Ø.configure(highlightbackground="#d9d9d9")
    la_VA_Ø.configure(highlightcolor="black")
    la_VA_Ø.configure(text=diametro_conector)

# =============================================================================
# JANELA GEOMETRIA
# =============================================================================
def call_janela_geometria():
    
    # =========================================================================
    #     #           INSERIR PERFIL
    # =========================================================================
    def call_ja_geo_per_inserir():
        
        janela_perfil_inserir=tk.Tk()

        janela_perfil_inserir.geometry("340x500+600+4")
        janela_perfil_inserir.minsize(148, 1)
        janela_perfil_inserir.maxsize(1924, 1055)
        janela_perfil_inserir.resizable(0, 0)
        janela_perfil_inserir.iconbitmap('icones/geral.ico')
        janela_perfil_inserir.title("Section Options")
        janela_perfil_inserir.configure(background="#d9d9d9")
        janela_perfil_inserir.configure(highlightbackground="#d9d9d9")
        janela_perfil_inserir.configure(highlightcolor="black")

        Frame2 = tk.Frame(janela_perfil_inserir)
        Frame2.place(relx=0.029, rely=0.014, relheight=0.84, relwidth=0.941)
        Frame2.configure(relief='groove')
        Frame2.configure(borderwidth="2")
        Frame2.configure(relief="groove")
        Frame2.configure(background="#d9d9d9")
        Frame2.configure(cursor="fleur")
        Frame2.configure(highlightbackground="#d9d9d9")
        Frame2.configure(highlightcolor="black")

        la_perfil = tk.Label(Frame2)
        la_perfil.place(relx=0.031, rely=0.021, height=14, width=49)
        la_perfil.configure(activebackground="#f9f9f9")
        la_perfil.configure(activeforeground="black")
        la_perfil.configure(background="#d9d9d9")
        la_perfil.configure(disabledforeground="#a3a3a3")
        la_perfil.configure(font="-family {Segoe UI} -size 9 -weight bold -slant italic")
        la_perfil.configure(foreground="#000000")
        la_perfil.configure(highlightbackground="#d9d9d9")
        la_perfil.configure(highlightcolor="black")
        la_perfil.configure(text='''Section''')

        la_bf = tk.Label(Frame2)
        la_bf.place(relx=0.031, rely=0.088, height=13, width=40)
        la_bf.configure(activebackground="#f9f9f9")
        la_bf.configure(activeforeground="black")
        la_bf.configure(background="#d9d9d9")
        la_bf.configure(disabledforeground="#a3a3a3")
        la_bf.configure(foreground="#000000")
        la_bf.configure(highlightbackground="#d9d9d9")
        la_bf.configure(highlightcolor="black")
        la_bf.configure(justify='left')
        la_bf.configure(text='''bf=''')

        la_tf = tk.Label(Frame2)
        la_tf.place(relx=0.028, rely=0.152, height=14, width=40)
        la_tf.configure(activebackground="#f9f9f9")
        la_tf.configure(activeforeground="black")
        la_tf.configure(background="#d9d9d9")
        la_tf.configure(disabledforeground="#a3a3a3")
        la_tf.configure(foreground="#000000")
        la_tf.configure(highlightbackground="#d9d9d9")
        la_tf.configure(highlightcolor="black")
        la_tf.configure(justify='left')
        la_tf.configure(text='''tf=''')

        la_h = tk.Label(Frame2)
        la_h.place(relx=0.028, rely=0.219, height=13, width=40)
        la_h.configure(activebackground="#f9f9f9")
        la_h.configure(activeforeground="black")
        la_h.configure(background="#d9d9d9")
        la_h.configure(disabledforeground="#a3a3a3")
        la_h.configure(foreground="#000000")
        la_h.configure(highlightbackground="#d9d9d9")
        la_h.configure(highlightcolor="black")
        la_h.configure(justify='left')
        la_h.configure(text='''h=''')

        la_d = tk.Label(Frame2)
        la_d.place(relx=0.028, rely=0.283, height=14, width=40)
        la_d.configure(activebackground="#f9f9f9")
        la_d.configure(activeforeground="black")
        la_d.configure(background="#d9d9d9")
        la_d.configure(disabledforeground="#a3a3a3")
        la_d.configure(foreground="#000000")
        la_d.configure(highlightbackground="#d9d9d9")
        la_d.configure(highlightcolor="black")
        la_d.configure(justify='left')
        la_d.configure(text='''d=''')

        la_d_ = tk.Label(Frame2)
        la_d_.place(relx=0.028, rely=0.35, height=13, width=40)
        la_d_.configure(activebackground="#f9f9f9")
        la_d_.configure(activeforeground="black")
        la_d_.configure(background="#d9d9d9")
        la_d_.configure(disabledforeground="#a3a3a3")
        la_d_.configure(foreground="#000000")
        la_d_.configure(highlightbackground="#d9d9d9")
        la_d_.configure(highlightcolor="black")
        la_d_.configure(justify='left')
        la_d_.configure(text='''d_=''')

        la_tw = tk.Label(Frame2)
        la_tw.place(relx=0.472, rely=0.088, height=13, width=40)
        la_tw.configure(activebackground="#f9f9f9")
        la_tw.configure(activeforeground="black")
        la_tw.configure(background="#d9d9d9")
        la_tw.configure(disabledforeground="#a3a3a3")
        la_tw.configure(foreground="#000000")
        la_tw.configure(highlightbackground="#d9d9d9")
        la_tw.configure(highlightcolor="black")
        la_tw.configure(justify='left')
        la_tw.configure(text='''tw=''')

        la_ry = tk.Label(Frame2)
        la_ry.place(relx=0.472, rely=0.152, height=14, width=40)
        la_ry.configure(activebackground="#f9f9f9")
        la_ry.configure(activeforeground="black")
        la_ry.configure(background="#d9d9d9")
        la_ry.configure(disabledforeground="#a3a3a3")
        la_ry.configure(foreground="#000000")
        la_ry.configure(highlightbackground="#d9d9d9")
        la_ry.configure(highlightcolor="black")
        la_ry.configure(justify='left')
        la_ry.configure(text='''ry=''')

        la_wx = tk.Label(Frame2)
        la_wx.place(relx=0.469, rely=0.219, height=13, width=40)
        la_wx.configure(activebackground="#f9f9f9")
        la_wx.configure(activeforeground="black")
        la_wx.configure(background="#d9d9d9")
        la_wx.configure(disabledforeground="#a3a3a3")
        la_wx.configure(foreground="#000000")
        la_wx.configure(highlightbackground="#d9d9d9")
        la_wx.configure(highlightcolor="black")
        la_wx.configure(justify='left')
        la_wx.configure(text='''Wx=''')

        la_ix = tk.Label(Frame2)
        la_ix.place(relx=0.469, rely=0.283, height=14, width=40)
        la_ix.configure(activebackground="#f9f9f9")
        la_ix.configure(activeforeground="black")
        la_ix.configure(background="#d9d9d9")
        la_ix.configure(disabledforeground="#a3a3a3")
        la_ix.configure(foreground="#000000")
        la_ix.configure(highlightbackground="#d9d9d9")
        la_ix.configure(highlightcolor="black")
        la_ix.configure(justify='left')
        la_ix.configure(text='''Ix=''')

        la_area = tk.Label(Frame2)
        la_area.place(relx=0.469, rely=0.35, height=13, width=40)
        la_area.configure(activebackground="#f9f9f9")
        la_area.configure(activeforeground="black")
        la_area.configure(background="#d9d9d9")
        la_area.configure(disabledforeground="#a3a3a3")
        la_area.configure(foreground="#000000")
        la_area.configure(highlightbackground="#d9d9d9")
        la_area.configure(highlightcolor="black")
        la_area.configure(justify='left')
        la_area.configure(text='''Area=''')

        la_laje = tk.Label(Frame2)
        la_laje.place(relx=0.028, rely=0.436, height=14, width=49)
        la_laje.configure(activebackground="#f9f9f9")
        la_laje.configure(activeforeground="black")
        la_laje.configure(background="#d9d9d9")
        la_laje.configure(disabledforeground="#a3a3a3")
        la_laje.configure(font="-family {Segoe UI} -size 9 -weight bold -slant italic")
        la_laje.configure(foreground="#000000")
        la_laje.configure(highlightbackground="#d9d9d9")
        la_laje.configure(highlightcolor="black")
        la_laje.configure(text='''Slab''')

        la_tc = tk.Label(Frame2)
        la_tc.place(relx=0.028, rely=0.5, height=14, width=40)
        la_tc.configure(activebackground="#f9f9f9")
        la_tc.configure(activeforeground="black")
        la_tc.configure(background="#d9d9d9")
        la_tc.configure(disabledforeground="#a3a3a3")
        la_tc.configure(foreground="#000000")
        la_tc.configure(highlightbackground="#d9d9d9")
        la_tc.configure(highlightcolor="black")
        la_tc.configure(text='''tc=''')
        
        la_Lb_max = tk.Label(Frame2)
        la_Lb_max.place(relx=0.430, rely=0.5, height=14, width=50)
        la_Lb_max.configure(activebackground="#f9f9f9")
        la_Lb_max.configure(activeforeground="black")
        la_Lb_max.configure(background="#d9d9d9")
        la_Lb_max.configure(disabledforeground="#a3a3a3")
        la_Lb_max.configure(foreground="#000000")
        la_Lb_max.configure(highlightbackground="#d9d9d9")
        la_Lb_max.configure(highlightcolor="black")
        la_Lb_max.configure(text='''Lb_máx=''')

        la_armadura_longitudinal = tk.Label(Frame2)
        la_armadura_longitudinal.place(relx=0.028, rely=0.567, height=14, width=125)
        la_armadura_longitudinal.configure(activebackground="#f9f9f9")
        la_armadura_longitudinal.configure(activeforeground="black")
        la_armadura_longitudinal.configure(background="#d9d9d9")
        la_armadura_longitudinal.configure(disabledforeground="#a3a3a3")
        la_armadura_longitudinal.configure(font="-family {Segoe UI} -size 9 -weight bold -slant italic")
        la_armadura_longitudinal.configure(foreground="#000000")
        la_armadura_longitudinal.configure(highlightbackground="#d9d9d9")
        la_armadura_longitudinal.configure(highlightcolor="black")
        la_armadura_longitudinal.configure(text='''Longitudinal Bars''')

        la_n_barras = tk.Label(Frame2)
        la_n_barras.place(relx=0.01, rely=0.631, height=14, width=55)
        la_n_barras.configure(activebackground="#f9f9f9")
        la_n_barras.configure(activeforeground="black")
        la_n_barras.configure(background="#d9d9d9")
        la_n_barras.configure(disabledforeground="#a3a3a3")
        la_n_barras.configure(foreground="#000000")
        la_n_barras.configure(highlightbackground="#d9d9d9")
        la_n_barras.configure(highlightcolor="black")
        la_n_barras.configure(text='''Bar Nº=''')

        la_Ø_barras= tk.Label(Frame2)
        la_Ø_barras.place(relx=0.338, rely=0.631, height=14, width=40)
        la_Ø_barras.configure(activebackground="#f9f9f9")
        la_Ø_barras.configure(activeforeground="black")
        la_Ø_barras.configure(background="#d9d9d9")
        la_Ø_barras.configure(disabledforeground="#a3a3a3")
        la_Ø_barras.configure(foreground="#000000")
        la_Ø_barras.configure(highlightbackground="#d9d9d9")
        la_Ø_barras.configure(highlightcolor="black")
        la_Ø_barras.configure(text='''Ø=''')

        la_cobri = tk.Label(Frame2)
        la_cobri.place(relx=0.647, rely=0.631, height=14, width=40)
        la_cobri.configure(activebackground="#f9f9f9")
        la_cobri.configure(activeforeground="black")
        la_cobri.configure(background="#d9d9d9")
        la_cobri.configure(disabledforeground="#a3a3a3")
        la_cobri.configure(foreground="#000000")
        la_cobri.configure(highlightbackground="#d9d9d9")
        la_cobri.configure(highlightcolor="black")
        la_cobri.configure(text='''c=''')

        la_conectores = tk.Label(Frame2)
        la_conectores.place(relx=0.028, rely=0.731, height=13, width=49)
        la_conectores.configure(activebackground="#f9f9f9")
        la_conectores.configure(activeforeground="black")
        la_conectores.configure(background="#d9d9d9")
        la_conectores.configure(disabledforeground="#a3a3a3")
        la_conectores.configure(font="-family {Segoe UI} -size 9 -weight bold -slant italic")
        la_conectores.configure(foreground="#000000")
        la_conectores.configure(highlightbackground="#d9d9d9")
        la_conectores.configure(highlightcolor="black")
        la_conectores.configure(text='''Stud''')

        la_Ø = tk.Label(Frame2)
        la_Ø.place(relx=0.472, rely=0.795, height=14, width=29)
        la_Ø.configure(activebackground="#f9f9f9")
        la_Ø.configure(activeforeground="black")
        la_Ø.configure(background="#d9d9d9")
        la_Ø.configure(disabledforeground="#a3a3a3")
        la_Ø.configure(foreground="#000000")
        la_Ø.configure(highlightbackground="#d9d9d9")
        la_Ø.configure(highlightcolor="black")
        la_Ø.configure(text='''Ø=''')

        la_fucs = tk.Label(Frame2)
        la_fucs.place(relx=0.028, rely=0.795, height=14, width=40)
        la_fucs.configure(activebackground="#f9f9f9")
        la_fucs.configure(activeforeground="black")
        la_fucs.configure(background="#d9d9d9")
        la_fucs.configure(disabledforeground="#a3a3a3")
        la_fucs.configure(foreground="#000000")
        la_fucs.configure(highlightbackground="#d9d9d9")
        la_fucs.configure(highlightcolor="black")
        la_fucs.configure(text='''fucs=''')

        la_γc = tk.Label(Frame2)
        la_γc.place(relx=0.031, rely=0.862, height=13, width=40)
        la_γc.configure(activebackground="#f9f9f9")
        la_γc.configure(activeforeground="black")
        la_γc.configure(background="#d9d9d9")
        la_γc.configure(disabledforeground="#a3a3a3")
        la_γc.configure(foreground="#000000")
        la_γc.configure(highlightbackground="#d9d9d9")
        la_γc.configure(highlightcolor="black")
        la_γc.configure(text='''γc=''')


        if (teste_insere_perfil==0):
            box_perfi_bf = tk.Entry(Frame2)
            box_perfi_bf.place(relx=0.175, rely=0.076, height=25, relwidth=0.25)
            box_perfi_bf.configure(background="white")
            box_perfi_bf.configure(disabledforeground="#a3a3a3")
            box_perfi_bf.configure(font="TkFixedFont")
            box_perfi_bf.configure(foreground="#000000")
            box_perfi_bf.configure(highlightbackground="#d9d9d9")
            box_perfi_bf.configure(highlightcolor="black")
            box_perfi_bf.configure(insertbackground="black")
            box_perfi_bf.configure(selectbackground="#c4c4c4")
            box_perfi_bf.configure(selectforeground="black")
    
            box_perfi_tf = tk.Entry(Frame2)
            box_perfi_tf.place(relx=0.175, rely=0.143, height=25, relwidth=0.25)
            box_perfi_tf.configure(background="white")
            box_perfi_tf.configure(disabledforeground="#a3a3a3")
            box_perfi_tf.configure(font="TkFixedFont")
            box_perfi_tf.configure(foreground="#000000")
            box_perfi_tf.configure(highlightbackground="#d9d9d9")
            box_perfi_tf.configure(highlightcolor="black")
            box_perfi_tf.configure(insertbackground="black")
            box_perfi_tf.configure(selectbackground="#c4c4c4")
            box_perfi_tf.configure(selectforeground="black")
    
            box_perfi_h = tk.Entry(Frame2)
            box_perfi_h.place(relx=0.175, rely=0.207,height=25, relwidth=0.25)
            box_perfi_h.configure(background="white")
            box_perfi_h.configure(disabledforeground="#a3a3a3")
            box_perfi_h.configure(font="TkFixedFont")
            box_perfi_h.configure(foreground="#000000")
            box_perfi_h.configure(highlightbackground="#d9d9d9")
            box_perfi_h.configure(highlightcolor="black")
            box_perfi_h.configure(insertbackground="black")
            box_perfi_h.configure(selectbackground="#c4c4c4")
            box_perfi_h.configure(selectforeground="black")
    
            box_perfi_d = tk.Entry(Frame2)
            box_perfi_d.place(relx=0.175, rely=0.271,height=25, relwidth=0.25)
            box_perfi_d.configure(background="white")
            box_perfi_d.configure(disabledforeground="#a3a3a3")
            box_perfi_d.configure(font="TkFixedFont")
            box_perfi_d.configure(foreground="#000000")
            box_perfi_d.configure(highlightbackground="#d9d9d9")
            box_perfi_d.configure(highlightcolor="black")
            box_perfi_d.configure(insertbackground="black")
            box_perfi_d.configure(selectbackground="#c4c4c4")
            box_perfi_d.configure(selectforeground="black")
    
            box_perfi_d_ = tk.Entry(Frame2)
            box_perfi_d_.place(relx=0.175, rely=0.338, height=25, relwidth=0.25)
    
            box_perfi_d_.configure(background="white")
            box_perfi_d_.configure(disabledforeground="#a3a3a3")
            box_perfi_d_.configure(font="TkFixedFont")
            box_perfi_d_.configure(foreground="#000000")
            box_perfi_d_.configure(highlightbackground="#d9d9d9")
            box_perfi_d_.configure(highlightcolor="black")
            box_perfi_d_.configure(insertbackground="black")
            box_perfi_d_.configure(selectbackground="#c4c4c4")
            box_perfi_d_.configure(selectforeground="black")
    
            box_perfi_tw = tk.Entry(Frame2)
            box_perfi_tw.place(relx=0.625, rely=0.076, height=25, relwidth=0.25)
    
            box_perfi_tw.configure(background="white")
            box_perfi_tw.configure(disabledforeground="#a3a3a3")
            box_perfi_tw.configure(font="TkFixedFont")
            box_perfi_tw.configure(foreground="#000000")
            box_perfi_tw.configure(highlightbackground="#d9d9d9")
            box_perfi_tw.configure(highlightcolor="black")
            box_perfi_tw.configure(insertbackground="black")
            box_perfi_tw.configure(selectbackground="#c4c4c4")
            box_perfi_tw.configure(selectforeground="black")
    
            box_perfi_ry = tk.Entry(Frame2)
            box_perfi_ry.place(relx=0.625, rely=0.143, height=25, relwidth=0.25)
    
            box_perfi_ry.configure(background="white")
            box_perfi_ry.configure(disabledforeground="#a3a3a3")
            box_perfi_ry.configure(font="TkFixedFont")
            box_perfi_ry.configure(foreground="#000000")
            box_perfi_ry.configure(highlightbackground="#d9d9d9")
            box_perfi_ry.configure(highlightcolor="black")
            box_perfi_ry.configure(insertbackground="black")
            box_perfi_ry.configure(selectbackground="#c4c4c4")
            box_perfi_ry.configure(selectforeground="black")
    
            box_perfi_Wx = tk.Entry(Frame2)
            box_perfi_Wx.place(relx=0.625, rely=0.207, height=25, relwidth=0.25)
    
            box_perfi_Wx.configure(background="white")
            box_perfi_Wx.configure(disabledforeground="#a3a3a3")
            box_perfi_Wx.configure(font="TkFixedFont")
            box_perfi_Wx.configure(foreground="#000000")
            box_perfi_Wx.configure(highlightbackground="#d9d9d9")
            box_perfi_Wx.configure(highlightcolor="black")
            box_perfi_Wx.configure(insertbackground="black")
            box_perfi_Wx.configure(selectbackground="#c4c4c4")
            box_perfi_Wx.configure(selectforeground="black")
    
            box_perfi_Ix = tk.Entry(Frame2)
            box_perfi_Ix.place(relx=0.625, rely=0.271, height=25, relwidth=0.25)
    
            box_perfi_Ix.configure(background="white")
            box_perfi_Ix.configure(disabledforeground="#a3a3a3")
            box_perfi_Ix.configure(font="TkFixedFont")
            box_perfi_Ix.configure(foreground="#000000")
            box_perfi_Ix.configure(highlightbackground="#d9d9d9")
            box_perfi_Ix.configure(highlightcolor="black")
            box_perfi_Ix.configure(insertbackground="black")
            box_perfi_Ix.configure(selectbackground="#c4c4c4")
            box_perfi_Ix.configure(selectforeground="black")
    
            box_perfi_area_perfil = tk.Entry(Frame2)
            box_perfi_area_perfil.place(relx=0.625, rely=0.338, height=25, relwidth=0.25)
            box_perfi_area_perfil.configure(background="white")
            box_perfi_area_perfil.configure(disabledforeground="#a3a3a3")
            box_perfi_area_perfil.configure(font="TkFixedFont")
            box_perfi_area_perfil.configure(foreground="#000000")
            box_perfi_area_perfil.configure(highlightbackground="#d9d9d9")
            box_perfi_area_perfil.configure(highlightcolor="black")
            box_perfi_area_perfil.configure(insertbackground="black")
            box_perfi_area_perfil.configure(selectbackground="#c4c4c4")
            box_perfi_area_perfil.configure(selectforeground="black")
        else:
            la_VA_perfil_bf = tk.Label(Frame2)
            la_VA_perfil_bf.place(relx=0.156, rely=0.067, height=26, width=72)
            la_VA_perfil_bf.configure(background="#ffffff")
            la_VA_perfil_bf.configure(disabledforeground="#a3a3a3")
            la_VA_perfil_bf.configure(foreground="#000000")
            la_VA_perfil_bf.configure(text=round(bf,4))
    
            la_VA_perfil_tf = tk.Label(Frame2)
            la_VA_perfil_tf.place(relx=0.156, rely=0.138, height=26, width=72)
            la_VA_perfil_tf.configure(activebackground="#f9f9f9")
            la_VA_perfil_tf.configure(activeforeground="black")
            la_VA_perfil_tf.configure(background="#ffffff")
            la_VA_perfil_tf.configure(disabledforeground="#a3a3a3")
            la_VA_perfil_tf.configure(foreground="#000000")
            la_VA_perfil_tf.configure(highlightbackground="#d9d9d9")
            la_VA_perfil_tf.configure(highlightcolor="black")
            la_VA_perfil_tf.configure(text=round(tf,4))
    
            la_VA_perfil_h = tk.Label(Frame2)
            la_VA_perfil_h.place(relx=0.156, rely=0.21, height=26, width=72)
            la_VA_perfil_h.configure(activebackground="#f9f9f9")
            la_VA_perfil_h.configure(activeforeground="black")
            la_VA_perfil_h.configure(background="#ffffff")
            la_VA_perfil_h.configure(disabledforeground="#a3a3a3")
            la_VA_perfil_h.configure(foreground="#000000")
            la_VA_perfil_h.configure(highlightbackground="#d9d9d9")
            la_VA_perfil_h.configure(highlightcolor="black")
            la_VA_perfil_h.configure(text=round(h,4))
    
            la_VA_perfil_d = tk.Label(Frame2)
            la_VA_perfil_d.place(relx=0.156, rely=0.281, height=26, width=72)
            la_VA_perfil_d.configure(activebackground="#f9f9f9")
            la_VA_perfil_d.configure(activeforeground="black")
            la_VA_perfil_d.configure(background="#ffffff")
            la_VA_perfil_d.configure(disabledforeground="#a3a3a3")
            la_VA_perfil_d.configure(foreground="#000000")
            la_VA_perfil_d.configure(highlightbackground="#d9d9d9")
            la_VA_perfil_d.configure(highlightcolor="black")
            la_VA_perfil_d.configure(text=round(d,4))
    
            la_VA_perfil_d_ = tk.Label(Frame2)
            la_VA_perfil_d_.place(relx=0.156, rely=0.352, height=26, width=72)
            la_VA_perfil_d_.configure(activebackground="#f9f9f9")
            la_VA_perfil_d_.configure(activeforeground="black")
            la_VA_perfil_d_.configure(background="#ffffff")
            la_VA_perfil_d_.configure(disabledforeground="#a3a3a3")
            la_VA_perfil_d_.configure(foreground="#000000")
            la_VA_perfil_d_.configure(highlightbackground="#d9d9d9")
            la_VA_perfil_d_.configure(highlightcolor="black")
            la_VA_perfil_d_.configure(text=round(d_,4))
    
            la_VA_perfil_tw = tk.Label(Frame2)
            la_VA_perfil_tw.place(relx=0.594, rely=0.067, height=26, width=72)
            la_VA_perfil_tw.configure(activebackground="#f9f9f9")
            la_VA_perfil_tw.configure(activeforeground="black")
            la_VA_perfil_tw.configure(background="#ffffff")
            la_VA_perfil_tw.configure(cursor="fleur")
            la_VA_perfil_tw.configure(disabledforeground="#a3a3a3")
            la_VA_perfil_tw.configure(foreground="#000000")
            la_VA_perfil_tw.configure(highlightbackground="#d9d9d9")
            la_VA_perfil_tw.configure(highlightcolor="black")
            la_VA_perfil_tw.configure(text=round(tw,4))
    
            la_VA_perfil_ry = tk.Label(Frame2)
            la_VA_perfil_ry.place(relx=0.594, rely=0.138, height=26, width=72)
            la_VA_perfil_ry.configure(activebackground="#f9f9f9")
            la_VA_perfil_ry.configure(activeforeground="black")
            la_VA_perfil_ry.configure(background="#ffffff")
            la_VA_perfil_ry.configure(disabledforeground="#a3a3a3")
            la_VA_perfil_ry.configure(foreground="#000000")
            la_VA_perfil_ry.configure(highlightbackground="#d9d9d9")
            la_VA_perfil_ry.configure(highlightcolor="black")
            la_VA_perfil_ry.configure(text=round(ry,4))
    
            la_VA_perfil_Wx = tk.Label(Frame2)
            la_VA_perfil_Wx.place(relx=0.594, rely=0.21, height=26, width=72)
            la_VA_perfil_Wx.configure(activebackground="#f9f9f9")
            la_VA_perfil_Wx.configure(activeforeground="black")
            la_VA_perfil_Wx.configure(background="#ffffff")
            la_VA_perfil_Wx.configure(disabledforeground="#a3a3a3")
            la_VA_perfil_Wx.configure(foreground="#000000")
            la_VA_perfil_Wx.configure(highlightbackground="#d9d9d9")
            la_VA_perfil_Wx.configure(highlightcolor="black")
            la_VA_perfil_Wx.configure(text=round(Wx,6))
    
            la_VA_perfil_Ix = tk.Label(Frame2)
            la_VA_perfil_Ix.place(relx=0.594, rely=0.281, height=26, width=72)
            la_VA_perfil_Ix.configure(activebackground="#f9f9f9")
            la_VA_perfil_Ix.configure(activeforeground="black")
            la_VA_perfil_Ix.configure(background="#ffffff")
            la_VA_perfil_Ix.configure(disabledforeground="#a3a3a3")
            la_VA_perfil_Ix.configure(foreground="#000000")
            la_VA_perfil_Ix.configure(highlightbackground="#d9d9d9")
            la_VA_perfil_Ix.configure(highlightcolor="black")
            la_VA_perfil_Ix.configure(text=round(I_p,6))
    
            la_VA_perfil_area = tk.Label(Frame2)
            la_VA_perfil_area.place(relx=0.594, rely=0.352, height=26, width=72)
            la_VA_perfil_area.configure(activebackground="#f9f9f9")
            la_VA_perfil_area.configure(activeforeground="black")
            la_VA_perfil_area.configure(background="#ffffff")
            la_VA_perfil_area.configure(disabledforeground="#a3a3a3")
            la_VA_perfil_area.configure(foreground="#000000")
            la_VA_perfil_area.configure(highlightbackground="#d9d9d9")
            la_VA_perfil_area.configure(highlightcolor="black")
            la_VA_perfil_area.configure(text=round(area_p,4))
            
            
        box_laje_tc = tk.Entry(Frame2)
        box_laje_tc.place(relx=0.156, rely=0.488, height=25, relwidth=0.156)
        box_laje_tc.configure(background="white")
        box_laje_tc.configure(disabledforeground="#a3a3a3")
        box_laje_tc.configure(font="TkFixedFont")
        box_laje_tc.configure(foreground="#000000")
        box_laje_tc.configure(highlightbackground="#d9d9d9")
        box_laje_tc.configure(highlightcolor="black")
        box_laje_tc.configure(insertbackground="black")
        box_laje_tc.configure(selectbackground="#c4c4c4")
        box_laje_tc.configure(selectforeground="black")
        
        box_laje_Lb_max = tk.Entry(Frame2)
        box_laje_Lb_max.place(relx=0.622, rely=0.488, height=25, relwidth=0.25)
        box_laje_Lb_max.configure(background="white")
        box_laje_Lb_max.configure(disabledforeground="#a3a3a3")
        box_laje_Lb_max.configure(font="TkFixedFont")
        box_laje_Lb_max.configure(foreground="#000000")
        box_laje_Lb_max.configure(highlightbackground="#d9d9d9")
        box_laje_Lb_max.configure(highlightcolor="black")
        box_laje_Lb_max.configure(insertbackground="black")
        box_laje_Lb_max.configure(selectbackground="#c4c4c4")
        box_laje_Lb_max.configure(selectforeground="black")        
        
        box_N_barras= tk.Entry(Frame2)
        box_N_barras.place(relx=0.19, rely=0.621,height=25, relwidth=0.156)
        box_N_barras.configure(background="white")
        box_N_barras.configure(disabledforeground="#a3a3a3")
        box_N_barras.configure(font="TkFixedFont")
        box_N_barras.configure(foreground="#000000")
        box_N_barras.configure(highlightbackground="#d9d9d9")
        box_N_barras.configure(highlightcolor="black")
        box_N_barras.configure(insertbackground="black")
        box_N_barras.configure(selectbackground="#c4c4c4")
        box_N_barras.configure(selectforeground="black")


        box_Ø_barras = tk.Entry(Frame2)
        box_Ø_barras.place(relx=0.453, rely=0.621,height=25, relwidth=0.156)
        box_Ø_barras.configure(background="white")
        box_Ø_barras.configure(disabledforeground="#a3a3a3")
        box_Ø_barras.configure(font="TkFixedFont")
        box_Ø_barras.configure(foreground="#000000")
        box_Ø_barras.configure(highlightbackground="#d9d9d9")
        box_Ø_barras.configure(highlightcolor="black")
        box_Ø_barras.configure(insertbackground="black")
        box_Ø_barras.configure(selectbackground="#c4c4c4")
        box_Ø_barras.configure(selectforeground="black")

        box_As_cobri = tk.Entry(Frame2)
        box_As_cobri.place(relx=0.75, rely=0.621, height=25, relwidth=0.156)
        box_As_cobri.configure(background="white")
        box_As_cobri.configure(disabledforeground="#a3a3a3")
        box_As_cobri.configure(font="TkFixedFont")
        box_As_cobri.configure(foreground="#000000")
        box_As_cobri.configure(highlightbackground="#d9d9d9")
        box_As_cobri.configure(highlightcolor="black")
        box_As_cobri.configure(insertbackground="black")
        box_As_cobri.configure(selectbackground="#c4c4c4")
        box_As_cobri.configure(selectforeground="black")

        box_conector_fucs = tk.Entry(Frame2)
        box_conector_fucs.place(relx=0.156, rely=0.786, height=25, relwidth=0.156)
        box_conector_fucs.configure(background="white")
        box_conector_fucs.configure(disabledforeground="#a3a3a3")
        box_conector_fucs.configure(font="TkFixedFont")
        box_conector_fucs.configure(foreground="#000000")
        box_conector_fucs.configure(highlightbackground="#d9d9d9")
        box_conector_fucs.configure(highlightcolor="black")
        box_conector_fucs.configure(insertbackground="black")
        box_conector_fucs.configure(selectbackground="#c4c4c4")
        box_conector_fucs.configure(selectforeground="black")

        box_conector_γc = tk.Entry(Frame2)
        box_conector_γc.place(relx=0.156, rely=0.857, height=25, relwidth=0.156)
        box_conector_γc.configure(background="white")
        box_conector_γc.configure(disabledforeground="#a3a3a3")
        box_conector_γc.configure(font="TkFixedFont")
        box_conector_γc.configure(foreground="#000000")
        box_conector_γc.configure(highlightbackground="#d9d9d9")
        box_conector_γc.configure(highlightcolor="black")
        box_conector_γc.configure(insertbackground="black")
        box_conector_γc.configure(selectbackground="#c4c4c4")
        box_conector_γc.configure(selectforeground="black")

        box_conector_Ø = tk.Entry(Frame2)
        box_conector_Ø.place(relx=0.563, rely=0.786, height=25, relwidth=0.156)
        box_conector_Ø.configure(background="white")
        box_conector_Ø.configure(disabledforeground="#a3a3a3")
        box_conector_Ø.configure(font="TkFixedFont")
        box_conector_Ø.configure(foreground="#000000")
        box_conector_Ø.configure(highlightbackground="#d9d9d9")
        box_conector_Ø.configure(highlightcolor="black")
        box_conector_Ø.configure(insertbackground="black")
        box_conector_Ø.configure(selectbackground="#c4c4c4")
        box_conector_Ø.configure(selectforeground="black")


        def take_entry_perfis():
            global tc , Lb_max , n_barras , diametro_barras , cobrimento , fucs , yc_conector , diametro_conector
#            if (teste_entry==1):
            global     d , tf , h , d_ ,bf, tw , Wx , Ix , area_p , ry , I_p , ycs
        
            
            tc                = float(box_laje_tc            .get())
            Lb_max            = float(box_laje_Lb_max        .get())
            n_barras          = float(box_N_barras           .get())
            diametro_barras   = float(box_Ø_barras           .get())
            cobrimento        = float(box_As_cobri           .get())
            fucs              = float(box_conector_fucs      .get())
            yc_conector       = float(box_conector_γc        .get())
            diametro_conector = float(box_conector_Ø         .get())
            
            ycs=yc_conector
            
            if (teste_insere_perfil==0):
                d      =       float(box_perfi_d           .get())
                tf     =       float(box_perfi_tf          .get())
                h      =       float(box_perfi_h           .get())
                d_     =       float(box_perfi_d_          .get())
                bf     =       float(box_perfi_bf          .get())
                tw     =       float(box_perfi_tw          .get())
                Wx     =       float(box_perfi_Wx          .get())
                I_p    =       float(box_perfi_Ix          .get())
                ry     =       float(box_perfi_ry          .get())
                area_p =       float(box_perfi_area_perfil .get())
            
            
            janela_perfil_inserir.destroy()
            janela_geometria.destroy()
            
            Reescreve_labels_frame1()

        btn_destroy_perfil_inserir = tk.Button(janela_perfil_inserir)
        btn_destroy_perfil_inserir.place(relx=0.353, rely=0.89, height=40, width=100)
        btn_destroy_perfil_inserir.configure(activebackground="#ececec")
        btn_destroy_perfil_inserir.configure(activeforeground="#000000")
        btn_destroy_perfil_inserir.configure(background="#0000ff")
        btn_destroy_perfil_inserir.configure(disabledforeground="#a3a3a3")
        btn_destroy_perfil_inserir.configure(foreground="#ffffff")
        btn_destroy_perfil_inserir.configure(highlightbackground="#d9d9d9")
        btn_destroy_perfil_inserir.configure(highlightcolor="black")
        btn_destroy_perfil_inserir.configure(pady="0")
        btn_destroy_perfil_inserir.configure(text='''>>>''')
        btn_destroy_perfil_inserir.configure(command=take_entry_perfis)
        
        janela_perfil_inserir.mainloop()
    
    # =========================================================================
    #     #           SELECIONAR PERFIL
    # =========================================================================
    
    def call_ja_geo_per_selecionar():
        global teste_insere_perfil
        global d , tf , h , d_ ,bf, bs , tw , Wx , I_p , area_p , ry    
        teste_insere_perfil=1

        janela_selecionar=tk.Tk()
        
        janela_selecionar.geometry("400x600+922+109")
        janela_selecionar.minsize(148, 1)
        janela_selecionar.maxsize(1924, 1055)
        janela_selecionar.resizable(1, 1)
        janela_selecionar.title("Section Select")
        janela_selecionar.configure(background="#d9d9d9")
        janela_selecionar.iconbitmap('icones/geral.ico')
        
        listbox_perfis = tk.Listbox(janela_selecionar)
        listbox_perfis.place(relx=0.025, rely=0.05, relheight=0.83, relwidth=0.95)
        listbox_perfis.configure(background="white")
        listbox_perfis.configure(disabledforeground="#a3a3a3")
        listbox_perfis.configure(font="TkFixedFont")
        listbox_perfis.configure(foreground="#000000")
        ######     ADICIONA A LISTA DE PERFIS NA LISTA     #####
        nn=2
        while nn <= contador:
            listbox_perfis.insert((nn-2),dada_numérico[nn,0:2])
            nn=nn+1
            
        ######     ATRIBUIR O VALOR DA LISTA SELECIONADO     #####
        def take_xlsx_perfil():
            global             d , tf , h , d_ ,bf, bs , tw , Wx , I_p , area_p , ry   
            n=listbox_perfis.curselection()                                         # Pega o valor da linha selecionada
            n=int(n[0])                                                             # Transforma em inteiro
            perfil=dados[n,:]                                                       # Pega linha referente ao perfil selecionado
            
            d      =       (  perfil[1] /1000  )
            tf     =       (  perfil[5] /1000  )
            h      =       (  perfil[6] /1000  )
            d_     =       (  perfil[7] /1000  )           #trocar
            bf     =       (  perfil[2] /1000  )
            bs     =       (  perfil[3] /1000  )
            tw     =       (  perfil[4] /1000  )
            Wx     =       (  perfil[10]/1e6   )
            I_p     =       (  perfil[9] /1e8   )
            area_p =       (  perfil[8] /10000 )           #trocar
            ry     =       (  perfil[15] /100 )
            janela_selecionar.destroy()
            call_ja_geo_per_inserir()
            
            
        botao_seguinte_selecioneperfil = tk.Button(janela_selecionar)
        botao_seguinte_selecioneperfil.place(relx=0.375, rely=0.917, height=33, width=100)
        botao_seguinte_selecioneperfil.configure(activebackground="#ececec")
        botao_seguinte_selecioneperfil.configure(activeforeground="#000000")
        botao_seguinte_selecioneperfil.configure(background="#000080")
        botao_seguinte_selecioneperfil.configure(disabledforeground="#a3a3a3")
        botao_seguinte_selecioneperfil.configure(foreground="#ffffff")
        botao_seguinte_selecioneperfil.configure(highlightbackground="#d9d9d9")
        botao_seguinte_selecioneperfil.configure(highlightcolor="#ffffff")
        botao_seguinte_selecioneperfil.configure(pady="0")
        botao_seguinte_selecioneperfil.configure(text='''>>>''')
        botao_seguinte_selecioneperfil.configure(command=take_xlsx_perfil)
            
        la_seleciona_perfil = tk.Label(janela_selecionar)
        la_seleciona_perfil.place(relx=-0.025, rely=0.0, height=26, width=192)
        la_seleciona_perfil.configure(background="#d9d9d9")
        la_seleciona_perfil.configure(disabledforeground="#a3a3a3")
        la_seleciona_perfil.configure(foreground="#000000")
        la_seleciona_perfil.configure(justify='left')
        la_seleciona_perfil.configure(text='''Section select...''')
        
        janela_selecionar.mainloop

    
    #             DESTROY JANELA GEOMETRIA
    def destroy_janela_geometria():

        janela_geometria.destroy()
    
###############################################################################

    janela_geometria=tk.Tk()

    font9 = "-family {Segoe UI} -size 9 -weight bold -slant italic"  \
        ""
    
    janela_geometria.geometry("340x190+400+120")
    janela_geometria.minsize(148, 1)
    janela_geometria.maxsize(1924, 1055)
    janela_geometria.resizable(0, 0)
    janela_geometria.title("Span details")
    janela_geometria.configure(background="#d9d9d9")
    janela_geometria.iconbitmap('icones/geral.ico')
    janela_geometria.title("Beam Section")
    
    frame_destroy_j_g_perfil = tk.Frame(janela_geometria)
    frame_destroy_j_g_perfil.place(relx=0.029, rely=0.0526, relheight=0.631, relwidth=0.941)
    frame_destroy_j_g_perfil.configure(relief='groove')
    frame_destroy_j_g_perfil.configure(borderwidth="2")
    frame_destroy_j_g_perfil.configure(relief="groove")
    frame_destroy_j_g_perfil.configure(background="#d9d9d9")
    
    la_jg_p = tk.Label(frame_destroy_j_g_perfil)
    la_jg_p.place(relx=0.031, rely=0.083, height=26, width=82)
    la_jg_p.configure(background="#d9d9d9")
    la_jg_p.configure(disabledforeground="#a3a3a3")
    la_jg_p.configure(font=font9)
    la_jg_p.configure(foreground="#000000")
    la_jg_p.configure(text='''Section''')
    
    btn_jg_p_selecionar = tk.Button(frame_destroy_j_g_perfil)
    btn_jg_p_selecionar.place(relx=0.125, rely=0.5, height=35, width=100)
    btn_jg_p_selecionar.configure(activebackground="#ececec")
    btn_jg_p_selecionar.configure(activeforeground="#000000")
    btn_jg_p_selecionar.configure(background="#d9d9d9")
    btn_jg_p_selecionar.configure(disabledforeground="#a3a3a3")
    btn_jg_p_selecionar.configure(foreground="#000000")
    btn_jg_p_selecionar.configure(highlightbackground="#d9d9d9")
    btn_jg_p_selecionar.configure(highlightcolor="black")
    btn_jg_p_selecionar.configure(pady="0")
    btn_jg_p_selecionar.configure(text='''Select''')
    btn_jg_p_selecionar.configure(command=call_ja_geo_per_selecionar)
    
    
    btn_jg_p_inserir = tk.Button(frame_destroy_j_g_perfil)
    btn_jg_p_inserir.place(relx=0.563, rely=0.5, height=35, width=100)
    btn_jg_p_inserir.configure(activebackground="#ececec")
    btn_jg_p_inserir.configure(activeforeground="#000000")
    btn_jg_p_inserir.configure(background="#d9d9d9")
    btn_jg_p_inserir.configure(disabledforeground="#a3a3a3")
    btn_jg_p_inserir.configure(foreground="#000000")
    btn_jg_p_inserir.configure(highlightbackground="#d9d9d9")
    btn_jg_p_inserir.configure(highlightcolor="black")
    btn_jg_p_inserir.configure(pady="0")
    btn_jg_p_inserir.configure(text='''Insert''')
    btn_jg_p_inserir.configure(command=call_ja_geo_per_inserir)
    
    btn_destroy_j_g = tk.Button(janela_geometria)
    btn_destroy_j_g.place(relx=0.397, rely=0.736, height=40, width=70)
    btn_destroy_j_g.configure(activebackground="#ececec")
    btn_destroy_j_g.configure(activeforeground="#000000")
    btn_destroy_j_g.configure(background="#000080")
    btn_destroy_j_g.configure(disabledforeground="#a3a3a3")
    btn_destroy_j_g.configure(foreground="#ffffff")
    btn_destroy_j_g.configure(highlightbackground="#d9d9d9")
    btn_destroy_j_g.configure(highlightcolor="#ffffff")
    btn_destroy_j_g.configure(pady="0")
    btn_destroy_j_g.configure(text='''>>>''')
    btn_destroy_j_g.configure(command=destroy_janela_geometria)
    
    
    janela_geometria.mainloop()


def n_vaos_func():
    trechos=tk.StringVar()
    
    def cargas_vao():
        global trechos 
        trechos      =   int(combobox_n_vaos   .get())
        
        def destroy_cargas():
            global q , L 
            L   =np.zeros(trechos)
            q   =np.zeros(trechos)
            if (trechos==1):
                L[0]    =   float(box_dim_trecho1_L   .get())
                q[0]    =   float(box_dim_trecho1_Q   .get())
                
            elif (trechos==2):
                L[0]    =   float(box_dim_trecho1_L   .get())
                q[0]    =   float(box_dim_trecho1_Q   .get())
                L[1]    =   float(box_dim_trecho2_L   .get())
                q[1]    =   float(box_dim_trecho2_Q   .get())
            else:
                L[0]    =   float(box_dim_trecho1_L   .get())
                q[0]    =   float(box_dim_trecho1_Q   .get())
                L[1]    =   float(box_dim_trecho2_L   .get())
                q[1]    =   float(box_dim_trecho2_Q   .get())
                L[2]    =   float(box_dim_trecho3_L   .get())
                q[2]    =   float(box_dim_trecho3_Q   .get())
                
            janela_trecho.destroy()
            n_vaos.destroy()
            
        if (trechos==1):
            janela_trecho=tk.Tk()
    
            janela_trecho.geometry("340x180+895+168")
            janela_trecho.minsize(148, 1)
            janela_trecho.maxsize(1924, 1055)
            janela_trecho.resizable(1, 1)
            janela_trecho.title("Span details")
            janela_trecho.configure(background="#d9d9d9")
            janela_trecho.configure(highlightbackground="#d9d9d9")
            janela_trecho.configure(highlightcolor="black")
    
            frame_trecho_1_dim = tk.Frame(janela_trecho)
            frame_trecho_1_dim.place(relx=0.029, rely=0.072, relheight=0.667, relwidth=0.941)
            frame_trecho_1_dim.configure(relief='groove')
            frame_trecho_1_dim.configure(borderwidth="2")
            frame_trecho_1_dim.configure(relief="groove")
            frame_trecho_1_dim.configure(background="#d9d9d9")
            frame_trecho_1_dim.configure(highlightbackground="#d9d9d9")
            frame_trecho_1_dim.configure(highlightcolor="black")
    
            la_dim_trecho1 = tk.Label(frame_trecho_1_dim)
            la_dim_trecho1.place(relx=0.063, rely=0.083, height=26, width=98)
            la_dim_trecho1.configure(activebackground="#f9f9f9")
            la_dim_trecho1.configure(activeforeground="black")
            la_dim_trecho1.configure(background="#d9d9d9")
            la_dim_trecho1.configure(disabledforeground="#a3a3a3")
            la_dim_trecho1.configure(font="-family {Segoe UI} -size 9 -weight bold -slant italic")
            la_dim_trecho1.configure(foreground="#000000")
            la_dim_trecho1.configure(highlightbackground="#d9d9d9")
            la_dim_trecho1.configure(highlightcolor="black")
            la_dim_trecho1.configure(text='''1º Span''')
    
            la_dim_trecho1_L = tk.Label(frame_trecho_1_dim)
            la_dim_trecho1_L.place(relx=0.031, rely=0.5, height=26, width=42)
            la_dim_trecho1_L.configure(activebackground="#f9f9f9")
            la_dim_trecho1_L.configure(activeforeground="black")
            la_dim_trecho1_L.configure(background="#d9d9d9")
            la_dim_trecho1_L.configure(disabledforeground="#a3a3a3")
            la_dim_trecho1_L.configure(foreground="#000000")
            la_dim_trecho1_L.configure(highlightbackground="#d9d9d9")
            la_dim_trecho1_L.configure(highlightcolor="black")
            la_dim_trecho1_L.configure(text='''L=''')
    
            box_dim_trecho1_L = tk.Entry(frame_trecho_1_dim)
            box_dim_trecho1_L.place(relx=0.125, rely=0.5, height=24, relwidth=0.325)
            box_dim_trecho1_L.configure(background="white")
            box_dim_trecho1_L.configure(disabledforeground="#a3a3a3")
            box_dim_trecho1_L.configure(font="TkFixedFont")
            box_dim_trecho1_L.configure(foreground="#000000")
            box_dim_trecho1_L.configure(highlightbackground="#d9d9d9")
            box_dim_trecho1_L.configure(highlightcolor="black")
            box_dim_trecho1_L.configure(insertbackground="black")
            box_dim_trecho1_L.configure(selectbackground="#c4c4c4")
            box_dim_trecho1_L.configure(selectforeground="black")
    
            la_dim_trecho1_Q = tk.Label(frame_trecho_1_dim)
            la_dim_trecho1_Q.place(relx=0.5, rely=0.5, height=26, width=42)
            la_dim_trecho1_Q.configure(activebackground="#f9f9f9")
            la_dim_trecho1_Q.configure(activeforeground="black")
            la_dim_trecho1_Q.configure(background="#d9d9d9")
            la_dim_trecho1_Q.configure(disabledforeground="#a3a3a3")
            la_dim_trecho1_Q.configure(foreground="#000000")
            la_dim_trecho1_Q.configure(highlightbackground="#d9d9d9")
            la_dim_trecho1_Q.configure(highlightcolor="black")
            la_dim_trecho1_Q.configure(text='''Q=''')
    
            box_dim_trecho1_Q = tk.Entry(frame_trecho_1_dim)
            box_dim_trecho1_Q.place(relx=0.609, rely=0.5, height=24, relwidth=0.325)
            box_dim_trecho1_Q.configure(background="white")
            box_dim_trecho1_Q.configure(disabledforeground="#a3a3a3")
            box_dim_trecho1_Q.configure(font="TkFixedFont")
            box_dim_trecho1_Q.configure(foreground="#000000")
            box_dim_trecho1_Q.configure(highlightbackground="#d9d9d9")
            box_dim_trecho1_Q.configure(highlightcolor="black")
            box_dim_trecho1_Q.configure(insertbackground="black")
            box_dim_trecho1_Q.configure(selectbackground="#c4c4c4")
            box_dim_trecho1_Q.configure(selectforeground="black")
    
            but_seguinte_trechos = tk.Button(janela_trecho)
            but_seguinte_trechos.place(relx=0.382, rely=0.778, height=33, width=80)
            but_seguinte_trechos.configure(activebackground="#ececec")
            but_seguinte_trechos.configure(activeforeground="#000000")
            but_seguinte_trechos.configure(background="#0000a0")
            but_seguinte_trechos.configure(disabledforeground="#a3a3a3")
            but_seguinte_trechos.configure(foreground="#ffffff")
            but_seguinte_trechos.configure(highlightbackground="#d9d9d9")
            but_seguinte_trechos.configure(highlightcolor="black")
            but_seguinte_trechos.configure(pady="0")
            but_seguinte_trechos.configure(text='''>>>''')
            but_seguinte_trechos.configure(command=destroy_cargas)
            
            janela_trecho.mainloop()
        elif(trechos==2):
            
            janela_trecho=tk.Tk()
            
            janela_trecho.geometry("340x310+845+149")
            janela_trecho.minsize(148, 1)
            janela_trecho.maxsize(1924, 1055)
            janela_trecho.resizable(1, 1)
            janela_trecho.title("Span details")
            janela_trecho.configure(background="#d9d9d9")
            janela_trecho.configure(highlightbackground="#d9d9d9")
            janela_trecho.configure(highlightcolor="black")
            janela_trecho.iconbitmap('icones/geral.ico')
    
            frame_trecho_1_dim = tk.Frame(janela_trecho)
            frame_trecho_1_dim.place(relx=0.029, rely=0.032, relheight=0.387, relwidth=0.941)
            frame_trecho_1_dim.configure(relief='groove')
            frame_trecho_1_dim.configure(borderwidth="2")
            frame_trecho_1_dim.configure(relief="groove")
            frame_trecho_1_dim.configure(background="#d9d9d9")
            frame_trecho_1_dim.configure(highlightbackground="#d9d9d9")
            frame_trecho_1_dim.configure(highlightcolor="black")
    
            la_dim_trecho1 = tk.Label(frame_trecho_1_dim)
            la_dim_trecho1.place(relx=0.063, rely=0.083, height=26, width=98)
            la_dim_trecho1.configure(activebackground="#f9f9f9")
            la_dim_trecho1.configure(activeforeground="black")
            la_dim_trecho1.configure(background="#d9d9d9")
            la_dim_trecho1.configure(disabledforeground="#a3a3a3")
            la_dim_trecho1.configure(font="-family {Segoe UI} -size 9 -weight bold -slant italic")
            la_dim_trecho1.configure(foreground="#000000")
            la_dim_trecho1.configure(highlightbackground="#d9d9d9")
            la_dim_trecho1.configure(highlightcolor="black")
            la_dim_trecho1.configure(text='''1º Span''')
    
            la_dim_trecho1_L = tk.Label(frame_trecho_1_dim)
            la_dim_trecho1_L.place(relx=0.031, rely=0.5, height=26, width=42)
            la_dim_trecho1_L.configure(activebackground="#f9f9f9")
            la_dim_trecho1_L.configure(activeforeground="black")
            la_dim_trecho1_L.configure(background="#d9d9d9")
            la_dim_trecho1_L.configure(disabledforeground="#a3a3a3")
            la_dim_trecho1_L.configure(foreground="#000000")
            la_dim_trecho1_L.configure(highlightbackground="#d9d9d9")
            la_dim_trecho1_L.configure(highlightcolor="black")
            la_dim_trecho1_L.configure(text='''L=''')
    
            box_dim_trecho1_L = tk.Entry(frame_trecho_1_dim)
            box_dim_trecho1_L.place(relx=0.125, rely=0.5, height=24, relwidth=0.325)
            box_dim_trecho1_L.configure(background="white")
            box_dim_trecho1_L.configure(disabledforeground="#a3a3a3")
            box_dim_trecho1_L.configure(font="TkFixedFont")
            box_dim_trecho1_L.configure(foreground="#000000")
            box_dim_trecho1_L.configure(highlightbackground="#d9d9d9")
            box_dim_trecho1_L.configure(highlightcolor="black")
            box_dim_trecho1_L.configure(insertbackground="black")
            box_dim_trecho1_L.configure(selectbackground="#c4c4c4")
            box_dim_trecho1_L.configure(selectforeground="black")
    
            la_dim_trecho1_Q = tk.Label(frame_trecho_1_dim)
            la_dim_trecho1_Q.place(relx=0.5, rely=0.5, height=26, width=42)
            la_dim_trecho1_Q.configure(activebackground="#f9f9f9")
            la_dim_trecho1_Q.configure(activeforeground="black")
            la_dim_trecho1_Q.configure(background="#d9d9d9")
            la_dim_trecho1_Q.configure(disabledforeground="#a3a3a3")
            la_dim_trecho1_Q.configure(foreground="#000000")
            la_dim_trecho1_Q.configure(highlightbackground="#d9d9d9")
            la_dim_trecho1_Q.configure(highlightcolor="black")
            la_dim_trecho1_Q.configure(text='''Q=''')
    
            box_dim_trecho1_Q = tk.Entry(frame_trecho_1_dim)
            box_dim_trecho1_Q.place(relx=0.609, rely=0.5, height=24, relwidth=0.325)
            box_dim_trecho1_Q.configure(background="white")
            box_dim_trecho1_Q.configure(disabledforeground="#a3a3a3")
            box_dim_trecho1_Q.configure(font="TkFixedFont")
            box_dim_trecho1_Q.configure(foreground="#000000")
            box_dim_trecho1_Q.configure(highlightbackground="#d9d9d9")
            box_dim_trecho1_Q.configure(highlightcolor="black")
            box_dim_trecho1_Q.configure(insertbackground="black")
            box_dim_trecho1_Q.configure(selectbackground="#c4c4c4")
            box_dim_trecho1_Q.configure(selectforeground="black")
    
            frame_trecho_2_dim = tk.Frame(janela_trecho)
            frame_trecho_2_dim.place(relx=0.029, rely=0.452, relheight=0.387, relwidth=0.941)
            frame_trecho_2_dim.configure(relief='groove')
            frame_trecho_2_dim.configure(borderwidth="2")
            frame_trecho_2_dim.configure(relief="groove")
            frame_trecho_2_dim.configure(background="#d9d9d9")
            frame_trecho_2_dim.configure(highlightbackground="#d9d9d9")
            frame_trecho_2_dim.configure(highlightcolor="black")
    
            la_dim_trecho2 = tk.Label(frame_trecho_2_dim)
            la_dim_trecho2.place(relx=0.063, rely=0.083, height=26, width=98)
            la_dim_trecho2.configure(activebackground="#f9f9f9")
            la_dim_trecho2.configure(activeforeground="black")
            la_dim_trecho2.configure(background="#d9d9d9")
            la_dim_trecho2.configure(disabledforeground="#a3a3a3")
            la_dim_trecho2.configure(font="-family {Segoe UI} -size 9 -weight bold -slant italic")
            la_dim_trecho2.configure(foreground="#000000")
            la_dim_trecho2.configure(highlightbackground="#d9d9d9")
            la_dim_trecho2.configure(highlightcolor="black")
            la_dim_trecho2.configure(text='''2º Span''')
    
            la_dim_trecho2_L = tk.Label(frame_trecho_2_dim)
            la_dim_trecho2_L.place(relx=0.031, rely=0.5, height=26, width=42)
            la_dim_trecho2_L.configure(activebackground="#f9f9f9")
            la_dim_trecho2_L.configure(activeforeground="black")
            la_dim_trecho2_L.configure(background="#d9d9d9")
            la_dim_trecho2_L.configure(disabledforeground="#a3a3a3")
            la_dim_trecho2_L.configure(foreground="#000000")
            la_dim_trecho2_L.configure(highlightbackground="#d9d9d9")
            la_dim_trecho2_L.configure(highlightcolor="black")
            la_dim_trecho2_L.configure(text='''L=''')
    
            box_dim_trecho2_L = tk.Entry(frame_trecho_2_dim)
            box_dim_trecho2_L.place(relx=0.125, rely=0.5, height=24, relwidth=0.325)
            box_dim_trecho2_L.configure(background="white")
            box_dim_trecho2_L.configure(disabledforeground="#a3a3a3")
            box_dim_trecho2_L.configure(font="TkFixedFont")
            box_dim_trecho2_L.configure(foreground="#000000")
            box_dim_trecho2_L.configure(highlightbackground="#d9d9d9")
            box_dim_trecho2_L.configure(highlightcolor="black")
            box_dim_trecho2_L.configure(insertbackground="black")
            box_dim_trecho2_L.configure(selectbackground="#c4c4c4")
            box_dim_trecho2_L.configure(selectforeground="black")
    
            la_dim_trecho2_Q = tk.Label(frame_trecho_2_dim)
            la_dim_trecho2_Q.place(relx=0.5, rely=0.5, height=26, width=42)
            la_dim_trecho2_Q.configure(activebackground="#f9f9f9")
            la_dim_trecho2_Q.configure(activeforeground="black")
            la_dim_trecho2_Q.configure(background="#d9d9d9")
            la_dim_trecho2_Q.configure(disabledforeground="#a3a3a3")
            la_dim_trecho2_Q.configure(foreground="#000000")
            la_dim_trecho2_Q.configure(highlightbackground="#d9d9d9")
            la_dim_trecho2_Q.configure(highlightcolor="black")
            la_dim_trecho2_Q.configure(text='''Q=''')
    
            box_dim_trecho2_Q = tk.Entry(frame_trecho_2_dim)
            box_dim_trecho2_Q.place(relx=0.609, rely=0.5, height=24, relwidth=0.325)
            box_dim_trecho2_Q.configure(background="white")
            box_dim_trecho2_Q.configure(disabledforeground="#a3a3a3")
            box_dim_trecho2_Q.configure(font="TkFixedFont")
            box_dim_trecho2_Q.configure(foreground="#000000")
            box_dim_trecho2_Q.configure(highlightbackground="#d9d9d9")
            box_dim_trecho2_Q.configure(highlightcolor="black")
            box_dim_trecho2_Q.configure(insertbackground="black")
            box_dim_trecho2_Q.configure(selectbackground="#c4c4c4")
            box_dim_trecho2_Q.configure(selectforeground="black")
    
            but_seguinte_trechos = tk.Button(janela_trecho)
            but_seguinte_trechos.place(relx=0.382, rely=0.871, height=33, width=80)
            but_seguinte_trechos.configure(activebackground="#ececec")
            but_seguinte_trechos.configure(activeforeground="#000000")
            but_seguinte_trechos.configure(background="#0000a0")
            but_seguinte_trechos.configure(disabledforeground="#a3a3a3")
            but_seguinte_trechos.configure(foreground="#ffffff")
            but_seguinte_trechos.configure(highlightbackground="#d9d9d9")
            but_seguinte_trechos.configure(highlightcolor="black")
            but_seguinte_trechos.configure(pady="0")
            but_seguinte_trechos.configure(text='''>>>''')
            but_seguinte_trechos.configure(command=destroy_cargas)
            
            janela_trecho.mainloop()
        else:
            janela_trecho=tk.Tk()
    
            janela_trecho.geometry("340x440+845+149")
            janela_trecho.minsize(148, 1)
            janela_trecho.maxsize(1924, 1055)
            janela_trecho.resizable(1, 1)
            janela_trecho.title("Span details")
            janela_trecho.configure(background="#d9d9d9")
            janela_trecho.configure(highlightbackground="#d9d9d9")
            janela_trecho.configure(highlightcolor="black")
    
            frame_trecho_1_dim = tk.Frame(janela_trecho)
            frame_trecho_1_dim.place(relx=0.029, rely=0.023, relheight=0.273, relwidth=0.941)
            frame_trecho_1_dim.configure(relief='groove')
            frame_trecho_1_dim.configure(borderwidth="2")
            frame_trecho_1_dim.configure(relief="groove")
            frame_trecho_1_dim.configure(background="#d9d9d9")
            frame_trecho_1_dim.configure(highlightbackground="#d9d9d9")
            frame_trecho_1_dim.configure(highlightcolor="black")
    
            la_dim_trecho1 = tk.Label(frame_trecho_1_dim)
            la_dim_trecho1.place(relx=0.063, rely=0.083, height=26, width=98)
            la_dim_trecho1.configure(activebackground="#f9f9f9")
            la_dim_trecho1.configure(activeforeground="black")
            la_dim_trecho1.configure(background="#d9d9d9")
            la_dim_trecho1.configure(disabledforeground="#a3a3a3")
            la_dim_trecho1.configure(font="-family {Segoe UI} -size 9 -weight bold -slant italic")
            la_dim_trecho1.configure(foreground="#000000")
            la_dim_trecho1.configure(highlightbackground="#d9d9d9")
            la_dim_trecho1.configure(highlightcolor="black")
            la_dim_trecho1.configure(text='''1º Span''')
    
            la_dim_trecho1_L = tk.Label(frame_trecho_1_dim)
            la_dim_trecho1_L.place(relx=0.031, rely=0.5, height=26, width=42)
            la_dim_trecho1_L.configure(activebackground="#f9f9f9")
            la_dim_trecho1_L.configure(activeforeground="black")
            la_dim_trecho1_L.configure(background="#d9d9d9")
            la_dim_trecho1_L.configure(disabledforeground="#a3a3a3")
            la_dim_trecho1_L.configure(foreground="#000000")
            la_dim_trecho1_L.configure(highlightbackground="#d9d9d9")
            la_dim_trecho1_L.configure(highlightcolor="black")
            la_dim_trecho1_L.configure(text='''L=''')
    
            box_dim_trecho1_L = tk.Entry(frame_trecho_1_dim)
            box_dim_trecho1_L.place(relx=0.125, rely=0.5, height=24, relwidth=0.325)
            box_dim_trecho1_L.configure(background="white")
            box_dim_trecho1_L.configure(disabledforeground="#a3a3a3")
            box_dim_trecho1_L.configure(font="TkFixedFont")
            box_dim_trecho1_L.configure(foreground="#000000")
            box_dim_trecho1_L.configure(highlightbackground="#d9d9d9")
            box_dim_trecho1_L.configure(highlightcolor="black")
            box_dim_trecho1_L.configure(insertbackground="black")
            box_dim_trecho1_L.configure(selectbackground="#c4c4c4")
            box_dim_trecho1_L.configure(selectforeground="black")
    
            la_dim_trecho1_Q = tk.Label(frame_trecho_1_dim)
            la_dim_trecho1_Q.place(relx=0.5, rely=0.5, height=26, width=42)
            la_dim_trecho1_Q.configure(activebackground="#f9f9f9")
            la_dim_trecho1_Q.configure(activeforeground="black")
            la_dim_trecho1_Q.configure(background="#d9d9d9")
            la_dim_trecho1_Q.configure(disabledforeground="#a3a3a3")
            la_dim_trecho1_Q.configure(foreground="#000000")
            la_dim_trecho1_Q.configure(highlightbackground="#d9d9d9")
            la_dim_trecho1_Q.configure(highlightcolor="black")
            la_dim_trecho1_Q.configure(text='''Q=''')
    
            box_dim_trecho1_Q = tk.Entry(frame_trecho_1_dim)
            box_dim_trecho1_Q.place(relx=0.609, rely=0.5, height=24, relwidth=0.325)
            box_dim_trecho1_Q.configure(background="white")
            box_dim_trecho1_Q.configure(disabledforeground="#a3a3a3")
            box_dim_trecho1_Q.configure(font="TkFixedFont")
            box_dim_trecho1_Q.configure(foreground="#000000")
            box_dim_trecho1_Q.configure(highlightbackground="#d9d9d9")
            box_dim_trecho1_Q.configure(highlightcolor="black")
            box_dim_trecho1_Q.configure(insertbackground="black")
            box_dim_trecho1_Q.configure(selectbackground="#c4c4c4")
            box_dim_trecho1_Q.configure(selectforeground="black")
    
            frame_trecho_2_dim = tk.Frame(janela_trecho)
            frame_trecho_2_dim.place(relx=0.029, rely=0.318, relheight=0.273, relwidth=0.941)
            frame_trecho_2_dim.configure(relief='groove')
            frame_trecho_2_dim.configure(borderwidth="2")
            frame_trecho_2_dim.configure(relief="groove")
            frame_trecho_2_dim.configure(background="#d9d9d9")
            frame_trecho_2_dim.configure(highlightbackground="#d9d9d9")
            frame_trecho_2_dim.configure(highlightcolor="black")
    
            la_dim_trecho2 = tk.Label(frame_trecho_2_dim)
            la_dim_trecho2.place(relx=0.063, rely=0.083, height=26, width=98)
            la_dim_trecho2.configure(activebackground="#f9f9f9")
            la_dim_trecho2.configure(activeforeground="black")
            la_dim_trecho2.configure(background="#d9d9d9")
            la_dim_trecho2.configure(disabledforeground="#a3a3a3")
            la_dim_trecho2.configure(font="-family {Segoe UI} -size 9 -weight bold -slant italic")
            la_dim_trecho2.configure(foreground="#000000")
            la_dim_trecho2.configure(highlightbackground="#d9d9d9")
            la_dim_trecho2.configure(highlightcolor="black")
            la_dim_trecho2.configure(text='''2º Span''')
    
            la_dim_trecho2_L = tk.Label(frame_trecho_2_dim)
            la_dim_trecho2_L.place(relx=0.031, rely=0.5, height=26, width=42)
            la_dim_trecho2_L.configure(activebackground="#f9f9f9")
            la_dim_trecho2_L.configure(activeforeground="black")
            la_dim_trecho2_L.configure(background="#d9d9d9")
            la_dim_trecho2_L.configure(disabledforeground="#a3a3a3")
            la_dim_trecho2_L.configure(foreground="#000000")
            la_dim_trecho2_L.configure(highlightbackground="#d9d9d9")
            la_dim_trecho2_L.configure(highlightcolor="black")
            la_dim_trecho2_L.configure(text='''L=''')
    
            box_dim_trecho2_L = tk.Entry(frame_trecho_2_dim)
            box_dim_trecho2_L.place(relx=0.125, rely=0.5, height=24, relwidth=0.325)
            box_dim_trecho2_L.configure(background="white")
            box_dim_trecho2_L.configure(disabledforeground="#a3a3a3")
            box_dim_trecho2_L.configure(font="TkFixedFont")
            box_dim_trecho2_L.configure(foreground="#000000")
            box_dim_trecho2_L.configure(highlightbackground="#d9d9d9")
            box_dim_trecho2_L.configure(highlightcolor="black")
            box_dim_trecho2_L.configure(insertbackground="black")
            box_dim_trecho2_L.configure(selectbackground="#c4c4c4")
            box_dim_trecho2_L.configure(selectforeground="black")
    
            la_dim_trecho2_Q = tk.Label(frame_trecho_2_dim)
            la_dim_trecho2_Q.place(relx=0.5, rely=0.5, height=26, width=42)
            la_dim_trecho2_Q.configure(activebackground="#f9f9f9")
            la_dim_trecho2_Q.configure(activeforeground="black")
            la_dim_trecho2_Q.configure(background="#d9d9d9")
            la_dim_trecho2_Q.configure(disabledforeground="#a3a3a3")
            la_dim_trecho2_Q.configure(foreground="#000000")
            la_dim_trecho2_Q.configure(highlightbackground="#d9d9d9")
            la_dim_trecho2_Q.configure(highlightcolor="black")
            la_dim_trecho2_Q.configure(text='''Q=''')
    
            box_dim_trecho2_Q = tk.Entry(frame_trecho_2_dim)
            box_dim_trecho2_Q.place(relx=0.609, rely=0.5, height=24, relwidth=0.325)
            box_dim_trecho2_Q.configure(background="white")
            box_dim_trecho2_Q.configure(disabledforeground="#a3a3a3")
            box_dim_trecho2_Q.configure(font="TkFixedFont")
            box_dim_trecho2_Q.configure(foreground="#000000")
            box_dim_trecho2_Q.configure(highlightbackground="#d9d9d9")
            box_dim_trecho2_Q.configure(highlightcolor="black")
            box_dim_trecho2_Q.configure(insertbackground="black")
            box_dim_trecho2_Q.configure(selectbackground="#c4c4c4")
            box_dim_trecho2_Q.configure(selectforeground="black")
    
            frame_trecho_3_dim = tk.Frame(janela_trecho)
            frame_trecho_3_dim.place(relx=0.029, rely=0.614, relheight=0.273, relwidth=0.941)
            frame_trecho_3_dim.configure(relief='groove')
            frame_trecho_3_dim.configure(borderwidth="2")
            frame_trecho_3_dim.configure(relief="groove")
            frame_trecho_3_dim.configure(background="#d9d9d9")
            frame_trecho_3_dim.configure(highlightbackground="#d9d9d9")
            frame_trecho_3_dim.configure(highlightcolor="black")
    
            la_dim_trecho3 = tk.Label(frame_trecho_3_dim)
            la_dim_trecho3.place(relx=0.063, rely=0.083, height=26, width=98)
            la_dim_trecho3.configure(activebackground="#f9f9f9")
            la_dim_trecho3.configure(activeforeground="black")
            la_dim_trecho3.configure(background="#d9d9d9")
            la_dim_trecho3.configure(disabledforeground="#a3a3a3")
            la_dim_trecho3.configure(font="-family {Segoe UI} -size 9 -weight bold -slant italic")
            la_dim_trecho3.configure(foreground="#000000")
            la_dim_trecho3.configure(highlightbackground="#d9d9d9")
            la_dim_trecho3.configure(highlightcolor="black")
            la_dim_trecho3.configure(text='''3º Span''')
    
            la_dim_trecho3_L = tk.Label(frame_trecho_3_dim)
            la_dim_trecho3_L.place(relx=0.031, rely=0.5, height=26, width=42)
            la_dim_trecho3_L.configure(activebackground="#f9f9f9")
            la_dim_trecho3_L.configure(activeforeground="black")
            la_dim_trecho3_L.configure(background="#d9d9d9")
            la_dim_trecho3_L.configure(disabledforeground="#a3a3a3")
            la_dim_trecho3_L.configure(foreground="#000000")
            la_dim_trecho3_L.configure(highlightbackground="#d9d9d9")
            la_dim_trecho3_L.configure(highlightcolor="black")
            la_dim_trecho3_L.configure(text='''L=''')
    
            box_dim_trecho3_L = tk.Entry(frame_trecho_3_dim)
            box_dim_trecho3_L.place(relx=0.125, rely=0.5, height=24, relwidth=0.325)
            box_dim_trecho3_L.configure(background="white")
            box_dim_trecho3_L.configure(disabledforeground="#a3a3a3")
            box_dim_trecho3_L.configure(font="TkFixedFont")
            box_dim_trecho3_L.configure(foreground="#000000")
            box_dim_trecho3_L.configure(highlightbackground="#d9d9d9")
            box_dim_trecho3_L.configure(highlightcolor="black")
            box_dim_trecho3_L.configure(insertbackground="black")
            box_dim_trecho3_L.configure(selectbackground="#c4c4c4")
            box_dim_trecho3_L.configure(selectforeground="black")
    
            la_dim_trecho3_Q = tk.Label(frame_trecho_3_dim)
            la_dim_trecho3_Q.place(relx=0.5, rely=0.5, height=26, width=42)
            la_dim_trecho3_Q.configure(activebackground="#f9f9f9")
            la_dim_trecho3_Q.configure(activeforeground="black")
            la_dim_trecho3_Q.configure(background="#d9d9d9")
            la_dim_trecho3_Q.configure(disabledforeground="#a3a3a3")
            la_dim_trecho3_Q.configure(foreground="#000000")
            la_dim_trecho3_Q.configure(highlightbackground="#d9d9d9")
            la_dim_trecho3_Q.configure(highlightcolor="black")
            la_dim_trecho3_Q.configure(text='''Q=''')
    
            box_dim_trecho3_Q = tk.Entry(frame_trecho_3_dim)
            box_dim_trecho3_Q.place(relx=0.609, rely=0.5, height=24, relwidth=0.325)
            box_dim_trecho3_Q.configure(background="white")
            box_dim_trecho3_Q.configure(disabledforeground="#a3a3a3")
            box_dim_trecho3_Q.configure(font="TkFixedFont")
            box_dim_trecho3_Q.configure(foreground="#000000")
            box_dim_trecho3_Q.configure(highlightbackground="#d9d9d9")
            box_dim_trecho3_Q.configure(highlightcolor="black")
            box_dim_trecho3_Q.configure(insertbackground="black")
            box_dim_trecho3_Q.configure(selectbackground="#c4c4c4")
            box_dim_trecho3_Q.configure(selectforeground="black")
    
            but_seguinte_trechos = tk.Button(janela_trecho)
            but_seguinte_trechos.place(relx=0.382, rely=0.909, height=33, width=80)
            but_seguinte_trechos.configure(activebackground="#ececec")
            but_seguinte_trechos.configure(activeforeground="#000000")
            but_seguinte_trechos.configure(background="#0000ff")
            but_seguinte_trechos.configure(disabledforeground="#a3a3a3")
            but_seguinte_trechos.configure(foreground="#ffffff")
            but_seguinte_trechos.configure(highlightbackground="#d9d9d9")
            but_seguinte_trechos.configure(highlightcolor="black")
            but_seguinte_trechos.configure(pady="0")
            but_seguinte_trechos.configure(text='''>>>''')
            but_seguinte_trechos.configure(command=destroy_cargas)
            
            janela_trecho.mainloop()
        
    n_vaos=tk.Tk()

    font9 = "-family {Segoe UI} -size 11 -weight bold -slant "  \
        "italic"
    style = ttk.Style()
    style.configure('.',background=_bgcolor)
    style.configure('.',foreground=_fgcolor)
    style.configure('.',font="TkDefaultFont")
    style.map('.',background=
        [('selected', _compcolor), ('active',_ana2color)])
    
    n_vaos.geometry("300x150+797+151")
    n_vaos.minsize(148, 1)
    n_vaos.maxsize(1924, 1055)
    n_vaos.resizable(1, 1)
    n_vaos.iconbitmap('icones/geral.ico')
    n_vaos.title("Span data")
    n_vaos.configure(background="#d9d9d9")
    
    la_n_vaos = tk.Label(n_vaos)
    la_n_vaos.place(relx=0.083, rely=0.1, height=33, width=250)
    la_n_vaos.configure(background="#d9d9d9")
    la_n_vaos.configure(disabledforeground="#a3a3a3")
    la_n_vaos.configure(font=font9)
    la_n_vaos.configure(foreground="#000000")
    la_n_vaos.configure(text='''Number of beam spans:''')
    
    combobox_n_vaos = ttk.Combobox(n_vaos)
    combobox_n_vaos.place(relx=0.2, rely=0.4, relheight=0.173, relwidth=0.623)
    combobox_n_vaos.configure(values=["1","2","3"])
    combobox_n_vaos.configure(takefocus="")
    
    btn_n_vaos = tk.Button(n_vaos)
    btn_n_vaos.place(relx=0.4, rely=0.667, height=43, width=56)
    btn_n_vaos.configure(activebackground="#ececec")
    btn_n_vaos.configure(activeforeground="#000000")
    btn_n_vaos.configure(background="#0000ff")
    btn_n_vaos.configure(disabledforeground="#a3a3a3")
    btn_n_vaos.configure(foreground="#ffffff")
    btn_n_vaos.configure(highlightbackground="#d9d9d9")
    btn_n_vaos.configure(highlightcolor="black")
    btn_n_vaos.configure(pady="0")
    btn_n_vaos.configure(text='''>>>''')
    btn_n_vaos.configure(command=cargas_vao)
    
    
    n_vaos.mainloop()





def janela_mat():
    global fck , yc , E_a , fy , ya , E_as , fs , ys
    
    def take_mat():
        global fck , yc , E_a , fy , ya , E_as , fs , ys
        fck    =   float(box_fck   .get())
        yc     =   float(box_yc   .get())
        
        E_a    =   float(box_E_a   .get())
        fy    =   float(box_fy   .get())
        ya      =   float(box_ya   .get())
        
        E_as    =   float(box_E_As   .get())
        fs    =   float(box_fs   .get())
        ys      =   float(box_ys   .get())
        
        janela_materiais.destroy()

    
    
    janela_materiais=tk.Tk()
    
    janela_materiais.geometry("340x511+500+200")
    janela_materiais.minsize(148, 1)
    janela_materiais.maxsize(1924, 1055)
    janela_materiais.resizable(1, 1)
    janela_materiais.iconbitmap('icones/geral.ico')
    janela_materiais.title("Material Property")
    janela_materiais.configure(background="#d9d9d9")
    janela_materiais.configure(highlightbackground="#d9d9d9")
    janela_materiais.configure(highlightcolor="black")
    
    frame_prop_concreto = tk.Frame(janela_materiais)
    frame_prop_concreto.place(relx=0.029, rely=0.02, relheight=0.188, relwidth=0.941)
    frame_prop_concreto.configure(relief='groove')
    frame_prop_concreto.configure(borderwidth="2")
    frame_prop_concreto.configure(relief="groove")
    frame_prop_concreto.configure(background="#d9d9d9")
    frame_prop_concreto.configure(highlightbackground="#d9d9d9")
    frame_prop_concreto.configure(highlightcolor="black")
    
    la_concreto = tk.Label(frame_prop_concreto)
    la_concreto.place(relx=0.063, rely=0.063, height=21, width=98)
    la_concreto.configure(activebackground="#f9f9f9")
    la_concreto.configure(activeforeground="black")
    la_concreto.configure(background="#d9d9d9")
    la_concreto.configure(disabledforeground="#a3a3a3")
    la_concreto.configure(font="-family {Segoe UI} -size 9 -weight bold -slant italic")
    la_concreto.configure(foreground="#000000")
    la_concreto.configure(highlightbackground="#d9d9d9")
    la_concreto.configure(highlightcolor="black")
    la_concreto.configure(text='''Concrete''')
    
    la_fck = tk.Label(frame_prop_concreto)
    la_fck.place(relx=0.031, rely=0.6, height=21, width=30)
    la_fck.configure(activebackground="#f9f9f9")
    la_fck.configure(activeforeground="black")
    la_fck.configure(background="#d9d9d9")
    la_fck.configure(disabledforeground="#a3a3a3")
    la_fck.configure(foreground="#000000")
    la_fck.configure(highlightbackground="#d9d9d9")
    la_fck.configure(highlightcolor="black")
    la_fck.configure(text='''fc=''')
    
    box_fck = tk.Entry(frame_prop_concreto)
    box_fck.place(relx=0.156, rely=0.563,height=24, relwidth=0.325)
    box_fck.configure(background="white")
    box_fck.configure(disabledforeground="#a3a3a3")
    box_fck.configure(font="TkFixedFont")
    box_fck.configure(foreground="#000000")
    box_fck.configure(highlightbackground="#d9d9d9")
    box_fck.configure(highlightcolor="black")
    box_fck.configure(insertbackground="black")
    box_fck.configure(selectbackground="#c4c4c4")
    box_fck.configure(selectforeground="black")
    
    la_yc = tk.Label(frame_prop_concreto)
    la_yc.place(relx=0.5, rely=0.6, height=21, width=42)
    la_yc.configure(activebackground="#f9f9f9")
    la_yc.configure(activeforeground="black")
    la_yc.configure(background="#d9d9d9")
    la_yc.configure(disabledforeground="#a3a3a3")
    la_yc.configure(foreground="#000000")
    la_yc.configure(highlightbackground="#d9d9d9")
    la_yc.configure(highlightcolor="black")
    la_yc.configure(text='''yc=''')
    
    box_yc = tk.Entry(frame_prop_concreto)
    box_yc.place(relx=0.625, rely=0.563,height=24, relwidth=0.325)
    box_yc.configure(background="white")
    box_yc.configure(disabledforeground="#a3a3a3")
    box_yc.configure(font="TkFixedFont")
    box_yc.configure(foreground="#000000")
    box_yc.configure(highlightbackground="#d9d9d9")
    box_yc.configure(highlightcolor="black")
    box_yc.configure(insertbackground="black")
    box_yc.configure(selectbackground="#c4c4c4")
    box_yc.configure(selectforeground="black")
    
    frame_perfil = tk.Frame(janela_materiais)
    frame_perfil.place(relx=0.029, rely=0.227, relheight=0.294, relwidth=0.941)
    frame_perfil.configure(relief='groove')
    frame_perfil.configure(borderwidth="2")
    frame_perfil.configure(relief="groove")
    frame_perfil.configure(background="#d9d9d9")
    frame_perfil.configure(highlightbackground="#d9d9d9")
    frame_perfil.configure(highlightcolor="black")
    
    la_perfil = tk.Label(frame_perfil)
    la_perfil.place(relx=0.063, rely=0.06, height=33, width=98)
    la_perfil.configure(activebackground="#f9f9f9")
    la_perfil.configure(activeforeground="black")
    la_perfil.configure(background="#d9d9d9")
    la_perfil.configure(disabledforeground="#a3a3a3")
    la_perfil.configure(font="-family {Segoe UI} -size 9 -weight bold -slant italic")
    la_perfil.configure(foreground="#000000")
    la_perfil.configure(highlightbackground="#d9d9d9")
    la_perfil.configure(highlightcolor="black")
    la_perfil.configure(text='''Steel I-Section''')
    
    la_E_a = tk.Label(frame_perfil)
    la_E_a.place(relx=0.025, rely=0.373, height=33, width=35)
    la_E_a.configure(activebackground="#f9f9f9")
    la_E_a.configure(activeforeground="black")
    la_E_a.configure(background="#d9d9d9")
    la_E_a.configure(disabledforeground="#a3a3a3")
    la_E_a.configure(foreground="#000000")
    la_E_a.configure(highlightbackground="#d9d9d9")
    la_E_a.configure(highlightcolor="black")
    la_E_a.configure(text='''E_a=''')
    
    box_E_a = tk.Entry(frame_perfil)
    box_E_a.place(relx=0.125, rely=0.407,height=24, relwidth=0.325)
    box_E_a.configure(background="white")
    box_E_a.configure(disabledforeground="#a3a3a3")
    box_E_a.configure(font="TkFixedFont")
    box_E_a.configure(foreground="#000000")
    box_E_a.configure(highlightbackground="#d9d9d9")
    box_E_a.configure(highlightcolor="black")
    box_E_a.configure(insertbackground="black")
    box_E_a.configure(selectbackground="#c4c4c4")
    box_E_a.configure(selectforeground="black")
    
    la_fy = tk.Label(frame_perfil)
    la_fy.place(relx=0.5, rely=0.393, height=32, width=42)
    la_fy.configure(activebackground="#f9f9f9")
    la_fy.configure(activeforeground="black")
    la_fy.configure(background="#d9d9d9")
    la_fy.configure(disabledforeground="#a3a3a3")
    la_fy.configure(foreground="#000000")
    la_fy.configure(highlightbackground="#d9d9d9")
    la_fy.configure(highlightcolor="black")
    la_fy.configure(text='''fy=''')
    
    box_fy = tk.Entry(frame_perfil)
    box_fy.place(relx=0.609, rely=0.407,height=24, relwidth=0.325)
    box_fy.configure(background="white")
    box_fy.configure(disabledforeground="#a3a3a3")
    box_fy.configure(font="TkFixedFont")
    box_fy.configure(foreground="#000000")
    box_fy.configure(highlightbackground="#d9d9d9")
    box_fy.configure(highlightcolor="black")
    box_fy.configure(insertbackground="black")
    box_fy.configure(selectbackground="#c4c4c4")
    box_fy.configure(selectforeground="black")
    
    box_ya = tk.Entry(frame_perfil)
    box_ya.place(relx=0.125, rely=0.68,height=24, relwidth=0.325)
    box_ya.configure(background="white")
    box_ya.configure(disabledforeground="#a3a3a3")
    box_ya.configure(font="TkFixedFont")
    box_ya.configure(foreground="#000000")
    box_ya.configure(highlightbackground="#d9d9d9")
    box_ya.configure(highlightcolor="black")
    box_ya.configure(insertbackground="black")
    box_ya.configure(selectbackground="#c4c4c4")
    box_ya.configure(selectforeground="black")
    
    la_ya = tk.Label(frame_perfil)
    la_ya.place(relx=0.031, rely=0.653, height=32, width=30)
    la_ya.configure(activebackground="#f9f9f9")
    la_ya.configure(activeforeground="black")
    la_ya.configure(background="#d9d9d9")
    la_ya.configure(disabledforeground="#a3a3a3")
    la_ya.configure(foreground="#000000")
    la_ya.configure(highlightbackground="#d9d9d9")
    la_ya.configure(highlightcolor="black")
    la_ya.configure(text='''ya=''')
    
    frame_As_complementar = tk.Frame(janela_materiais)
    frame_As_complementar.place(relx=0.029, rely=0.54, relheight=0.294
            , relwidth=0.941)
    frame_As_complementar.configure(relief='groove')
    frame_As_complementar.configure(borderwidth="2")
    frame_As_complementar.configure(relief="groove")
    frame_As_complementar.configure(background="#d9d9d9")
    frame_As_complementar.configure(highlightbackground="#d9d9d9")
    frame_As_complementar.configure(highlightcolor="black")
    
    la_As_complementar = tk.Label(frame_As_complementar)
    la_As_complementar.place(relx=0.063, rely=0.06, height=33
            , width=138)
    la_As_complementar.configure(activebackground="#f9f9f9")
    la_As_complementar.configure(activeforeground="black")
    la_As_complementar.configure(background="#d9d9d9")
    la_As_complementar.configure(disabledforeground="#a3a3a3")
    la_As_complementar.configure(font="-family {Segoe UI} -size 9 -weight bold -slant italic")
    la_As_complementar.configure(foreground="#000000")
    la_As_complementar.configure(highlightbackground="#d9d9d9")
    la_As_complementar.configure(highlightcolor="black")
    la_As_complementar.configure(text='''Steel Reinforcement''')
    
    la_E_As = tk.Label(frame_As_complementar)
    la_E_As.place(relx=0.031, rely=0.373, height=33, width=45)
    la_E_As.configure(activebackground="#f9f9f9")
    la_E_As.configure(activeforeground="black")
    la_E_As.configure(background="#d9d9d9")
    la_E_As.configure(disabledforeground="#a3a3a3")
    la_E_As.configure(foreground="#000000")
    la_E_As.configure(highlightbackground="#d9d9d9")
    la_E_As.configure(highlightcolor="black")
    la_E_As.configure(text='''Es=''')
    
    box_E_As = tk.Entry(frame_As_complementar)
    box_E_As.place(relx=0.172, rely=0.407,height=24, relwidth=0.325)
    box_E_As.configure(background="white")
    box_E_As.configure(disabledforeground="#a3a3a3")
    box_E_As.configure(font="TkFixedFont")
    box_E_As.configure(foreground="#000000")
    box_E_As.configure(highlightbackground="#d9d9d9")
    box_E_As.configure(highlightcolor="black")
    box_E_As.configure(insertbackground="black")
    box_E_As.configure(selectbackground="#c4c4c4")
    box_E_As.configure(selectforeground="black")
    
    la_fs = tk.Label(frame_As_complementar)
    la_fs.place(relx=0.5, rely=0.393, height=32, width=42)
    la_fs.configure(activebackground="#f9f9f9")
    la_fs.configure(activeforeground="black")
    la_fs.configure(background="#d9d9d9")
    la_fs.configure(disabledforeground="#a3a3a3")
    la_fs.configure(foreground="#000000")
    la_fs.configure(highlightbackground="#d9d9d9")
    la_fs.configure(highlightcolor="black")
    la_fs.configure(text='''fs=''')
    
    box_fs = tk.Entry(frame_As_complementar)
    box_fs.place(relx=0.609, rely=0.407,height=24, relwidth=0.325)
    box_fs.configure(background="white")
    box_fs.configure(disabledforeground="#a3a3a3")
    box_fs.configure(font="TkFixedFont")
    box_fs.configure(foreground="#000000")
    box_fs.configure(highlightbackground="#d9d9d9")
    box_fs.configure(highlightcolor="black")
    box_fs.configure(insertbackground="black")
    box_fs.configure(selectbackground="#c4c4c4")
    box_fs.configure(selectforeground="black")
    
    box_ys = tk.Entry(frame_As_complementar)
    box_ys.place(relx=0.172, rely=0.7,height=24, relwidth=0.325)
    box_ys.configure(background="white")
    box_ys.configure(disabledforeground="#a3a3a3")
    box_ys.configure(font="TkFixedFont")
    box_ys.configure(foreground="#000000")
    box_ys.configure(highlightbackground="#d9d9d9")
    box_ys.configure(highlightcolor="black")
    box_ys.configure(insertbackground="black")
    box_ys.configure(selectbackground="#c4c4c4")
    box_ys.configure(selectforeground="black")
    
    la_ys = tk.Label(frame_As_complementar)
    la_ys.place(relx=0.063, rely=0.667, height=33, width=30)
    la_ys.configure(activebackground="#f9f9f9")
    la_ys.configure(activeforeground="black")
    la_ys.configure(background="#d9d9d9")
    la_ys.configure(disabledforeground="#a3a3a3")
    la_ys.configure(foreground="#000000")
    la_ys.configure(highlightbackground="#d9d9d9")
    la_ys.configure(highlightcolor="black")
    la_ys.configure(text='''ys=''')
        
    but_seguinte_materiais = tk.Button(janela_materiais)
    but_seguinte_materiais.place(relx=0.382, rely=0.908, height=33, width=80)
    but_seguinte_materiais.configure(activebackground="#ececec")
    but_seguinte_materiais.configure(activeforeground="#000000")
    but_seguinte_materiais.configure(background="#0000ff")
    but_seguinte_materiais.configure(disabledforeground="#a3a3a3")
    but_seguinte_materiais.configure(foreground="#ffffff")
    but_seguinte_materiais.configure(highlightbackground="#d9d9d9")
    but_seguinte_materiais.configure(highlightcolor="black")
    but_seguinte_materiais.configure(pady="0")
    but_seguinte_materiais.configure(text='''>>>''')
    but_seguinte_materiais.configure(command=take_mat)
    
    janela_materiais.mainloop()

    
def metodo_calculo():
    
    # def func_grau():
    #     def destroy_janela_grau():
    #         global DoC
    #         DoC      =   box_dim_grau1.get()
    #         janela_grau.destroy()
            
    #     if (interacao=="Partial"):
    #              janela_grau= tk.Tk()
        
    #              janela_grau.geometry("340x180+895+168")
    #              janela_grau.minsize(148, 1)
    #              janela_grau.maxsize(1924, 1200)
    #              janela_grau.resizable(1, 1)
    #              janela_grau.title("Connection degree")
    #              janela_grau.configure(background="#d9d9d9")
    #              janela_grau.configure(highlightbackground="#d9d9d9")
    #              janela_grau.configure(highlightcolor="black")
        
    #              frame_grau_1_dim = tk.Frame(janela_grau)
    #              frame_grau_1_dim.place(relx=0.029, rely=0.015, relheight=0.60, relwidth=0.941)
    #              frame_grau_1_dim.configure(relief='groove')
    #              frame_grau_1_dim.configure(borderwidth="2")
    #              frame_grau_1_dim.configure(relief="groove")
    #              frame_grau_1_dim.configure(background="#d9d9d9")
    #              frame_grau_1_dim.configure(highlightbackground="#d9d9d9")
    #              frame_grau_1_dim.configure(highlightcolor="black")
                 
    #              la_grau1 = tk.Label(janela_grau)
    #              la_grau1.place(relx=0.2, rely=0.1, height=33, width=200)
    #              la_grau1.configure(activebackground="#f9f9f9")
    #              la_grau1.configure(activeforeground="black")
    #              la_grau1.configure(background="#d9d9d9")
    #              la_grau1.configure(disabledforeground="#a3a3a3")
    #              la_grau1.configure(font="-family {Segoe UI} -size 11 -weight bold -slant italic")
    #              la_grau1.configure(foreground="#000000")
    #              la_grau1.configure(highlightbackground="#d9d9d9")
    #              la_grau1.configure(highlightcolor="black")
    #              la_grau1.configure(text='''Degree of Conection[%]:''')
        
    #              box_dim_grau1 = tk.Entry(janela_grau)
    #              box_dim_grau1.place(relx=0.325, rely=0.35, height=24, relwidth=0.325)
    #              box_dim_grau1.configure(background="white")
    #              box_dim_grau1.configure(disabledforeground="#a3a3a3")
    #              box_dim_grau1.configure(font="TkFixedFont")
    #              box_dim_grau1.configure(foreground="#000000")
    #              box_dim_grau1.configure(highlightbackground="#d9d9d9")
    #              box_dim_grau1.configure(highlightcolor="black")
    #              box_dim_grau1.configure(insertbackground="black")
    #              box_dim_grau1.configure(selectbackground="#c4c4c4")
    #              box_dim_grau1.configure(selectforeground="black")   
                 
    #              btn_grau = tk.Button(janela_grau)
    #              btn_grau.place(relx=0.4, rely=0.65, height=43, width=56)
    #              btn_grau.configure(activebackground="#ececec")
    #              btn_grau.configure(activeforeground="#000000")
    #              btn_grau.configure(background="#0000ff")
    #              btn_grau.configure(disabledforeground="#a3a3a3")
    #              btn_grau.configure(foreground="#ffffff")
    #              btn_grau.configure(highlightbackground="#d9d9d9")
    #              btn_grau.configure(highlightcolor="black")
    #              btn_grau.configure(pady="0")
    #              btn_grau.configure(text='''>>>''')
    #              btn_grau.configure(command=destroy_janela_grau)
    
    def func_grau():
        def destroy_janela_grau():
            global DoC
            DoC = box_dim_grau1.get()
            janela_grau.destroy()
        
        if interacao == "Partial":
            janela_grau = tk.Tk()
            janela_grau.geometry("340x180+895+168")
            janela_grau.title("Degree of Connection")
            janela_grau.configure(background="#d9d9d9")
            
            janela_grau.geometry("300x150+561+192")
            janela_grau.minsize(148, 1)
            janela_grau.maxsize(1924, 1055)
            janela_grau.resizable(1, 1)
            janela_grau.iconbitmap('icones/geral.ico')
            janela_grau.title("Design Method")
            janela_grau.configure(background="#d9d9d9")
            janela_grau.configure(highlightbackground="#d9d9d9")
            janela_grau.configure(highlightcolor="black")
        
            frame_grau_1_dim = tk.Frame(janela_grau, relief='groove', borderwidth=2, background="#d9d9d9")
            frame_grau_1_dim.place(relx=0.029, rely=0.015, relheight=0.60, relwidth=0.941)
        
            la_grau1 = tk.Label(janela_grau, text='Degree of Connection[%]:', font="-family {Segoe UI} -size 11 -weight bold -slant italic", background="#d9d9d9", foreground="#000000")
            la_grau1.place(relx=0.2, rely=0.1)
        
            box_dim_grau1 = tk.Entry(janela_grau)
            box_dim_grau1.place(relx=0.325, rely=0.35, height=24, relwidth=0.325)
        
            btn_grau = tk.Button(janela_grau, text='>>>', background="#0000ff", foreground="#ffffff", command=destroy_janela_grau)
            btn_grau.place(relx=0.4, rely=0.65, height=43, width=56)

            janela_grau.mainloop()
                

    def func_interacao():
    
        
        
        def destroy_janela_interacao():
            global interacao
            interacao      =   str(combobox_interacao   .get())
            janela_interacao.destroy()
            func_grau()
        
        if (norma=="NBR 8800"):
            janela_interacao=tk.Tk()
        
            style = ttk.Style()
            style.configure('.',background=_bgcolor)
            style.configure('.',foreground=_fgcolor)
            style.configure('.',font="TkDefaultFont")
            style.map('.',background=[('selected', _compcolor), ('active',_ana2color)])
        
            janela_interacao.geometry("300x150+561+192")
            janela_interacao.minsize(148, 1)
            janela_interacao.maxsize(1924, 1055)
            janela_interacao.resizable(1, 1)
            janela_interacao.iconbitmap('icones/geral.ico')
            janela_interacao.title("Design Method")
            janela_interacao.configure(background="#d9d9d9")
            janela_interacao.configure(highlightbackground="#d9d9d9")
            janela_interacao.configure(highlightcolor="black")
        
            la_normas = tk.Label(janela_interacao)
            la_normas.place(relx=0.083, rely=0.1, height=33, width=250)
            la_normas.configure(activebackground="#f9f9f9")
            la_normas.configure(activeforeground="black")
            la_normas.configure(background="#d9d9d9")
            la_normas.configure(disabledforeground="#a3a3a3")
            la_normas.configure(font="-family {Segoe UI} -size 11 -weight bold -slant italic")
            la_normas.configure(foreground="#000000")
            la_normas.configure(highlightbackground="#d9d9d9")
            la_normas.configure(highlightcolor="black")
            la_normas.configure(text='''Interaction:''')
        
            combobox_interacao = ttk.Combobox(janela_interacao)
            combobox_interacao.place(relx=0.2, rely=0.4, relheight=0.173, relwidth=0.623)
            combobox_interacao.configure(values=["Complete","Partial"])
            combobox_interacao.configure(takefocus="")
            combobox_interacao.current(0)
        
            btn_normas = tk.Button(janela_interacao)
            btn_normas.place(relx=0.4, rely=0.667, height=43, width=56)
            btn_normas.configure(activebackground="#ececec")
            btn_normas.configure(activeforeground="#000000")
            btn_normas.configure(background="#0000ff")
            btn_normas.configure(disabledforeground="#a3a3a3")
            btn_normas.configure(foreground="#ffffff")
            btn_normas.configure(highlightbackground="#d9d9d9")
            btn_normas.configure(highlightcolor="black")
            btn_normas.configure(pady="0")
            btn_normas.configure(text='''>>>''')
            btn_normas.configure(command=destroy_janela_interacao)
            
        
        
    def take_norma():
        global norma
        norma      =   str(combobox_norma   .get())
        janela_normas.destroy()
        func_interacao()

    janela_normas=tk.Tk()
    
    style = ttk.Style()
    style.configure('.',background=_bgcolor)
    style.configure('.',foreground=_fgcolor)
    style.configure('.',font="TkDefaultFont")
    style.map('.',background=[('selected', _compcolor), ('active',_ana2color)])

    janela_normas.geometry("300x150+561+192")
    janela_normas.minsize(148, 1)
    janela_normas.maxsize(1924, 1055)
    janela_normas.resizable(1, 1)
    janela_normas.iconbitmap('icones/geral.ico')
    janela_normas.title("Design Method")
    janela_normas.configure(background="#d9d9d9")
    janela_normas.configure(highlightbackground="#d9d9d9")
    janela_normas.configure(highlightcolor="black")

    la_normas = tk.Label(janela_normas)
    la_normas.place(relx=0.083, rely=0.1, height=33, width=250)
    la_normas.configure(activebackground="#f9f9f9")
    la_normas.configure(activeforeground="black")
    la_normas.configure(background="#d9d9d9")
    la_normas.configure(disabledforeground="#a3a3a3")
    la_normas.configure(font="-family {Segoe UI} -size 11 -weight bold -slant italic")
    la_normas.configure(foreground="#000000")
    la_normas.configure(highlightbackground="#d9d9d9")
    la_normas.configure(highlightcolor="black")
    la_normas.configure(text='''Design Based on:''')

    combobox_norma = ttk.Combobox(janela_normas)
    combobox_norma.place(relx=0.2, rely=0.4, relheight=0.173, relwidth=0.623)
    combobox_norma.configure(values=["NBR 8800"])
    combobox_norma.configure(takefocus="")
    combobox_norma.current(0)

    btn_normas = tk.Button(janela_normas)
    btn_normas.place(relx=0.4, rely=0.667, height=43, width=56)
    btn_normas.configure(activebackground="#ececec")
    btn_normas.configure(activeforeground="#000000")
    btn_normas.configure(background="#0000ff")
    btn_normas.configure(disabledforeground="#a3a3a3")
    btn_normas.configure(foreground="#ffffff")
    btn_normas.configure(highlightbackground="#d9d9d9")
    btn_normas.configure(highlightcolor="black")
    btn_normas.configure(pady="0")
    btn_normas.configure(text='''>>>''')
    btn_normas.configure(command=take_norma)   
    
    
    janela_normas.mainloop()
    

# =============================================================================
# =============================================================================
# # JANELA GERAL
# =============================================================================
# =============================================================================
    
    
janela_geral=tk.Tk()
global img2
img2=tk.PhotoImage(file="imagens/SECAO_330x344.png")

# =============================================================================
#                   DEFINDO VERIAVEIS DE ENTRADA E SAÍDA
# =============================================================================

###    PERFIIL

'''This class configures and populates the janela_gerallevel window.
    janela_geral is the janela_gerallevel containing window.'''
_bgcolor = '#d9d9d9'  # X11 color: 'gray85'
_fgcolor = '#000000'  # X11 color: 'black'
_compcolor = '#d9d9d9' # X11 color: 'gray85'
_ana1color = '#d9d9d9' # X11 color: 'gray85'
_ana2color = '#ececec' # Closest X11 color: 'gray92'


janela_geral.minsize(1400, 700)
janela_geral.maxsize(1536, 864)
janela_geral.geometry("1536x795+-8+0")
#janela_geral.resizable(False,False)
janela_geral.iconbitmap('icones/geral.ico')
janela_geral.title("COMBEAMS - Regulatory checks for composite beams")
janela_geral.configure(background="#d9d9d9")
janela_geral.configure(highlightbackground="#d9d9d9")
janela_geral.configure(highlightcolor="black")
#janela_geral.state('zoomed')

# =============================================================================
# FRAME 1- TRECHOS
# =============================================================================

Frame1 = tk.Frame(janela_geral)
Frame1.place(relx=0.827, rely=0.013, relheight=0.975, relwidth=0.167)
Frame1.configure(relief='groove')
Frame1.configure(borderwidth="2")
Frame1.configure(relief="groove")
Frame1.configure(background="#d9d9d9")
Frame1.configure(highlightbackground="#d9d9d9")
Frame1.configure(highlightcolor="black")

# =============================================================================
# FRAME 2-DADOS DO PERFIL
# =============================================================================

Frame2 = tk.Frame(janela_geral)
Frame2.place(relx=0.007, rely=0.013, relheight=0.975, relwidth=0.227)
Frame2.configure(relief='groove')
Frame2.configure(borderwidth="2")
Frame2.configure(relief="groove")
Frame2.configure(background="#d9d9d9")
Frame2.configure(highlightbackground="#d9d9d9")
Frame2.configure(highlightcolor="black")

Frame2_ima = tk.Frame(Frame2)
Frame2_ima.place(relx=0.015, rely=0.006, relheight=0.42, relwidth=0.971)
Frame2_ima.configure(relief='groove')
Frame2_ima.configure(borderwidth="2")
Frame2_ima.configure(relief="groove")
Frame2_ima.configure(background="#d9d9d9")
Frame2_ima.configure(highlightbackground="#d9d9d9")
Frame2_ima.configure(highlightcolor="black")

img=tk.PhotoImage(file="imagens/SECAO_330x344.png")
la_ima_ad_ = tk.Label(Frame2_ima)
la_ima_ad_.place(relx=-0.35, rely=-0.35, relheight=1.7, relwidth=1.7)
la_ima_ad_.configure(image=img)
la_ima_ad_.image=img

la_perfil = tk.Label(Frame2)
la_perfil.place(relx=0.029, rely=0.449, height=25, width=52)
la_perfil.configure(activebackground="#f9f9f9")
la_perfil.configure(activeforeground="black")
la_perfil.configure(background="#d9d9d9")
la_perfil.configure(disabledforeground="#a3a3a3")
la_perfil.configure(font="-family {Segoe UI} -size 9 -weight bold -slant italic")
la_perfil.configure(foreground="#000000")
la_perfil.configure(highlightbackground="#d9d9d9")
la_perfil.configure(highlightcolor="black")
la_perfil.configure(text='''Section''')

la_bf = tk.Label(Frame2)
la_bf.place(relx=0.029, rely=0.487, height=26, width=42)
la_bf.configure(activebackground="#f9f9f9")
la_bf.configure(activeforeground="black")
la_bf.configure(background="#d9d9d9")
la_bf.configure(disabledforeground="#a3a3a3")
la_bf.configure(foreground="#000000")
la_bf.configure(highlightbackground="#d9d9d9")
la_bf.configure(highlightcolor="black")
la_bf.configure(justify='left')
la_bf.configure(text='''bf=''')

la_tf = tk.Label(Frame2)
la_tf.place(relx=0.029, rely=0.526, height=26, width=42)
la_tf.configure(activebackground="#f9f9f9")
la_tf.configure(activeforeground="black")
la_tf.configure(background="#d9d9d9")
la_tf.configure(disabledforeground="#a3a3a3")
la_tf.configure(foreground="#000000")
la_tf.configure(highlightbackground="#d9d9d9")
la_tf.configure(highlightcolor="black")
la_tf.configure(justify='left')
la_tf.configure(text='''tf=''')

la_h = tk.Label(Frame2)
la_h.place(relx=0.029, rely=0.564, height=25, width=42)
la_h.configure(activebackground="#f9f9f9")
la_h.configure(activeforeground="black")
la_h.configure(background="#d9d9d9")
la_h.configure(disabledforeground="#a3a3a3")
la_h.configure(foreground="#000000")
la_h.configure(highlightbackground="#d9d9d9")
la_h.configure(highlightcolor="black")
la_h.configure(justify='left')
la_h.configure(text='''h=''')

la_d = tk.Label(Frame2)
la_d.place(relx=0.029, rely=0.603, height=26, width=42)
la_d.configure(activebackground="#f9f9f9")
la_d.configure(activeforeground="black")
la_d.configure(background="#d9d9d9")
la_d.configure(disabledforeground="#a3a3a3")
la_d.configure(foreground="#000000")
la_d.configure(highlightbackground="#d9d9d9")
la_d.configure(highlightcolor="black")
la_d.configure(justify='left')
la_d.configure(text='''d=''')

la_d_ = tk.Label(Frame2)
la_d_.place(relx=0.029, rely=0.641, height=26, width=42)
la_d_.configure(activebackground="#f9f9f9")
la_d_.configure(activeforeground="black")
la_d_.configure(background="#d9d9d9")
la_d_.configure(disabledforeground="#a3a3a3")
la_d_.configure(foreground="#000000")
la_d_.configure(highlightbackground="#d9d9d9")
la_d_.configure(highlightcolor="black")
la_d_.configure(justify='left')
la_d_.configure(text='''d_=''')

la_tw = tk.Label(Frame2)
la_tw.place(relx=0.471, rely=0.487, height=26, width=42)
la_tw.configure(activebackground="#f9f9f9")
la_tw.configure(activeforeground="black")
la_tw.configure(background="#d9d9d9")
la_tw.configure(disabledforeground="#a3a3a3")
la_tw.configure(foreground="#000000")
la_tw.configure(highlightbackground="#d9d9d9")
la_tw.configure(highlightcolor="black")
la_tw.configure(justify='left')
la_tw.configure(text='''tw=''')

la_ry = tk.Label(Frame2)
la_ry.place(relx=0.471, rely=0.526, height=26, width=42)
la_ry.configure(activebackground="#f9f9f9")
la_ry.configure(activeforeground="black")
la_ry.configure(background="#d9d9d9")
la_ry.configure(disabledforeground="#a3a3a3")
la_ry.configure(foreground="#000000")
la_ry.configure(highlightbackground="#d9d9d9")
la_ry.configure(highlightcolor="black")
la_ry.configure(justify='left')
la_ry.configure(text='''ry=''')

la_wx = tk.Label(Frame2)
la_wx.place(relx=0.471, rely=0.564, height=26, width=42)
la_wx.configure(activebackground="#f9f9f9")
la_wx.configure(activeforeground="black")
la_wx.configure(background="#d9d9d9")
la_wx.configure(disabledforeground="#a3a3a3")
la_wx.configure(foreground="#000000")
la_wx.configure(highlightbackground="#d9d9d9")
la_wx.configure(highlightcolor="black")
la_wx.configure(justify='left')
la_wx.configure(text='''Wx=''')

la_ix = tk.Label(Frame2)
la_ix.place(relx=0.471, rely=0.603, height=26, width=42)
la_ix.configure(activebackground="#f9f9f9")
la_ix.configure(activeforeground="black")
la_ix.configure(background="#d9d9d9")
la_ix.configure(disabledforeground="#a3a3a3")
la_ix.configure(foreground="#000000")
la_ix.configure(highlightbackground="#d9d9d9")
la_ix.configure(highlightcolor="black")
la_ix.configure(justify='left')
la_ix.configure(text='''Ix=''')

la_area = tk.Label(Frame2)
la_area.place(relx=0.471, rely=0.641, height=26, width=42)
la_area.configure(activebackground="#f9f9f9")
la_area.configure(activeforeground="black")
la_area.configure(background="#d9d9d9")
la_area.configure(disabledforeground="#a3a3a3")
la_area.configure(foreground="#000000")
la_area.configure(highlightbackground="#d9d9d9")
la_area.configure(highlightcolor="black")
la_area.configure(justify='left')
la_area.configure(text='''Area=''')

la_laje = tk.Label(Frame2)
la_laje.place(relx=0.029, rely=0.692, height=25, width=30)
la_laje.configure(activebackground="#f9f9f9")
la_laje.configure(activeforeground="black")
la_laje.configure(background="#d9d9d9")
la_laje.configure(disabledforeground="#a3a3a3")
la_laje.configure(font="-family {Segoe UI} -size 9 -weight bold -slant italic")
la_laje.configure(foreground="#000000")
la_laje.configure(highlightbackground="#d9d9d9")
la_laje.configure(highlightcolor="black")
la_laje.configure(text='''Slab''')

la_tc = tk.Label(Frame2)
la_tc.place(relx=0.029, rely=0.731, height=26, width=42)
la_tc.configure(activebackground="#f9f9f9")
la_tc.configure(activeforeground="black")
la_tc.configure(background="#d9d9d9")
la_tc.configure(disabledforeground="#a3a3a3")
la_tc.configure(foreground="#000000")
la_tc.configure(highlightbackground="#d9d9d9")
la_tc.configure(highlightcolor="black")
la_tc.configure(text='''tc=''')

la_armadura_longitudinal = tk.Label(Frame2)
la_armadura_longitudinal.place(relx=0.029, rely=0.782, height=25, width=104)
la_armadura_longitudinal.configure(activebackground="#f9f9f9")
la_armadura_longitudinal.configure(activeforeground="black")
la_armadura_longitudinal.configure(background="#d9d9d9")
la_armadura_longitudinal.configure(disabledforeground="#a3a3a3")
la_armadura_longitudinal.configure(font="-family {Segoe UI} -size 9 -weight bold -slant italic")
la_armadura_longitudinal.configure(foreground="#000000")
la_armadura_longitudinal.configure(highlightbackground="#d9d9d9")
la_armadura_longitudinal.configure(highlightcolor="black")
la_armadura_longitudinal.configure(text='''Longitudinal Bars''')

la_ass = tk.Label(Frame2)
la_ass.place(relx=0.029, rely=0.821, height=25, width=42)
la_ass.configure(activebackground="#f9f9f9")
la_ass.configure(activeforeground="black")
la_ass.configure(background="#d9d9d9")
la_ass.configure(disabledforeground="#a3a3a3")
la_ass.configure(foreground="#000000")
la_ass.configure(highlightbackground="#d9d9d9")
la_ass.configure(highlightcolor="black")
la_ass.configure(text='''Ass=''')

la_asi = tk.Label(Frame2)
la_asi.place(relx=0.338, rely=0.821, height=25, width=42)
la_asi.configure(activebackground="#f9f9f9")
la_asi.configure(activeforeground="black")
la_asi.configure(background="#d9d9d9")
la_asi.configure(disabledforeground="#a3a3a3")
la_asi.configure(foreground="#000000")
la_asi.configure(highlightbackground="#d9d9d9")
la_asi.configure(highlightcolor="black")
la_asi.configure(text='''Asi=''')

la_cobri = tk.Label(Frame2)
la_cobri.place(relx=0.647, rely=0.821, height=25, width=42)
la_cobri.configure(activebackground="#f9f9f9")
la_cobri.configure(activeforeground="black")
la_cobri.configure(background="#d9d9d9")
la_cobri.configure(disabledforeground="#a3a3a3")
la_cobri.configure(foreground="#000000")
la_cobri.configure(highlightbackground="#d9d9d9")
la_cobri.configure(highlightcolor="black")
la_cobri.configure(text='''c=''')

la_conectores = tk.Label(Frame2)
la_conectores.place(relx=0.029, rely=0.872, height=25, width=35)
la_conectores.configure(activebackground="#f9f9f9")
la_conectores.configure(activeforeground="black")
la_conectores.configure(background="#d9d9d9")
la_conectores.configure(disabledforeground="#a3a3a3")
la_conectores.configure(font="-family {Segoe UI} -size 9 -weight bold -slant italic")
la_conectores.configure(foreground="#000000")
la_conectores.configure(highlightbackground="#d9d9d9")
la_conectores.configure(highlightcolor="black")
la_conectores.configure(text='''Studs''')

la_Ø = tk.Label(Frame2)
la_Ø.place(relx=0.029, rely=0.949, height=26, width=42)
la_Ø.configure(activebackground="#f9f9f9")
la_Ø.configure(activeforeground="black")
la_Ø.configure(background="#d9d9d9")
la_Ø.configure(disabledforeground="#a3a3a3")
la_Ø.configure(foreground="#000000")
la_Ø.configure(highlightbackground="#d9d9d9")
la_Ø.configure(highlightcolor="black")
la_Ø.configure(text='''Ø=''')

la_fucs = tk.Label(Frame2)
la_fucs.place(relx=0.029, rely=0.91, height=26, width=42)
la_fucs.configure(activebackground="#f9f9f9")
la_fucs.configure(activeforeground="black")
la_fucs.configure(background="#d9d9d9")
la_fucs.configure(disabledforeground="#a3a3a3")
la_fucs.configure(foreground="#000000")
la_fucs.configure(highlightbackground="#d9d9d9")
la_fucs.configure(highlightcolor="black")
la_fucs.configure(text='''fucs=''')

la_γc = tk.Label(Frame2)
la_γc.place(relx=0.471, rely=0.91, height=25, width=31)
la_γc.configure(activebackground="#f9f9f9")
la_γc.configure(activeforeground="black")
la_γc.configure(background="#d9d9d9")
la_γc.configure(disabledforeground="#a3a3a3")
la_γc.configure(foreground="#000000")
la_γc.configure(highlightbackground="#d9d9d9")
la_γc.configure(highlightcolor="black")
la_γc.configure(text='''γc=''')

# =============================================================================
# FRAME 3 - BOTÕES
# =============================================================================

Frame3 = tk.Frame(janela_geral)
Frame3.place(relx=0.24, rely=0.013, relheight=0.065, relwidth=0.58)
Frame3.configure(relief='groove')
Frame3.configure(borderwidth="2")
Frame3.configure(relief="groove")
Frame3.configure(background="#d9d9d9")
Frame3.configure(highlightbackground="#d9d9d9")
Frame3.configure(highlightcolor="black")

img_btn_geometria=tk.PhotoImage(file="icones/img_btn_geometria_33x33.png")
img_btn_dimensoes=tk.PhotoImage(file="icones/img_btn_dimensoes_2_33x33.png")
img_btn_diag_carga=tk.PhotoImage(file="icones/img_btn_diag_carga_33x33.png")

btn_geometria = tk.Button(Frame3)
btn_geometria.place(relx=0.006, rely=0.096, height=40, width=40)
btn_geometria.configure(activebackground="#ececec")
btn_geometria.configure(activeforeground="#000000")
btn_geometria.configure(background="#d9d9d9")
btn_geometria.configure(disabledforeground="#a3a3a3")
btn_geometria.configure(foreground="#000000")
btn_geometria.configure(highlightbackground="#d9d9d9")
btn_geometria.configure(highlightcolor="black")
btn_geometria.configure(pady="0")
btn_geometria.configure(image=img_btn_geometria)
btn_geometria.configure(anchor="w")
btn_geometria.configure(command=call_janela_geometria)

btn_dimensoes = tk.Button(Frame3)
btn_dimensoes.place(relx=0.057, rely=0.096, height=40, width=40)
btn_dimensoes.configure(activebackground="#ececec")
btn_dimensoes.configure(activeforeground="#000000")
btn_dimensoes.configure(background="#d9d9d9")
btn_dimensoes.configure(disabledforeground="#a3a3a3")
btn_dimensoes.configure(foreground="#000000")
btn_dimensoes.configure(highlightbackground="#d9d9d9")
btn_dimensoes.configure(highlightcolor="black")
btn_dimensoes.configure(pady="0")
btn_dimensoes.configure(image=img_btn_dimensoes)
btn_dimensoes.configure(anchor="w")
btn_dimensoes.configure(command=n_vaos_func)


font008 = "-family {Cambria Math} -size 20 -slant italic"
font010 = "-family {Candara Light} -size 10 -slant italic"
font009 = "-family {Candara Light} -size 20 -slant italic"

btn_materiais = tk.Button(Frame3)
btn_materiais.place(relx=0.109, rely=0.096, height=40, width=40)
btn_materiais.configure(activebackground="#ececec")
btn_materiais.configure(activeforeground="#000000")
btn_materiais.configure(background="#d9d9d9")
btn_materiais.configure(disabledforeground="#a3a3a3")
btn_materiais.configure(foreground="#000000")
btn_materiais.configure(highlightbackground="#d9d9d9")
btn_materiais.configure(highlightcolor="black")
btn_materiais.configure(pady="0")
btn_materiais.configure(font=font008)
btn_materiais.configure(text='''E''')
btn_materiais.configure(command=janela_mat)


btn_modelo_calculo = tk.Button(Frame3)
btn_modelo_calculo.place(relx=0.161, rely=0.096, height=40, width=40)
btn_modelo_calculo.configure(font=font009)
btn_modelo_calculo.configure(activebackground="#ececec")
btn_modelo_calculo.configure(activeforeground="#000000")
btn_modelo_calculo.configure(background="#d9d9d9")
btn_modelo_calculo.configure(disabledforeground="#a3a3a3")
btn_modelo_calculo.configure(foreground="#000000")
btn_modelo_calculo.configure(highlightbackground="#d9d9d9")
btn_modelo_calculo.configure(highlightcolor="black")
btn_modelo_calculo.configure(pady="0")
btn_modelo_calculo.configure(text='''f''')
btn_modelo_calculo.configure(command=metodo_calculo)


btn_diag_cortante = tk.Button(Frame3)
btn_diag_cortante.place(relx=0.506, rely=0.096, height=40, width=40)
btn_diag_cortante.configure(activebackground="#ececec")
btn_diag_cortante.configure(activeforeground="#000000")
btn_diag_cortante.configure(background="#d9d9d9")
btn_diag_cortante.configure(disabledforeground="#a3a3a3")
btn_diag_cortante.configure(foreground="#000000")
btn_diag_cortante.configure(highlightbackground="#d9d9d9")
btn_diag_cortante.configure(highlightcolor="black")
btn_diag_cortante.configure(pady="0")
btn_diag_cortante.configure(font=font009)
btn_diag_cortante.configure(text='''S''')
#if (norma=="NBR 8800"):
btn_diag_cortante.configure(command=CALCULO_CORTE_NBR)




btn_diag_momento = tk.Button(Frame3)
btn_diag_momento.place(relx=0.557, rely=0.096, height=40, width=40)
btn_diag_momento.configure(activebackground="#ececec")
btn_diag_momento.configure(activeforeground="#000000")
btn_diag_momento.configure(background="#d9d9d9")
btn_diag_momento.configure(disabledforeground="#a3a3a3")
btn_diag_momento.configure(foreground="#000000")
btn_diag_momento.configure(highlightbackground="#d9d9d9")
btn_diag_momento.configure(highlightcolor="black")
btn_diag_momento.configure(pady="0")
btn_diag_momento.configure(font=font009)
btn_diag_momento.configure(text='''M''')
#if (norma=="NBR 8800"):
btn_diag_momento.configure(command=CALCULO_MOMENTO_NBR)

btn_relatorio = tk.Button(Frame3)
btn_relatorio.place(relx=0.859, rely=0.096, height=40, width=120)
btn_relatorio.configure(activebackground="#ececec")
btn_relatorio.configure(activeforeground="#000000")
btn_relatorio.configure(background="#d9d9d9")
btn_relatorio.configure(disabledforeground="#a3a3a3")
btn_relatorio.configure(foreground="#000000")
btn_relatorio.configure(highlightbackground="#d9d9d9")
btn_relatorio.configure(highlightcolor="black")
btn_relatorio.configure(pady="0")
btn_relatorio.configure(font=font009)
btn_relatorio.configure(text='''Report''')
btn_relatorio.configure(command=FUNC_RELATORIO)


# =============================================================================
# FRAME 4- DIAGRAMA SOLICITANTE
# =============================================================================

Frame4_solicitante = tk.Frame(janela_geral)
Frame4_solicitante.place(relx=0.24, rely=0.088, relheight=0.315, relwidth=0.58)
Frame4_solicitante.configure(relief='groove')
Frame4_solicitante.configure(borderwidth="2")
Frame4_solicitante.configure(relief="groove")
Frame4_solicitante.configure(background="#d9d9d9")
Frame4_solicitante.configure(highlightbackground="#d9d9d9")
Frame4_solicitante.configure(highlightcolor="black")

# =============================================================================
# FRAME 5- DIAGRAMA RESISTENTE
# =============================================================================

Frame5_resistente = tk.Frame(janela_geral)
Frame5_resistente.place(relx=0.24, rely=0.413, relheight=0.315, relwidth=0.58)
Frame5_resistente.configure(relief='groove')
Frame5_resistente.configure(borderwidth="2")
Frame5_resistente.configure(relief="groove")
Frame5_resistente.configure(background="#d9d9d9")
Frame5_resistente.configure(highlightbackground="#d9d9d9")
Frame5_resistente.configure(highlightcolor="black")

# =============================================================================
# FRAME 6 - DISRIBUIÇÃO DE CONECTORES
# =============================================================================

Frame6_conectores = tk.Frame(janela_geral)
Frame6_conectores.place(relx=0.24, rely=0.738, relheight=0.25, relwidth=0.58)
Frame6_conectores.configure(relief='groove')
Frame6_conectores.configure(borderwidth="2")
Frame6_conectores.configure(relief="groove")
Frame6_conectores.configure(background="#d9d9d9")
Frame6_conectores.configure(highlightbackground="#d9d9d9")
Frame6_conectores.configure(highlightcolor="black")

# =============================================================================
# MENU
# =============================================================================

def FUNC_JANELA_SOBRE():
    
    janela_sobre= tk.Tk()
    
    _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
    _fgcolor = '#000000'  # X11 color: 'black'
    _compcolor = '#d9d9d9' # X11 color: 'gray85'
    _ana1color = '#d9d9d9' # X11 color: 'gray85'
    _ana2color = '#ececec' # Closest X11 color: 'gray92'
    font10 = "-family {Segoe UI} -size 9 -weight bold"
    font11 = "-family {Segoe UI} -size 10 -weight bold"
    font12 = "-family {Segoe UI} -size 10 -weight bold"
    font13 = "-family {Segoe UI} -size 9"
    font14 = "-family {Segoe UI} -size 10"
    font9 = "-family {Times New Roman} -size 11"
    font7 = "-family {Times New Roman} -size 7"
    font18 = "-family {Segoe UI} -size 16"
    
    janela_sobre.geometry("820x680")
    janela_sobre.minsize(148, 1)
    janela_sobre.maxsize(1924, 1055)
    janela_sobre.resizable(0, 0)
    janela_sobre.title("About COMBEAMS")
    janela_sobre.configure(background="#d9d9d9")  
    
    # Frame3 = tk.Frame(janela_sobre)
    # Frame3.place(relx=0.007, rely=0.013, relheight=0.25, relwidth=0.25)
    # Frame3.configure(relief='groove')
    # Frame3.configure(borderwidth="2")
    # Frame3.configure(relief="groove")
    # Frame3.configure(background="#d9d9d9")
    # Frame3.configure(highlightbackground="#d9d9d9")
    # Frame3.configure(highlightcolor="black")

    # Frame3_ima = tk.Frame(Frame3)
    # Frame3_ima.place(relx=0.015, rely=0.006, relheight=0.971, relwidth=0.971)
    # Frame3_ima.configure(relief='groove')
    # Frame3_ima.configure(borderwidth="2")
    # Frame3_ima.configure(relief="groove")
    # Frame3_ima.configure(background="#d9d9d9")
    # Frame3_ima.configure(highlightbackground="#d9d9d9")
    # Frame3_ima.configure(highlightcolor="black")

    # img=tk.PhotoImage(file="imagens/ufrgs3.png")
    # la_ima_ufrgs_ = tk.Label(Frame3_ima)
    # la_ima_ufrgs_.place(relx=-0.35, rely=-0.35, relheight=1.7, relwidth=1.7)
    # la_ima_ufrgs_.configure(image=img)
    # la_ima_ufrgs_.image=img
    
    la_COMBEAMS = tk.Label(janela_sobre)
    la_COMBEAMS.place(relx=0.427, rely=0.154, height=30, width=120)
    la_COMBEAMS.configure(background="#d9d9d9")
    la_COMBEAMS.configure(disabledforeground="#a3a3a3")
    la_COMBEAMS.configure(font=font18)
    la_COMBEAMS.configure(foreground="#000000")
    la_COMBEAMS.configure(text='''COMBEAMS''')
    
    la_versao = tk.Label(janela_sobre)
    la_versao.place(relx=0.427, rely=0.221, height=30, width=120)
    la_versao.configure(background="#d9d9d9")
    la_versao.configure(disabledforeground="#a3a3a3")
    la_versao.configure(font=font10)
    la_versao.configure(foreground="#000000")
    la_versao.configure(text='''Version 1.00.00''')
    
    la_UFRGS = tk.Label(janela_sobre)
    la_UFRGS.place(relx=0.241, rely=0.445, height=30, width=424)
    la_UFRGS.configure(background="#d9d9d9")
    la_UFRGS.configure(disabledforeground="#a3a3a3")
    la_UFRGS.configure(font=font11)
    la_UFRGS.configure(foreground="#000000")
    la_UFRGS.configure(takefocus="")
    la_UFRGS.configure(text='''Federal University of Rio Grande do Sul - UFRGS''')
    
    la_PPGEC = tk.Label(janela_sobre)
    la_PPGEC.place(relx=0.24, rely=0.475, height=30, width=424)
    la_PPGEC.configure(activebackground="#f9f9f9")
    la_PPGEC.configure(background="#d9d9d9")
    la_PPGEC.configure(disabledforeground="#a3a3a3")
    la_PPGEC.configure(font="-family {Segoe UI} -size 10 -weight bold")
    la_PPGEC.configure(foreground="#000000")
    la_PPGEC.configure(highlightbackground="#d9d9d9")
    la_PPGEC.configure(highlightcolor="black")
    la_PPGEC.configure(takefocus="")
    la_PPGEC.configure(text='''Postgraduate Program in Civil Engineering''')
    
    la_DESENVOLVIDO = tk.Label(janela_sobre)
    la_DESENVOLVIDO.place(relx=0.24, rely=0.301, height=30, width=424)
    la_DESENVOLVIDO.configure(activebackground="#f9f9f9")
    la_DESENVOLVIDO.configure(background="#d9d9d9")
    la_DESENVOLVIDO.configure(disabledforeground="#a3a3a3")
    la_DESENVOLVIDO.configure(font="-family {Segoe UI} -size 10 -weight bold")
    la_DESENVOLVIDO.configure(foreground="#000000")
    la_DESENVOLVIDO.configure(highlightbackground="#d9d9d9")
    la_DESENVOLVIDO.configure(highlightcolor="black")
    la_DESENVOLVIDO.configure(takefocus="")
    la_DESENVOLVIDO.configure(text='''Developed by:''')
    
    la_DESENVOLVIDO = tk.Label(janela_sobre)
    la_DESENVOLVIDO.place(relx=0.24, rely=0.351, height=30, width=424)
    la_DESENVOLVIDO.configure(activebackground="#f9f9f9")
    la_DESENVOLVIDO.configure(background="#d9d9d9")
    la_DESENVOLVIDO.configure(disabledforeground="#a3a3a3")
    la_DESENVOLVIDO.configure(font=font12)
    la_DESENVOLVIDO.configure(foreground="#000000")
    la_DESENVOLVIDO.configure(highlightbackground="#d9d9d9")
    la_DESENVOLVIDO.configure(highlightcolor="black")
    la_DESENVOLVIDO.configure(takefocus="")
    la_DESENVOLVIDO.configure(text='''Jorge Tamayo, Lucas Aguiar, Cristian de Campos,\n Daniel Matos, Inácio Morcsh''')
    
    txt_python = tk.Text(janela_sobre)
    txt_python.place(relx=0.24, rely=0.588, relheight=0.124, relwidth=0.518)
    txt_python.configure(background="#d9d9d9")
    txt_python.configure(blockcursor="1")
    txt_python.configure(borderwidth="0")
    txt_python.configure(font=font11)
    txt_python.configure(foreground="black")
    txt_python.configure(highlightbackground="#d9d9d9")
    txt_python.configure(highlightcolor="black")
    txt_python.configure(insertbackground="black")
    txt_python.configure(selectbackground="#c4c4c4")
    txt_python.configure(selectforeground="black")
    txt_python.configure(takefocus="0")
    txt_python.configure(wrap="word")
    txt_python.insert(INSERT, "This software was produced using the Python language in version 3.7.3 \nThe graphical user interface was created using the Tkinter library")
    txt_python.tag_add("here", "0.0", "4.20")
    txt_python.tag_config("here", justify="center")
    
    # Other required packages: pandas, numpy, xlsxwriter, matplotlib, sys
    
    txt_responsabilidade = tk.Text(janela_sobre)
    txt_responsabilidade.place(relx=0.104, rely=0.735, relheight=0.175, relwidth=0.794)
    txt_responsabilidade.configure(background="#d9d9d9")
    txt_responsabilidade.configure(blockcursor="1")
    txt_responsabilidade.configure(borderwidth="0")
    txt_responsabilidade.configure(font=font13)
    txt_responsabilidade.configure(foreground="black")
    txt_responsabilidade.configure(highlightbackground="#d9d9d9")
    txt_responsabilidade.configure(highlightcolor="black")
    txt_responsabilidade.configure(insertbackground="black")
    txt_responsabilidade.configure(selectbackground="#c4c4c4")
    txt_responsabilidade.configure(selectforeground="black")
    txt_responsabilidade.configure(takefocus="0")
    txt_responsabilidade.configure(wrap="word")
    txt_responsabilidade.insert(INSERT, "\nBSD 3-Clause License \nCopyright (c) 2024, Lucas Aguiar \nRedistribution and use in source and binary forms, with or without modification, are permitted provided that the following conditions are met: \n1. Redistributions of source code must retain the above copyright notice, this list of conditions and the following disclaimer. \n2. Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the following disclaimer in the documentation and/or other materials provided with the distribution. \n3. Neither the name of the copyright holder nor the names of its contributors may be used to endorse or promote products derived from this software without specific prior written permission.")
    txt_responsabilidade.tag_add("here", "0.0", "7.6")
    txt_responsabilidade.tag_config("here", justify="left")
    
    def fechar_janela():
        janela_sobre.destroy()
    
    btn_fechar_sobre = tk.Button(janela_sobre, command=fechar_janela)
    btn_fechar_sobre.place(relx=0.463, rely=0.941, height=30, width=60)
    btn_fechar_sobre.configure(activebackground="#ececec")
    btn_fechar_sobre.configure(activeforeground="#000000")
    btn_fechar_sobre.configure(background="#d9d9d9")
    btn_fechar_sobre.configure(disabledforeground="#a3a3a3")
    btn_fechar_sobre.configure(foreground="#000000")
    btn_fechar_sobre.configure(highlightbackground="#d9d9d9")
    btn_fechar_sobre.configure(highlightcolor="black")
    btn_fechar_sobre.configure(pady="0")
    btn_fechar_sobre.configure(takefocus="0")
    btn_fechar_sobre.configure(text='''Close''')
    
    janela_sobre.mainloop()


def FUNC_JANELA_HELP():
    
    janela_sobre= tk.Tk()
    
    _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
    _fgcolor = '#000000'  # X11 color: 'black'
    _compcolor = '#d9d9d9' # X11 color: 'gray85'
    _ana1color = '#d9d9d9' # X11 color: 'gray85'
    _ana2color = '#ececec' # Closest X11 color: 'gray92'
    font10 = "-family {Segoe UI} -size 9 -weight bold"
    font11 = "-family {Segoe UI} -size 10 -weight bold"
    font12 = "-family {Segoe UI} -size 10 -weight bold"
    font13 = "-family {Segoe UI} -size 9"
    font14 = "-family {Segoe UI} -size 10"
    font9 = "-family {Times New Roman} -size 11"
    font7 = "-family {Times New Roman} -size 7"
    
    janela_sobre.geometry("820x680")
    janela_sobre.minsize(148, 1)
    janela_sobre.maxsize(500, 150)
    janela_sobre.resizable(0, 0)
    janela_sobre.title("HELP")
    janela_sobre.configure(background="#d9d9d9")  
    
    txt_responsabilidade = tk.Text(janela_sobre)
    txt_responsabilidade.place(relx=0.0, rely=0.2, relheight=0.8, relwidth=1)
    txt_responsabilidade.configure(background="#d9d9d9")
    txt_responsabilidade.configure(blockcursor="1")
    txt_responsabilidade.configure(borderwidth="0")
    txt_responsabilidade.configure(font=font14)
    txt_responsabilidade.configure(foreground="black")
    txt_responsabilidade.configure(highlightbackground="#d9d9d9")
    txt_responsabilidade.configure(highlightcolor="black")
    txt_responsabilidade.configure(insertbackground="black")
    txt_responsabilidade.configure(selectbackground="#c4c4c4")
    txt_responsabilidade.configure(selectforeground="black")
    txt_responsabilidade.configure(takefocus="0")
    txt_responsabilidade.configure(wrap="word")
    txt_responsabilidade.insert(INSERT, "Instructions and use of this program can be found in the following references:\nhttps://github.com/Lucassaaguiar/COMBEAMS")
    txt_responsabilidade.tag_add("here", "0.0", "7.6")
    txt_responsabilidade.tag_config("here", justify="center")
    
    def fechar_janela():
        janela_sobre.destroy()
    
    btn_fechar_sobre = tk.Button(janela_sobre, command=fechar_janela)
    btn_fechar_sobre.place(relx=0.45, rely=0.65, height=30, width=60)
    btn_fechar_sobre.configure(activebackground="#ececec")
    btn_fechar_sobre.configure(activeforeground="#000000")
    btn_fechar_sobre.configure(background="#d9d9d9")
    btn_fechar_sobre.configure(disabledforeground="#a3a3a3")
    btn_fechar_sobre.configure(foreground="#000000")
    btn_fechar_sobre.configure(highlightbackground="#d9d9d9")
    btn_fechar_sobre.configure(highlightcolor="black")
    btn_fechar_sobre.configure(pady="0")
    btn_fechar_sobre.configure(takefocus="0")
    btn_fechar_sobre.configure(text='''Close''')

    janela_sobre.mainloop()

#   CRIANDO OS MENUS
menu_geral   = Menu(janela_geral)
menu_arquivo = Menu(menu_geral, tearoff=0)
menu_ajuda   = Menu(menu_geral, tearoff=0)

#  CRIANDO O MENU ARQUIVO
menu_arquivo.add_command(label="New",command=reset_program)
menu_arquivo.add_command(label="Open",command=janela_nome)
menu_arquivo.add_command(label="Save",command=FUNC_RELATORIO)
menu_arquivo.add_separator()
menu_arquivo.add_command(label="Close",command=close)
menu_geral.add_cascade(label="File",menu=menu_arquivo)

#  CRIANDO O MENU AJUDA
menu_geral.add_cascade(label="Help",command=FUNC_JANELA_HELP)

#  CRIANDO O MENU SOBRE
menu_geral.add_cascade(label="About",command=FUNC_JANELA_SOBRE)






janela_geral.config(menu=menu_geral)



#=============================================================================#
janela_geral.mainloop()




# =============================================================================
# # =============================================================================
# # # FIM FIM
# # =============================================================================
# =============================================================================

# =============================================================================



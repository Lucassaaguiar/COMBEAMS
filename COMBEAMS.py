import tkinter as tk
import tkinter.font as font
import tkinter.ttk as ttk
import pandas as pd
import numpy as np
import xlsxwriter as sl
import subprocess
import sys

from tkinter import *

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure

data = pd.read_excel(r"DOCS/tabela_perfis.xlsx")
dada_numérico = data.values
dados = dada_numérico[2:120, 2:24]

# =============================================================================
# =============================================================================
# # # =========================================================================
# # # #       ################# INITIAL CONFGURATIONS  ########################
# # # =========================================================================
# =============================================================================
# =============================================================================

# CONFIG FUNCTIONS

def Config_frame(var, relx, rely, height, width, ft, text):
    var.place(relx = relx, rely = rely, height = height, width = width)
    var.configure(activebackground="#f9f9f9")
    var.configure(activeforeground="black")
    var.configure(background="#d9d9d9")
    var.configure(disabledforeground="#a3a3a3")
    var.configure(font=ft)
    var.configure(foreground="#000000")
    var.configure(highlightbackground="#d9d9d9")
    var.configure(justify="left")
    var.configure(highlightcolor="black")
    var.configure(text=text)
    
def Config_box(box, relx, rely, height, relwidth, ft):   
    box.place(relx=relx, rely=rely, height=height, relwidth=relwidth)
    box.configure(background="white")
    box.configure(disabledforeground="#a3a3a3")
    box.configure(font=ft)
    box.configure(foreground="#000000")
    box.configure(highlightbackground="#d9d9d9")
    box.configure(highlightcolor="black")
    box.configure(insertbackground="black")
    box.configure(selectbackground="#c4c4c4")
    box.configure(selectforeground="black")
    
def Config_entry(entry, relx, rely, height, relwidth):
    entry.place(relx=relx, rely=rely, height=height, relwidth=relwidth)
    entry.configure(background="white")
    entry.configure(disabledforeground="#a3a3a3")
    entry.configure(font="TkFixedFont")
    entry.configure(foreground="#000000")
    entry.configure(highlightbackground="#d9d9d9")
    entry.configure(highlightcolor="black")
    entry.configure(insertbackground="black")
    entry.configure(selectbackground="#c4c4c4")
    entry.configure(selectforeground="black")
    
def Config_buttom(btn, relx, rely, height, width):
    btn.place(relx=relx, rely=rely, height=height, width= width)
    btn.configure(activebackground="#ececec")
    btn.configure(activeforeground="#000000")
    btn.configure(background="#d9d9d9")
    btn.configure(disabledforeground="#a3a3a3")
    btn.configure(foreground="#000000")
    btn.configure(highlightbackground="#d9d9d9")
    btn.configure(highlightcolor="black")
    
# FONT STYLES AND COLORS CONFIG

tk_font     = "TkFixedFont"
S_font9     = "-family {Segoe UI} -size 9"
Sb_font9    = "-family {Segoe UI} -size 9 -weight bold"
Sbi_font9   = "-family {Segoe UI} -size 9 -weight bold -slant italic" ""
S_font10    = "-family {Segoe UI} -size 10"
Sb_font10   = "-family {Segoe UI} -size 10 -weight bold"
Sbi_font10  = "-family {Segoe UI} -size 10 -weight bold -slant italic"

Sb_font18   = "-family {Segoe UI} -size 18 -weight bold"

font008 = "-family {Cambria Math} -size 20 -slant italic"
font010 = "-family {Candara Light} -size 10 -slant italic"
font009 = "-family {Candara Light} -size 20 -slant italic"

_bgcolor = "#d9d9d9"    # X11 color: 'gray85'
_fgcolor = "#000000"    # X11 color: 'black'
_compcolor = "#d9d9d9"  # X11 color: 'gray85'
_ana1color = "#d9d9d9"  # X11 color: 'gray85'
_ana2color = "#ececec"  # Closest X11 color: 'gray92'

# =============================================================================
# =============================================================================
# # # =========================================================================
# # # #       ############# WRITE THE RIGHT FRAME ##################
# # # =========================================================================
# =============================================================================
# =============================================================================

def window_error_func():
    global texto_erro, texto_erro1, texto_erro2, texto_erro3, texto_erro4, texto_erro5, texto_erro6

    def destroy_window_error():
        janela_erro.destroy()

    janela_erro = tk.Tk()

    janela_erro.geometry("500x200+500+300")
    janela_erro.minsize(148, 1)
    janela_erro.maxsize(1924, 1055)
    janela_erro.resizable(1, 1)
    janela_erro.title("Error")
    janela_erro.iconbitmap("icones/geral.ico")
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
    btn_sair_janela_erro.configure(font="-family {Segoe UI} -size 12")
    btn_sair_janela_erro.configure(foreground="#000000")
    btn_sair_janela_erro.configure(highlightbackground="#d9d9d9")
    btn_sair_janela_erro.configure(highlightcolor="black")
    btn_sair_janela_erro.configure(pady="0")
    btn_sair_janela_erro.configure(text="""Exit""")
    btn_sair_janela_erro.configure(command=destroy_window_error)

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
        if n > 0:  
            txt_erro.insert(END, "%d - " % (n))  
        txt_erro.insert(END, texto_erro[n])

    janela_erro.mainloop()


def write_frame_section():
    # =============================================================================
    # FRAME 1 - SECTION
    # =============================================================================
    _x_ = "<x<"

    Frame1 = tk.Frame(janela_geral)
    Frame1.place(relx=0.827, rely=0.013, relheight=0.975, relwidth=0.167)
    Frame1.configure(relief="groove")
    Frame1.configure(borderwidth="2")
    Frame1.configure(relief="groove")
    Frame1.configure(background="#d9d9d9")
    Frame1.configure(highlightbackground="#d9d9d9")
    Frame1.configure(highlightcolor="black")

    #       FRAME SECTION 01

    msd_max_1 = round(-1 * MM[int(x_VV0[0] * 100)], 2)
    vsd_max_1 = round(VV[0], 2)

    Frame1_1 = tk.Frame(Frame1)
    Frame1_1.place(relx=0.02, rely=0.006, relheight=0.191, relwidth=0.96)
    Frame1_1.configure(relief="groove")
    Frame1_1.configure(borderwidth="2")
    Frame1_1.configure(relief="groove")
    Frame1_1.configure(background="#d9d9d9")
    Frame1_1.configure(highlightbackground="#d9d9d9")
    Frame1_1.configure(highlightcolor="black")

    la_trecho_01 = tk.Label(Frame1_1)
    Config_frame(la_trecho_01, relx=0.046, rely=0.067, height=22, width=103,
                 ft=Sb_font10, text="""Region 01""")

    la_trecho_01_posicao = tk.Label(Frame1_1)
    Config_frame(la_trecho_01_posicao, relx=0.504, rely=0.054, height=22,
                 width=83, ft=Sb_font10, text=(x_MM0[0], _x_, x_MM0[1]))

    la_trecho_01_n_con = tk.Label(Frame1_1)
    Config_frame(la_trecho_01_n_con, relx=0.042, rely=0.228, height=22,
                 width=121, ft=S_font9, text="""Number of Studs =""")

    la_trecho_01_VA_n_con = tk.Label(Frame1_1)
    Config_frame(la_trecho_01_VA_n_con, relx=0.546, rely=0.228, height=22,
                 width=46, ft=S_font9, text=n_con[0])

    la_trecho_01_esp = tk.Label(Frame1_1)
    Config_frame(la_trecho_01_esp, relx=0.042, rely=0.396, height=22, width=75,
                 ft=S_font9, text="""Spacing =""")

    la_trecho_01_VA_esp = tk.Label(Frame1_1)
    Config_frame(la_trecho_01_VA_esp, relx=0.546, rely=0.396, height=22,
                 width=46, ft=S_font9, text=round(espac[0], 3))

    la_trecho_01_mrd = tk.Label(Frame1_1)
    Config_frame(la_trecho_01_mrd, relx=0.083, rely=0.564, height=22, width=48,
                 ft=S_font9, text="""Mᵤ =""")

    la_trecho_01_VA_mrd = tk.Label(Frame1_1)
    Config_frame(la_trecho_01_VA_mrd, relx=0.279, rely=0.564, height=22,
                 width=58, ft=S_font9, text=round(Mrd[0], 1))

    la_trecho_01_msd = tk.Label(Frame1_1)
    Config_frame(la_trecho_01_msd, relx=0.508, rely=0.564, height=22, width=48,
                 ft=S_font9, text="""Mᵣ =""")

    la_trecho_01_VA_msd = tk.Label(Frame1_1)
    Config_frame(la_trecho_01_VA_msd, relx=0.696, rely=0.564, height=22,
                 width=46, ft=S_font9, text=msd_max_1)

    la_trecho_01_vrd = tk.Label(Frame1_1)
    Config_frame(la_trecho_01_vrd, relx=0.092, rely=0.732, height=22, width=41,
                 ft=S_font9, text="""Vᵤ =""")

    la_trecho_01_vsd = tk.Label(Frame1_1)
    Config_frame(la_trecho_01_vsd, relx=0.533, rely=0.738, height=22, width=41,
                 ft=S_font9, text="""Vᵣ =""")

    la_trecho_01_VA_vrd = tk.Label(Frame1_1)
    Config_frame(la_trecho_01_VA_vrd, relx=0.279, rely=0.732, height=22,
                 width=54, ft=S_font9, text=round(Vrd, 1))

    la_trecho_01_VA_vsd = tk.Label(Frame1_1)
    Config_frame(la_trecho_01_VA_vsd, relx=0.696, rely=0.732, height=22,
                 width=46, ft=S_font9, text=vsd_max_1)

    #       FRAME SECTION 02
    if trechos >= 2:
        msd_max_2 = -round(MM[int(L[1] * 100)], 2)
        msd_max_3 = -round(MM[int(x_VV0[1] * 100)], 2)

        vsd_max_2 = round(
            max(abs((VV[int(L[1] * 100 - 2): int(L[1] * 100 + 1)]))), 2)
        vsd_max_3 = round(
            max(abs(VV[int(x_MM0[2] * 100): int(x_MM0[3] * 100)])), 2)

        Frame1_2 = tk.Frame(Frame1)
        Frame1_2.place(relx=0.02, rely=0.205, relheight=0.191, relwidth=0.96)
        Frame1_2.configure(relief="groove")
        Frame1_2.configure(borderwidth="2")
        Frame1_2.configure(relief="groove")
        Frame1_2.configure(background="#d9d9d9")
        Frame1_2.configure(highlightbackground="#d9d9d9")
        Frame1_2.configure(highlightcolor="black")

        latrecho_2 = tk.Label(Frame1_2)
        Config_frame(latrecho_2, relx=0.042, rely=0.067, height=22, width=103,
                     ft=Sb_font10, text="""Region 02""")

        la_trecho_02_posicao = tk.Label(Frame1_2)
        Config_frame(la_trecho_02_posicao, relx=0.504, rely=0.054, height=22,
                     width=83, ft=Sb_font10, text=(x_MM0[1], _x_, x_MM0[2]))

        la_trecho_02_n_con = tk.Label(Frame1_2)
        Config_frame(la_trecho_02_n_con, relx=0.042, rely=0.228, height=22,
                     width=121, ft=S_font9, text="""Number of Studs=""")

        la_trecho_02_VA_n_con = tk.Label(Frame1_2)
        Config_frame(la_trecho_02_VA_n_con, relx=0.546, rely=0.228, height=22,
                     width=46, ft=S_font9, text=n_con[1])

        la_trecho_02_esp = tk.Label(Frame1_2)
        Config_frame(la_trecho_02_esp, relx=0.042, rely=0.396, height=22,
                     width=75, ft=S_font9, text="""Spacing =""")

        la_trecho_02_VA_esp = tk.Label(Frame1_2)
        Config_frame(la_trecho_02_VA_esp, relx=0.546, rely=0.396, height=22,
                     width=46, ft=S_font9, text=round(espac[1], 3))

        la_trecho_02_mrd = tk.Label(Frame1_2)
        Config_frame(la_trecho_02_mrd, relx=0.083, rely=0.56, height=22,
                     width=48, ft=S_font9, text="""Mᵤ =""")

        la_trecho_02_VA_mrd = tk.Label(Frame1_2)
        Config_frame(la_trecho_02_VA_mrd, relx=0.279, rely=0.564, height=22,
                     width=58, ft=S_font9, text=round(Mrd[1], 1))

        la_trecho_02_msd = tk.Label(Frame1_2)
        Config_frame(la_trecho_02_msd, relx=0.508, rely=0.564, height=22,
                     width=48, ft=S_font9, text="""Mᵣ =""")

        la_trecho_02_VA_msd = tk.Label(Frame1_2)
        Config_frame(la_trecho_02_VA_msd, relx=0.696, rely=0.564, height=22,
                     width=46, ft=S_font9, text=msd_max_2)

        la_trecho_02_vrd = tk.Label(Frame1_2)
        Config_frame(la_trecho_02_vrd, relx=0.092, rely=0.732, height=22,
                     width=41, ft=S_font9, text="""Vᵤ =""")

        la_trecho_02_vsd = tk.Label(Frame1_2)
        Config_frame(la_trecho_02_vsd, relx=0.533, rely=0.738, height=22,
                     width=41, ft=S_font9, text="""Vᵣ =""")

        la_trecho_02_VA_vrd = tk.Label(Frame1_2)
        Config_frame(la_trecho_02_VA_vrd, relx=0.279, rely=0.732, height=22,
                     width=54, ft=S_font9, text=round(Vrd, 1))

        la_trecho_02_VA_vsd = tk.Label(Frame1_2)
        Config_frame(la_trecho_02_VA_vsd, relx=0.696, rely=0.732, height=22,
                     width=46, ft=S_font9, text=vsd_max_2)

        #       FRAME SECTION 03

        Frame1_3 = tk.Frame(Frame1)
        Frame1_3.place(relx=0.02, rely=0.404, relheight=0.191, relwidth=0.96)
        Frame1_3.configure(relief="groove")
        Frame1_3.configure(borderwidth="2")
        Frame1_3.configure(relief="groove")
        Frame1_3.configure(background="#d9d9d9")
        Frame1_3.configure(highlightbackground="#d9d9d9")
        Frame1_3.configure(highlightcolor="black")

        latrecho_3 = tk.Label(Frame1_3)
        Config_frame(latrecho_3, relx=0.046, rely=0.067, height=22, width=103,
                     ft=Sb_font10, text="""Region 03""")

        la_trecho_03_posicao = tk.Label(Frame1_3)
        Config_frame(la_trecho_03_posicao, relx=0.504, rely=0.054, height=22,
                     width=83, ft=Sb_font10, text=(x_MM0[2], _x_, x_MM0[3]))

        la_trecho_03_n_con = tk.Label(Frame1_3)
        Config_frame(la_trecho_03_n_con, relx=0.042, rely=0.228, height=22,
                     width=121, ft=S_font9, text="""Number of Studs =""")

        la_trecho_03_VA_n_con = tk.Label(Frame1_3)
        Config_frame(la_trecho_03_VA_n_con, relx=0.546, rely=0.228, height=22,
                     width=46, ft=S_font9, text=n_con[2])

        la_trecho_03_esp = tk.Label(Frame1_3)
        Config_frame(la_trecho_03_esp, relx=0.042, rely=0.396, height=22,
                     width=75, ft=S_font9, text="""Spacing =""")

        la_trecho_03_VA_esp = tk.Label(Frame1_3)
        Config_frame(la_trecho_03_VA_esp, relx=0.546, rely=0.396, height=22,
                     width=46, ft=S_font9, text=round(espac[2], 3))

        la_trecho_03_mrd = tk.Label(Frame1_3)
        Config_frame(la_trecho_03_mrd, relx=0.083, rely=0.56, height=22,
                     width=48, ft=S_font9, text="""Mᵤ =""")

        la_trecho_03_VA_mrd = tk.Label(Frame1_3)
        Config_frame(la_trecho_03_VA_mrd, relx=0.279, rely=0.564, height=22,
                     width=58, ft=S_font9, text=round(Mrd[2], 1))

        la_trecho_03_msd = tk.Label(Frame1_3)
        Config_frame(la_trecho_03_msd, relx=0.508, rely=0.564, height=22,
                     width=48, ft=S_font9, text="""Mᵣ =""")

        la_trecho_03_VA_msd = tk.Label(Frame1_3)
        Config_frame(la_trecho_03_VA_msd, relx=0.696, rely=0.564, height=22,
                     width=46, ft=S_font9, text=msd_max_3)

        la_trecho_03_vrd = tk.Label(Frame1_3)
        Config_frame(la_trecho_03_vrd, relx=0.092, rely=0.732, height=22,
                     width=41, ft=S_font9, text="""Vᵤ =""")

        la_trecho_03_vsd = tk.Label(Frame1_3)
        Config_frame(la_trecho_03_vsd, relx=0.533, rely=0.738, height=22,
                     width=41, ft=S_font9, text="""Vᵣ =""")

        la_trecho_03_VA_vrd = tk.Label(Frame1_3)
        Config_frame(la_trecho_03_VA_vrd, relx=0.279, rely=0.732, height=22,
                     width=54, ft=S_font9, text=round(Vrd, 1))

        la_trecho_03_VA_vsd = tk.Label(Frame1_3)
        Config_frame(la_trecho_03_VA_vsd, relx=0.696, rely=0.732, height=22,
                     width=46, ft=S_font9, text=vsd_max_3)

    if trechos >= 3:
        msd_max_4 = -round(MM[int(L[2] * 100)], 2)
        msd_max_5 = -round(MM[int(x_VV0[2] * 100)], 2)

        vsd_max_4 = round(
            max(abs((VV[int(L[2] * 100 - 2): int(L[2] * 100 + 1)]))), 2)
        vsd_max_5 = round(
            max(abs(VV[int(x_MM0[4] * 100): int(x_MM0[5] * 100)])), 2)

        #       FRAME SECTION 04

        Frame1_4 = tk.Frame(Frame1)
        Frame1_4.place(relx=0.02, rely=0.603, relheight=0.191, relwidth=0.96)
        Frame1_4.configure(relief="groove")
        Frame1_4.configure(borderwidth="2")
        Frame1_4.configure(relief="groove")
        Frame1_4.configure(background="#d9d9d9")
        Frame1_4.configure(highlightbackground="#d9d9d9")
        Frame1_4.configure(highlightcolor="black")

        latrecho_4 = tk.Label(Frame1_4)
        Config_frame(latrecho_4, relx=0.046, rely=0.067, height=22, width=103,
                     ft=Sb_font10, text="""Region 04""")

        la_trecho_04_posicao = tk.Label(Frame1_4)
        Config_frame(la_trecho_04_posicao, relx=0.504, rely=0.054, height=22,
                     width=83, ft=Sb_font10, text=(x_MM0[3], _x_, x_MM0[4]))

        la_trecho_04_n_con = tk.Label(Frame1_4)
        Config_frame(la_trecho_04_n_con, relx=0.042, rely=0.228, height=22,
                     width=121, ft=S_font9, text="""Number of Studs=""")

        la_trecho_04_VA_n_con = tk.Label(Frame1_4)
        Config_frame(la_trecho_04_VA_n_con, relx=0.546, rely=0.228, height=22,
                     width=46, ft=S_font9, text=n_con[3])

        la_trecho_04_esp = tk.Label(Frame1_4)
        Config_frame(la_trecho_04_esp, relx=0.042, rely=0.396, height=22,
                     width=75, ft=S_font9, text="""Spacing=""")

        la_trecho_04_VA_esp = tk.Label(Frame1_4)
        Config_frame(la_trecho_04_VA_esp, relx=0.546, rely=0.396, height=22,
                     width=46, ft=S_font9, text=round(espac[3], 3))

        la_trecho_04_mrd = tk.Label(Frame1_4)
        Config_frame(la_trecho_04_mrd, relx=0.083, rely=0.56, height=22,
                     width=48, ft=S_font9, text="""Mᵤ =""")

        la_trecho_04_VA_mrd = tk.Label(Frame1_4)
        Config_frame(la_trecho_04_VA_mrd, relx=0.279, rely=0.564, height=22,
                     width=58, ft=S_font9, text=round(Mrd[3], 1))

        la_trecho_04_msd = tk.Label(Frame1_4)
        Config_frame(la_trecho_04_msd, relx=0.508, rely=0.564, height=22,
                     width=48, ft=S_font9, text="""Mᵣ =""")

        la_trecho_04_VA_msd = tk.Label(Frame1_4)
        Config_frame(la_trecho_04_VA_msd, relx=0.696, rely=0.564, height=22,
                     width=48, ft=S_font9, text=msd_max_4)

        la_trecho_04_vrd = tk.Label(Frame1_4)
        Config_frame(la_trecho_04_vrd, relx=0.092, rely=0.732, height=22,
                     width=48, ft=S_font9, text="""Vᵤ =""")

        la_trecho_04_vsd = tk.Label(Frame1_4)
        Config_frame(la_trecho_04_vsd, relx=0.533, rely=0.738, height=22,
                     width=48, ft=S_font9, text="""Vᵣ =""")

        la_trecho_04_VA_vrd = tk.Label(Frame1_4)
        Config_frame(la_trecho_04_VA_vrd, relx=0.279, rely=0.732, height=22,
                     width=48, ft=S_font9, text=round(Vrd, 1))

        la_trecho_04_VA_vsd = tk.Label(Frame1_4)
        Config_frame(la_trecho_04_VA_vsd, relx=0.696, rely=0.732, height=22,
                     width=48, ft=S_font9, text=vsd_max_4)

        #       FRAME SECTION 05

        Frame1_5 = tk.Frame(Frame1)
        Frame1_5.place(relx=0.02, rely=0.801, relheight=0.191, relwidth=0.96)
        Frame1_5.configure(relief="groove")
        Frame1_5.configure(borderwidth="2")
        Frame1_5.configure(relief="groove")
        Frame1_5.configure(background="#d9d9d9")
        Frame1_5.configure(highlightbackground="#d9d9d9")
        Frame1_5.configure(highlightcolor="black")

        latrecho_5 = tk.Label(Frame1_5)
        Config_frame(latrecho_5, relx=0.046, rely=0.067, height=22, width=103,
                     ft=Sb_font10, text="""Region 05""")

        la_trecho_05_posicao = tk.Label(Frame1_5)
        Config_frame(la_trecho_05_posicao, relx=0.504, rely=0.054, height=22,
                     width=83, ft=Sb_font10, text=(x_MM0[4], _x_, x_MM0[5]))

        la_trecho_05_n_con = tk.Label(Frame1_5)
        Config_frame(la_trecho_05_n_con, relx=0.042, rely=0.228, height=22,
                     width=121, ft=S_font9, text="""Number of Studs=""")

        la_trecho_05_VA_n_con = tk.Label(Frame1_5)
        Config_frame(la_trecho_05_VA_n_con, relx=0.546, rely=0.228, height=22,
                     width=46, ft=S_font9, text=n_con[4])

        la_trecho_05_esp = tk.Label(Frame1_5)
        Config_frame(la_trecho_05_esp, relx=0.042, rely=0.396, height=22,
                     width=75, ft=S_font9, text="""Spacing =""")

        la_trecho_05_VA_esp = tk.Label(Frame1_5)
        Config_frame(la_trecho_05_VA_esp, relx=0.546, rely=0.396, height=22,
                     width=46, ft=S_font9, text=round(espac[4], 3))

        la_trecho_05_mrd = tk.Label(Frame1_5)
        Config_frame(la_trecho_05_mrd, relx=0.083, rely=0.56, height=22,
                     width=48, ft=S_font9, text="""Mᵤ =""")

        la_trecho_05_VA_mrd = tk.Label(Frame1_5)
        Config_frame(la_trecho_05_VA_mrd, relx=0.279, rely=0.564, height=22,
                     width=58, ft=S_font9, text=round(Mrd[4], 1))

        la_trecho_05_msd = tk.Label(Frame1_5)
        Config_frame(la_trecho_05_msd, relx=0.508, rely=0.564, height=22,
                     width=48, ft=S_font9, text="""Mᵣ =""")

        la_trecho_05_VA_msd = tk.Label(Frame1_5)
        Config_frame(la_trecho_05_VA_msd, relx=0.696, rely=0.564, height=22,
                     width=48, ft=S_font9, text=msd_max_5)

        la_trecho_05_vrd = tk.Label(Frame1_5)
        Config_frame(la_trecho_05_vrd, relx=0.092, rely=0.732, height=22,
                     width=48, ft=S_font9, text="""Vᵤ =""")

        la_trecho_05_vsd = tk.Label(Frame1_5)
        Config_frame(la_trecho_05_vsd, relx=0.533, rely=0.738, height=22,
                     width=48, ft=S_font9, text="""Vᵣ =""")

        la_trecho_05_VA_vrd = tk.Label(Frame1_5)
        Config_frame(la_trecho_05_VA_vrd, relx=0.279, rely=0.732, height=22,
                     width=48, ft=S_font9, text=round(Vrd, 1))

        la_trecho_05_VA_vsd = tk.Label(Frame1_5)
        Config_frame(la_trecho_05_VA_vsd, relx=0.696, rely=0.732, height=22,
                     width=48, ft=S_font9, text=vsd_max_5)

# =============================================================================
# =============================================================================
# # # =========================================================================
# # # # ############   FUNCTIONS THAT CREATE THE PLOTTING   ###################
# # # =========================================================================
# =============================================================================
# =============================================================================

# =============================================================================
# FUNCTION THAT CREATES THE BEAMS AND SUPPORTS
# =============================================================================

def creat_beam_support(fig):

    v = np.zeros(int(sum(L) / 0.01))  # VERTICAL VECTOR FOR D-BEAM LINE
    h = np.arange(0, sum(L), 0.01)    # HORIZONTAL VECTOR FOR BEAM LINE
    # CREATING A VARIABLE WITH THE DATA FROM THIS GRAPH
    viga = fig.add_subplot(111)
    viga.plot(h, v, "black", linewidth=2)  # PLOTTING THE BEAM DATA

    # CREATES SUPPORTS
    aux = 0
    for kk in range(trechos + 1):
        apoio_base = 0
        apoio_lat_esq = 0
        apoio_lat_dir = 0
        apoiox = 0
        apoioy = 0

        apoiox = np.arange((aux - 0.2), (aux + 0.2), 0.01)
        apoioy = np.zeros(len(apoiox)) - 0.28

        # apoio_base=fig.add_subplot(111)
        viga.plot(apoiox, apoioy, "green", linewidth=1.6)

        apoiox = np.arange((aux - 0.2), (aux), 0.01)
        apoioy = np.linspace(-0.27, -0.03, len(apoiox))

        # apoio_lat_esq=fig.add_subplot(111)
        viga.plot(apoiox, apoioy, "green", linewidth=1.6)

        apoiox = np.arange(aux, aux + 0.2, 0.01)
        apoioy = np.linspace(-0.03, -0.27, len(apoiox))

        # apoio_lat_dir=fig.add_subplot(111)
        viga.plot(apoiox, apoioy, "green", linewidth=1.6)

        if kk < trechos:
            aux = aux + L[kk]

    # REMOVING THE FRAME
    viga.spines["right"].set_color("white")
    viga.spines["top"].set_color("white")
    viga.spines["left"].set_color("white")
    viga.spines["bottom"].set_color("white")

    # SETTING THE HEIGHT OF THE GRAPH WINDOW
    viga.axis([-1, sum(L) + 1, -2.5, 2.5])

    # DISCONNECTING THE AXES

    fig.gca().axes.get_yaxis().set_visible(False)  # REMOVE AXES FROM THE GRAPH
    fig.gca().axes.get_xaxis().set_visible(False)

    return viga

# =============================================================================#

# =============================================================================
# PLOTTING OF THE SHEAR GRAPH
# =============================================================================

def shear_acting_graph():
    global fig

    Frame4_solicitante = tk.Frame(janela_geral)
    Frame4_solicitante.place(
        relx=0.24,
        rely=0.088,
        relheight=0.315,
        relwidth=0.58)
    Frame4_solicitante.configure(relief="groove")
    Frame4_solicitante.configure(borderwidth="2")
    Frame4_solicitante.configure(relief="groove")
    Frame4_solicitante.configure(background="#d9d9d9")
    Frame4_solicitante.configure(highlightbackground="#d9d9d9")
    Frame4_solicitante.configure(highlightcolor="black")

    fig = Figure(figsize=(1, 1), dpi=100)  # CREATE THE FIGURE

    corte = creat_beam_support(fig)

    #    SET SCREEN RATIO
    max_abs = max(np.abs(VV))
    rel_tela = max_abs / 2

    #    PLOTTING THE CUTTING GRAPH

    corte.plot(xx, VV / rel_tela, "blue", linewidth=0.5)

    #    CREATING THE INITIAL AND FINAL LINES OF THE DIAGRAM

    # VERTICAL VECTOR FOR THE STRAIGHT LINE OF SHEAR SUPPORT 1
    v = np.arange(
        0, VV[0] / rel_tela, 0.01
    )  
    
    # HORIZONTAL VECTOR FOR THE STRAIGHT LINE OF SHEAR SUPPORT 1
    h = np.zeros(len(v))

    corte.plot(h, v, "blue", linewidth=0.5)

    v = np.arange(
        VV[len(VV) - 1] / rel_tela, 0, 0.01
    )  
    h = (
        np.zeros(len(v)) + Lt
    ) 

    corte.plot(h, v, "blue", linewidth=0.5)
    corte.annotate("CALCULATED REQUIRED SHEAR FORCE",
                   xy=(2, 1), xytext=(-3, 2.8))

    #    PLACING TEXTS AT MAXIMUM POINTS

    for jj in range(2):
        aux_x = 0
        if jj == 1:
            aux_x = L[0]
        for kk in range(trechos):
            aa = jj
            # corte_max=fig.add_subplot(111)
            if jj == 1 and kk == (trechos - 1):
                aa = -1
            a = round(VV[int(aux_x * 100 + aa)], 0)
            posx = aux_x + 0.1
            corte.annotate(a, xy=(2, 1), xytext=(posx, 1.2 * (a / rel_tela)))
            aux_x = aux_x + L[kk]

    # The tk.DrawingArea.
    canvas = FigureCanvasTkAgg(fig, master=Frame4_solicitante)
    canvas.draw()
    toolbar = NavigationToolbar2Tk(canvas, Frame4_solicitante)
    toolbar.update()
    canvas.get_tk_widget().pack(
        side=tk.TOP, fill=tk.BOTH, expand=1
    )  # POSITIONS THE GRAPHIC IN THE FRAME

# =============================================================================#

# =============================================================================
# RESISTANT SHEAR GRAPH
# =============================================================================

def shear_resistence_graph():
    global fig

    Frame5_resistente = tk.Frame(janela_geral)
    Frame5_resistente.place(
        relx=0.24,
        rely=0.413,
        relheight=0.315,
        relwidth=0.58)
    Frame5_resistente.configure(relief="groove")
    Frame5_resistente.configure(borderwidth="2")
    Frame5_resistente.configure(relief="groove")
    Frame5_resistente.configure(background="#d9d9d9")
    Frame5_resistente.configure(highlightbackground="#d9d9d9")
    Frame5_resistente.configure(highlightcolor="black")

    fig = Figure(figsize=(1, 1), dpi=100) 

    corte = creat_beam_support(fig)

    #    SET SCREEN RATIO
    rel_tela = Vrd / 2

    #    CREATING THE INITIAL AND FINAL LINES OF THE DIAGRAM
    ini = 0
    fim = Vrd / rel_tela
    Ltotal = 0
    altura = Vrd / rel_tela
    for k in range(2):
        Ltotal = 0

        for j in range(2):
            if k == 1:
                ini = -Vrd / rel_tela
                fim = 0
            if j == 1:
                Ltotal = Lt
            v = np.arange(
                ini, fim, 0.01
            )  # VERTICAL VECTOR FOR THE STRAIGHT LINE OF SHEAR SUPPORT 1
            h = (
                np.zeros(len(v)) + Ltotal
            )  # HORIZONTAL VECTOR FOR THE STRAIGHT LINE OF SHEAR SUPPORT 1

            corte.plot(h, v, "blue", linewidth=0.5)

        if k == 1:
            altura = -Vrd / rel_tela
        h = np.arange(
            0, Lt, 0.01
        )  # VERTICAL VECTOR FOR THE STRAIGHT LINE OF CUTTING SUPPORT 1
        v = (
            np.zeros(len(h)) + altura
        )  # HORIZONTAL VECTOR FOR THE STRAIGHT LINE OF CUTTING SUPPORT 1
        corte.plot(h, v, "blue", linewidth=0.5)

        corte.annotate(
            round(Vrd, 1), xy=(2, 1), xytext=(Lt / 2 - 0.4, (Vrd / rel_tela))
        )
        corte.annotate(
            round(-Vrd, 1), xy=(2, 1), xytext=(Lt / 2 - 0.4, (-Vrd / rel_tela))
        )
        corte.annotate("CALCULATED SHEAR CAPACITY",
                       xy=(2, 1), xytext=(-3, 2.8))

    # The tk.DrawingArea.
    canvas = FigureCanvasTkAgg(fig, master=Frame5_resistente)
    canvas.draw()
    toolbar = NavigationToolbar2Tk(canvas, Frame5_resistente)
    toolbar.update()
    canvas.get_tk_widget().pack(
        side=tk.TOP, fill=tk.BOTH, expand=1
    )  # POSITIONS THE GRAPHIC IN THE FRAME

# =============================================================================#

# =============================================================================
# RESISTANT MOMENT GRAPH
# =============================================================================

def moment_resistence_graph():
    global fig

    Frame5_resistente = tk.Frame(janela_geral)
    Frame5_resistente.place(
        relx=0.24,
        rely=0.413,
        relheight=0.315,
        relwidth=0.58)
    Frame5_resistente.configure(relief="groove")
    Frame5_resistente.configure(borderwidth="2")
    Frame5_resistente.configure(relief="groove")
    Frame5_resistente.configure(background="#d9d9d9")
    Frame5_resistente.configure(highlightbackground="#d9d9d9")
    Frame5_resistente.configure(highlightcolor="black")

    fig = Figure(figsize=(1, 1), dpi=100) 
    mom = creat_beam_support(fig)

    #    SET SCREEN RATIO
    max_abs = max(np.abs(Mrd))
    rel_tela = max_abs / 2

    #    CREATING THE INITIAL AND FINAL LINES OF THE DIAGRAM
    for k in range(len(Mrd)):
        for j in range(2):
            if Mrd[k] >= 0:
                aux_v_i = -Mrd[k] / rel_tela
                aux_v_f = 0

            elif Mrd[k] < 0:
                aux_v_i = 0
                aux_v_f = -Mrd[k] / rel_tela

            v = np.arange(
                aux_v_i, aux_v_f, 0.01
            )  
            h = np.zeros(len(v)) + (
                x_MM0[k + j]
            )  
            mom.plot(h, v, "blue", linewidth=0.5)

        h = np.arange(
            x_MM0[k], x_MM0[k + 1], 0.01
        )  
        v = (np.zeros(len(h))) - (
            Mrd[k] / rel_tela
        )  
        mom.plot(h, v, "blue", linewidth=0.5)

        posx = (x_MM0[k] + x_MM0[k + 1]) / 2
        a = round(Mrd[k], 1)
        mom.annotate(a, xy=(2, 1), xytext=(posx - 0.4, (-a / rel_tela)))
        mom.annotate("CALCULATED BENDING MOMENT CAPACITY",
                     xy=(2, 1), xytext=(-3, 2.8))

    # The tk.DrawingArea.
    canvas = FigureCanvasTkAgg(fig, master=Frame5_resistente)
    canvas.draw()

    toolbar = NavigationToolbar2Tk(canvas, Frame5_resistente)
    toolbar.update()

    canvas.get_tk_widget().pack(
        side=tk.TOP, fill=tk.BOTH, expand=1
    )  # POSITIONS THE GRAPHIC IN THE FRAME

# =============================================================================#

# =============================================================================
# ACTIVE MOMENT GRAPH
# =============================================================================

def moment_acting_graph():
    global fig

    Frame4_solicitante = tk.Frame(janela_geral)
    Frame4_solicitante.place(
        relx=0.24,
        rely=0.088,
        relheight=0.315,
        relwidth=0.58)
    Frame4_solicitante.configure(relief="groove")
    Frame4_solicitante.configure(borderwidth="2")
    Frame4_solicitante.configure(relief="groove")
    Frame4_solicitante.configure(background="#d9d9d9")
    Frame4_solicitante.configure(highlightbackground="#d9d9d9")
    Frame4_solicitante.configure(highlightcolor="black")

    fig = Figure(figsize=(1, 1), dpi=100)  # CREATE THE FIGURE

    mom = creat_beam_support(fig)

    #    SET SCREEN RATIO
    max_abs = max(np.abs(MM))
    rel_tela = max_abs / 2

    mom.plot(xx, MM / rel_tela, "blue", linewidth=0.5)

    for jj in range(trechos):
        a = round(MM[int(x_VV0[jj] * 100)], 3)
        posx = x_VV0[jj]

        v = np.arange(
            MM[int(x_VV0[jj] * 100)] / rel_tela, 0, 0.01
        )  
        h = (
            np.zeros(len(v)) + posx
        )  
        mom.plot(h, v, "blue", linewidth=0.5)
        mom.annotate(-1 * a, xy=(2, 1),
                     xytext=(posx - 0.2, -0.5 + (a / rel_tela)))

    posx = 0
    for jj in range(trechos - 1):
        posx = posx + L[jj]
        a = round(MM[int(posx * 100)], 1)

        v = np.arange(
            0, MM[int(posx * 100)] / rel_tela, 0.01
        )  
        h = (
            np.zeros(len(v)) + posx
        )  
        mom.plot(h, v, "blue", linewidth=0.5)
        mom.annotate(-1 * a, xy=(2, 1),
                     xytext=(posx - 0.2, +0.5 + (a / rel_tela)))
        mom.annotate("CALCULATED REQUIRED BENDING MOMENT",
                     xy=(2, 1), xytext=(-3, 2.8))

    canvas = FigureCanvasTkAgg(fig, master=Frame4_solicitante)
    canvas.draw()

    toolbar = NavigationToolbar2Tk(canvas, Frame4_solicitante)
    toolbar.update()

    canvas.get_tk_widget().pack(
        side=tk.TOP, fill=tk.BOTH, expand=1
    )  

# =============================================================================#

# =============================================================================
# SHEAR EFECT RESULT
# =============================================================================

def shear_result_graph():
    global fig

    Frame6_conectores = tk.Frame(janela_geral)
    Frame6_conectores.place(
        relx=0.24,
        rely=0.738,
        relheight=0.25,
        relwidth=0.58)
    Frame6_conectores.configure(relief="groove")
    Frame6_conectores.configure(borderwidth="2")
    Frame6_conectores.configure(relief="groove")
    Frame6_conectores.configure(background="#d9d9d9")
    Frame6_conectores.configure(highlightbackground="#d9d9d9")
    Frame6_conectores.configure(highlightcolor="black")

    fig = Figure(figsize=(1, 1), dpi=100)  # CREATE THE FIGURE

    corte = creat_beam_support(fig)

    # SET SCREEN RATIO
    max_abs = max(np.abs(VV))
    rel_tela = max_abs / 2
    corte.plot(xx, VV / rel_tela, "Red", linewidth=0.3)

    #    CREATING THE INITIAL AND FINAL LINES OF THE DIAGRA

    v = np.arange(
        0, VV[0] / rel_tela, 0.01
    )  
    h = np.zeros(len(v))
    corte.plot(h, v, "green", linewidth=0.3)

    v = np.arange(
        VV[len(VV) - 1] / rel_tela, 0, 0.01
    )  
    h = (
        np.zeros(len(v)) + Lt
    )  
    corte.plot(h, v, "green", linewidth=0.3)

    #    PLOTING THE RESISTANT SHEAR GRAPH

    ini = 0
    fim = Vrd / rel_tela
    Ltotal = 0
    altura = Vrd / rel_tela
    for k in range(2):
        Ltotal = 0

        for j in range(2):
            if k == 1:
                ini = -Vrd / rel_tela
                fim = 0
            if j == 1:
                Ltotal = Lt
            v = np.arange(
                ini, fim, 0.01
            )  
            h = (
                np.zeros(len(v)) + Ltotal
            ) 
            corte.plot(h, v, "green", linewidth=0.3)

        if k == 1:
            altura = -Vrd / rel_tela
        h = np.arange(
            0, Lt, 0.01
        )  
        v = (
            np.zeros(len(h)) + altura
        )  
        corte.plot(h, v, "green", linewidth=0.3)

    # CREATES THE LINES THAT SEPARATE THE SECTIONS OF NULL MOMENT
    if trechos == 1:
        j = 0
    if trechos == 2:
        j = 2
    if trechos == 3:
        j = 4
    for k in range(j):
        v = np.arange(-10, 10, 0.01)
        h = np.zeros(len(v)) + x_MM0[k + 1]
        corte.plot(h, v, "gray", linewidth=1)

    for k in range(len(Mrd)):
        b = ((x_MM0[k + 1] - x_MM0[k]) / 2) + x_MM0[k]
        corte.annotate(k + 1, xy=(2, 1), xytext=(b, -3))

    a = 0

    # CREATING THE APPEARANCE OF STUDS
    for k in range(len(Mrd)):
        if k == 0:
            xcon = cobrimento
        elif k >= 1:
            xcon = x_MM0[k]
        a = 0

        for j in range(int(n_con[k])):
            if trechos == 1:
                xcon = xcon + a
                v = np.arange(0, 0.3, 0.01)
                h = np.zeros(len(v)) + xcon
                corte.plot(h, v, "black", linewidth=1.5)

                h = np.arange(xcon - 0.02, xcon + 0.02, 0.01)
                v = np.zeros(len(h)) + 0.3
                corte.plot(h, v, "black", linewidth=1.5)

                a = espac[k]

            elif trechos >= 2 and k == 0:
                xcon = xcon + a
                v = np.arange(0, 0.3, 0.01)
                h = np.zeros(len(v)) + xcon
                corte.plot(h, v, "black", linewidth=1.5)

                h = np.arange(xcon - 0.02, xcon + 0.02, 0.01)
                v = np.zeros(len(h)) + 0.3
                corte.plot(h, v, "black", linewidth=1.5)

                a = espac[k]

            elif (
                (trechos >= 2 and k == 1)
                or (trechos == 3 and k == 1)
                or (trechos == 3 and k == 2)
                or (trechos == 3 and k == 3)
            ):
                if j == 0:
                    b = espac[k] / 2
                else:
                    b = 0
                xcon = xcon + a + b
                v = np.arange(0, 0.3, 0.01)
                h = np.zeros(len(v)) + xcon
                corte.plot(h, v, "black", linewidth=1.5)

                h = np.arange(xcon - 0.02, xcon + 0.02, 0.01)
                v = np.zeros(len(h)) + 0.3
                corte.plot(h, v, "black", linewidth=1.5)

                a = espac[k]

            elif (trechos == 2 and k == 2) or (trechos == 3 and k == 4):
                a = espac[k]
                xcon = xcon + a
                v = np.arange(0, 0.3, 0.01)
                h = np.zeros(len(v)) + xcon
                corte.plot(h, v, "black", linewidth=1.5)

                h = np.arange(xcon - 0.02, xcon + 0.02, 0.01)
                v = np.zeros(len(h)) + 0.3
                corte.plot(h, v, "black", linewidth=1.5)

    # The tk.DrawingArea
    canvas = FigureCanvasTkAgg(fig, master=Frame6_conectores)
    canvas.draw()

    toolbar = NavigationToolbar2Tk(canvas, Frame6_conectores)
    toolbar.update()

    canvas.get_tk_widget().pack(
        side=tk.TOP, fill=tk.BOTH, expand=1
    )  # POSITIONS THE GRAPHIC IN THE FRAME

# =============================================================================#

# =============================================================================
# MOMENT RESULT PLOT
# ============================================================================

def moment_result_grapah():
    global fig

    Frame6_conectores = tk.Frame(janela_geral)
    Frame6_conectores.place(
        relx=0.24,
        rely=0.738,
        relheight=0.25,
        relwidth=0.58)
    Frame6_conectores.configure(relief="groove")
    Frame6_conectores.configure(borderwidth="2")
    Frame6_conectores.configure(relief="groove")
    Frame6_conectores.configure(background="#d9d9d9")
    Frame6_conectores.configure(highlightbackground="#d9d9d9")
    Frame6_conectores.configure(highlightcolor="black")

    fig = Figure(figsize=(1, 1), dpi=100)  # CREATE THE FIGURE

    mom = creat_beam_support(fig)

    #    SET SCREEN RATIO
    max_abs = max(np.abs(VV))
    rel_tela = max_abs / 2

    #    PLOTTING THE ACTING MOMENTUM GRAPH

    mom.plot(xx, MM / rel_tela, "Red", linewidth=0.3)

    #    CREATING THE INITIAL AND FINAL LINES OF THE DIAGRAM
    for k in range(len(Mrd)):
        for j in range(2):
            if Mrd[k] >= 0:
                aux_v_i = -Mrd[k] / rel_tela
                aux_v_f = 0

            elif Mrd[k] < 0:
                aux_v_i = 0
                aux_v_f = -Mrd[k] / rel_tela

            v = np.arange(
                aux_v_i, aux_v_f, 0.01
            )  
            h = np.zeros(len(v)) + (
                x_MM0[k + j]
            )  
            mom.plot(h, v, "green", linewidth=0.3)

        h = np.arange(
            x_MM0[k], x_MM0[k + 1], 0.01
        )  
        v = (np.zeros(len(h))) - (
            Mrd[k] / rel_tela
        )  
        mom.plot(h, v, "green", linewidth=0.3)

    # CREATES THE LINES THAT SEPARATE THE SECTIONS OF NULL MOMENT
    for k in range(len(Mrd)):
        b = ((x_MM0[k + 1] - x_MM0[k]) / 2) + x_MM0[k]
        mom.annotate(k + 1, xy=(2, 1), xytext=(b, -3))

    a = 0
    # CREATING THE APPEARANCE OF STUDS
    for k in range(len(Mrd)):
        if k == 0:
            xcon = cobrimento
        elif k >= 1:
            xcon = x_MM0[k]
        a = 0

        for j in range(int(n_con[k])):
            if trechos == 1:
                xcon = xcon + a
                v = np.arange(0, 0.3, 0.01)
                h = np.zeros(len(v)) + xcon
                mom.plot(h, v, "black", linewidth=1.5)

                h = np.arange(xcon - 0.02, xcon + 0.02, 0.01)
                v = np.zeros(len(h)) + 0.3
                mom.plot(h, v, "black", linewidth=1.5)

                a = espac[k]

            elif trechos >= 2 and k == 0:
                xcon = xcon + a
                v = np.arange(0, 0.3, 0.01)
                h = np.zeros(len(v)) + xcon
                mom.plot(h, v, "black", linewidth=1.5)

                h = np.arange(xcon - 0.02, xcon + 0.02, 0.01)
                v = np.zeros(len(h)) + 0.3
                mom.plot(h, v, "black", linewidth=1.5)

                a = espac[k]

            elif (
                (trechos >= 2 and k == 1)
                or (trechos == 3 and k == 1)
                or (trechos == 3 and k == 2)
                or (trechos == 3 and k == 3)
            ):
                if j == 0:
                    b = espac[k] / 2
                else:
                    b = 0
                xcon = xcon + a + b
                v = np.arange(0, 0.3, 0.01)
                h = np.zeros(len(v)) + xcon
                mom.plot(h, v, "black", linewidth=1.5)

                h = np.arange(xcon - 0.02, xcon + 0.02, 0.01)
                v = np.zeros(len(h)) + 0.3
                mom.plot(h, v, "black", linewidth=1.5)

                a = espac[k]

            elif (trechos == 2 and k == 2) or (trechos == 3 and k == 4):
                a = espac[k]
                xcon = xcon + a
                v = np.arange(0, 0.3, 0.01)
                h = np.zeros(len(v)) + xcon
                mom.plot(h, v, "black", linewidth=1.5)

                h = np.arange(xcon - 0.02, xcon + 0.02, 0.01)
                v = np.zeros(len(h)) + 0.3
                mom.plot(h, v, "black", linewidth=1.5)

    canvas = FigureCanvasTkAgg(fig, master=Frame6_conectores)
    canvas.draw()

    toolbar = NavigationToolbar2Tk(canvas, Frame6_conectores)
    toolbar.update()

    canvas.get_tk_widget().pack(
        side=tk.TOP, fill=tk.BOTH, expand=1
    )  # POSITIONS THE GRAPHIC IN THE FRAME

# =============================================================================#

# # # =========================================================================
# # # # #####################      READING EXCEL FILE      ####################
# # # =========================================================================

def func_data_in():
    global trechos, L, q
    global bf, bs, tf, h, d, d_, tw, ry, Wx, I_p, area_p
    global norma, interacao, Lb_max, tc, n_barras, diametro_barras, cobrimento, fucs, ycs, diametro_conector, DoC
    global fck, yc, E_a, fy, ya, E_as, fs, ys

    base = pd.read_excel(nome_arquivo)
    base_numérico = base.values

    # =============================================================================
    # LOAD COLLECTION AND SPACES
    # =============================================================================

    trechos = int(base_numérico[0, 1])

    L = np.zeros(trechos)
    q = np.zeros(trechos)

    for read in range(trechos):
        L[read] = base_numérico[2 + read, 1]
        q[read] = base_numérico[5 + read, 1]

    # =============================================================================
    # COLLECTION OF PROFILE DATA
    # =============================================================================

    bf = base_numérico[3, 4]
    bs = base_numérico[3, 4]
    tf = base_numérico[4, 4]
    h = round(base_numérico[5, 4], 6)
    d = base_numérico[6, 4]
    d_ = base_numérico[7, 4]

    tw = base_numérico[3, 7]
    ry = base_numérico[4, 7]
    Wx = base_numérico[5, 7]
    I_p = base_numérico[6, 7]
    area_p = base_numérico[7, 7]

    # =============================================================================
    # COLLECTION OF GENERAL DATA
    # =============================================================================

    norma = base_numérico[1, 5]
    interacao = base_numérico[10, 7]
    Lb_max = base_numérico[11, 7]
    tc = base_numérico[12, 7]
    n_barras = base_numérico[13, 7]
    diametro_barras = base_numérico[14, 7]
    cobrimento = base_numérico[15, 7]
    fucs = base_numérico[16, 7]
    diametro_conector = base_numérico[17, 7]
    ycs = base_numérico[18, 7]
    DoC = base_numérico[19, 7]

    # =============================================================================
    # COLLECTION OF MATERIAL DATA
    # =============================================================================

    fck = base_numérico[21, 7]
    yc = base_numérico[22, 7]

    E_a = base_numérico[23, 7]
    fy = base_numérico[24, 7]
    ya = base_numérico[25, 7]

    E_as = base_numérico[26, 7]
    fs = base_numérico[27, 7]
    ys = base_numérico[28, 7]

    rewrite_labels_frame1()

def name_window():
    def take_name():
        global nome_arquivo
        nome_arquivo = box_take_nomes.get()
        janela_carregar.destroy()
        func_data_in()

    janela_carregar = tk.Tk()

    style = ttk.Style()
    style.configure(".", background=_bgcolor)
    style.configure(".", foreground=_fgcolor)
    style.configure(".", font="TkDefaultFont")
    style.map(
        ".", background=[
            ("selected", _compcolor), ("active", _ana2color)])

    janela_carregar.geometry("300x150+561+192")
    janela_carregar.minsize(148, 1)
    janela_carregar.maxsize(1924, 1055)
    janela_carregar.resizable(1, 1)
    janela_carregar.iconbitmap("icones/geral.ico")
    janela_carregar.title("File Selection")
    janela_carregar.configure(background="#d9d9d9")
    janela_carregar.configure(highlightbackground="#d9d9d9")
    janela_carregar.configure(highlightcolor="black")

    la_normas = tk.Label(janela_carregar)
    Config_frame(la_normas, relx=0.083, rely=0.1, height=33, width=250,
                 ft=Sbi_font10, text="""File Name (.xlsx)""")

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
    btn_take_nomes.configure(text=""">>>""")
    btn_take_nomes.configure(command=take_name)

    janela_carregar.mainloop()

def close():
    janela_geral.destroy()

entry_text = None

def reset_program():
    # Close the current program
    janela_geral.destroy()
    # Restart the current program
    subprocess.Popen([sys.executable] + sys.argv)

# =============================================================================
# =============================================================================
# # # =========================================================================
# # # # ###################   NBR8800 CALCULATIONS     ########################
# # # =========================================================================
# =============================================================================
# =============================================================================

# =============================================================================
# CALCULATIONS OF STIFFNESS, INTERNAL FORCES, AND REACTIONS
# =============================================================================

def active_efforts():
    global xx, MM, VV, x_VV0, x_MM0, texto_erro, msd_max_, vsd_max_
    KG = np.zeros((4 + (trechos * 2 - 2), 4 + (trechos * 2 - 2)))
    KG_a = np.zeros((trechos + 1, trechos + 1))
    KG_aa = np.zeros((trechos + 1, trechos + 1))
    cont_1 = 0
    for n in range(trechos):  # Creates the global stiffness matrix
        a = cont_1
        b = cont_1 + 1
        c = cont_1 + 2
        d = cont_1 + 3

        k12 = 12 / L[n] ** 3
        k06 = 6 / L[n] ** 2
        k04 = 4 / L[n]
        k02 = 2 / L[n]

        KG[a, a] = KG[a, a] + k12
        KG[b, a] = KG[b, a] + k06
        KG[b, b] = KG[b, b] + k04
        KG[c, a] = KG[c, a] - k12
        KG[c, b] = KG[c, b] - k06
        KG[c, c] = KG[c, c] + k12
        KG[d, a] = KG[d, a] + k06
        KG[d, b] = KG[d, b] + k02
        KG[d, c] = KG[d, c] - k06
        KG[d, d] = KG[d, d] + k04

        KG[a, b] = KG[b, a]
        KG[a, c] = KG[c, a]
        KG[a, d] = KG[d, a]
        KG[b, c] = KG[c, b]
        KG[b, d] = KG[d, b]
        KG[c, d] = KG[d, c]

        cont_1 = cont_1 + 2
    for l in range(trechos + 1):
        for c in range(trechos + 1):
            KG_aa[l, c] = KG[
                l * 2 + 1, c * 2 + 1
            ]  # Creates the reduced stiffness matrix

    KG_a = np.linalg.inv(KG_aa)  # Invert the reduced matrix

    if trechos == 1:  # Calculate the reactions if the beam has 1 section
        aux2 = (q * L) / 2
        M = [0, 0]
        U = np.matmul(KG_a, M)
        Ug = [0, U[0], 0, U[1]]
        R = [aux2[0], 0, aux2[0], 0]
        R = R + np.matmul(KG, Ug)

    elif trechos == 2:  #  Calculate the reactions if the beam has 2 sections
        aux = (q * L**2) / 8
        aux2 = (q * L) / 8
        Mb = aux[0] - aux[1]
        M = [0, Mb, 0]
        U = np.matmul(KG_a, M)
        Ug = [0, U[0], 0, U[1], 0, U[2]]
        R = [3 * aux2[0], 0, (5 * aux2[0] + 5 * aux2[1]), 0, 3 * aux2[1], 0]
        R = R + np.matmul(KG, Ug)

    elif trechos == 3:  # Calculate the reactions if the beam has 3 sections
        aux = (q * L**2) / 8
        aux2 = (q * L) / 8
        Mb = aux[0] - (2 * aux[1] / 3)
        Mc = (2 * aux[1] / 3) - aux[2]
        M = [0, Mb, Mc, 0]
        U = np.matmul(KG_a, M)
        Ug = [0, U[0], 0, U[1], 0, U[2], 0, U[3]]
        R = [
            3 * aux2[0],
            0,
            (5 * aux2[0] + 4 * aux2[1]),
            0,
            (4 * aux2[1] + 5 * aux2[2]),
            0,
            3 * aux2[2],
            0,
        ]
        R = R + np.matmul(KG, Ug)

    # CREATES THE MOMENT AND SHEAR FORCE VECTORS IN RELATION TO THE VECTOR xx
    for k in range(len(xx)):
        if k <= (100 * L[0]):
            MM[k] = -R[0] * xx[k] + (q[0] * xx[k] ** 2) / 2
            VV[k] = R[0] - (xx[k] * q[0])
            # # DEFINES THE POINT OF MAXIMUM POSITIVE MOMENT OF EACH SECTION, THE
            # # MAXIMUM NEGATIVE MOMENT IS ON TOP OF THE SUPPORT
            x_VV0[0] = (R[0] / q[0])

        elif k >= (100 * L[0]) and k <= (100 * L[0] + 100 * L[1]) and (trechos >= 2):
            MM[k] = (
                -R[0] * xx[k]
                + (q[0] * L[0] * (xx[k] - L[0] / 2))
                - (R[2] * (xx[k] - L[0]))
                + (q[1] * (xx[k] - L[0]) * ((xx[k] - L[0]) / 2))
            )
            VV[k] = R[0] - (L[0] * q[0]) + R[2] - ((xx[k] - L[0]) * q[1])
            x_VV0[1] = ((R[0] + R[2] - (L[0] * q[0])) / q[1]) + L[0]

        elif k >= (100 * L[0] + 100 * L[1]) and (trechos == 3):
            MM[k] = (
                -R[0] * xx[k]
                + (q[0] * L[0] * (xx[k] - L[0] / 2))
                - (R[2] * (xx[k] - L[0]))
                + (q[1] * L[1] * (xx[k] - L[0] - L[1] / 2))
                - (R[4] * (xx[k] - L[0] - L[1]))
                + (q[2] * (xx[k] - L[0] - L[1]) * ((xx[k] - L[0] - L[1]) / 2))
            )
            VV[k] = (
                R[0]
                - (L[0] * q[0])
                + R[2]
                - (L[1] * q[1])
                + R[4]
                - ((xx[k] - L[0] - L[1]) * q[2])
            )
            x_VV0[2] = (
                ((R[0] + R[2] + R[4] - (L[0] * q[0]) - (L[1] * q[1])) / q[2])
                + L[0]
                + L[1]
            )

    MM = MM * 1
    VV = VV * 1
    #       SOLVE THE 2ND DEGREE EQ AND FIND OUT WHERE THE MOMENT IS NULL

    for k in range(trechos):
        if k == 0:
            a = q[0] / 2
            b = -R[0]
            c = 0
        elif k == 1:
            a = q[1] / 2
            b = -R[0] + q[0] * L[0] - R[2] - q[1] * L[0]
            c = -((q[0] * L[0] ** 2) / 2) + \
                ((q[1] * L[0] ** 2) / 2) + R[2] * L[0]
        elif k == 2:
            a = q[2] / 2
            b = -R[6]
            c = 0

        x = (b**2) - (4 * a * c)

        if x >= 0:
            x = np.sqrt(x)
            x1 = (-b + x) / (2 * a)
            x2 = (-b - x) / (2 * a)
            if k == 2:
                a = x1
                x1 = Lt - x2
                x2 = Lt - a
        else:
            texto_erro += [
                "NO REAL ROOTS FOUND!"
            ]
            window_error_func()
            print(
                "NO REAL ROOTS FOUND!"
            )

        x_MM0[k * 2] = round(x2, 2)
        x_MM0[(k + 1) * 2 - 1] = round(x1, 2)

    # LOOP THAT DEFINES THE MAXIMUM CUTTING MOMENT AND EFFORT IN EACH SECTION

    if trechos >= 1:
        msd_max_[0] = round(-1 * MM[int(x_VV0[0] * 100)], 2)
        vsd_max_[0] = round(VV[0], 2)

        if trechos >= 2:
            msd_max_[1] = -round(MM[int(L[1] * 100)], 2)
            msd_max_[2] = -round(MM[int(x_VV0[1] * 100)], 2)

            vsd_max_[1] = round(
                max(abs((VV[int(L[1] * 100 - 2): int(L[1] * 100 + 1)]))), 2
            )
            vsd_max_[2] = round(
                max(abs(VV[int(x_MM0[2] * 100): int(x_MM0[3] * 100)])), 2
            )

            if trechos >= 3:
                msd_max_[3] = -round(MM[int(L[2] * 100)], 2)
                msd_max_[4] = -round(MM[int(x_VV0[2] * 100)], 2)

                vsd_max_[3] = round(
                    max(abs((VV[int(L[2] * 100 - 2): int(L[2] * 100 + 1)]))), 2
                )
                vsd_max_[4] = round(
                    max(abs(VV[int(x_MM0[4] * 100): int(x_MM0[5] * 100)])), 2
                )

# =============================================================================#

# =============================================================================
# FUNCTION THAT CREATES VECTORS
# =============================================================================

def create_vectors():
    global size_vetor, lb, Ccd, Tad, Mrd, Vrd, a, Lt, xx, MM, VV, x_VV0, x_MM0, MdistRd, LN, Msd, n_con, espac, tex, tex_1
    global texto_erro, msd_max_, vsd_max_, erros, pos_err, LN, a_ln, ws_vetor, wi_vetor, limitador
    global d3, d4, d5

    for n in range(trechos):
        if n == 0:
            size_vetor = 1
        else:
            size_vetor = size_vetor + 2

    lb = np.zeros(size_vetor)  # FLANGE width VECTOR
    Ccd = np.zeros(size_vetor)
    Tad = np.zeros(size_vetor)
    Mrd = np.zeros(size_vetor)
    Msd = np.zeros(size_vetor)
    Vrd = np.zeros(size_vetor)
    n_con = np.zeros(size_vetor)
    espac = np.zeros(size_vetor)
    a_ln = np.zeros(size_vetor)

    d3 = np.zeros(size_vetor)
    d4 = np.zeros(size_vetor)
    d5 = np.zeros(size_vetor)

    msd_max_ = np.zeros(size_vetor)
    vsd_max_ = np.zeros(size_vetor)

    LN = ["---", "---", "---", "---", "---"]
    texto_erro = ["Error Check\n\n"]
    limitador = [
        "----",
        "----",
        "----",
        "----",
        "----",
    ]

    # CREATES VECTORS TO DEFINE ACTIVE EFFORTS
    Lt = sum(L)
    xx = np.linspace(0, Lt, int(100 * Lt))
    MM = np.zeros(len(xx))
    VV = np.zeros(len(xx))

    x_VV0 = np.zeros(trechos)
    x_MM0 = np.zeros(trechos * 2)
    MdistRd = [0, 0]

    ws_vetor = np.zeros(size_vetor)
    wi_vetor = np.zeros(size_vetor)

# =============================================================================#

# =============================================================================
# # ===========================================================================
# # DESIGN FOLLOWING NBR8800
# # ===========================================================================
# =============================================================================

####################################################
#####              EFFECTIVE width          ########
####################################################

def width():
    global lb
    if trechos == 1:
        lb[0] = min(2 * L[0] / 8, Lb_max)
    elif trechos == 2:
        lb[0] = min((2 * (4 * L[0] / 5)) / 8, Lb_max)
        lb[1] = min((2 * (L[0] + L[1]) / 4) / 8, Lb_max)
        lb[2] = min((2 * (4 * L[1] / 5)) / 8, Lb_max)
    elif trechos == 3:
        lb[0] = min((2 * (4 * L[0] / 5)) / 8, Lb_max)
        lb[1] = min((2 * (L[0] + L[1]) / 4) / 8, Lb_max)
        lb[2] = min((2 * 7 * L[1] / 10) / 8, Lb_max)
        lb[3] = min((2 * (L[1] + L[2]) / 4) / 8, Lb_max)
        lb[4] = min((2 * (4 * L[2] / 5)) / 8, Lb_max)

####################################################
#####     CROSS SECTION CLASSIFICATION      ########
####################################################

def classify():
    global classificacao, texto_erro, lambda_, lambda_p, lambda_r
    bs = bf
    if bf == bs:
        # print("seção é duplamente simetrica")
        lambda_ = d_ / tw
        lambda_p = 3.76 * np.sqrt((E_a / fy))
        lambda_r = 5.70 * np.sqrt((E_a / fy))

        if lambda_ <= lambda_p:
            classificacao = "compacta"

        elif lambda_p <= lambda_ <= lambda_r:
            classificacao = "semicompacta"

        elif lambda_r <= lambda_:
            classificacao = "semicompacta"
    else:
        texto_erro += ["The section is not doubly symmetric."]
        window_error_func()
        exit()
        print("The section is not doubly symmetric.")

####################################################
#####                   OTHERS               #######
####################################################

def properties():
    global Tad, Ccd, ws, wi, ws_vetor, wi_vetor

    Tad = (
        area_p * fyd
    )  # Maximum stress allowed by the metal profile. (area * stress/area).
    # Calculation resistant force of compressed thickness of concrete slab;
    # The 0.85 is responsible for the reduction of resistance due to the effect of
    # Rüsch (long-lasting effects)
    Ccd[kk] = (0.85 * fcd * lb[kk] * tc)

    # =============================================================================
    # SLAB PROPERTIES
    # =============================================================================

    area_c = lb[kk] * tc / alpha_e  # Concrete equivalent area
    yc = tc / 2  # CG_y= Center of gravity y
    ayc = yc * area_c  #
    ayc2 = (yc**2) * area_c  #
    I_c = ((area_c / tc) * tc**3) / 12  # Inertia

    # =============================================================================
    # PROFILE PROPERTIES
    # =============================================================================

    yp = (d / 2) + tc  # CG_y= Center of gravity y
    ayp = yp * area_p  #
    ayp2 = (yp**2) * area_p  #

    # =============================================================================
    # MIXED SECTION PROPERTIES
    # =============================================================================

    area_t = area_c + area_p  # Total section area
    ayt = ayc + ayp  
    ayt2 = ayp2 + ayc2  
    I_t = I_c + I_p  

    # Distance from the top edge of the slab to the GC of the composite section.
    ys = ayt / area_t
    # Distance from the lower edge of the profile to the CG of the mixed section.
    yi = (d + tc) - ys
    I = I_t + ayt2 - (area_t * ys**2)  # Inércia da seção mista

    # Elastic modulus of resistance of the composite cross section in relation to
    # flexion axis superior to the CG.
    ws = (I / ys)
    # Elastic modulus of resistance of the composite cross section in relation to
    # bending axis lower than the CG.
    wi = (I / yi)
    ws_vetor[kk] = ws
    wi_vetor[kk] = wi

# =============================================================================
#           #####################################################
#           ######          CHECK THE SHEAR FORCE          ######
#           #####################################################
# =============================================================================

def shear():
    global kv, Vpl, lambda_corte, lambda_p_corte, lambda_r_corte, Vrd

    kv = 5  # Without transverse stiffeners
    # Shear force corresponding to the plasticization of the core by shear;
    Vpl = (0.60 * (d * tw) * fy)

    lambda_corte = d / tw
    lambda_p_corte = 1.10 * np.sqrt(((E_a * kv) / fy))
    lambda_r_corte = 1.37 * np.sqrt(((E_a * kv) / fy))

    if lambda_corte <= lambda_p_corte:
        Vrd = Vpl / ya

    elif lambda_p_corte <= lambda_ <= lambda_r_corte:
        Vrd = (lambda_p_corte / lambda_corte) * (Vpl / ya)

    elif lambda_r_corte <= lambda_corte:
        Vrd = 1.24 * ((lambda_p_corte / lambda_corte) ** 2) * (Vpl / ya)

    Vrd = round(Vrd, 2)

# =============================================================================
#           #####################################################
#           ######     POSITIVE BENDING MOMENT CHECKING    ######
#           #####################################################
# =============================================================================

def positive_moment():
    global Mrd, a, LN, yp, texto_erro, LN, a_ln

    if classificacao == "compacta":
        # =============================================================================
        #     ##   COMPACT SECTION    ##
        # =============================================================================
        if interacao == "Complete":
            # =============================================================================
            #         ## FULL INTERACTION  ##
            # =============================================================================
            if Ccd[kk] >= Tad:  # Neutral line in the concrete slab;
                # =============================================================================
                #                ## L-N ON THE SLABE ##
                # =============================================================================
                LN[kk] = "laje"
                a_ln[kk] = (Tad) / (
                    0.85 * fcd * lb[kk]
                )  # Thickness of the compressed region of the slab
                S_Qrd = Tad
                if a_ln[kk] > tc:
                    exit()
                Mrd[kk] = 1 * Tad * (d1 + hf + tc - (a_ln[kk] / 2))
                yp = 0
            else:  # Neutral line in the steel profile
                # =============================================================================
                #             # L-N IN PROFILE 
                # =============================================================================

                a_ln[kk] = tc
                Cad = (Tad - Ccd[kk]) * 0.5
                S_Qrd = Ccd[kk]
                if Cad < (fyd * bf * tf):
                    LN[kk] = "Mesa"
                    ######
                    # Neutral line on the steel profile Flange
                    ######
                    # Compressed profile thickness
                    yp = (Cad / (fyd * bf * tf)) * tf
                    yt = (
                        (tf / 2) * (bf * tf)
                        + (tf + h / 2) * (h * tw)
                        + ((tf - yp) / 2 + h + tf) * ((tf - yp) * bf)
                    ) / ((bf * tf) + (h * tw) + (tf - yp) * bf)
                    # Center of gravity of the profile's tensioned section
                    yc = yp / 2  # Center of gravity of the compressed section of the profile
                    a_ln[kk] = a_ln[kk] + yp
                else:
                    ######
                    # Neutral line in the WEB of the steel profile;
                    ######
                    LN[kk] = "Alma"
                    yp = tf + (
                        h * ((Cad - (fyd * bf * tf)) / (fyd * tw * h))
                    )  # Compressed profile thickness
                    yt = (
                        (tf / 2) * (bf * tf)
                        + ((d - yp + tf) / 2) * ((h + tf - yp) * tw)
                    ) / ((bf * tf) + ((h + tf - yp) * tw))
                    # Center of gravity of the profile's tensioned section
                    yc = ((tf / 2) * (bf * tf) + (((yp - tf) / 2) + tf)
                          * (tw * (yp - tf))) / ((bf * tf) + (tw * (yp - tf)))
                    # Center of gravity of the compressed section of the profile
                    a_ln[kk] = a_ln[kk] + yp

                Mrd[kk] = 1 * (Cad * (d - yt - yc) + Ccd[kk]
                               * ((tc / 2) + hf + d - yt))

        elif interacao == "Partial":
            # =============================================================================
            #         ##  PARTIAL INTERACTION ##
            # =============================================================================

            # In this case there are two neutral lines in the set.
            if L[c] > 25:
                texto_erro += [
                    "Beam with a span greater than 25 meters. Partial interaction not allowed"
                ]
                window_error_func()
                print(
                    "Beam with a span greater than 25 meters. Partial interaction not allowed"
                )
                exit()
            Le = 4 * L[c] / 5
            ni = 1 - ((E_a / (578 * fy)) * (0.75 - 0.03 * Le))
            if ni < 0.4:
                ni = 0.4

            if Tad < Ccd[kk]:
                aux1 = Tad
            else:
                aux1 = Ccd[kk]

            S_Qrd = aux1 * ni
            Ccd[kk] = S_Qrd
            Cad = (Tad - Ccd[kk]) * 0.5
            a_ln[kk] = Ccd[kk] / (
                0.85 * fcd * bf
            )  # Depth of neutral axis in concrete slab
            if Cad < (fyd * bf * tf):
                ######
                # Neutral line of the metal profile on the TABLE;
                yp = (Cad / (fyd * bf * tf)) * tf
                yt = (
                    (tf / 2) * (bf * tf)
                    + (tf + h / 2) * (h * tw)
                    + ((tf - yp) / 2 + h + tf) * ((tf - yp) * bf)
                ) / ((bf * tf) + (h * tw) + (tf - yp) * bf)
                yc = yp / 2  

            else:
                yp = tf + (
                    h * ((Cad - (fyd * bf * tf)) / (fyd * tw * h))
                )  
                yt = ((tf / 2) * (bf * tf) + ((d - yp + tf) / 2) * \
                      ((h + tf - yp) * tw)) / ((bf * tf) + ((h + tf - yp) * tw))
                yc = ((tf / 2) * (bf * tf) + (((yp - tf) / 2) + tf) *
                      (tw * (yp - tf))) / ((bf * tf) + (tw * (yp - tf)))

            Mrd[kk] = 1 * (Cad * (d - yt - yc) + Ccd[kk] *
                           (tc - (a_ln[kk] / 2) + hf + d - yt))

    elif classificacao == "semicompacta":
        # =============================================================================
        #     ## SEMI-COMPACT SECTION  ##
        # =============================================================================
        if interacao == "Complete":
            # =============================================================================
            #         ## FULL INTERACTION  ##
            # =============================================================================
            if Tad < Ccd[kk]:
                aux1 = Tad
            else:
                aux1 = Ccd[kk]

            S_Qrd = aux1
            Mrdt = fyd * wi
            Mrdc = 0.85 * fcd * ws * alpha_e
            if Mrdt < Mrdc:
                aux2 = Mrdt
            else:
                aux2 = Mrdc
            Mrd[kk] = aux2

        elif interacao == "Partial":
            # =============================================================================
            #         ## PARTIAL INTERACTION  ##
            # =============================================================================

            # In this case there are two neutral lines in the set.

            if L[c] > 25:
                texto_erro += [
                    "Beam with a span greater than 25 meters. Partial interaction not allowed"
                ]
                window_error_func()
                print(
                    "Beam with a span greater than 25 meters. Partial interaction not allowed"
                )
                exit()
            ni = 1 - (E_a / (578 * fy)) * (0.75 - 0.03 * L[c])
            if ni < 0.4:
                ni = 0.4

            if Tad < Ccd[kk]:
                Fhd = Tad
            else:
                Fhd = Ccd[kk]
            S_Qrd = Fhd * ni

            wef = wa + np.sqrt(S_Qrd / Fhd) * (wi - wa)

            Mrdt = fyd * wef
            Mrdc = 0.85 * fcd * ws * alpha_e
            if Mrdt < Mrdc:
                aux2 = Mrdt
            else:
                aux2 = Mrdc
            Mrd[kk] = aux2

# =============================================================================
#           #####################################################
#           ######     CHECKING NEGATIVE BENDING MOMENT    ######
#           #####################################################
# =============================================================================

def negative_moment():
    global MdistRd, Tds, texto_erro, d3, d4, d5
    # DEFINITION OF THE NEUTRAL LINE

    Asl_e = Asl * alpha_f
    A_mesa_s = bs * tf
    A_mesa_i = bf * tf
    A_alma = h * tw

    A_total = Asl_e + A_mesa_s + A_mesa_i + A_alma

    y_ = (
        (A_mesa_i * tf / 2)
        + (A_alma * (tf + h / 2))
        + (A_mesa_s * (tf + h + tf / 2))
        + (Asl_e * (d + tc - cobrimento - diametro_barras / 2))
    ) / A_total
    a_ln[nn] = y_

    # INITIAL CHECKS

    if (bf / tf) > (
        0.38 * (np.sqrt(E_a / fy))
    ):
        texto_erro += [
            "The flange will suffer local buckling, please increase the thickness of the compressed table!"
        ]
        print(
            "\nThe flange will suffer local buckling, please increase the thickness of the compressed table!\n"
        )
    aux = (2 * (y_ - tf) - 2 * ry) / tw

    if 3.76 * np.sqrt(E_a / fy) < aux:
        texto_erro += [
            "The web section will suffer local buckling, please increase the slab thickness or change the profile"
        ]
        window_error_func()
        print(
            "The web section will suffer local buckling, please increase the slab thickness or change the profile!"
        )
        exit()

    # CROSS SECTION STRENGTH

    Tds = Asl * fsd  # reinforcement yield stress
    Tds_e = Tds * alpha_f  # equivalent reinforcement yield stress

    if classificacao == "compacta":
        #     ## COMPACT SECTION ##
        if y_ >= (tf + h):
            LN[nn] = "mesa superior"
            # Neutral line on the upper flange;
            Aac = (bf * tf) + (h * tw) + ((y_ - h - tf) * bs)
            Aat = (A_mesa_s + A_mesa_i + A_alma) - Aac
            cg_ac = (
                (A_mesa_i * tf / 2)
                + (A_alma * (tf + h / 2))
                + (((y_ - tf - h) * bs) * (((y_ - tf - h) / 2) + h + tf))
            ) / (A_mesa_i + A_alma + ((y_ - tf - h) * bs))

            cg_at = ((d - y_) * bf * (((d - y_) / 2) + (y_))) / ((d - y_) * bf)

            # Neutral line in the profile core;
        else:
            LN[nn] = "alma"
            Aac = (bf * tf) + ((y_ - tf) * tw)
            Aat = area_p - Aac
            cg_ac = (
                (A_mesa_i * tf / 2) + (((y_ - tf) * tw) * (((y_ - tf) / 2) + tf))
            ) / (A_mesa_i + ((y_ - tf) * tw))
            cg_at = (
                ((h + tf - y_) * tw) * (((h + tf - y_) / 2) + y_)
                + (bs * tf) * (d - tf / 2)
            ) / (((h + tf - y_) * tw) + (bs * tf))

        d3[nn] = (d + tc - cobrimento - diametro_barras / 2) - y_
        d4[nn] = cg_at - y_
        d5[nn] = y_ - cg_ac

        Mrd[nn] = -1 * (Tds * d3[nn] + Aat * fyd * d4[nn] + Aac * fyd * d5[nn])

        Mrk = Tds * d3[nn] * ya + Aat * fyd * \
            d4[nn] * ya + Aac * fyd * d5[nn] * ya
    else:
        #     ##   NON-COMPACT SECTION    ##
        texto_erro += ["NBR 8800 only allows compact continuous beams!"]
        window_error_func()
        print("NBR 8800 only allows compact continuous beams!")
        exit()

    # CHECKING LATERAL BUCKLING WITH CROSS SECTION DISTORTION
    Cbdist = 1
    ho = h + tf
    lambda_dist = (
        5
        * (1 + (tw * (h + tf) / (4 * bf * tf)))
        * ((fy**2 / (E_a * Cbdist) ** 2) * ((ho / tw) ** 3) * (tf / bf)) ** 0.25
    )

    if lambda_dist < 0.4:
        Xdist = 1
    elif lambda_dist <= 1.5:
        Xdist = 0.658 ** (lambda_dist**2)
    elif lambda_dist > 1.5:
        Xdist = 0.877 / (lambda_dist**2)

    MdistRd[c] = Xdist * Mrd[nn]
    Mrd[nn] = MdistRd[c]

# =============================================================================#

# =============================================================================
#           ##########################################################
#           ###    SIZING THE NUMBER AND POSITION OF CONNECTORS    ###
#           ##########################################################
# =============================================================================

def studs():
    global Qrd, pos_err, erros, n_con, espac, limitador
    area_secao_con = np.pi * (diametro_conector / 2) ** 2

    aux_1_qrd = (area_secao_con * np.sqrt(fck * E_c)) / (2)
    aux_2_qrd = (1 * 1 * area_secao_con * fucs) / ycs

    if aux_1_qrd >= aux_2_qrd:
        Qrd = aux_2_qrd
    else:
        Qrd = aux_1_qrd

    c = 0
    for k in range(trechos):
        Msd[c] = -MM[int(x_VV0[k] * 100)]

        if interacao == "Complete" or "complete":
            if LN[c] == "laje":
                n_con[c] = 2 * (
                    int((Tad / Qrd)) + 1
                )  # Number of connectors in the entire section (so times 2)
                limitador[c] = "Plastification of steel section"

            else:
                n_con[c] = 2 * (int((Ccd[c] / Qrd)) + 1)
                limitador[c] = "Concrete slab crushing"
        else:
            Fsh = np.min(Ccd[c], Tad) * (DoC / 100)
            n_con[c] = 2 * (int((Fsh / Qrd) + 1))

        L_ = round(x_MM0[c + 1] - x_MM0[c], 2)

        if trechos == 1:  # A
            recuo = cobrimento * 2

            espac[c] = round(
                (L_ - recuo - diametro_conector) / (n_con[c] - 1) - 0.0004, 3
            )
            recuo_considerado = 100 * ((L_ - (espac[c] * (n_con[c] - 1))) / 2)

        elif (
            (trechos >= 2 and k == 0)
            or (trechos == 2 and k == 1)
            or (trechos == 3 and k == 2)
        ):  
            recuo = cobrimento
            espac[c] = round((L_ - recuo) / (n_con[c]), 3)

        else:
            recuo = 0
            espac[c] = round((L_) / (n_con[c]), 3)

        if espac[c] < (
                6 * diametro_conector):  # VERIFICATION OF MINIMUM DISTANCE
            espac[c] = round((6 * diametro_conector), 3)
            n_con[c] = int((L_ - recuo) / espac[c])
            espac[c] = round((L_ - recuo) / (n_con[c]), 3)

        if espac[c] > (8 * tc):  # CHECKING THE MAXIMUM DISTANCE
            espac[c] = 8 * tc
            n_con[c] = int((L_ - recuo) / espac[c])
            espac[c] = (L_ - recuo) / (n_con[c])
        c = c + 2

    c = 1
    a = 0
    for k in range(trechos - 1):
        limitador[c] = "Plastification of steel bars"
        a = a + L[k]
        Msd[c] = -MM[int(a * 100)]

        n_con[c] = 2 * (int(Tds / Qrd) + 1)

        L_ = x_MM0[c + 1] - x_MM0[c]

        espac[c] = L_ / (n_con[c])

        if espac[c] < (
                6 * diametro_conector):  # VERIFICATION OF MINIMUM DISTANCE
            espac[c] = round((6 * diametro_conector), 3)
            n_con[c] = int((L_) / espac[c])
            espac[c] = round((L_) / (n_con[c]), 3)

        if espac[c] > (8 * tc):  # CHECKING THE MAXIMUM DISTANCE
            espac[c] = 8 * tc
            n_con[c] = int((L_) / espac[c])
            espac[c] = round((L_) / (n_con[c]), 3)
        c = c + 2

# =============================================================================#

# =============================================================================
# # ===========================================================================
# # FUNCTION THAT COMBINES THE FUNCTIONS OF NBR8800
# # ===========================================================================
# =============================================================================

def resistant_efforts():
    global kk, nn, c

    width()
    classify()
    shear()

    #    LOOP FOR CALCULATING THE POSITIVE MOMENT OF EACH SECTION
    kk = 0
    for c in range(
        trechos
    ):  # RESISTANT POSITIVE MOMENT /// RESISTANT SHEARING FORCE
        properties()  # Tad ; Ccd ; wi ; ws
        positive_moment()
        kk = kk + 2

    #    LOOP FOR CALCULATING THE NEGATIVE MOMENT OF EACH SECTION
    nn = 1
    for c in range(trechos - 1):
        negative_moment()
        nn = nn + 2

    #    CALLS THE FUNCTION THAT SIZES THE CONNECTORS
    studs()

def general_calculation():
    global fs, E_a, fy, ya, fck, yc, tc, hf, cobrimento, d1, fyd, fcd, fsd, E_c, alpha_e
    global alpha_f, massa, d, bf, bs, tw, tf, h, d_, area_p, I_p, wa, ry, Asl, diametro_barras
    global interacao

    # Pre-slab thickness (m)
    hf = 0
    # Distance from the geometric center to the upper face of this profile (m)
    d1 = d / 2
    fyd = (
        fy / ya
    )  # Calculation yield stress of structural steel
    fcd = (
        fck / yc
    )  # Calculation strength of concrete                    
    fsd = (
        fs / ya
    )  # Design yield strength of reinforcement steel (KN/m²)
    E_c = (
        4760 * (np.sqrt(fck / 1000)) * 1000
    )  # Modulus of elasticity of concrete (KN/m²)
    alpha_e = (
        E_a / E_c
    )  #Razão modular
    alpha_f = (
        fsd / fyd
    )  # Yield stress ratio between profile steel and reinforcement
    Asl = n_barras * (np.pi * (diametro_barras / 2) ** 2)

    create_vectors()
    active_efforts()
    resistant_efforts()

def check_moment():
    global texto_erro, texto_erro1, texto_erro2, texto_erro3, texto_erro4, texto_erro5, texto_erro6
    for k in range(len(Mrd)):
        if abs(Msd[k]) > abs(Mrd[k]):
            texto_erro += ["Error in region"]
            texto_erro += [k + 1]
            texto_erro += ["\nRequired moment > Moment capacity!"]
            texto_erro += ["\n\nRequired moment in the region:  "]
            texto_erro += [round(Msd[k], 2)]
            texto_erro += ["\nMoment capacity in the region:   "]
            texto_erro += [round(Mrd[k], 2)]
            window_error_func()

def shear_check():
    global texto_erro, texto_erro1, texto_erro2, texto_erro3, texto_erro4, texto_erro5, texto_erro6

    if abs(max(VV)) > abs(Vrd):
        texto_erro += ["Error...."]
        texto_erro += ["\n!Required shear > Shear capacity"]
        texto_erro += ["\n\nRequired Shear in the region:  "]
        texto_erro += [round(abs(max(VV)), 2)]
        texto_erro += ["\nShear capacity in the region:   "]
        texto_erro += [round(Vrd, 2)]
        window_error_func()

def calculation_shear_nbr():
    general_calculation()
    shear_acting_graph()
    shear_resistence_graph()
    shear_result_graph()
    write_frame_section()
    shear_check()

def calculation_moment_nbr():
    general_calculation()
    moment_acting_graph()
    moment_resistence_graph()
    moment_result_grapah()
    write_frame_section()
    check_moment()

# # # # ==================================================================
# # # # # #######################       EXCEL REPORT       ###############
# # # # ==================================================================

def func_report():
    outexcel = sl.Workbook("Report_NBR8800.xlsx")
    outsheet = outexcel.add_worksheet()
    outsheet.hide_gridlines(2)

    outsheet.set_column(0, 8, 10)

    formato_subtitulos = outexcel.add_format(
        {"bold": 1, "align": "center", "valign": "vcenter", "border": 1}
    )

    formato_c = outexcel.add_format(
        {
            "align": "center",
            "valign": "vcenter",
        }
    )

    formato_c_b = outexcel.add_format(
        {
            "align": "center",
            "bold": 1,
            "valign": "vcenter",
            "text_wrap": "true",
        }
    )

    formato_correto = outexcel.add_format(
        {
            "align": "center",
            "valign": "vcenter",
            "text_wrap": "true",
            "bg_color": "green",
        }
    )

    formato_erro = outexcel.add_format(
        {"align": "center", "valign": "vcenter", "text_wrap": "true", "bg_color": "red"}
    )

    linha = 1
    # =============================================================================
    # LINEAR DATA
    # =============================================================================
    outsheet.merge_range(0, 0, 0, 1, "LINEAR DATA", formato_subtitulos)

    outsheet.write(linha, 0, "regions=", formato_c_b)
    outsheet.write(linha, 1, trechos, formato_c)

    for n in range(trechos):
        outsheet.write(linha + n + 2, 0, "L%d=" % (n + 1), formato_c_b)
        outsheet.write(linha + n + 2, 1, L[n], formato_c)

        outsheet.write(linha + n + 5, 0, "q%d=" % (n + 1), formato_c_b)
        outsheet.write(linha + n + 5, 1, q[n], formato_c)

    linha = 2
    # =============================================================================
    # PROFILE DATA
    # =============================================================================

    outsheet.merge_range("C1:H1", "SECTION DATA", formato_subtitulos)

    outsheet.write(linha + 2, 3, "bf=", formato_c_b)
    outsheet.write(linha + 2, 4, bf, formato_c)
    outsheet.write(linha + 3, 3, "tf=", formato_c_b)
    outsheet.write(linha + 3, 4, tf, formato_c)
    outsheet.write(linha + 4, 3, "h=", formato_c_b)
    outsheet.write(linha + 4, 4, h, formato_c)
    outsheet.write(linha + 5, 3, "d=", formato_c_b)
    outsheet.write(linha + 5, 4, d, formato_c)
    outsheet.write(linha + 6, 3, "d'=", formato_c_b)
    outsheet.write(linha + 6, 4, d_, formato_c)

    outsheet.write(linha + 2, 6, "tw=", formato_c_b)
    outsheet.write(linha + 2, 7, tw, formato_c)
    outsheet.write(linha + 3, 6, "ry=", formato_c_b)
    outsheet.write(linha + 3, 7, ry, formato_c)
    outsheet.write(linha + 4, 6, "Wx=", formato_c_b)
    outsheet.write(linha + 4, 7, Wx, formato_c)
    outsheet.write(linha + 5, 6, "Ix=", formato_c_b)
    outsheet.write(linha + 5, 7, I_p, formato_c)
    outsheet.write(linha + 6, 6, "Área=", formato_c_b)
    outsheet.write(linha + 6, 7, area_p, formato_c)

    outsheet.insert_image(linha + 8, 1, "imagens\\SECAO_330x344.png")
    # =============================================================================
    # GENERAL DATA
    # =============================================================================
    linha = 10

    outsheet.merge_range(
        linha,
        6,
        linha,
        7,
        "GENERAL DATA",
        formato_subtitulos)

    outsheet.write(linha + 1, 6, "Interação=", formato_c_b)
    outsheet.write(linha + 1, 7, interacao, formato_c)
    outsheet.write(linha + 2, 6, "Lb_máx=", formato_c_b)
    outsheet.write(linha + 2, 7, Lb_max, formato_c)
    outsheet.write(linha + 3, 6, "tc=", formato_c_b)
    outsheet.write(linha + 3, 7, tc, formato_c)
    outsheet.write(linha + 4, 6, "Nº barras=", formato_c_b)
    outsheet.write(linha + 4, 7, n_barras, formato_c)
    outsheet.write(linha + 5, 6, "Ø barras=", formato_c_b)
    outsheet.write(linha + 5, 7, diametro_barras, formato_c)
    outsheet.write(linha + 6, 6, "c=", formato_c_b)
    outsheet.write(linha + 6, 7, cobrimento, formato_c)
    outsheet.write(linha + 7, 6, "fucs=", formato_c_b)
    outsheet.write(linha + 7, 7, fucs, formato_c)
    outsheet.write(linha + 8, 6, "Ø conector=", formato_c_b)
    outsheet.write(linha + 8, 7, diametro_conector, formato_c)
    outsheet.write(linha + 9, 6, "y conector=", formato_c_b)
    outsheet.write(linha + 9, 7, ycs, formato_c)
    if interacao == "Partial":
        outsheet.write(linha + 10, 6, "DoC=", formato_c_b)
        outsheet.write(linha + 10, 7, DoC, formato_c)

    # =============================================================================
    # MATERIALS
    # =============================================================================
    linha = 21

    outsheet.merge_range(linha, 6, linha, 7, "MATERIALS", formato_subtitulos)

    outsheet.write(linha + 1, 6, "fck=", formato_c_b)
    outsheet.write(linha + 1, 7, fck, formato_c)
    outsheet.write(linha + 2, 6, "yc=", formato_c_b)
    outsheet.write(linha + 2, 7, yc, formato_c)
    outsheet.write(linha + 3, 6, "E aço=", formato_c_b)
    outsheet.write(linha + 3, 7, E_a, formato_c)
    outsheet.write(linha + 4, 6, "fy=", formato_c_b)
    outsheet.write(linha + 4, 7, fy, formato_c)
    outsheet.write(linha + 5, 6, "ya=", formato_c_b)
    outsheet.write(linha + 5, 7, ya, formato_c)
    outsheet.write(linha + 6, 6, "E armadura=", formato_c_b)
    outsheet.write(linha + 6, 7, E_as, formato_c)
    outsheet.write(linha + 7, 6, "fs=", formato_c_b)
    outsheet.write(linha + 7, 7, fs, formato_c)
    outsheet.write(linha + 8, 6, "ys=", formato_c_b)
    outsheet.write(linha + 8, 7, ys, formato_c)

    # =============================================================================
    # OTHERS
    # =============================================================================
    linha = 31
    outsheet.merge_range(linha, 0, linha, 7, "OTHERS", formato_subtitulos)

    outsheet.write(linha + 1, 0, "hf=", formato_c_b)
    outsheet.write(linha + 1, 1, hf, formato_c)
    outsheet.write(linha + 2, 0, "fyd=", formato_c_b)
    outsheet.write(linha + 2, 1, fyd, formato_c)

    outsheet.write(linha + 1, 2, "fcd=", formato_c_b)
    outsheet.write(linha + 1, 3, fcd, formato_c)
    outsheet.write(linha + 2, 2, "fsd=", formato_c_b)
    outsheet.write(linha + 2, 3, fsd, formato_c)

    outsheet.write(linha + 1, 4, "E concreto=", formato_c_b)
    outsheet.write(linha + 1, 5, E_c, formato_c)
    outsheet.write(linha + 2, 4, "Asl=", formato_c_b)
    outsheet.write(linha + 2, 5, Asl, formato_c)

    outsheet.write(linha + 1, 6, "alpha e=", formato_c_b)
    outsheet.write(linha + 1, 7, alpha_e, formato_c)
    outsheet.write(linha + 2, 6, "alpha f=", formato_c_b)
    outsheet.write(linha + 2, 7, alpha_f, formato_c)

    # =============================================================================
    # # ======================================================================
    # # NBR 8800
    # # ======================================================================
    # =============================================================================

    # =============================================================================
    # EFFECTIVE width
    # =============================================================================
    linha = 36

    outsheet.merge_range(
        linha,
        0,
        linha,
        7,
        "EFFECTIVE width",
        formato_subtitulos)

    if trechos == 1:
        outsheet.insert_image(
            linha + 2, 0, "imagens\a_trecho.jpeg", {"x_scale": 0.65, "y_scale": 0.65}
        )
    elif trechos == 2:
        outsheet.insert_image(
            linha + 2, 0, "imagens\b_trecho.png", {"x_scale": 0.3, "y_scale": 0.3}
        )
    else:
        outsheet.insert_image(
            linha + 2, 0, "imagens\\c_trecho.png", {"x_scale": 0.3, "y_scale": 0.3}
        )
    l = 45
    c = 0
    for n in range(size_vetor):
        l = l + 0.3
        outsheet.write(int(l), c, "Lb %d =" % (n + 1), formato_c_b)
        outsheet.write(int(l), c + 1, lb[n], formato_c_b)
        outsheet.write(int(l) - 5 + n, 6, "L%d efetivo=" % (n + 1), formato_c)
        outsheet.write(int(l) - 5 + n, 7, x_MM0[n + 1] - x_MM0[n], formato_c)
        c = c + 3
        if c == 9:
            c = 0

    # =============================================================================
    # SECTION CLASSIFICATION
    # =============================================================================

    outsheet.merge_range("A48:H48", "CLASSIFICATION", formato_subtitulos)

    outsheet.merge_range("A49:H49", classificacao, formato_c_b)

    linha = 50

    outsheet.write(linha - 1, 1, "λ=%d" % lambda_, formato_c_b)
    outsheet.write(linha - 1, 3, "λp= %d" % lambda_p, formato_c_b)
    outsheet.write(linha - 1, 5, "λr= %d" % lambda_r, formato_c_b)

    # =============================================================================
    # PROPERTIES
    # =============================================================================

    outsheet.merge_range("A52:H52", "PROPERTIES", formato_subtitulos)

    # Concrete slab calculation bearing force

    outsheet.merge_range(
        "A54:D54",
        "Strength of Concrete Slab",
        formato_subtitulos)
    linha = linha + 5
    for n in range(size_vetor):
        outsheet.write(linha + n, 1, "Ccd%d=" % (n + 1), formato_c_b)
        if n == 1 or n == 3:
            outsheet.write(linha + n, 2, "tensile", formato_c)
        else:
            outsheet.write(linha + n, 2, Ccd[n], formato_c)

    # Profile calculation resistant force

    outsheet.merge_range(
        "E54:H54",
        "Strength of steel section",
        formato_subtitulos)

    outsheet.write(linha, 5, "Tad=", formato_c_b)
    outsheet.write(linha, 6, Tad, formato_c)

    # Elastic modulus of resistance of the section

    outsheet.merge_range(
        "A63:D65",
        "Section elastic modulus of resistance \n mixed transverse in relation to the bending axis \n higher than CG.",
        formato_c_b,
    )
    outsheet.merge_range(
        "E63:H65",
        "Section elastic modulus of resistance \n mixed transverse in relation to the bending axis \n lower than CG.",
        formato_c_b,
    )
    linha = linha + 12
    for n in range(size_vetor):
        outsheet.write(linha + n, 1, "ws %d=" % (n + 1), formato_c_b)
        outsheet.write(linha + n, 2, ws_vetor[n], formato_c)

        outsheet.write(linha + n, 5, "wi %d=" % (n + 1), formato_c_b)
        outsheet.write(linha + n, 6, wi_vetor[n], formato_c)

    # =============================================================================
    # CHECKING THE CUTTING FORCE
    # =============================================================================

    linha = linha + 12
    outsheet.merge_range("A75:H75", "REQUIRED SHEAR", formato_subtitulos)

    outsheet.merge_range(
        "A77:H77",
        "The required shear is given considering the resistance of the steel section!",
        formato_c_b,
    )

    outsheet.write(linha, 1, "k=", formato_c_b)
    outsheet.write(linha, 2, 5, formato_c)
    outsheet.write(linha + 1, 1, "Vpl=", formato_c_b)
    outsheet.write(linha + 1, 2, Vpl, formato_c)
    outsheet.write(linha + 2, 1, "Vrd=", formato_subtitulos)
    outsheet.write(linha + 2, 2, Vrd, formato_c_b)

    outsheet.write(linha, 5, "λ=", formato_c_b)
    outsheet.write(linha, 6, round(lambda_corte, 2), formato_c)
    outsheet.write(linha + 1, 5, "λp=", formato_c_b)
    outsheet.write(linha + 1, 6, round(lambda_p_corte, 2), formato_c)
    outsheet.write(linha + 2, 5, "λr=", formato_c_b)
    outsheet.write(linha + 2, 6, round(lambda_r_corte, 2), formato_c)

    # =============================================================================
    # POSITIVE MOMENT
    # =============================================================================

    linha = linha + 4
    outsheet.merge_range(
        linha,
        0,
        linha,
        7,
        "POSITIVE MOMENT",
        formato_subtitulos)

    xlsx1 = 0
    xlsx2 = 0

    outsheet.merge_range(
        linha + 2,
        0,
        linha + 2,
        4,
        "Compressed section thickness",
        formato_subtitulos)

    linha = linha + 3

    for n in range(size_vetor):
        outsheet.write(linha + n, 0, "Trecho %d" % (n + 1), formato_c_b)
        if n == 1 or n == 3:
            outsheet.merge_range(
                linha + n, 1, linha + n, 4, "Negative Moment", formato_c
            )
        else:
            outsheet.merge_range(
                linha +
                n,
                1,
                linha +
                n,
                2,
                "Neutral line in %s" %
                LN[n],
                formato_c)
            outsheet.write(linha + n, 3, "Hc=", formato_c_b)
            outsheet.write(linha + n, 4, round(a_ln[n], 4), formato_c)

        linha = linha + 8
        xlsx1 = 8
        xlsx2 = 11

    outsheet.merge_range(
        linha + 2 - xlsx2,
        6,
        linha + 2 - xlsx2,
        7,
        "Moment Capacity",
        formato_subtitulos,
    )
    for n in range(size_vetor):
        if n == 1 or n == 3:
            outsheet.merge_range(
                linha + n - xlsx1,
                6,
                linha + n - 8,
                7,
                "Negative Moment",
                formato_c)
        else:
            outsheet.write(
                linha + n - xlsx1, 6, "Mrd %d=" %
                (n + 1), formato_c_b)
            outsheet.write(linha + n - xlsx1, 7, round(Mrd[n], 2), formato_c_b)
    linha = linha + 8
    linha = linha - xlsx1

    # =============================================================================
    # NEGATIVE MOMENT
    # =============================================================================

    outsheet.merge_range(
        linha,
        0,
        linha,
        7,
        "NEGATIVE MOMENT",
        formato_subtitulos)

    xlsx1 = 0

    for n in range(size_vetor):
        if n == 1 or n == 3:
            outsheet.merge_range(
                linha + 2, 1, linha + 2, 6, "REGION %d" %
                (n + 1), formato_subtitulos)

            outsheet.merge_range(
                linha + 3, 1, linha + 3, 5, "Compressed section thickness ="
            )
            outsheet.write(
                linha + 3 + xlsx1,
                6,
                round(
                    a_ln[n],
                    5),
                formato_c_b)

            outsheet.merge_range(
                linha + 4,
                1,
                linha + 4,
                5,
                "d3 = distancia do CG da armadura à linha neutra =",
            )
            outsheet.write(linha + 4 + xlsx1, 6, round(d3[n], 2), formato_c_b)

            outsheet.merge_range(
                linha +
                5,
                1,
                linha +
                5,
                5,
                "d4 = distance from the CG of the armature to the neutral axis =",
            )
            outsheet.write(linha + 5 + xlsx1, 6, round(d4[n], 2), formato_c_b)

            outsheet.merge_range(
                linha +
                6,
                1,
                linha +
                6,
                5,
                "d5 = distance from the CG of the compressed area to the neutral axis =",
            )
            outsheet.write(linha + 6 + xlsx1, 6, round(d5[n], 2), formato_c_b)

            outsheet.merge_range(
                linha + 7, 1, linha + 7, 5, "bending moment capacity ="
            )
            outsheet.write(linha + 7 + xlsx1, 6, round(Mrd[n], 2), formato_c_b)

            linha = linha + 7

    # =============================================================================
    # VERIFICATION OF SHEAR AND MOMENTS
    # =============================================================================

    linha = linha + 3
    outsheet.merge_range(linha, 0, linha, 7, "CHECKS", formato_subtitulos)

    linha = linha + 2

    outsheet.merge_range(
        linha,
        2,
        linha,
        5,
        "Bending Moment",
        formato_subtitulos)
    outsheet.write(linha + 1, 2, "Regions", formato_subtitulos)
    outsheet.write(linha + 1, 3, "Mrd", formato_subtitulos)
    outsheet.write(linha + 1, 4, "Msd", formato_subtitulos)
    outsheet.write(linha + 1, 5, "Status", formato_subtitulos)

    linha = linha + 2

    for n in range(size_vetor):
        if np.sqrt(Mrd[n] ** 2) >= np.sqrt(msd_max_[n] ** 2):
            outsheet.write(linha + n, 2, "Region %d" % n, formato_c)
            outsheet.write(linha + n, 3, round(Mrd[n], 2), formato_c)
            outsheet.write(linha + n, 4, round(msd_max_[n], 2), formato_c)
            outsheet.write(linha + n, 5, "OK!", formato_correto)
        else:
            outsheet.write(linha + n, 2, "Region %d" % n, formato_c)
            outsheet.write(linha + n, 3, round(Mrd[n], 2), formato_c)
            outsheet.write(linha + n, 4, round(msd_max_[n], 2), formato_c)
            outsheet.write(linha + n, 5, "FAILURE!", formato_erro)

    linha = linha + 6

    outsheet.merge_range(
        linha,
        2,
        linha,
        5,
        "Shear required",
        formato_subtitulos)
    outsheet.write(linha + 1, 2, "Region", formato_subtitulos)
    outsheet.write(linha + 1, 3, "Vrd", formato_subtitulos)
    outsheet.write(linha + 1, 4, "Vsd", formato_subtitulos)
    outsheet.write(linha + 1, 5, "Status", formato_subtitulos)

    linha = linha + 2
    for n in range(size_vetor):
        if Vrd >= vsd_max_[n]:
            outsheet.write(linha + n, 2, "Region %d" % n, formato_c)
            outsheet.write(linha + n, 3, round(Vrd, 2), formato_c)
            outsheet.write(linha + n, 4, round(vsd_max_[n], 2), formato_c)
            outsheet.write(linha + n, 5, "OK!", formato_correto)
        else:
            outsheet.write(linha + n, 2, "Region %d" % n, formato_c)
            outsheet.write(linha + n, 3, round(Vrd, 2), formato_c)
            outsheet.write(linha + n, 4, round(vsd_max_[n], 2), formato_c)
            outsheet.write(linha + n, 5, "FAILURE!", formato_erro)

    # =============================================================================
    # STUDS
    # =============================================================================

    linha = linha + 7
    outsheet.merge_range(linha, 0, linha, 7, "SHEAR STUDS", formato_subtitulos)

    outsheet.write(linha + 2, 1, "Regions", formato_subtitulos)
    outsheet.write(linha + 2, 2, "Qrd", formato_subtitulos)
    outsheet.write(linha + 2, 3, "Nº con.", formato_subtitulos)
    outsheet.write(linha + 2, 4, "Pitch", formato_subtitulos)
    outsheet.merge_range(
        linha + 2, 5, linha + 2, 7, "STUDS LIMATITION", formato_subtitulos
    )

    linha = linha + 3
    for n in range(size_vetor):
        outsheet.write(linha + n, 1, "Region %d" % n, formato_c)
        outsheet.write(linha + n, 2, round(Qrd, 3), formato_c)
        outsheet.write(linha + n, 3, n_con[n], formato_c)
        outsheet.write(linha + n, 4, round(espac[n], 3), formato_c)
        outsheet.merge_range(
            linha + n,
            5,
            linha + n,
            7,
            limitador[n],
            formato_c)

    outexcel.close()

cont1 = 0
contador = (len(dados[:, 1])) - 1
teste_insere_perfil = 0

# =============================================================================
# =============================================================================
# =============================================================================
# # # =========================================================================
# # # # ####################### GRAPHICAL USER INTERFACE ######################
# # # =========================================================================
# =============================================================================
# =============================================================================

def rewrite_labels_frame1():
    la_VA_bf = tk.Label(Frame2)
    Config_frame(la_VA_bf, relx=0.176, rely=0.487, height=26, width=72,
                 ft=S_font9, text=bf)

    la_VA_tf = tk.Label(Frame2)
    Config_frame(la_VA_tf, relx=0.176, rely=0.526, height=26, width=72,
                 ft=S_font9, text=tf)

    la_VA_h = tk.Label(Frame2)
    Config_frame(la_VA_h, relx=0.176, rely=0.564, height=26, width=72,
                 ft=S_font9, text=h)

    la_VA_d = tk.Label(Frame2)
    Config_frame(la_VA_d, relx=0.176, rely=0.603, height=25, width=72,
                 ft=S_font9, text=d)

    la_VA_d_ = tk.Label(Frame2)
    Config_frame(la_VA_d_, relx=0.176, rely=0.641, height=26, width=72,
                 ft=S_font9, text=d_)

    la_VA_tw = tk.Label(Frame2)
    Config_frame(la_VA_tw, relx=0.618, rely=0.487, height=26, width=72,
                 ft=S_font9, text=tw)

    la_VA_ry = tk.Label(Frame2)
    Config_frame(la_VA_ry, relx=0.618, rely=0.526, height=26, width=72,
                 ft=S_font9, text=ry)

    la_VA_wx = tk.Label(Frame2)
    Config_frame(la_VA_wx, relx=0.618, rely=0.564, height=26, width=72,
                 ft=S_font9, text=Wx)

    la_VA_ix = tk.Label(Frame2)
    Config_frame(la_VA_ix, relx=0.618, rely=0.603, height=26, width=72,
                 ft=S_font9, text=I_p)

    la_VA_area = tk.Label(Frame2)
    Config_frame(la_VA_area, relx=0.618, rely=0.641, height=25, width=72,
                 ft=S_font9, text=area_p)

    la_VA_tc = tk.Label(Frame2)
    Config_frame(la_VA_tc, relx=0.176, rely=0.731, height=25, width=72,
                 ft=S_font9, text=tc)

    la_VA_n_barras = tk.Label(Frame2)
    Config_frame(la_VA_n_barras, relx=0.162, rely=0.821, height=25, width=52,
                 ft=S_font9, text=n_barras)

    la_VA_diametro_barras = tk.Label(Frame2)
    Config_frame(la_VA_diametro_barras, relx=0.471, rely=0.821, height=25,
                 width=52, ft=S_font9, text=diametro_barras)

    la_VA_cobri = tk.Label(Frame2)
    Config_frame(la_VA_cobri, relx=0.765, rely=0.821, height=25, width=52,
                 ft=S_font9, text=cobrimento)

    la_VA_fucs = tk.Label(Frame2)
    Config_frame(la_VA_fucs, relx=0.176, rely=0.91, height=26, width=72,
                 ft=S_font9, text=fucs)

    la_VA_γc = tk.Label(Frame2)
    Config_frame(la_VA_γc, relx=0.588, rely=0.91, height=26, width=72,
                 ft=S_font9, text=ycs)

    la_VA_Ø = tk.Label(Frame2)
    Config_frame(la_VA_Ø, relx=0.176, rely=0.949, height=25, width=72,
                 ft=S_font9, text=diametro_conector)

# =============================================================================
# WINDOW GEOMETRY
# =============================================================================

def call_geometry_window():
    # =========================================================================
    #     #           PROFILE INPUT
    # =========================================================================
    def call_ja_geo_per_insert():
        janela_perfil_inserir = tk.Tk()

        janela_perfil_inserir.geometry("340x500+600+4")
        janela_perfil_inserir.minsize(148, 1)
        janela_perfil_inserir.maxsize(1924, 1055)
        janela_perfil_inserir.resizable(0, 0)
        janela_perfil_inserir.iconbitmap("icones/geral.ico")
        janela_perfil_inserir.title("Section Options")
        janela_perfil_inserir.configure(background="#d9d9d9")
        janela_perfil_inserir.configure(highlightbackground="#d9d9d9")
        janela_perfil_inserir.configure(highlightcolor="black")

        Frame2 = tk.Frame(janela_perfil_inserir)
        Frame2.place(relx=0.029, rely=0.014, relheight=0.84, relwidth=0.941)
        Frame2.configure(relief="groove")
        Frame2.configure(borderwidth="2")
        Frame2.configure(relief="groove")
        Frame2.configure(background="#d9d9d9")
        Frame2.configure(cursor="fleur")
        Frame2.configure(highlightbackground="#d9d9d9")
        Frame2.configure(highlightcolor="black")

        la_perfil = tk.Label(Frame2)
        Config_frame(la_perfil, relx=0.031, rely=0.021, height=14, width=49,
                     ft=Sbi_font10, text="""Section""")

        la_bf = tk.Label(Frame2)
        Config_frame(la_bf, relx=0.031, rely=0.088, height=13, width=40,
                     ft=S_font9, text="""bf=""")

        la_tf = tk.Label(Frame2)
        Config_frame(la_tf, relx=0.028, rely=0.152, height=14, width=40,
                     ft=S_font9, text="""tf=""")

        la_h = tk.Label(Frame2)
        Config_frame(la_h, relx=0.028, rely=0.219, height=13, width=40,
                     ft=S_font9, text="""h=""")

        la_d = tk.Label(Frame2)
        Config_frame(la_d, relx=0.028, rely=0.283, height=14, width=40,
                     ft=S_font9, text="""d=""")

        la_d_ = tk.Label(Frame2)
        Config_frame(la_d_, relx=0.028, rely=0.35, height=13, width=40,
                     ft=S_font9, text="""d_=""")
        la_d_.place(relx=0.028, rely=0.35, height=13, width=40)

        la_tw = tk.Label(Frame2)
        Config_frame(la_tw, relx=0.472, rely=0.088, height=13, width=40,
                     ft=S_font9, text="""tw=""")

        la_ry = tk.Label(Frame2)
        Config_frame(la_ry, relx=0.472, rely=0.152, height=14, width=40,
                     ft=S_font9, text="""ry=""")

        la_wx = tk.Label(Frame2)
        Config_frame(la_wx, relx=0.469, rely=0.219, height=13, width=40,
                     ft=S_font9, text="""wx=""")

        la_ix = tk.Label(Frame2)
        Config_frame(la_ix, relx=0.469, rely=0.283, height=14, width=40,
                     ft=S_font9, text="""Ix=""")

        la_area = tk.Label(Frame2)
        Config_frame(la_area, relx=0.469, rely=0.35, height=13, width=40,
                     ft=S_font9, text="""Area=""")

        la_slab = tk.Label(Frame2)
        Config_frame(la_slab, relx=0.028, rely=0.45, height=14,
                     width=45, ft=Sbi_font10, text="""Slab""")

        la_tc = tk.Label(Frame2)
        Config_frame(la_tc, relx=0.028, rely=0.5, height=13, width=40,
                     ft=S_font9, text="""tc=""")

        la_Lb_max = tk.Label(Frame2)
        Config_frame(la_Lb_max, relx=0.430, rely=0.5, height=14, width=50,
                     ft=S_font9, text="""Lb_máx=""")

        la_armadura_longitudinal = tk.Label(Frame2)
        Config_frame(
            la_armadura_longitudinal,
            relx=0.028,
            rely=0.567,
            height=14,
            width=125,
            ft=Sbi_font10,
            text="""Longitudinal Bars""")

        la_n_barras = tk.Label(Frame2)
        Config_frame(la_n_barras, relx=0.01, rely=0.631, height=14, width=55,
                     ft=S_font9, text="""Bar Nº=""")

        la_Ø_barras = tk.Label(Frame2)
        Config_frame(la_Ø_barras, relx=0.338, rely=0.631, height=14, width=40,
                     ft=S_font9, text="""Ø=""")

        la_cobri = tk.Label(Frame2)
        Config_frame(la_cobri, relx=0.647, rely=0.631, height=14, width=40,
                     ft=S_font9, text="""c=""")

        la_conectores = tk.Label(Frame2)
        Config_frame(
            la_conectores,
            relx=0.028,
            rely=0.731,
            height=13,
            width=49,
            ft=Sbi_font10,
            text="""Stud=""")

        la_Ø = tk.Label(Frame2)
        Config_frame(la_Ø, relx=0.472, rely=0.795, height=14, width=29,
                     ft=S_font9, text="""Ø=""")

        la_fucs = tk.Label(Frame2)
        Config_frame(la_fucs, relx=0.028, rely=0.795, height=14, width=40,
                     ft=S_font9, text="""fucs=""")

        la_γc = tk.Label(Frame2)
        Config_frame(la_γc, relx=0.031, rely=0.862, height=13, width=40,
                     ft=S_font9, text="""γc=""")

        if teste_insere_perfil == 0:
            box_perfi_bf = tk.Entry(Frame2)
            Config_box(box_perfi_bf, relx=0.175, rely=0.076, height=25,
                       relwidth=0.25, ft=tk_font)

            box_perfi_tf = tk.Entry(Frame2)
            Config_box(box_perfi_tf, relx=0.175, rely=0.143, height=25,
                       relwidth=0.25, ft=tk_font)

            box_perfi_h = tk.Entry(Frame2)
            Config_box(box_perfi_h, relx=0.175, rely=0.207, height=25,
                       relwidth=0.25, ft=tk_font)

            box_perfi_d = tk.Entry(Frame2)
            Config_box(box_perfi_d, relx=0.175, rely=0.271, height=25,
                       relwidth=0.25, ft=tk_font)

            box_perfi_d_ = tk.Entry(Frame2)
            Config_box(box_perfi_d_, relx=0.175, rely=0.338, height=25,
                       relwidth=0.25, ft=tk_font)

            box_perfi_tw = tk.Entry(Frame2)
            Config_box(box_perfi_tw, relx=0.625, rely=0.076, height=25,
                       relwidth=0.25, ft=tk_font)

            box_perfi_ry = tk.Entry(Frame2)
            Config_box(box_perfi_ry, relx=0.625, rely=0.143, height=25,
                       relwidth=0.25, ft=tk_font)

            box_perfi_Wx = tk.Entry(Frame2)
            Config_box(box_perfi_Wx, relx=0.625, rely=0.207, height=25,
                       relwidth=0.25, ft=tk_font)

            box_perfi_Ix = tk.Entry(Frame2)
            Config_box(box_perfi_Ix, relx=0.625, rely=0.271, height=25,
                       relwidth=0.25, ft=tk_font)

            box_perfi_profilearea = tk.Entry(Frame2)
            Config_box(
                box_perfi_profilearea,
                relx=0.625,
                rely=0.338,
                height=25,
                relwidth=0.25,
                ft=tk_font)

        else:
            la_VA_perfil_bf = tk.Label(Frame2)
            Config_frame(la_VA_perfil_bf, relx=0.156, rely=0.067, height=26,
                         width=72, ft=S_font9, text=round(bf, 4))

            la_VA_perfil_tf = tk.Label(Frame2)
            Config_frame(la_VA_perfil_tf, relx=0.156, rely=0.138, height=26,
                         width=72, ft=S_font9, text=round(tf, 4))

            la_VA_perfil_h = tk.Label(Frame2)
            Config_frame(la_VA_perfil_h, relx=0.156, rely=0.21, height=26,
                         width=72, ft=S_font9, text=round(h, 4))

            la_VA_perfil_d = tk.Label(Frame2)
            Config_frame(la_VA_perfil_d, relx=0.156, rely=0.281, height=26,
                         width=72, ft=S_font9, text=round(d, 4))

            la_VA_perfil_d_ = tk.Label(Frame2)
            Config_frame(la_VA_perfil_d_, relx=0.156, rely=0.352, height=26,
                         width=72, ft=S_font9, text=round(d_, 4))

            la_VA_perfil_tw = tk.Label(Frame2)
            Config_frame(la_VA_perfil_tw, relx=0.594, rely=0.067, height=26,
                         width=72, ft=S_font9, text=round(tw, 4))

            la_VA_perfil_ry = tk.Label(Frame2)
            Config_frame(la_VA_perfil_ry, relx=0.594, rely=0.138, height=26,
                         width=72, ft=S_font9, text=round(ry, 4))

            la_VA_perfil_Wx = tk.Label(Frame2)
            Config_frame(la_VA_perfil_Wx, relx=0.594, rely=0.21, height=26,
                         width=72, ft=S_font9, text=round(Wx, 6))

            la_VA_perfil_Ix = tk.Label(Frame2)
            Config_frame(la_VA_perfil_Ix, relx=0.594, rely=0.281, height=26,
                         width=72, ft=S_font9, text=round(I_p, 6))

            la_VA_perfil_area = tk.Label(Frame2)
            Config_frame(la_VA_perfil_area, relx=0.594, rely=0.352, height=26,
                         width=72, ft=S_font9, text=round(area_p, 4))

        box_laje_tc = tk.Entry(Frame2)
        Config_entry(box_laje_tc, relx=0.156, rely=0.488, height=25,
                     relwidth=0.156)

        box_laje_Lb_max = tk.Entry(Frame2)
        Config_entry(box_laje_Lb_max, relx=0.622, rely=0.488, height=25,
                     relwidth=0.25)

        box_N_barras = tk.Entry(Frame2)
        Config_entry(box_N_barras, relx=0.19, rely=0.621, height=25,
                     relwidth=0.156)

        box_Ø_barras = tk.Entry(Frame2)
        Config_entry(box_Ø_barras, relx=0.453, rely=0.621, height=25,
                     relwidth=0.156)

        box_As_cobri = tk.Entry(Frame2)
        Config_entry(box_As_cobri, relx=0.75, rely=0.621, height=25,
                     relwidth=0.156)

        box_conector_fucs = tk.Entry(Frame2)
        Config_entry(box_conector_fucs, relx=0.156, rely=0.786, height=25,
                     relwidth=0.156)

        box_conector_γc = tk.Entry(Frame2)
        Config_entry(box_conector_γc, relx=0.156, rely=0.857, height=25,
                     relwidth=0.156)

        box_conector_Ø = tk.Entry(Frame2)
        Config_entry(box_conector_Ø, relx=0.563, rely=0.786, height=25,
                     relwidth=0.156)

        def take_entry_profile():
            global tc, Lb_max, n_barras, diametro_barras, cobrimento, fucs, yc_conector, diametro_conector
            #            if (teste_entry==1):
            global d, tf, h, d_, bf, tw, Wx, Ix, area_p, ry, I_p, ycs

            tc = float(box_laje_tc.get())
            Lb_max = float(box_laje_Lb_max.get())
            n_barras = float(box_N_barras.get())
            diametro_barras = float(box_Ø_barras.get())
            cobrimento = float(box_As_cobri.get())
            fucs = float(box_conector_fucs.get())
            yc_conector = float(box_conector_γc.get())
            diametro_conector = float(box_conector_Ø.get())

            ycs = yc_conector

            if teste_insere_perfil == 0:
                d = float(box_perfi_d.get())
                tf = float(box_perfi_tf.get())
                h = float(box_perfi_h.get())
                d_ = float(box_perfi_d_.get())
                bf = float(box_perfi_bf.get())
                tw = float(box_perfi_tw.get())
                Wx = float(box_perfi_Wx.get())
                I_p = float(box_perfi_Ix.get())
                ry = float(box_perfi_ry.get())
                area_p = float(box_perfi_area_perfil.get())

            janela_perfil_inserir.destroy()
            janela_geometria.destroy()

            rewrite_labels_frame1()

        btn_destroy_perfil_inserir = tk.Button(janela_perfil_inserir)
        btn_destroy_perfil_inserir.place(
            relx=0.353, rely=0.89, height=40, width=100)
        btn_destroy_perfil_inserir.configure(activebackground="#ececec")
        btn_destroy_perfil_inserir.configure(activeforeground="#000000")
        btn_destroy_perfil_inserir.configure(background="#0000ff")
        btn_destroy_perfil_inserir.configure(disabledforeground="#a3a3a3")
        btn_destroy_perfil_inserir.configure(foreground="#ffffff")
        btn_destroy_perfil_inserir.configure(highlightbackground="#d9d9d9")
        btn_destroy_perfil_inserir.configure(highlightcolor="black")
        btn_destroy_perfil_inserir.configure(pady="0")
        btn_destroy_perfil_inserir.configure(text=""">>>""")
        btn_destroy_perfil_inserir.configure(command=take_entry_profile)

        janela_perfil_inserir.mainloop()

    # =========================================================================
    #     #           PROFILE SLECT
    # =========================================================================

    def call_ja_geo_per_select():
        global teste_insere_perfil
        global d, tf, h, d_, bf, bs, tw, Wx, I_p, area_p, ry
        teste_insere_perfil = 1

        janela_selecionar = tk.Tk()

        janela_selecionar.geometry("400x600+922+109")
        janela_selecionar.minsize(148, 1)
        janela_selecionar.maxsize(1924, 1055)
        janela_selecionar.resizable(1, 1)
        janela_selecionar.title("Section Select")
        janela_selecionar.configure(background="#d9d9d9")
        janela_selecionar.iconbitmap("icones/geral.ico")

        listbox_perfis = tk.Listbox(janela_selecionar)
        listbox_perfis.place(
            relx=0.025,
            rely=0.05,
            relheight=0.83,
            relwidth=0.95)
        listbox_perfis.configure(background="white")
        listbox_perfis.configure(disabledforeground="#a3a3a3")
        listbox_perfis.configure(font="TkFixedFont")
        listbox_perfis.configure(foreground="#000000")
        ######     ADD A PROFILE TYPE IN A LIST OF PROFILE     #####
        nn = 2
        while nn <= contador:
            listbox_perfis.insert((nn - 2), dada_numérico[nn, 0:2])
            nn = nn + 1

        ######     ASSIGN SELECTED LIST VALUE    #####
        def take_xlsx_profile():
            global d, tf, h, d_, bf, bs, tw, Wx, I_p, area_p, ry
            n = listbox_perfis.curselection()  # Get the value of the selected row
            n = int(n[0])  # Transform into integer
            perfil = dados[n, :]  # Get line related to the selected profile

            d = perfil[1] / 1000
            tf = perfil[5] / 1000
            h = perfil[6] / 1000
            d_ = perfil[7] / 1000 
            bf = perfil[2] / 1000
            bs = perfil[3] / 1000
            tw = perfil[4] / 1000
            Wx = perfil[10] / 1e6
            I_p = perfil[9] / 1e8
            area_p = perfil[8] / 10000  
            ry = perfil[15] / 100
            janela_selecionar.destroy()
            call_ja_geo_per_insert()

        botao_seguinte_selecioneperfil = tk.Button(janela_selecionar)
        botao_seguinte_selecioneperfil.place(
            relx=0.375, rely=0.917, height=33, width=100
        )
        botao_seguinte_selecioneperfil.configure(activebackground="#ececec")
        botao_seguinte_selecioneperfil.configure(activeforeground="#000000")
        botao_seguinte_selecioneperfil.configure(background="#000080")
        botao_seguinte_selecioneperfil.configure(disabledforeground="#a3a3a3")
        botao_seguinte_selecioneperfil.configure(foreground="#ffffff")
        botao_seguinte_selecioneperfil.configure(highlightbackground="#d9d9d9")
        botao_seguinte_selecioneperfil.configure(highlightcolor="#ffffff")
        botao_seguinte_selecioneperfil.configure(pady="0")
        botao_seguinte_selecioneperfil.configure(text=""">>>""")
        botao_seguinte_selecioneperfil.configure(command=take_xlsx_profile)

        la_seleciona_perfil = tk.Label(janela_selecionar)
        la_seleciona_perfil.place(relx=-0.025, rely=0.0, height=26, width=192)
        la_seleciona_perfil.configure(background="#d9d9d9")
        la_seleciona_perfil.configure(disabledforeground="#a3a3a3")
        la_seleciona_perfil.configure(foreground="#000000")
        la_seleciona_perfil.configure(justify="left")
        la_seleciona_perfil.configure(text="""Section select...""")

        janela_selecionar.mainloop

    # DESTROY WINDOW GEOMETRY
    def destroy_geometric_window():
        janela_geometria.destroy()

    ##########################################################################

    janela_geometria = tk.Tk()

    janela_geometria.geometry("340x190+400+120")
    janela_geometria.minsize(148, 1)
    janela_geometria.maxsize(1924, 1055)
    janela_geometria.resizable(0, 0)
    janela_geometria.title("Span details")
    janela_geometria.configure(background="#d9d9d9")
    janela_geometria.iconbitmap("icones/geral.ico")
    janela_geometria.title("Beam Section")

    frame_destroy_j_g_perfil = tk.Frame(janela_geometria)
    frame_destroy_j_g_perfil.place(
        relx=0.029, rely=0.0526, relheight=0.631, relwidth=0.941
    )
    frame_destroy_j_g_perfil.configure(relief="groove")
    frame_destroy_j_g_perfil.configure(borderwidth="2")
    frame_destroy_j_g_perfil.configure(relief="groove")
    frame_destroy_j_g_perfil.configure(background="#d9d9d9")

    la_jg_p = tk.Label(frame_destroy_j_g_perfil)
    la_jg_p.place(relx=0.031, rely=0.083, height=26, width=82)
    la_jg_p.configure(background="#d9d9d9")
    la_jg_p.configure(disabledforeground="#a3a3a3")
    la_jg_p.configure(font=Sbi_font9)
    la_jg_p.configure(foreground="#000000")
    la_jg_p.configure(text="""Section""")

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
    btn_jg_p_selecionar.configure(text="""Select""")
    btn_jg_p_selecionar.configure(command=call_ja_geo_per_select)

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
    btn_jg_p_inserir.configure(text="""Insert""")
    btn_jg_p_inserir.configure(command=call_ja_geo_per_insert)

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
    btn_destroy_j_g.configure(text=""">>>""")
    btn_destroy_j_g.configure(command=destroy_geometric_window)

    janela_geometria.mainloop()

def n_span_func():
    trechos = tk.StringVar()

    def loads_span():
        global trechos
        trechos = int(combobox_n_vaos.get())

        def destroy_loads():
            global q, L
            L = np.zeros(trechos)
            q = np.zeros(trechos)
            if trechos == 1:
                L[0] = float(box_dim_trecho1_L.get())
                q[0] = float(box_dim_trecho1_Q.get())

            elif trechos == 2:
                L[0] = float(box_dim_trecho1_L.get())
                q[0] = float(box_dim_trecho1_Q.get())
                L[1] = float(box_dim_trecho2_L.get())
                q[1] = float(box_dim_trecho2_Q.get())
            else:
                L[0] = float(box_dim_trecho1_L.get())
                q[0] = float(box_dim_trecho1_Q.get())
                L[1] = float(box_dim_trecho2_L.get())
                q[1] = float(box_dim_trecho2_Q.get())
                L[2] = float(box_dim_trecho3_L.get())
                q[2] = float(box_dim_trecho3_Q.get())

            janela_trecho.destroy()
            n_vaos.destroy()

        if trechos == 1:
            janela_trecho = tk.Tk()

            janela_trecho.geometry("340x180+895+168")
            janela_trecho.minsize(148, 1)
            janela_trecho.maxsize(1924, 1055)
            janela_trecho.resizable(1, 1)
            janela_trecho.title("Span details")
            janela_trecho.configure(background="#d9d9d9")
            janela_trecho.configure(highlightbackground="#d9d9d9")
            janela_trecho.configure(highlightcolor="black")

            frame_trecho_1_dim = tk.Frame(janela_trecho)
            frame_trecho_1_dim.place(
                relx=0.029, rely=0.072, relheight=0.667, relwidth=0.941
            )
            frame_trecho_1_dim.configure(relief="groove")
            frame_trecho_1_dim.configure(borderwidth="2")
            frame_trecho_1_dim.configure(relief="groove")
            frame_trecho_1_dim.configure(background="#d9d9d9")
            frame_trecho_1_dim.configure(highlightbackground="#d9d9d9")
            frame_trecho_1_dim.configure(highlightcolor="black")

            la_dim_trecho1 = tk.Label(frame_trecho_1_dim)
            Config_frame(la_dim_trecho1, relx=0.063, rely=0.083, height=26,
                         width=98, ft=Sbi_font9, text="""1º Span""")

            la_dim_trecho1_L = tk.Label(frame_trecho_1_dim)
            Config_frame(la_dim_trecho1_L, relx=0.031, rely=0.5, height=26,
                         width=42, ft=S_font9, text="""L=""")

            box_dim_trecho1_L = tk.Entry(frame_trecho_1_dim)
            Config_entry(box_dim_trecho1_L, relx=0.125, rely=0.5, height=24,
                         relwidth=0.325)

            la_dim_trecho1_Q = tk.Label(frame_trecho_1_dim)
            Config_frame(la_dim_trecho1_Q, relx=0.5, rely=0.5, height=26,
                         width=42, ft=S_font9, text="""Q=""")

            box_dim_trecho1_Q = tk.Entry(frame_trecho_1_dim)
            Config_entry(box_dim_trecho1_Q, relx=0.609, rely=0.5, height=24,
                         relwidth=0.325)

            but_seguinte_trechos = tk.Button(janela_trecho)
            but_seguinte_trechos.place(
                relx=0.382, rely=0.778, height=33, width=80)
            but_seguinte_trechos.configure(activebackground="#ececec")
            but_seguinte_trechos.configure(activeforeground="#000000")
            but_seguinte_trechos.configure(background="#0000a0")
            but_seguinte_trechos.configure(disabledforeground="#a3a3a3")
            but_seguinte_trechos.configure(foreground="#ffffff")
            but_seguinte_trechos.configure(highlightbackground="#d9d9d9")
            but_seguinte_trechos.configure(highlightcolor="black")
            but_seguinte_trechos.configure(pady="0")
            but_seguinte_trechos.configure(text=""">>>""")
            but_seguinte_trechos.configure(command=destroy_loads)

            janela_trecho.mainloop()
        elif trechos == 2:
            janela_trecho = tk.Tk()

            janela_trecho.geometry("340x310+845+149")
            janela_trecho.minsize(148, 1)
            janela_trecho.maxsize(1924, 1055)
            janela_trecho.resizable(1, 1)
            janela_trecho.title("Span details")
            janela_trecho.configure(background="#d9d9d9")
            janela_trecho.configure(highlightbackground="#d9d9d9")
            janela_trecho.configure(highlightcolor="black")
            janela_trecho.iconbitmap("icones/geral.ico")

            frame_trecho_1_dim = tk.Frame(janela_trecho)
            frame_trecho_1_dim.place(
                relx=0.029, rely=0.032, relheight=0.387, relwidth=0.941
            )
            frame_trecho_1_dim.configure(relief="groove")
            frame_trecho_1_dim.configure(borderwidth="2")
            frame_trecho_1_dim.configure(relief="groove")
            frame_trecho_1_dim.configure(background="#d9d9d9")
            frame_trecho_1_dim.configure(highlightbackground="#d9d9d9")
            frame_trecho_1_dim.configure(highlightcolor="black")

            la_dim_trecho1 = tk.Label(frame_trecho_1_dim)
            Config_frame(la_dim_trecho1, relx=0.063, rely=0.083, height=26,
                         width=98, ft=Sbi_font9, text="""1º Span""")

            la_dim_trecho1_L = tk.Label(frame_trecho_1_dim)
            Config_frame(la_dim_trecho1_L, relx=0.031, rely=0.5, height=26,
                         width=42, ft=S_font9, text="""L=""")

            box_dim_trecho1_L = tk.Entry(frame_trecho_1_dim)
            Config_entry(box_dim_trecho1_L, relx=0.125, rely=0.5, height=24,
                         relwidth=0.325)

            la_dim_trecho1_Q = tk.Label(frame_trecho_1_dim)
            Config_frame(la_dim_trecho1_Q, relx=0.5, rely=0.5, height=26,
                         width=42, ft=S_font9, text="""Q=""")

            box_dim_trecho1_Q = tk.Entry(frame_trecho_1_dim)
            Config_entry(box_dim_trecho1_Q, relx=0.609, rely=0.5, height=24,
                         relwidth=0.325)

            frame_trecho_2_dim = tk.Frame(janela_trecho)
            frame_trecho_2_dim.place(
                relx=0.029, rely=0.452, relheight=0.387, relwidth=0.941
            )
            frame_trecho_2_dim.configure(relief="groove")
            frame_trecho_2_dim.configure(borderwidth="2")
            frame_trecho_2_dim.configure(relief="groove")
            frame_trecho_2_dim.configure(background="#d9d9d9")
            frame_trecho_2_dim.configure(highlightbackground="#d9d9d9")
            frame_trecho_2_dim.configure(highlightcolor="black")

            la_dim_trecho2 = tk.Label(frame_trecho_2_dim)
            Config_frame(la_dim_trecho2, relx=0.063, rely=0.083, height=26,
                         width=98, ft=Sbi_font9, text="""2º Span""")

            la_dim_trecho2_L = tk.Label(frame_trecho_2_dim)
            Config_frame(la_dim_trecho2_L, relx=0.031, rely=0.5, height=26,
                         width=42, ft=S_font9, text="""L=""")

            box_dim_trecho2_L = tk.Entry(frame_trecho_2_dim)
            Config_entry(box_dim_trecho2_L, relx=0.125, rely=0.5, height=24,
                         relwidth=0.325)

            la_dim_trecho2_Q = tk.Label(frame_trecho_2_dim)
            Config_frame(la_dim_trecho2_Q, relx=0.5, rely=0.5, height=26,
                         width=42, ft=S_font9, text="""Q=""")

            box_dim_trecho2_Q = tk.Entry(frame_trecho_2_dim)
            Config_entry(box_dim_trecho2_Q, relx=0.609, rely=0.5, height=24,
                         relwidth=0.325)

            but_seguinte_trechos = tk.Button(janela_trecho)
            but_seguinte_trechos.place(
                relx=0.382, rely=0.871, height=33, width=80)
            but_seguinte_trechos.configure(activebackground="#ececec")
            but_seguinte_trechos.configure(activeforeground="#000000")
            but_seguinte_trechos.configure(background="#0000a0")
            but_seguinte_trechos.configure(disabledforeground="#a3a3a3")
            but_seguinte_trechos.configure(foreground="#ffffff")
            but_seguinte_trechos.configure(highlightbackground="#d9d9d9")
            but_seguinte_trechos.configure(highlightcolor="black")
            but_seguinte_trechos.configure(pady="0")
            but_seguinte_trechos.configure(text=""">>>""")
            but_seguinte_trechos.configure(command=destroy_loads)

            janela_trecho.mainloop()
        else:
            janela_trecho = tk.Tk()

            janela_trecho.geometry("340x440+845+149")
            janela_trecho.minsize(148, 1)
            janela_trecho.maxsize(1924, 1055)
            janela_trecho.resizable(1, 1)
            janela_trecho.title("Span details")
            janela_trecho.configure(background="#d9d9d9")
            janela_trecho.configure(highlightbackground="#d9d9d9")
            janela_trecho.configure(highlightcolor="black")

            frame_trecho_1_dim = tk.Frame(janela_trecho)
            frame_trecho_1_dim.place(
                relx=0.029, rely=0.023, relheight=0.273, relwidth=0.941
            )
            frame_trecho_1_dim.configure(relief="groove")
            frame_trecho_1_dim.configure(borderwidth="2")
            frame_trecho_1_dim.configure(relief="groove")
            frame_trecho_1_dim.configure(background="#d9d9d9")
            frame_trecho_1_dim.configure(highlightbackground="#d9d9d9")
            frame_trecho_1_dim.configure(highlightcolor="black")

            la_dim_trecho1 = tk.Label(frame_trecho_1_dim)
            Config_frame(la_dim_trecho1, relx=0.063, rely=0.083, height=26,
                         width=98, ft=Sbi_font9, text="""1º Span""")

            la_dim_trecho1_L = tk.Label(frame_trecho_1_dim)
            Config_frame(la_dim_trecho1_L, relx=0.031, rely=0.5, height=26,
                         width=42, ft=S_font9, text="""L=""")

            box_dim_trecho1_L = tk.Entry(frame_trecho_1_dim)
            Config_entry(box_dim_trecho1_L, relx=0.125, rely=0.5, height=24,
                         relwidth=0.325)

            la_dim_trecho1_Q = tk.Label(frame_trecho_1_dim)
            Config_frame(la_dim_trecho1_Q, relx=0.5, rely=0.5, height=26,
                         width=42, ft=S_font9, text="""Q=""")

            box_dim_trecho1_Q = tk.Entry(frame_trecho_1_dim)
            Config_entry(box_dim_trecho1_Q, relx=0.609, rely=0.5, height=24,
                         relwidth=0.325)

            frame_trecho_2_dim = tk.Frame(janela_trecho)
            frame_trecho_2_dim.place(
                relx=0.029, rely=0.318, relheight=0.273, relwidth=0.941
            )
            frame_trecho_2_dim.configure(relief="groove")
            frame_trecho_2_dim.configure(borderwidth="2")
            frame_trecho_2_dim.configure(relief="groove")
            frame_trecho_2_dim.configure(background="#d9d9d9")
            frame_trecho_2_dim.configure(highlightbackground="#d9d9d9")
            frame_trecho_2_dim.configure(highlightcolor="black")

            la_dim_trecho2 = tk.Label(frame_trecho_2_dim)
            Config_frame(la_dim_trecho2, relx=0.063, rely=0.083, height=26,
                         width=98, ft=Sbi_font9, text="""2º Span""")

            la_dim_trecho2_L = tk.Label(frame_trecho_2_dim)
            Config_frame(la_dim_trecho2_L, relx=0.031, rely=0.5, height=26,
                         width=42, ft=S_font9, text="""L=""")

            box_dim_trecho2_L = tk.Entry(frame_trecho_2_dim)
            Config_entry(box_dim_trecho2_L, relx=0.125, rely=0.5, height=24,
                         relwidth=0.325)

            la_dim_trecho2_Q = tk.Label(frame_trecho_2_dim)
            Config_frame(la_dim_trecho2_Q, relx=0.5, rely=0.5, height=26,
                         width=42, ft=S_font9, text="""Q=""")

            box_dim_trecho2_Q = tk.Entry(frame_trecho_2_dim)
            Config_entry(box_dim_trecho2_Q, relx=0.609, rely=0.5, height=24,
                         relwidth=0.325)

            frame_trecho_3_dim = tk.Frame(janela_trecho)
            frame_trecho_3_dim.place(
                relx=0.029, rely=0.614, relheight=0.273, relwidth=0.941
            )
            frame_trecho_3_dim.configure(relief="groove")
            frame_trecho_3_dim.configure(borderwidth="2")
            frame_trecho_3_dim.configure(relief="groove")
            frame_trecho_3_dim.configure(background="#d9d9d9")
            frame_trecho_3_dim.configure(highlightbackground="#d9d9d9")
            frame_trecho_3_dim.configure(highlightcolor="black")

            la_dim_trecho3 = tk.Label(frame_trecho_3_dim)
            Config_frame(la_dim_trecho3, relx=0.063, rely=0.083, height=26,
                         width=98, ft=Sbi_font9, text="""3º Span""")

            la_dim_trecho3_L = tk.Label(frame_trecho_3_dim)
            Config_frame(la_dim_trecho3_L, relx=0.031, rely=0.5, height=26,
                         width=42, ft=S_font9, text="""L=""")

            box_dim_trecho3_L = tk.Entry(frame_trecho_3_dim)
            Config_entry(box_dim_trecho3_L, relx=0.125, rely=0.5, height=24,
                         relwidth=0.325)

            la_dim_trecho3_Q = tk.Label(frame_trecho_3_dim)
            Config_frame(la_dim_trecho3_Q, relx=0.5, rely=0.5, height=26,
                         width=42, ft=S_font9, text="""Q=""")

            box_dim_trecho3_Q = tk.Entry(frame_trecho_3_dim)
            Config_entry(box_dim_trecho3_Q, relx=0.609, rely=0.5, height=24,
                         relwidth=0.325)

            but_seguinte_trechos = tk.Button(janela_trecho)
            but_seguinte_trechos.place(
                relx=0.382, rely=0.909, height=33, width=80)
            but_seguinte_trechos.configure(activebackground="#ececec")
            but_seguinte_trechos.configure(activeforeground="#000000")
            but_seguinte_trechos.configure(background="#0000ff")
            but_seguinte_trechos.configure(disabledforeground="#a3a3a3")
            but_seguinte_trechos.configure(foreground="#ffffff")
            but_seguinte_trechos.configure(highlightbackground="#d9d9d9")
            but_seguinte_trechos.configure(highlightcolor="black")
            but_seguinte_trechos.configure(pady="0")
            but_seguinte_trechos.configure(text=""">>>""")
            but_seguinte_trechos.configure(command=destroy_loads)

            janela_trecho.mainloop()

    n_vaos = tk.Tk()

    style = ttk.Style()
    style.configure(".", background=_bgcolor)
    style.configure(".", foreground=_fgcolor)
    style.configure(".", font="TkDefaultFont")
    style.map(
        ".", background=[
            ("selected", _compcolor), ("active", _ana2color)])

    n_vaos.geometry("300x150+797+151")
    n_vaos.minsize(148, 1)
    n_vaos.maxsize(1924, 1055)
    n_vaos.resizable(1, 1)
    n_vaos.iconbitmap("icones/geral.ico")
    n_vaos.title("Span data")
    n_vaos.configure(background="#d9d9d9")

    la_n_vaos = tk.Label(n_vaos)
    la_n_vaos.place(relx=0.083, rely=0.1, height=33, width=250)
    la_n_vaos.configure(background="#d9d9d9")
    la_n_vaos.configure(disabledforeground="#a3a3a3")
    la_n_vaos.configure(font=Sb_font10)
    la_n_vaos.configure(foreground="#000000")
    la_n_vaos.configure(text="""Number of beam spans:""")

    combobox_n_vaos = ttk.Combobox(n_vaos)
    combobox_n_vaos.place(relx=0.2, rely=0.4, relheight=0.173, relwidth=0.623)
    combobox_n_vaos.configure(values=["1", "2", "3"])
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
    btn_n_vaos.configure(text=""">>>""")
    btn_n_vaos.configure(command=loads_span)

    n_vaos.mainloop()


def window_mat():
    global fck, yc, E_a, fy, ya, E_as, fs, ys

    def take_mat():
        global fck, yc, E_a, fy, ya, E_as, fs, ys
        fck = float(box_fck.get())
        yc = float(box_yc.get())

        E_a = float(box_E_a.get())
        fy = float(box_fy.get())
        ya = float(box_ya.get())

        E_as = float(box_E_As.get())
        fs = float(box_fs.get())
        ys = float(box_ys.get())

        janela_materiais.destroy()

    janela_materiais = tk.Tk()

    janela_materiais.geometry("340x511+500+200")
    janela_materiais.minsize(148, 1)
    janela_materiais.maxsize(1924, 1055)
    janela_materiais.resizable(1, 1)
    janela_materiais.iconbitmap("icones/geral.ico")
    janela_materiais.title("Material Property")
    janela_materiais.configure(background="#d9d9d9")
    janela_materiais.configure(highlightbackground="#d9d9d9")
    janela_materiais.configure(highlightcolor="black")

    frame_prop_concreto = tk.Frame(janela_materiais)
    frame_prop_concreto.place(
        relx=0.029,
        rely=0.02,
        relheight=0.188,
        relwidth=0.941)
    frame_prop_concreto.configure(relief="groove")
    frame_prop_concreto.configure(borderwidth="2")
    frame_prop_concreto.configure(relief="groove")
    frame_prop_concreto.configure(background="#d9d9d9")
    frame_prop_concreto.configure(highlightbackground="#d9d9d9")
    frame_prop_concreto.configure(highlightcolor="black")

    la_concreto = tk.Label(frame_prop_concreto)
    Config_frame(la_concreto, relx=0.063, rely=0.063, height=21, width=98,
                 ft=Sbi_font9, text="""Concrete""")

    la_fck = tk.Label(frame_prop_concreto)
    Config_frame(la_fck, relx=0.031, rely=0.6, height=21, width=30,
                 ft=S_font9, text="""fc=""")

    box_fck = tk.Entry(frame_prop_concreto)
    Config_entry(box_fck, relx=0.156, rely=0.563, height=24, relwidth=0.325)

    la_yc = tk.Label(frame_prop_concreto)
    Config_frame(la_yc, relx=0.5, rely=0.6, height=21, width=42,
                 ft=S_font9, text="""yc=""")

    box_yc = tk.Entry(frame_prop_concreto)
    Config_entry(box_yc, relx=0.625, rely=0.563, height=24, relwidth=0.325)

    frame_perfil = tk.Frame(janela_materiais)
    frame_perfil.place(relx=0.029, rely=0.227, relheight=0.294, relwidth=0.941)
    frame_perfil.configure(relief="groove")
    frame_perfil.configure(borderwidth="2")
    frame_perfil.configure(relief="groove")
    frame_perfil.configure(background="#d9d9d9")
    frame_perfil.configure(highlightbackground="#d9d9d9")
    frame_perfil.configure(highlightcolor="black")

    la_perfil = tk.Label(frame_perfil)
    Config_frame(la_perfil, relx=0.063, rely=0.06, height=33, width=98,
                 ft=Sbi_font9, text="""Steel I-Section""")

    la_E_a = tk.Label(frame_perfil)
    Config_frame(la_E_a, relx=0.025, rely=0.373, height=33, width=35,
                 ft=S_font9, text="""E_a=""")

    box_E_a = tk.Entry(frame_perfil)
    Config_entry(box_E_a, relx=0.125, rely=0.407, height=24, relwidth=0.325)

    la_fy = tk.Label(frame_perfil)
    Config_frame(la_fy, relx=0.5, rely=0.393, height=32, width=42,
                 ft=S_font9, text="""fy=""")

    box_fy = tk.Entry(frame_perfil)
    Config_entry(box_fy, relx=0.609, rely=0.407, height=24, relwidth=0.325)

    box_ya = tk.Entry(frame_perfil)
    Config_entry(box_ya, relx=0.125, rely=0.68, height=24, relwidth=0.325)

    la_ya = tk.Label(frame_perfil)
    Config_frame(la_ya, relx=0.031, rely=0.653, height=32, width=30,
                 ft=S_font9, text="""ya=""")

    frame_As_complementar = tk.Frame(janela_materiais)
    frame_As_complementar.place(
        relx=0.029,
        rely=0.54,
        relheight=0.294,
        relwidth=0.941)
    frame_As_complementar.configure(relief="groove")
    frame_As_complementar.configure(borderwidth="2")
    frame_As_complementar.configure(relief="groove")
    frame_As_complementar.configure(background="#d9d9d9")
    frame_As_complementar.configure(highlightbackground="#d9d9d9")
    frame_As_complementar.configure(highlightcolor="black")

    la_As_complementar = tk.Label(frame_As_complementar)
    Config_frame(la_As_complementar, relx=0.063, rely=0.06, height=33,
                 width=138, ft=Sbi_font9, text="""Steel Reinforcement""")

    la_E_As = tk.Label(frame_As_complementar)
    Config_frame(la_E_As, relx=0.031, rely=0.373, height=33, width=45,
                 ft=S_font9, text="""Es=""")

    box_E_As = tk.Entry(frame_As_complementar)
    Config_entry(box_E_As, relx=0.172, rely=0.407, height=24, relwidth=0.325)

    la_fs = tk.Label(frame_As_complementar)
    Config_frame(la_fs, relx=0.5, rely=0.393, height=32, width=42,
                 ft=S_font9, text="""fs=""")

    box_fs = tk.Entry(frame_As_complementar)
    Config_entry(box_fs, relx=0.609, rely=0.407, height=24, relwidth=0.325)

    box_ys = tk.Entry(frame_As_complementar)
    Config_entry(box_ys, relx=0.172, rely=0.7, height=24, relwidth=0.325)

    la_ys = tk.Label(frame_As_complementar)
    Config_frame(la_ys, relx=0.063, rely=0.667, height=33, width=30,
                 ft=S_font9, text="""ys=""")

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
    but_seguinte_materiais.configure(text=""">>>""")
    but_seguinte_materiais.configure(command=take_mat)

    janela_materiais.mainloop()

def desing_method():

    def func_grau():
        def destroy_window_grau():
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
            janela_grau.iconbitmap("icones/geral.ico")
            janela_grau.title("Design Method")
            janela_grau.configure(background="#d9d9d9")
            janela_grau.configure(highlightbackground="#d9d9d9")
            janela_grau.configure(highlightcolor="black")

            frame_grau_1_dim = tk.Frame(
                janela_grau,
                relief="groove",
                borderwidth=2,
                background="#d9d9d9")
            frame_grau_1_dim.place(
                relx=0.029, rely=0.015, relheight=0.60, relwidth=0.941
            )

            la_grau1 = tk.Label(
                janela_grau,
                text="Degree of Connection[%]:",
                font="-family {Segoe UI} -size 11 -weight bold -slant italic",
                background="#d9d9d9",
                foreground="#000000",
            )
            la_grau1.place(relx=0.2, rely=0.1)

            box_dim_grau1 = tk.Entry(janela_grau)
            box_dim_grau1.place(
                relx=0.325,
                rely=0.35,
                height=24,
                relwidth=0.325)

            btn_grau = tk.Button(
                janela_grau,
                text=">>>",
                background="#0000ff",
                foreground="#ffffff",
                command=destroy_window_grau,
            )
            btn_grau.place(relx=0.4, rely=0.65, height=43, width=56)

            janela_grau.mainloop()

    def func_inter():
        def destroy_inter_window():
            global interacao
            interacao = str(combobox_interacao.get())
            janela_interacao.destroy()
            func_grau()

        if norma == "NBR 8800":
            janela_interacao = tk.Tk()

            style = ttk.Style()
            style.configure(".", background=_bgcolor)
            style.configure(".", foreground=_fgcolor)
            style.configure(".", font="TkDefaultFont")
            style.map(
                ".", background=[
                    ("selected", _compcolor), ("active", _ana2color)])

            janela_interacao.geometry("300x150+561+192")
            janela_interacao.minsize(148, 1)
            janela_interacao.maxsize(1924, 1055)
            janela_interacao.resizable(1, 1)
            janela_interacao.iconbitmap("icones/geral.ico")
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
            la_normas.configure(
                font="-family {Segoe UI} -size 11 -weight bold -slant italic"
            )
            la_normas.configure(foreground="#000000")
            la_normas.configure(highlightbackground="#d9d9d9")
            la_normas.configure(highlightcolor="black")
            la_normas.configure(text="""Interaction:""")

            combobox_interacao = ttk.Combobox(janela_interacao)
            combobox_interacao.place(
                relx=0.2, rely=0.4, relheight=0.173, relwidth=0.623
            )
            combobox_interacao.configure(values=["Complete", "Partial"])
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
            btn_normas.configure(text=""">>>""")
            btn_normas.configure(command=destroy_inter_window)

    def take_standards():
        global norma
        norma = str(combobox_norma.get())
        janela_normas.destroy()
        func_inter()

    janela_normas = tk.Tk()

    style = ttk.Style()
    style.configure(".", background=_bgcolor)
    style.configure(".", foreground=_fgcolor)
    style.configure(".", font="TkDefaultFont")
    style.map(
        ".", background=[
            ("selected", _compcolor), ("active", _ana2color)])

    janela_normas.geometry("300x150+561+192")
    janela_normas.minsize(148, 1)
    janela_normas.maxsize(1924, 1055)
    janela_normas.resizable(1, 1)
    janela_normas.iconbitmap("icones/geral.ico")
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
    la_normas.configure(
        font="-family {Segoe UI} -size 11 -weight bold -slant italic")
    la_normas.configure(foreground="#000000")
    la_normas.configure(highlightbackground="#d9d9d9")
    la_normas.configure(highlightcolor="black")
    la_normas.configure(text="""Design Based on:""")

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
    btn_normas.configure(text=""">>>""")
    btn_normas.configure(command=take_standards)

    janela_normas.mainloop()

# =============================================================================
# =============================================================================
# # GENERAL WINDOW
# =============================================================================
# =============================================================================

janela_geral = tk.Tk()
global img2
img2 = tk.PhotoImage(file="imagens/SECAO_330x344.png")

# =============================================================================
#                   DEFINING INPUT AND OUTPUT VERIABLES
# =============================================================================

"""This class configures and populates the janela_gerallevel window.
    janela_geral is the janela_gerallevel containing window."""
_bgcolor = "#d9d9d9"    # X11 color: 'gray85'
_fgcolor = "#000000"    # X11 color: 'black'
_compcolor = "#d9d9d9"  # X11 color: 'gray85'
_ana1color = "#d9d9d9"  # X11 color: 'gray85'
_ana2color = "#ececec"  # Closest X11 color: 'gray92'

janela_geral.minsize(1400, 700)
janela_geral.maxsize(1536, 864)
janela_geral.geometry("1536x795+-8+0")
janela_geral.iconbitmap("icones/geral.ico")
janela_geral.title("COMBEAMS - Regulatory checks for composite beams")
janela_geral.configure(background="#d9d9d9")
janela_geral.configure(highlightbackground="#d9d9d9")
janela_geral.configure(highlightcolor="black")

# =============================================================================
# FRAME 1- EXCERPTS
# =============================================================================

Frame1 = tk.Frame(janela_geral)
Frame1.place(relx=0.827, rely=0.013, relheight=0.975, relwidth=0.167)
Frame1.configure(relief="groove")
Frame1.configure(borderwidth="2")
Frame1.configure(relief="groove")
Frame1.configure(background="#d9d9d9")
Frame1.configure(highlightbackground="#d9d9d9")
Frame1.configure(highlightcolor="black")

# =============================================================================
# FRAME 2-PROFILE DATA
# =============================================================================

Frame2 = tk.Frame(janela_geral)
Frame2.place(relx=0.007, rely=0.013, relheight=0.975, relwidth=0.227)
Frame2.configure(relief="groove")
Frame2.configure(borderwidth="2")
Frame2.configure(relief="groove")
Frame2.configure(background="#d9d9d9")
Frame2.configure(highlightbackground="#d9d9d9")
Frame2.configure(highlightcolor="black")

Frame2_ima = tk.Frame(Frame2)
Frame2_ima.place(relx=0.015, rely=0.006, relheight=0.42, relwidth=0.971)
Frame2_ima.configure(relief="groove")
Frame2_ima.configure(borderwidth="2")
Frame2_ima.configure(relief="groove")
Frame2_ima.configure(background="#d9d9d9")
Frame2_ima.configure(highlightbackground="#d9d9d9")
Frame2_ima.configure(highlightcolor="black")

img = tk.PhotoImage(file="imagens/SECAO_330x344.png")
la_ima_ad_ = tk.Label(Frame2_ima)
la_ima_ad_.place(relx=-0.35, rely=-0.35, relheight=1.7, relwidth=1.7)
la_ima_ad_.configure(image=img)
la_ima_ad_.image = img

la_perfil = tk.Label(Frame2)
Config_frame(la_perfil, relx=0.029, rely=0.449, height=25, width=52,
             ft=Sbi_font9, text="""Section""")

la_bf = tk.Label(Frame2)
Config_frame(la_bf, relx=0.029, rely=0.487, height=26, width=42,
             ft=S_font9, text="""bf=""")

la_tf = tk.Label(Frame2)
Config_frame(la_tf, relx=0.029, rely=0.526, height=26, width=42,
             ft=S_font9, text="""tf=""")

la_h = tk.Label(Frame2)
Config_frame(la_h, relx=0.029, rely=0.564, height=25, width=42,
             ft=S_font9, text="""h=""")

la_d = tk.Label(Frame2)
Config_frame(la_d, relx=0.029, rely=0.603, height=26, width=42,
             ft=S_font9, text="""d=""")

la_d_ = tk.Label(Frame2)
Config_frame(la_d_, relx=0.029, rely=0.641, height=26, width=42,
             ft=S_font9, text="""d_=""")

la_tw = tk.Label(Frame2)
Config_frame(la_tw, relx=0.471, rely=0.487, height=26, width=42,
             ft=S_font9, text="""tw=""")

la_ry = tk.Label(Frame2)
Config_frame(la_ry, relx=0.471, rely=0.526, height=26, width=42,
             ft=S_font9, text="""ry=""")

la_wx = tk.Label(Frame2)
Config_frame(la_wx, relx=0.471, rely=0.564, height=26, width=42,
             ft=S_font9, text="""Wx=""")

la_ix = tk.Label(Frame2)
Config_frame(la_ix, relx=0.471, rely=0.603, height=26, width=42,
             ft=S_font9, text="""Ix=""")

la_area = tk.Label(Frame2)
Config_frame(la_area, relx=0.471, rely=0.641, height=26, width=42,
             ft=S_font9, text="""Area=""")

la_laje = tk.Label(Frame2)
Config_frame(la_laje, relx=0.029, rely=0.692, height=25, width=30,
             ft=Sbi_font9, text="""Slab""")

la_tc = tk.Label(Frame2)
Config_frame(la_tc, relx=0.029, rely=0.731, height=26, width=42,
             ft=S_font9, text="""tc=""")

la_armadura_longitudinal = tk.Label(Frame2)
Config_frame(la_armadura_longitudinal, relx=0.029, rely=0.782, height=25,
             width=104, ft=Sbi_font9, text="""Longitudinal Bars""")

la_ass = tk.Label(Frame2)
Config_frame(la_ass, relx=0.029, rely=0.821, height=25, width=42,
             ft=S_font9, text="""Ass=""")

la_asi = tk.Label(Frame2)
Config_frame(la_asi, relx=0.338, rely=0.821, height=25, width=42,
             ft=S_font9, text="""Asi=""")

la_cobri = tk.Label(Frame2)
Config_frame(la_cobri, relx=0.647, rely=0.821, height=25, width=42,
             ft=S_font9, text="""c=""")

la_conectores = tk.Label(Frame2)
Config_frame(la_conectores, relx=0.029, rely=0.872, height=25, width=35,
             ft=Sbi_font9, text="""Studs""")

la_Ø = tk.Label(Frame2)
Config_frame(la_Ø, relx=0.029, rely=0.949, height=26, width=42,
             ft=S_font9, text="""Ø=""")

la_fucs = tk.Label(Frame2)
Config_frame(la_fucs, relx=0.029, rely=0.91, height=26, width=42,
             ft=S_font9, text="""fucs=""")

la_γc = tk.Label(Frame2)
Config_frame(la_γc, relx=0.471, rely=0.91, height=25, width=31,
             ft=S_font9, text="""γc=""")

# =============================================================================
# FRAME 3 - BUTTONS
# =============================================================================

Frame3 = tk.Frame(janela_geral)
Frame3.place(relx=0.24, rely=0.013, relheight=0.065, relwidth=0.58)
Frame3.configure(relief="groove")
Frame3.configure(borderwidth="2")
Frame3.configure(relief="groove")
Frame3.configure(background="#d9d9d9")
Frame3.configure(highlightbackground="#d9d9d9")
Frame3.configure(highlightcolor="black")

img_btn_geometria = tk.PhotoImage(file="icones/img_btn_geometria_33x33.png")
img_btn_dimensoes = tk.PhotoImage(file="icones/img_btn_dimensoes_2_33x33.png")
img_btn_diag_carga = tk.PhotoImage(file="icones/img_btn_diag_carga_33x33.png")

btn_geometria = tk.Button(Frame3)
Config_buttom(btn_geometria, relx=0.006, rely=0.096, height=40, width=40)
btn_geometria.configure(pady="0")
btn_geometria.configure(image=img_btn_geometria)
btn_geometria.configure(anchor="w")
btn_geometria.configure(command=call_geometry_window)

btn_dimensoes = tk.Button(Frame3)
Config_buttom(btn_dimensoes, relx=0.057, rely=0.096, height=40, width=40)
btn_dimensoes.configure(pady="0")
btn_dimensoes.configure(image=img_btn_dimensoes)
btn_dimensoes.configure(anchor="w")
btn_dimensoes.configure(command=n_span_func)

btn_materiais = tk.Button(Frame3)
Config_buttom(btn_materiais, relx=0.109, rely=0.096, height=40, width=40)
btn_materiais.configure(pady="0")
btn_materiais.configure(font=font008)
btn_materiais.configure(text="""E""")
btn_materiais.configure(command=window_mat)

btn_modelo_calculo = tk.Button(Frame3)
Config_buttom(btn_modelo_calculo, relx=0.161, rely=0.096, height=40, width=40)
btn_modelo_calculo.configure(pady="0")
btn_modelo_calculo.configure(font=font009)
btn_modelo_calculo.configure(text="""f""")
btn_modelo_calculo.configure(command=desing_method)

btn_diag_cortante = tk.Button(Frame3)
Config_buttom(btn_diag_cortante, relx=0.506, rely=0.096, height=40, width=40)
btn_diag_cortante.configure(pady="0")
btn_diag_cortante.configure(font=font009)
btn_diag_cortante.configure(text="""S""")
btn_diag_cortante.configure(command=calculation_shear_nbr)

btn_diag_momento = tk.Button(Frame3)
Config_buttom(btn_diag_momento, relx=0.557, rely=0.096, height=40, width=40)
btn_diag_momento.place(relx=0.557, rely=0.096, height=40, width=40)
btn_diag_momento.configure(pady="0")
btn_diag_momento.configure(font=font009)
btn_diag_momento.configure(text="""M""")
btn_diag_momento.configure(command=calculation_moment_nbr)

btn_relatorio = tk.Button(Frame3)
Config_buttom(btn_relatorio, relx=0.859, rely=0.096, height=40, width=120)
btn_relatorio.configure(pady="0")
btn_relatorio.configure(font=font009)
btn_relatorio.configure(text="""Report""")
btn_relatorio.configure(command=func_report)

# =============================================================================
# FRAME 4- REQUESTING DIAGRAM
# =============================================================================

Frame4_solicitante = tk.Frame(janela_geral)
Frame4_solicitante.place(relx=0.24, rely=0.088, relheight=0.315, relwidth=0.58)
Frame4_solicitante.configure(relief="groove")
Frame4_solicitante.configure(borderwidth="2")
Frame4_solicitante.configure(relief="groove")
Frame4_solicitante.configure(background="#d9d9d9")
Frame4_solicitante.configure(highlightbackground="#d9d9d9")
Frame4_solicitante.configure(highlightcolor="black")

# =============================================================================
# FRAME 5- RESISTANT DIAGRAM
# =============================================================================

Frame5_resistente = tk.Frame(janela_geral)
Frame5_resistente.place(relx=0.24, rely=0.413, relheight=0.315, relwidth=0.58)
Frame5_resistente.configure(relief="groove")
Frame5_resistente.configure(borderwidth="2")
Frame5_resistente.configure(relief="groove")
Frame5_resistente.configure(background="#d9d9d9")
Frame5_resistente.configure(highlightbackground="#d9d9d9")
Frame5_resistente.configure(highlightcolor="black")

# =============================================================================
# FRAME 6 - CONNECTOR DISTRIBUTION
# =============================================================================

Frame6_conectores = tk.Frame(janela_geral)
Frame6_conectores.place(relx=0.24, rely=0.738, relheight=0.25, relwidth=0.58)
Frame6_conectores.configure(relief="groove")
Frame6_conectores.configure(borderwidth="2")
Frame6_conectores.configure(relief="groove")
Frame6_conectores.configure(background="#d9d9d9")
Frame6_conectores.configure(highlightbackground="#d9d9d9")
Frame6_conectores.configure(highlightcolor="black")



# =============================================================================
# MENU
# =============================================================================

def func_about_window():
    janela_sobre = tk.Tk()

    janela_sobre.geometry("820x680")
    janela_sobre.minsize(148, 1)
    janela_sobre.maxsize(1924, 1055)
    janela_sobre.resizable(0, 0)
    janela_sobre.title("About COMBEAMS")
    janela_sobre.configure(background="#d9d9d9")

    la_COMBEAMS = tk.Label(janela_sobre)
    Config_frame(la_COMBEAMS, relx=0.387, rely=0.154, height=30, width=180,
                 ft=Sb_font18, text="""COMBEAMS""")

    la_versao = tk.Label(janela_sobre)
    Config_frame(la_versao, relx=0.427, rely=0.221, height=30, width=120,
                 ft=Sb_font9, text="""Version 1.00.00""")

    la_UFRGS = tk.Label(janela_sobre)
    Config_frame(la_UFRGS, relx=0.241, rely=0.445,
                 height=30, width=424, ft=Sb_font9,
                 text="""Federal University of Rio Grande do Sul - UFRGS""")

    la_PPGEC = tk.Label(janela_sobre)
    Config_frame(la_versao, relx=0.24, rely=0.475,
                 height=30, width=424, ft=Sb_font10,
                 text="""Postgraduate Program in Civil Engineering""")

    la_DESENVOLVIDO = tk.Label(janela_sobre)
    Config_frame(la_DESENVOLVIDO, relx=0.24, rely=0.301, height=30, width=424,
                 ft=Sb_font10, text="""Developed by:""")

    la_DESENVOLVIDO = tk.Label(janela_sobre)
    Config_frame(
        la_DESENVOLVIDO,
        relx=0.24,
        rely=0.351,
        height=30,
        width=424,
        ft=Sb_font10,
        text="""Jorge Tamayo, Lucas Aguiar, Cristian de Campos,\n Daniel Matos, Inácio Morcsh""")

    txt_python = tk.Text(janela_sobre)
    txt_python.place(relx=0.24, rely=0.588, relheight=0.124, relwidth=0.518)
    txt_python.configure(background="#d9d9d9")
    txt_python.configure(blockcursor="1")
    txt_python.configure(borderwidth="0")
    txt_python.configure(font=Sb_font10)
    txt_python.configure(foreground="black")
    txt_python.configure(highlightbackground="#d9d9d9")
    txt_python.configure(highlightcolor="black")
    txt_python.configure(insertbackground="black")
    txt_python.configure(selectbackground="#c4c4c4")
    txt_python.configure(selectforeground="black")
    txt_python.configure(takefocus="0")
    txt_python.configure(wrap="word")
    txt_python.insert(
        INSERT,
        "This software was produced using the Python language in version 3.7.3 \nThe graphical user interface was created using the Tkinter library",
    )
    txt_python.tag_add("here", "0.0", "4.20")
    txt_python.tag_config("here", justify="center")

    txt_responsabilidade = tk.Text(janela_sobre)
    txt_responsabilidade.place(
        relx=0.104,
        rely=0.735,
        relheight=0.175,
        relwidth=0.794)
    txt_responsabilidade.configure(background="#d9d9d9")
    txt_responsabilidade.configure(blockcursor="1")
    txt_responsabilidade.configure(borderwidth="0")
    txt_responsabilidade.configure(font=S_font9)
    txt_responsabilidade.configure(foreground="black")
    txt_responsabilidade.configure(highlightbackground="#d9d9d9")
    txt_responsabilidade.configure(highlightcolor="black")
    txt_responsabilidade.configure(insertbackground="black")
    txt_responsabilidade.configure(selectbackground="#c4c4c4")
    txt_responsabilidade.configure(selectforeground="black")
    txt_responsabilidade.configure(takefocus="0")
    txt_responsabilidade.configure(wrap="word")
    txt_responsabilidade.insert(
        INSERT,
        "\nBSD 3-Clause License \nCopyright (c) 2024, Lucas Aguiar \nRedistribution and use in source and binary forms, with or without modification, are permitted provided that the following conditions are met: \n1. Redistributions of source code must retain the above copyright notice, this list of conditions and the following disclaimer. \n2. Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the following disclaimer in the documentation and/or other materials provided with the distribution. \n3. Neither the name of the copyright holder nor the names of its contributors may be used to endorse or promote products derived from this software without specific prior written permission.",
    )
    txt_responsabilidade.tag_add("here", "0.0", "7.6")
    txt_responsabilidade.tag_config("here", justify="left")

    def close_wondow():
        janela_sobre.destroy()

    btn_fechar_sobre = tk.Button(janela_sobre, command=close_wondow)
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
    btn_fechar_sobre.configure(text="""Close""")

    janela_sobre.mainloop()

def func_window_help():
    janela_sobre = tk.Tk()

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
    txt_responsabilidade.configure(font=S_font10)
    txt_responsabilidade.configure(foreground="black")
    txt_responsabilidade.configure(highlightbackground="#d9d9d9")
    txt_responsabilidade.configure(highlightcolor="black")
    txt_responsabilidade.configure(insertbackground="black")
    txt_responsabilidade.configure(selectbackground="#c4c4c4")
    txt_responsabilidade.configure(selectforeground="black")
    txt_responsabilidade.configure(takefocus="0")
    txt_responsabilidade.configure(wrap="word")
    txt_responsabilidade.insert(
        INSERT,
        "Instructions and use of this program can be found in the following references:\nhttps://github.com/Lucassaaguiar/COMBEAMS",
    )
    txt_responsabilidade.tag_add("here", "0.0", "7.6")
    txt_responsabilidade.tag_config("here", justify="center")

    def close_wondow():
        janela_sobre.destroy()

    btn_fechar_sobre = tk.Button(janela_sobre, command=close_wondow)
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
    btn_fechar_sobre.configure(text="""Close""")

    janela_sobre.mainloop()

#   CREATING THE MENUS
menu_geral = Menu(janela_geral)
menu_arquivo = Menu(menu_geral, tearoff=0)
menu_ajuda = Menu(menu_geral, tearoff=0)

#  CREATING THE FILE MENU
menu_arquivo.add_command(label="New", command=reset_program)
menu_arquivo.add_command(label="Open", command=name_window)
menu_arquivo.add_command(label="Save", command=func_report)
menu_arquivo.add_separator()
menu_arquivo.add_command(label="Close", command=close)
menu_geral.add_cascade(label="File", menu=menu_arquivo)

#  CREATING THE HELP MENU
menu_geral.add_cascade(label="Help", command=func_window_help)

# CREATING THE ABOUT MENU
menu_geral.add_cascade(label="About", command=func_about_window)

janela_geral.config(menu=menu_geral)

# ============================================================================#
janela_geral.mainloop()

# =============================================================================
# # ======================================================================
# # # END END
# # ======================================================================
# =============================================================================

# =============================================================================
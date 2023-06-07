""" Este programa calculará seu perfil empreendedor com base um 30 perguntas
e depois montará um gráfico de radar. Futuramente este programa se tornará um app
"""

import matplotlib.pyplot as plt
import numpy as np
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window
from kivymd.uix.screen import MDScreen

Window.size = 400,600

class Perguntas(MDScreen):
    pass


# class TelaDados(MDScreen):
#     def perguntas(self, resposta):
#         index = int(self.ids['pergunta'].text[:2])
#         if (index + 1) == 31:
#             self.respostas.append(resposta)
#             self.manager.current = TelaFinal().name
#         else:
#             self.ids['pergunta'].text = str(int(self.ids['pergunta'].text[:2]) + 1) + ' )' + ' ' + perguntas[int(self.ids['pergunta'].text[:2])]
#
#             #Respostas do usuário
#             if index == 1:
#                 self.respostas = []
#                 self.respostas.append(resposta)
#             else:
#                 self.respostas.append(resposta)
#             self.manager.current = TelaDados().name
#     pass
#
#     def soma(self):
#         # somas = [(self.respostas[0] + self.respostas[10] + self.respostas[20]), (self.respostas[9] + self.respostas[19] + self.respostas[21]),
#         #          (self.respostas[8] + self.respostas[18] + self.respostas[22]), (self.respostas[7] + self.respostas[17] + self.respostas[23]),
#         #          (self.respostas[6] + self.respostas[16] + self.respostas[24]), (self.respostas[5] + self.respostas[15] + self.respostas[25]),
#         #          (self.respostas[4] + self.respostas[14] + self.respostas[26]), (self.respostas[3] + self.respostas[13] + self.respostas[27]),
#         #          (self.respostas[2] + self.respostas[12] + self.respostas[28]), (self.respostas[1] + self.respostas[11] + self.respostas[29])]
#         #
#         # apura = ["Busca de oportunidades e iniciativa", "Persistência", "Comprometimento",
#         #          "Exigência de Qualidade e eficiência", "Correr riscos calculados", "Estabelecimento de metas",
#         #          "Busca de informação", "Planejamento e monitoramento sistemático", "Persuasão de rede de contatos",
#         #          "independência e autoconfiança"]
#         #
#         # table = pd.DataFrame(dict(r=somas, theta=apura))
#         # fig = px.line_polar(table, r='r', theta='theta', line_close=True)
#         # fig.show()
#         # time.sleep(5)
#         # Personalidade().stop()
#         pass


class Personalidade(MDApp):
    lista_perguntas = ["Faço as coisas antes de solicitado ou antes de forçado pelas circustâncias ",
                 "Busco autonomia em relação às regras e normas preestabelecidas por outras pessoas ",
                 "Formulo estratégias para influenciar ou persuadir outras pessoas ",
                 "Planejo dividindo tarefas de grande porte em subtarefas com prazos definidos ",
                 "Dedico-me pessoalmente a obter informações necessárias para o desenvolvimento de minhas atividades ",
                 "Estabeleço metas e objetivos que são desafiantes e que têm significado pessoal ",
                 "Ao tomar decisões, avalio alternativas e analiso os riscos envolvidos ",
                 "Encontro maneiras de fazer as coisas da melhor forma, mais rápido ou mais barata ",
                 "Assumo responsabilidde pessoal por solucionar problemas que possam \n prejudicar a conclusão de um trabalho nas condições estipuladas ",
                 "Busco soluções diante de um obstáculo significativo ",
                 "Desenvolvo novas ideias e projetos além das atuais soluções ou propostas estabelecidas ",
                 "Mantenho meu ponto de vista mesmo diante de oposição ou de resultados \n inicialmente dasanimadores ",
                 "Utilizo minhas rede de contatos como estratégia para atingir meus objetivos ",
                 "Constantemente reviso meus planos, lavando em conta os resultados \n obtidos e as mudanças que possam ter ocorrido ",
                 "Pesquiso como realizar determinada atividade ou projeto, antes de sua execução ",
                 "Tenho visão de longo prazo do que espero alcanças, de forma clara e específica ",
                 "Analiso as informações e tomo decisões para reduzir riscos e controlar resultados ",
                 "Faço as coisas de maneira que satisfaça ou excedam padrões de excelência ",
                 "Coloboro com a equipe de tabalho ou me coloco no lugar deles, \nse necessário, para terminar um trabalho ou tarefa ",
                 "Ajo repetidamente ou mudo para uma estratégia alternativa, a fim de enfrentar\n um desafio ou superar um obstáculo ",
                 "Aproveito oportunidades fora do comum para iniciar um novo projeto ou \natividade, estabelecer parcerias, ampliar aprendizados ",
                 "Faço um sacrifício pessoal ou um esforço extraordinário para completar uma tarefa ",
                 "Esforço-me para atender ou superar as expectativas das pessoas que me\n demandam tarefas e atividades diversas ",
                 "Asseguro que trabalho seja terminado a tempo e que atendas aos padrões\n de qualidade previamente combinados ",
                 "Coloco-me em situação que implicam desafios ou riscos moderados ",
                 "Estabeleço objetivos de curto prazo mensuráveis ",
                 "Consulto especialistas de um determinado assunto para esclarecimento de\n dúvidas e busca de apoio na realização de uma tarefa ou atividade ",
                 "Mantenho registros dos meus ganhos e gastos e utilizo-os para tomar decisões\n sobre compras ou investimentos ",
                 "Tenho boas relações com as pessoas com vistas em manter e ampliar minha rede\n de contatos ",
                 "Expresso confiança na minha própia capacidade de realizar uma tarefa \ndifícil ou de enfrentar um desafio "]
    resposta = []
    contador = 0

    def build(self):
        return Builder.load_file("KV/main.kv")

    def perguntas(self):
        self.contador += 1
        self.root.screens[1].ids.label_perguntas.text = self.lista_perguntas[self.contador]
        print(self.resposta)

    def mudar_tela(self, nome):
        if nome == "instrucao":
            self.root.screens[3].ids.text_instr.text = ''' O teste de Personalidade Empresarial é um teste autoavaliativo, portanto é crucial que todas as perguntas sejam respondidas em concordância com seus hábitos e personalidade.\n\n Para cada pergunta você terá 5 opções de resposta numeradas de 1 á 5 sendo, 1 como "não me identifico" e 5 como "me identifico totalmente".\n\n Ao final do teste seu resultado será computado e apresentado em um gráfico de radar.'''
            self.root.current = nome

        if nome == "perguntas":
            print(self.root.screens[1].ids)
            self.root.current = nome
            self.root.screens[1].ids.label_perguntas.text = "Faço as coisas antes de solicitado ou antes de forçado pelas circustâncias "
        else:
            self.root.current = nome

    def montar_grafico_radar(self):
        cat = ["Busca de oportunidades\n e iniciativa", "Persistência", "Comprometimento",
               "Exigência de\n Qualidade\n e eficiência", "Correr riscos calculados", "Estabelecimento de metas",
               "Busca de informação", "Planejamento e\n monitoramento\n sistemático", "Persuasão de\n rede de contatos",
               "independência e\n autoconfiança"]
        values = [(self.respostas[0] + self.respostas[10] + self.respostas[20]),(self.respostas[9] + self.respostas[19] + self.respostas[21]),
             (self.respostas[8] + self.respostas[18] + self.respostas[22]), (self.respostas[7] + self.respostas[17] + self.respostas[23]),
             (self.respostas[6] + self.respostas[16] + self.respostas[24]), (self.respostas[5] + self.respostas[15] + self.respostas[25]),
             (self.respostas[4] + self.respostas[14] + self.respostas[26]), (self.respostas[3] + self.respostas[13] + self.respostas[27]),
             (self.respostas[2] + self.respostas[12] + self.respostas[28]), (self.respostas[1] + self.respostas[11] + self.respostas[29])]

        N = len(cat)

        x_as = [n / float(N) * 2 * np.pi for n in range(N)]

        # Because our chart will be circular we need to append a copy of the first
        # value of each list at the end of each list with data
        values += values[:1]
        x_as += x_as[:1]

        # Set color of axes
        plt.rc('axes', linewidth=0.5, edgecolor="#888888")

        # Create polar plot
        ax = plt.subplot(111, polar=True)

        # Set clockwise rotation. That is:
        ax.set_theta_offset(np.pi / 2)
        ax.set_theta_direction(-1)

        # Set position of y-labels
        ax.set_rlabel_position(0)

        # Set color and linestyle of grid
        ax.xaxis.grid(True, color="#888888", linestyle='solid', linewidth=0.5)
        ax.yaxis.grid(True, color="#888888", linestyle='solid', linewidth=0.5)

        # Set number of radial axes and remove labels
        plt.xticks(x_as[:-1], [])

        # Set yticks
        plt.yticks([1, 3, 5, 7, 9, 11, 13, 15], ["1", "3", "5", "7", "9", "11", "13", "15"])

        # Plot data
        ax.plot(x_as, values, linewidth=0, linestyle='solid', zorder=3)

        # Fill area
        ax.fill(x_as, values, 'b', alpha=0.3)

        # Set axes limits
        plt.ylim(0, 15)

        # Draw ytick labels to make sure they fit properly
        for i in range(N):
            angle_rad = i / float(N) * 2 * np.pi

            if angle_rad == 0:
                ha, distance_ax = "center", 3
            elif 0 < angle_rad < np.pi:
                ha, distance_ax = "left", 1
            elif angle_rad == np.pi:
                ha, distance_ax = "center", 1
            else:
                ha, distance_ax = "right", 1

            # Forma de como será posicionado os labels
            # ax.text(ângulo, distância do centro, texto, tamanho, alinhamento horizontal, alinhamento vertical)
            ax.text(angle_rad, 15 + distance_ax, cat[i], size=12, horizontalalignment=ha, verticalalignment="center")

        # plt.savefig("fig1.png")
        plt.show()
        # plt.close()



Personalidade().run()


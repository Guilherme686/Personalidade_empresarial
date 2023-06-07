""" Este programa calculará seu perfil empreendedor combase um 30 perguntas
e depois montará um gráfico de radar. Futuramente este programa se tornará um app
"""

import plotly.express as px, pandas as pd
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
import time


'''
def Perfil():
    "Calcula o perfil de empreendedor"

    #------------------------- Definição das perguntas e respostas ------------------------------------------------
    perguntas = ["Faço as coisas antes de solicitado ou antes de forçado pelas circustâncias ",
                 "Busco autonomia em relação às regras e normas preestabelecidas por outras pessoas ",
                 "Formulo estratégias para influenciar ou persuadir outras pessoas ",
                 "Planejo dividindo tarefas de grande porte em subtarefas com prazos definidos ",
                 "Dedico-me pessoalmente a obter informações necessárias para o desenvolvimento de minhas atividades ",
                 "Estabeleço metas e objetivos que são desafiantes e que têm significado pessoal ",
                 "Ao tomar decisões, avalio alternativas e analiso os riscos envolvidos ",
                 "Encontro maneiras de fazer as coisas da melhor forma, mais rápido ou mais barata ",
                 "Assumo responsabilidde pessoal por solucionar problemas que possam prejudicar a conclusão de um trabalho nas condições estipuladas ",
                 "Busco soluções diante de um obstáculo significativo ",
                 "Desenvolvo novas ideias e projetos além das atuais soluções ou propostas estabelecidas ",
                 "Mantenho meu ponto de vista mesmo diante de oposição ou de resultados inicialmente dasanimadores ",
                 "Utilizo minhas rede de contatos como estratégia para atingir meus objetivos ",
                 "Constantemente reviso meus planos, lavando em conta os resultados obtidos e as mudanças que possam ter ocorrido ",
                 "Pesquiso como realizar determinada atividade ou projeto, antes de sua execução ",
                 "Tenho visão de longo prazo do que espero alcanças, de forma clara e específica ",
                 "Analiso as informações e tomo decisões para reduzir riscos e controlar resultados ",
                 "Faço as coisas de maneira que satisfaça ou excedam padrões de excelência ",
                 "Coloboro com a equipe de tabalho ou me coloco no lugar deles, se necessário, para terminar um trabalho ou tarefa ",
                 "Ajo repetidamente ou mudo para uma estratégia alternativa, a fim de enfrentar um desafio ou superar um obstáculo ",
                 "Aproveito oportunidades fora do comum para iniciar um novo projeto ou atividade, estabelecer parcerias, ampliar aprendizados ",
                 "Faço um sacrifício pessoal ou um esforço extraordinário para completar uma tarefa ",
                 "Esforço-me para atender ou superar as expectativas das pessoas que me demandam tarefas e atividades diversas ",
                 "Asseguro que trabalho seja terminado a tempo e que atendas aos padrões de qualidade previamente combinados ",
                 "Coloco-me em situação que implicam desafios ou riscos moderados ",
                 "Estabeleço objetivos de curto prazo mensuráveis ",
                 "Consulto especialistas de um determinado assunto para esclarecimento de dúvidas e busca de apoio na realização de uma tarefa ou atividade ",
                 "Mantenho registros dos meus ganhos e gastos e utilizo-os para tomar decisões sobre compras ou investimentos ",
                 "Tenho boas relações com as pessoas com vistas em manter e ampliar minha rede de contatos ",
                 "Expresso confiança na minha própia capacidade de realizar uma tarefa difícil ou de enfrentar um desafio "]
    
    respostas = []

    #-------------------- Introdução e Regras --------------------------------
    print("""Para preencher a autoavaliação, reflita e escolha o número que melhor
descreva a sua prática no dia a dia, conforme cada comportamento listado. \n
1 - Numca pratico este comportamento. \n
2 - Raramente pratico este comportamento. \n
3 - Algumas vezes pratico este comportamento. \n
4 - Na maioria das vezes pratico este comportamento. \n
5 - Sempre pratico este comportamento.\n""")

    #---------- For loop para respostas ------------------
    for i in range(len(perguntas)):
        print(i+1,")")
        respostas.append(int(input(perguntas[i])))
        print("\n")

    #---------- Definição de parâmetros ------------------------------
    apura = ["Busca de oportunidades e iniciativa", "Persistência", "Comprometimento", "Exigência de Qualidade e eficiência", "Correr riscos calculados", "Estabelecimento de metas",
             "Busca de informação", "Planejamento e monitoramento sistemático", "Persuasão de rede de contatos", "independência e autoconfiança"]
    #---------- Somas dos resultados ---------------------------------
    somas = [(respostas[0]+respostas[10]+respostas[20]),(respostas[9]+respostas[19]+respostas[21]), (respostas[8]+respostas[18]+respostas[22]), (respostas[7]+respostas[17]+respostas[23]),
             (respostas[6]+respostas[16]+respostas[24]),(respostas[5]+respostas[15]+respostas[25]),(respostas[4]+respostas[14]+respostas[26]),(respostas[3]+respostas[13]+respostas[27]),
             (respostas[2]+respostas[12]+respostas[28]),(respostas[1]+respostas[11]+respostas[29])]

    #------- Calculo de Realização, Planejamento e Poder -------------

    [realiza, planeja, poder] = [0,0,0]
    
    for j in range(len(somas)):
        if j <= 4:
            realiza += somas[j]
        elif j > 4 and j <= 7:
            planeja += somas[j]
        else:
            poder += somas[j]

    print("Realização =", realiza)
    print("\nPlanejamento =", planeja)
    print("\nPoder =", poder)
        
    #--------------- Plot do gráfico em radar ----------------------------
    table = pd.DataFrame(dict(r = somas, theta = apura))
    fig = px.line_polar(table, r = 'r', theta = 'theta', line_close = True)
    fig.show()
'''
perguntas = ["Faço as coisas antes de solicitado ou antes de forçado pelas circustâncias ",
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

contador_perguntas = 0


class Gerenciador(ScreenManager):
    pass
        
class TelaInicial(Screen):
    pass

class TelaInstrucoes(Screen):
    pass

class TelaFinal(Screen):
    pass

class TelaDados(Screen):
    def perguntas(self, resposta):
        index = int(self.ids['pergunta'].text[:2])
        if (index + 1) == 31:
            self.respostas.append(resposta)
            self.manager.current = TelaFinal().name
        else:
            self.ids['pergunta'].text = str(int(self.ids['pergunta'].text[:2]) + 1) + ' )' + ' ' + perguntas[int(self.ids['pergunta'].text[:2])]

            #Respostas do usuário
            if index == 1:
                self.respostas = []
                self.respostas.append(resposta)
            else:
                self.respostas.append(resposta)
            self.manager.current = TelaDados().name
    pass

    def soma(self):
        somas = [(self.respostas[0] + self.respostas[10] + self.respostas[20]), (self.respostas[9] + self.respostas[19] + self.respostas[21]),
                 (self.respostas[8] + self.respostas[18] + self.respostas[22]), (self.respostas[7] + self.respostas[17] + self.respostas[23]),
                 (self.respostas[6] + self.respostas[16] + self.respostas[24]), (self.respostas[5] + self.respostas[15] + self.respostas[25]),
                 (self.respostas[4] + self.respostas[14] + self.respostas[26]), (self.respostas[3] + self.respostas[13] + self.respostas[27]),
                 (self.respostas[2] + self.respostas[12] + self.respostas[28]), (self.respostas[1] + self.respostas[11] + self.respostas[29])]

        apura = ["Busca de oportunidades e iniciativa", "Persistência", "Comprometimento",
                 "Exigência de Qualidade e eficiência", "Correr riscos calculados", "Estabelecimento de metas",
                 "Busca de informação", "Planejamento e monitoramento sistemático", "Persuasão de rede de contatos",
                 "independência e autoconfiança"]

        table = pd.DataFrame(dict(r=somas, theta=apura))
        fig = px.line_polar(table, r='r', theta='theta', line_close=True)
        fig.show()
        time.sleep(5)
        Personalidade().stop()



class Personalidade(App):
    def build(self):
        return Gerenciador()

Personalidade().run()


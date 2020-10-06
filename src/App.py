import PySimpleGUI as sg
import json

class App(object):
    def __init__(self):
        sg.theme('Reddit')

        layout_inicial = [
            [sg.Text('Assa Cuca', font=("BratonComposer-Regular", 30), text_color='#f94a5a', background_color="#ffe6e8")],
            [sg.Image('res/mulher.png', background_color='#ffe6e8')],
            [sg.Button(key='-Button_Entrar-',image_filename='res/positivo_img.png', button_color=('#ffe6e8', '#ffe6e8'), border_width=0)]
        ]

        self.janela = sg.Window('Assa Cuca', layout_inicial, size=(320, 480), element_justification='center', background_color='#ffe6e8')

    def atualiza_eventos(self):
        while True:
            evento_pagina_inicial, valor_pagina_inicial = self.janela.read()
            if evento_pagina_inicial == sg.WINDOW_CLOSED:
                break
            if evento_pagina_inicial == '-Button_Entrar-':
                self.janela.Close()
                self.criar_layout_botoes()
                break

    def criar_layout_botoes(self):
        layout = [
            [sg.Text(background_color="#ffe6e8", size=(4, 9))],
            [sg.Text(background_color="#ffe6e8", size=(8, 1)), sg.Button(key="Button-Paes", image_filename='res/butt_paes.png', border_width=0, button_color=('#ffe6e8', '#ffe6e8'))],
            [sg.Text(background_color="#ffe6e8", size=(8, 1)), sg.Button(key="Button-Bolos", image_filename='res/butt_bolos.png', border_width=0, button_color=('#ffe6e8', '#ffe6e8'))],
            [sg.Text(background_color="#ffe6e8", size=(8, 1)), sg.Button(key="Button-Doces", image_filename='res/butt_doces.png', border_width=0, button_color=('#ffe6e8', '#ffe6e8'))],
            [sg.Text(background_color="#ffe6e8", size=(8, 1)), sg.Button(key="Button-Salgados", image_filename='res/butt_salgados.png', border_width=0, button_color=('#ffe6e8', '#ffe6e8'))]
        ]
        janela_botoes = sg.Window("Assa Cuca", layout, size=(320, 480), background_color='#ffe6e8')
        while True:
            evento_pagina_escolha, valor_pagina_escolha = janela_botoes.read()
            if evento_pagina_escolha == sg.WINDOW_CLOSED:
                break
            if evento_pagina_escolha == 'Button-Paes':
                janela_botoes.close()
                self.verificar_receita('paes.json')
                break
            if evento_pagina_escolha == 'Button-Bolos':
                janela_botoes.close()
                self.verificar_receita('bolos.json')
                break
            if evento_pagina_escolha == 'Button-Doces':
                janela_botoes.close()
                self.verificar_receita('doces.json')
                break
            if evento_pagina_escolha == 'Button-Salgados':
                janela_botoes.close()
                self.verificar_receita('salgados.json')
                break

    def verificar_receita(self, arquivo):
        try:
            with open(f'src/receitas/{arquivo}') as receitas:
                modelo = json.load(receitas)
        except FileNotFoundError:
            with open(f'src/receitas/{arquivo}', 'w') as receitas:
                modelo = {'Receitas': []}
                file = json.dumps(modelo, indent=2)
                receitas.write(file)

        if len(modelo["Receitas"]) == 0:
            self.adicionar_receita_layout(arquivo)
        else:
            self.ver_receitas_layout(arquivo)

    def ver_receitas_layout(self, file):
        treedata_ingredientes = sg.TreeData()

        tree_ingredientes = sg.Tree(treedata_ingredientes, headings=[], key='Tree-Igredientes')

        tabela_ingredientes = sg.Tab('Ingredientes', [[tree_ingredientes]], background_color='#ffe6e8', border_width=0, font=('Butter Chicken'), title_color='#37173f')
        tabela_modo_de_preparo = sg.Tab('Modo de Preparo', [[sg.Multiline()]], background_color='#ffe6e8', border_width=1, font=('Butter Chicken'), title_color='#37173f')

        layout = [
            [sg.TabGroup([[tabela_ingredientes]], font=('BratonComposer-Regular'), selected_title_color='#37173f', border_width=0, selected_background_color='#ffe6e8')],
            [sg.TabGroup([[tabela_modo_de_preparo]], font=('BratonComposer-Regular'), selected_title_color='#37173f', border_width=0, selected_background_color='#ffe6e8')]
        ]

        janela_receitas = sg.Window("Assa Cuca", layout, size=(320, 480), background_color='#ffe6e8')
        while True:
            evento_receitas, valor_receitas = janela_receitas.read()
            if evento_receitas == sg.WINDOW_CLOSED:
                break

    def adicionar_receita_layout(self, arquivo):
        layout = [
            [sg.Button(key='Button-Voltar', image_filename='res/butt_voltar.png', border_width=0, button_color=('#ffe6e8', '#ffe6e8'))],
            [sg.Text(background_color="#ffe6e8", size=(10,6))],
            [sg.Text(background_color="#ffe6e8", size=(9,1)), sg.Button(key='Button-Novo', image_filename='res/img_novo.png', border_width=0, button_color=('#ffe6e8', '#ffe6e8'))]
        ]

        janela_nova_receita = sg.Window("Assa Cuca", layout, size=(320, 480), background_color='#ffe6e8')
        while True:
            evento, valor = janela_nova_receita.read()
            if evento == sg.WINDOW_CLOSED:
                break
            if evento == 'Button-Voltar':
                janela_nova_receita.close()
                self.criar_layout_botoes()
            if evento == 'Button-Novo':
                janela_nova_receita.close()
                self.nova_receita()

    def add_igrediente(self):
        layout = [
            [sg.InputText(border_width=0)],
            [sg.Button('Adicionar', key='Button-Adicionar', border_width=0)]
        ]
        janela = sg.Window('Adicionar Igrediente', layout)
        while True:
            evento, valor = janela.read()
            if evento == sg.WINDOW_CLOSED:
                break
            if evento == 'Button-Adicionar':
                janela.close()
                return valor

    def add_icone(self, name):
        if 'trigo' in name:
            icon = 'res/icons/trigo.png'
        elif 'feijao' in name:
            icon = 'res/icons/feijao.png'
        elif 'frango' in name:
            icon = 'res/icons/frango.png'
        elif 'oleo' in name or 'óleo' in name:
            icon = 'res/icons/oleo.png'
        elif 'ovo' in name:
            icon = 'res/icons/ovo.png'
        elif 'queijo' in name:
            icon = 'res/icons/queijo.png'
        elif 'arroz' in name:
            icon = 'res/icons/arroz.png'
        else:
            icon = None

        return icon

    def nova_receita(self):
        tree = sg.TreeData()
        tree.Insert('', 'ING', 'IngredienteS', [])

        menu = ['Menu', ['Novo igrediente', 'DELETAR']]
        coluna_igredientes = sg.Column([[sg.Tree(tree, headings=[], key='Tree-Novos_Ingredientes', text_color='#f94a5a', font=('BratonComposer-Regular'), right_click_menu=menu, col0_width=100, num_rows=100, row_height=30,background_color="#ffcace", selected_row_colors=('#f94a5a','#f6bac1'))]], background_color="#ffe6e8")
        coluna_preparo = sg.Column([[sg.Multiline(size=(400,480), border_width=0)]], background_color="#ffe6e8")

        layout = [
            [sg.Multiline(background_color="#ffe6e8", text_color='#f94a5a',font=('BratonComposer-Regular'))],
            [sg.Pane([coluna_igredientes, coluna_preparo], orientation='horizontal', border_width=0, show_handle=False, background_color="#ffe6e8")]
        ]

        janela_criar_receita = sg.Window("Assa Cuca", layout, size=(420, 480), background_color="#ffe6e8", resizable=True)
        while True:
            evento, valor = janela_criar_receita.read()
            if evento == sg.WINDOW_CLOSED:
                break
            if evento == 'Novo igrediente':
                janela_criar_receita.disable()

                valor = self.add_igrediente()
                janela_criar_receita.enable()

                if valor != None:
                    icone = self.add_icone(valor[0].lower())
                    janela_criar_receita.Element('Tree-Novos_Ingredientes').Update(tree, tree.Insert('', f'{valor[0]}', valor[0], [], icon=icone))
                    

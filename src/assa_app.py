import PySimpleGUI as sg
from time import sleep

class AssaCucaApp:
    def __init__(self):
        self.janela_inicial = self.criar_tela_inicial()
        self.janela_categorias = None
        self.janela_menu_adicionar = None
        self.APP_RUN = True
        self.verificar_eventos()

    def criar_tela_inicial(self):
        layout_inicial = [
            [
                sg.Text(
                    'Assa Cuca',
                    font=("BratonComposer-Regular", 30),
                    text_color='#f94a5a',
                    background_color="#ffe6e8"),
            ],
            [
                sg.Button(
                    key='okay',
                    image_filename='res/mulher.png',
                    button_color = ('#ffe6e8',"#ffe6e8"),
                    border_width = 0,
                    pad = (0,0))]
        ]
        return sg.Window(
            title='Assa Cuca',
            layout=layout_inicial,
            background_color="#ffe6e8",
            finalize=True,
            element_justification='center')

    def criar_tela_escolher_categoria(self):
        tabelas = sg.TabGroup(
                key = "LB_receitas",
                font = ("BratonComposer-Regular", 12),
                background_color = "#ffe6e8",
                title_color='#f94a5a',
                selected_title_color = '#f94a5a',
                selected_background_color = '#e8b3ae',
                border_width = 0,
                layout=[[
                    sg.Tab(
                        key="Bolos",
                        background_color = '#e8b3ae',
                        title = 'Bolos',
                        layout = [[
                            sg.Listbox([], select_mode='LISTBOX_SELECT_MODE_SINGLE',key='Bolos_lista', size=(40,20), no_scrollbar=True,right_click_menu=["",["Nova Receita", 'Editar Receita','Deletar Receita']], font=("BratonComposer-Regular", 12))
                        ]]
                    ),
                    sg.Tab(
                        background_color = '#e8b3ae',
                        title = 'Doces',
                        layout = [[
                            sg.Listbox([], key='Doces_lista', size=(40,20), no_scrollbar=True,right_click_menu=["",["Nova Receita", 'Editar Receita','Deletar Receita']], font=("BratonComposer-Regular", 12))
                        ]]
                    ),
                    sg.Tab(
                        background_color = '#e8b3ae',
                        title = 'Pães',
                        layout = [[
                            sg.Listbox([], key='Pães_lista', size=(40,20), no_scrollbar=True,right_click_menu=["",["Nova Receita", 'Editar Receita','Deletar Receita']], font=("BratonComposer-Regular", 12))
                        ]]
                    ),
                    sg.Tab(
                        background_color = '#e8b3ae',
                        title = 'Salgados',
                        layout = [[
                            sg.Listbox([], key='Salgados_lista', size=(40,20), no_scrollbar=True, right_click_menu=["",["Nova Receita", 'Editar Receita','Deletar Receita']], font=("BratonComposer-Regular", 12))
                        ]]
                    )
                ]])
        return tabelas

    def criar_tela_principal_de_receitas(self, receita):
        layout_categorias = [[
            sg.Frame(
                'Categorias', [[self.criar_tela_escolher_categoria(), sg.VerticalSeparator(color='#f94a5a')]],
                border_width=0, title_location='n',
                background_color="#ffe6e8", font=("BratonComposer-Regular", 30),
                title_color='#f94a5a'
            ),
            self.criar_tela_informacoes_receita()
        ]]
        return sg.Window('Assa Cuca', layout=layout_categorias, finalize=True, background_color="#ffe6e8")

    def criar_tela_informacoes_receita(self):
        informacoes_receita = [
            [sg.Text("Modo de Preparo", font=("BratonComposer-Regular", 18))],
            [sg.Multiline()],
            [sg.Text("IngredienteS", font=("BratonComposer-Regular", 18))],
            [sg.Multiline()],
        ]
        layout =sg.Frame(
                '----', informacoes_receita,
                border_width=0, title_location='n',
                font=("BratonComposer-Regular", 30), title_color='#f94a5a',
                key='F_nome'
            )
        return layout

    def janela_adicionar_receita(self):
        layout_temp = [[
            sg.Input(key='INP_adicionar', border_width=0),
            sg.Button(
                "Criar",
                border_width=0,
                font="BratonComposer-Regular",
                button_color= ('#f94a5a','#e8b3ae'),
            )
        ]]
        return sg.Window('Adicionar Receita', layout_temp,
            element_justification='center',
            finalize=True,
            background_color = '#e8b3ae',
        )

    def verificar_eventos(self):
        while self.APP_RUN:
            window, evento, valor = sg.read_all_windows()
            if window == self.janela_inicial and evento == 'okay':
                self.janela_inicial.hide()
                self.janela_categorias = self.criar_tela_principal_de_receitas('---')

            if window == self.janela_categorias:
                if evento == sg.WIN_CLOSED:
                    self.APP_RUN = False

                if evento == 'Nova Receita':
                    nome_tabela = valor['LB_receitas']+"_lista"
                    receitas = valor[nome_tabela]
                    self.janela_menu_adicionar = self.janela_adicionar_receita()

                if evento == 'Editar Receita':
                    nome_tabela = valor['LB_receitas']+"_lista"
                    receita = self.janela_categorias.find_element(nome_tabela).get()
                    self.janela_categorias['F_nome'].update(value=receita[0])

            if window == self.janela_menu_adicionar:
                if evento == sg.WIN_CLOSED:
                    self.janela_menu_adicionar.close()

                if evento == "Criar" and valor["INP_adicionar"] != '':
                    receitas = self.janela_categorias.find_element(nome_tabela).GetListValues()
                    receitas.insert(0,valor["INP_adicionar"])
                    self.janela_categorias.find_element(nome_tabela).Update(receitas)
                    self.janela_menu_adicionar.close()

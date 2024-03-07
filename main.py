
#flet é a biblioteca usada neste projeto para criar o site/app
import flet as ft 

def main(pagina):
    titulo = ft.Text("Hashzap")
    chat = ft.Column()
    campo_mensagem = ft.TextField(label="Escreva sua mensagem aqui")
    nome_usuario = ft.TextField(label="Escreva o seu nome")
    
    
    
    def enviar_mensagem_tunel(informaçao):
        chat.controls.append(ft.Text(informaçao))
        pagina.update()
    pagina.pubsub.subscribe(enviar_mensagem_tunel)
    
    def enviar_mensagem(evento):
        texto_campo_mensagem = f"{nome_usuario.value}: {campo_mensagem.value}"
        
        pagina.pubsub.send_all(texto_campo_mensagem)
        
        campo_mensagem.value = ""
        pagina.update()
    botao_enviar = ft.ElevatedButton("Enviar mensagem", on_click=enviar_mensagem)
    
    def entrar_chat(evento):#codigo para que ao entrar no chat o popup e o botao de iniciar suma, entrando os botoes do chat
        popup.open = False 
        pagina.remove(botao_iniciar)
        linha_mensagem = ft.Row([
            campo_mensagem,
            botao_enviar
        ])
        pagina.add(chat)
        pagina.add(linha_mensagem)
        #pagina.update serve para atualizar a pagina toda vez que adicionamos algo nela
        texto = f"{nome_usuario.value} entrou no chat"
        pagina.pubsub.send_all(texto)
        pagina.update()
        
    popup = ft.AlertDialog(open=False,
                           modal=True,
                           title=ft.Text("Bem vindo ao Hashzap"),
                           content=nome_usuario,
                           actions=[ft.ElevatedButton("Enviar", on_click=entrar_chat)]
                           )
    
    def iniciar_chat(evento):
        pagina.dialog = popup
        popup.open = True
        pagina.update()
    botao_iniciar = ft.ElevatedButton("Iniciar chat", on_click=iniciar_chat)
    pagina.add(titulo) #codigo para adicionar as funçoes criadas na pagina
    pagina.add(botao_iniciar)
    
    
#funçao que avisa ao flet que o app começa ali na funçao main   
ft.app(main, port=5000, view=ft.WEB_BROWSER)
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

from numpy import number


from banco import insert,read,delete,update

#CORES
orange = '#ff4700'
black = "#000000"

app = Tk()
app.title("Sistema Py")
app.geometry("1080x500")
app.configure(background=black)
app.resizable(width=FALSE, height=FALSE)
tree = ttk.Treeview(app)

def tabela():

    for data in tree.get_children():
        tree.delete(data)

    for result in reverse(read()):
        tree.insert(parent='', index='end', iid=result, text="", values=(result), tag="orow")

    tree.tag_configure('orow', background='#EEEEEE')
    tree.grid(row=1, column=5, columnspan=4, rowspan=5, padx=10, pady=10)

def reverse(tuples):
    new_tup = tuples[::-1]
    return new_tup

def insert_data():
   
    itemId = str(id_user.get())
    nome_user = str(name_user.get())
    usuario = str(usuario_user.get())
    email = str(email_user.get())


    lista_inserir = [itemId, nome_user, usuario, email]

    for verificarVazio in lista_inserir:
        if verificarVazio == "":
          messagebox.showerror(title='Erro', message='Preencha todos os campos')
          return
    
    insert(str(itemId), str(nome_user.lower()), str(usuario.lower()), str(email.lower()))
    messagebox.showinfo(title="Sucesso", message="Cadastro realizado")
    
    id_user.delete(0, 'end')
    name_user.delete(0, 'end')
    usuario_user.delete(0, 'end')
    email_user.delete(0, 'end')

    tabela()

def delete_data():

    try:
        selected_item = tree.selection()[0]
        deleteData = str(tree.item(selected_item)['values'][0])
        delete(deleteData)
        messagebox.showwarning(title="Deletado", message="Cadastro Deletado")
        
        tabela()
    except IndexError:
        messagebox.showerror(title="Erro Delete", message="Selecione um dos usuários da tabela.")



def update_data():

    try:
        selected_item = tree.selection()[0]
        update_name = tree.item(selected_item)['values'][0]
        update(id_user.get(), name_user.get(), usuario_user.get(), email_user.get(), update_name)

        tabela()
    except IndexError:
         messagebox.showerror(title="Erro Update", message="Selecione um dos usuários da tabela.")


h1 = "Sistema De Cadastro"

titleLabel = Label(app,fg= 'white' , bg= black, text=h1, font=('Arial bold', 30), bd=5)
titleLabel.grid(row=0, column=0, columnspan=8, padx=25, pady=20)


idLabel = Label(app,fg=orange, bg= black, text="ID", font=('Arial bold', 15))
idLabel.grid(row=1, column=0, padx=10, pady=10)

nameLabel = Label(app,fg=orange, bg= black, text="Nome", font=('Arial bold', 15))
nameLabel.grid(row=2, column=0, padx=10, pady=10)

usuarioLabel = Label(app,fg=orange, bg= black, text="Usuario", font=('Arial bold', 15))
usuarioLabel.grid(row=3, column=0, padx=10, pady=10)

emailLabel = Label(app,fg=orange, bg= black, text="E-mail", font=('Arial bold', 15))
emailLabel.grid(row=4, column=0, padx=10, pady=10)

id_user = Entry(app, width=25, bd=5, font=('Arial bold', 15))
id_user.grid(row=1, column=1, columnspan=3, padx=5, pady=5)

name_user = Entry(app, width=25, bd=5, font=('Arial bold', 15))
name_user.grid(row=2, column=1, columnspan=3, padx=5, pady=5)

usuario_user = Entry(app, width=25, bd=5, font=('Arial bold', 15))
usuario_user.grid(row=3, column=1, columnspan=3, padx=5, pady=5)

email_user = Entry(app, width=25, bd=5, font=('Arial bold', 15))
email_user.grid(row=4, column=1, columnspan=3, padx=5, pady=5)




buttonEnter = Button(
    app, text="Enviar", padx=5, pady=5, width=5,
    bd=3, font=('Arial', 15), bg=orange,command=insert_data )
buttonEnter.grid(row=5, column=1, columnspan=1,pady=10)

buttonUpdate = Button(
    app, text="Atualizar", padx=5, pady=5, width=7,
    bd=3, font=('Arial', 15),  bg=orange,command=update_data)
buttonUpdate.grid(row=5, column=2, columnspan=1)

buttonDelete = Button(
    app, text="Deletar", padx=5, pady=5, width=5,
    bd=3, font=('Arial', 15),  bg=orange, command=delete_data )
buttonDelete.grid(row=5, column=3, columnspan=1)

#CARREGAR TABELA

style = ttk.Style()
style.configure("Treeview.Heading", font=('Arial bold', 15))

tree['columns'] = ("ID", "Nome", "Usuário", "E-mail")
tree.column("#0", width=0, stretch=NO)
tree.column("ID", anchor=W, width=50)
tree.column("Nome", anchor=W, width=200)
tree.column("Usuário", anchor=W, width=100)
tree.column("E-mail", anchor=W, width=270)
tree.heading("ID", text="ID", anchor=W)
tree.heading("Nome", text="Nome", anchor=W)
tree.heading("Usuário", text="Usuário", anchor=W)
tree.heading("E-mail", text="E-mail", anchor=W)

for data in tree.get_children():
  tree.delete(data)

for result in reverse(read()):
   tree.insert(parent='', index='end', iid=0, text="", values=(result), tag="orow")

tree.tag_configure('orow', background='#FFFFFF', font=('Arial bold', 15))
tree.grid(row=1, column=5, columnspan=4, rowspan=5, padx=10, pady=10)


app.mainloop()
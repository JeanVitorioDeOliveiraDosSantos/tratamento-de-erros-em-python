# git init : Ele inicia o arquivo git

# git status: ele mostrará o status atual da pag

# git add . : adiciona todas as pastas pedentes ou 
# seja adiciona tudo o que estiver pendente

# git add "nome do arquivo": ele vai adicionar apenas este documento 

# git commit -m " mensagem que especifica a alteração ": ele salva as alterções 

# git config --global user-name " aqui coloque sei=u nome de usuario registrado no GitHub "

# git config --global user " Aqui coloque seu e-mail cadastrado no GitHub " : Altera o e-mail onde estão suas alterações
 
# git remote add origin " link da pag onde vc fez o novo repositorio a ser efetuado o comando push "
 
# push : ele vai uppar as suas alterações para o server (" muitas vezes no primeiro push dentro de 
# uma branch vc terá que executar o comando que o git te pedirá ")

# git reflog: verá os hitorico de commits  

# git log: devolverá um inventario dos comits, o hitorico ///// digite a letra : q no seu teclado e ele irá sair do log

# git hist: verá o hitorico de commits assim como o raflog

# git reset --hard " id alcançavel pelos historicos de commits ": isso permitira que vc navegue entre versões antigas e niovas do seu cod 

# branche: são caminhos que vc vai seguir ou seja vc pode ter varias versões de um mesmo cod sem precisar perder o principal 

# merge: fusão de branchs

# git branch: isso lhe dirá quantas branchs existem no documneto

# git branch "nome aleatorio": isso vai definir uma nova branch

# git checkout "nome da branch": Isso irá te dar acesso a uma branche ou seja acesso

# git pull: caso vc esteja trabalhando com mais alguém isso trará as alteraçoes do servidor para a maquina

# git diff: Antes de vc adicionar as mudanças aponta as mudanças feitas no cod  

# git revert " id ": apaga algo

# git remote -v: vai remover o URL que vc tinha adicionado para usar como diretorio

# Caso vc queira ter um arquivo no qual o git não vai monitorar dentro da sua pasta salve o arquivo com o seguinte nome:
# .gitignore

# git diff --staged: isso mostrará o que está na sua staged area ou seja vc deu add mas ainda não comitou 

# git log -p: traz as mesmas propriedades que o log mas em um nivel de especificação maior 
 
# git log -p -"numero escolhido": ele vai delmitr um numero maximo de logs a serem apresentados na tela ( a contagem é feita de tráz pra frente )

# gitk: abre a interface grafica do git

# git commit --amend -m " mensagem da sua escolha ": isso adiciona suas alterações a ao ultimo commit já existente  

# git reset HEAD "nome do arquivo": isso retira da sua staged area o add que vc adicionou 
 
# staged area:  é onde o aequivo que vc deu add vai parar, o arquivo só sai de lá quando é dado o commit 
 
# git checkout --"nome do arquio": isos ira retirar reverter as alterações feitas em um arquivo onde vc adulterou recentemente 

# git rm "nome do arquivo": remove arquivos do seu repositorio 

# tags: servem para criar marcaçõs uma forma de poder facilitar o acesso a um determinado arquivo 
 
# git tag -a "nome da sua tag" -m " mensagem da sua tag ": isso irá criar uma tag nova  

# git tag "nome da sua tag " chave /id do comit no qual vc quer criar a tag -m" mensagem "
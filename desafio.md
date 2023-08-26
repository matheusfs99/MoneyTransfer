Usuários:
Tipo (lojista, comum)
Nome completo, cpf(unico), email(unico), senha

Usuários comuns podem transferir dinheiro para lojista e para outros usuários comuns.
Lojistas só recebem dinheiro, nao enviam.
Validar se o usuário possui saldo sulficiete antes de transferir o dinheiro.
Antes de finalizar a transferencia, consultar serviço externo de autorização
Se houver problema na transferencia, o dinheiro volta pra carteira do usuário que transferiu o dinheiro
Ao receber uma transferência, o usuário comum ou lojista deve receber uma notificação (por email ou sms) por serviço terceiro.


apps:
 - users
    vai tratar de criar usuários, definir os tipos etc
 - bank_account
    vai tratar da conta bancária dos usuários, transferencias, validar as transferencias etc


 - [x] criar api (crud) de usuários
 - [x] criar api (crud) de conta
 - [x] criar métodos de transferencias
 - [x] criar validações para transferencias
 - [ ] add servico de notificacao para usuario que receber transferencia

novas features:
 - form de criação de profile tem q ter as infos do user num unico form
 - no histórico de transações, passar o obj dos profiles, ao invés do nome
 - autenticaçao para transação tem q ser com token q identifique qual é o profile que vai transferir, 
e ai nao precisará passar o id dele no endpoint

extras:
 - criar documentacao no README.md
 - criar collection completa no insomnia e disponibilizar na documentacao
 - alterar projectname para conf e nome do diretório do projeto para backend
 - dockerizar o projeto
 - escrever testes com pytest
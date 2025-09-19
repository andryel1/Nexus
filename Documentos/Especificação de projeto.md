# 1. Perfis de Usuário

## 1.1 Usuário Final (Leitor)

Pessoa que acessa o sistema para consultar e reservar livros.
Deseja praticidade e rapidez para encontrar títulos e gerenciar reservas.

## 1.2 Administrador do Sistema

Responsável por gerenciar usuários, livros e monitorar reservas.
Responsável por gerenciar usuários, livros e monitorar reservas.
Pode cadastrar/editar/remover livros e acompanhar logs de notificações.

## 1.3 Sistema de Notificação

Atua como um agente autônomo.
Atua como um agente autônomo.
Responsável por enviar mensagens (notificação visual, e-mail simulado, ou log) quando eventos de reserva forem publicados.

# 2. Histórias de Usuário (User Stories)

## 2.1 Login e Cadastro
2.1 Login e Cadastro

Como usuário, quero realizar login, para acessar minhas informações de forma segura.

## 2.2 Pesquisa de Livros

Como usuário, quero pesquisar livros pelo título, autor ou categoria, para encontrar rapidamente o que desejo.

Como usuário, quero pesquisar livros pelo título, autor ou categoria, para encontrar rapidamente o que desejo.

2.3 Reserva de Livros

Como usuário, quero visualizar minhas reservas ativas, para acompanhar o que já solicitei.

## 2.4 Notificações

Como usuário, quero receber uma notificação quando minha reserva for registrada, para confirmar que deu certo.

Como usuário, quero receber uma notificação quando minha reserva for registrada, para confirmar que deu certo.

Como administrador, quero cadastrar, editar e remover livros, para manter o acervo atualizado.

#  3. Requisitos Funcionais

## 3.1 Frontend

RF01: Permitir login e cadastro de usuários.

RF02: Permitir pesquisa de livros por título, autor ou categoria.

RF03: Permitir a reserva de livros disponíveis.
RF05: Exibir notificações de reserva confirmada.

## 3.2 API Gateway

RF06: Roteamento de requisições do frontend para o microserviço correto.
3.2 API Gateway
RF07: Validação de tokens JWT para autenticação e autorização.

## 3.3 Auth Service

RF08: Cadastro de novos usuários com validação de dados.
3.3 Auth Service
RF09: Login e autenticação via JWT.

## 3.4 Books Service

RF10: CRUD de livros (criar, consultar, atualizar e remover).
3.4 Books Service
RF11: Consulta de disponibilidade de livros.

## 3.5 Reservations Service

RF12: Registro de reservas de livros.
3.5 Reservations Service
RF13: Publicação do evento reserva_criada no RabbitMQ.

## 3.6 Notification Service

RF14: Consumir eventos de reserva do RabbitMQ.
3.6 Notification Service
RF15: Enviar notificação ao usuário (via log, e-mail simulado ou frontend).

# 📌 4. Requisitos Não Funcionais

RNF01: O sistema deve ser acessível via navegador em dispositivos desktop e mobile.

RNF01: O sistema deve ser acessível via navegador em dispositivos desktop e mobile.

RNF02: O sistema deve utilizar autenticação baseada em JWT.

RNF03: O processamento de eventos deve ser assíncrono (via RabbitMQ).

RNF04: O sistema deve ser desenvolvido com arquitetura de microsserviços.

RNF05: O frontend deve ser responsivo e de fácil usabilidade.

RNF06: O sistema deve suportar até 100 usuários simultâneos sem degradação perceptível de desempenho (meta inicial).

RNF07: Logs de ações críticas (login, reserva, notificações) devem ser armazenados para auditoria.

RNF08: Tempo de resposta das requisições (API Gateway → microserviços) deve ser inferior a 2 segundos em condições normais.
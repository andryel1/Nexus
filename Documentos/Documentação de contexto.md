# Introdução

O sistema proposto tem como objetivo modernizar a forma como os usuários interagem com bibliotecas digitais, oferecendo uma solução baseada em arquitetura de microserviços. A aplicação integra recursos de autenticação, gerenciamento de livros, reservas e notificações em tempo real, garantindo escalabilidade, segurança e facilidade de manutenção. Com o uso de mensageria assíncrona (RabbitMQ), os serviços se comunicam de maneira desacoplada, o que possibilita maior confiabilidade e eficiência no processamento das operações.

## Justificativa

Muitas bibliotecas, tanto físicas quanto digitais, enfrentam dificuldades na gestão de usuários, livros e reservas, além de não possuírem sistemas que ofereçam notificações rápidas e uma experiência integrada para o usuário. A utilização de uma arquitetura monolítica pode limitar a escalabilidade e a manutenção da aplicação, dificultando a evolução do sistema ao longo do tempo.
A adoção de uma arquitetura de microserviços, aliada a um barramento de eventos como o RabbitMQ, justifica-se pela flexibilidade, resiliência e modularidade que proporciona. Isso garante que cada serviço seja independente, permitindo futuras expansões, como integração com sistemas de pagamento, relatórios de uso ou até machine learning para recomendações de leitura.

## Objetivo

O objetivo principal do sistema é disponibilizar uma plataforma simples, eficiente e escalável para:

- Autenticação de usuários com segurança.
- Pesquisa e gerenciamento de livros de forma prática.
- Criação de reservas de exemplares disponíveis.
- Envio de notificações automáticas sobre o status das reservas.

Além disso, busca-se fornecer uma base tecnológica sólida, que pode ser expandida em ambientes de produção real, aplicando boas práticas de desenvolvimento, integração contínua e arquitetura distribuída.

## Público-alvo

O sistema é voltado para:

- Usuários finais: leitores que desejam acessar e reservar livros de forma rápida, sem burocracia.
- Bibliotecas e instituições de ensino: que buscam digitalizar e automatizar processos de empréstimo e reserva de livros.
- Estudantes e desenvolvedores de software: interessados em compreender, praticar e aplicar conceitos de microserviços, mensageria assíncrona e API Gateway em um cenário realista.

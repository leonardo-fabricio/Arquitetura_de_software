<h1 align="center">Arquitetura Piper and Filter</h1>

<h1 align="center">Tecnologias Utilizdas</h1>
<li align="center"> java</li>
<br>

<h1 align="center">Informações</h1>
<p align="center">
Sockets Sincrono é uma aplicação desenvolvida em java, cujo objetivo é criar um canal de comunicação entre um cliente e um servidor.
</p>
<p align="center">
A aplicação está dividida em duas classes java, sendo uma para o papel de server e outra para o papel de cliente/usuário, respectivamente.
</p>

<h1 align="center">Características</h1>
<p align="center">
Na classe server, é instanciado um objeto do tipo serversocket o que permite a esta classe o "dever" de esperar conexões, ja na classe cliente
</p>
<p align="center">
é criado um objeto socket, ou também chamado de conexão, ou simplesmente cliente. A partir desse objeto é possivel realizar as comunicações entre as classes
</p>
<p align="center">
No exemplo mostrado a unica função de ambas as classes são as conexões e troca de mensagens sincronas, ou seja, uma classe manda uma mensagem
</p>
<p align="center">
e fica aguardando alguma resposta, nesse tipo de comunicação não é possivel enviar multiplas mensagens
</p>


<h1 align="center">Fluxo de dados</h1>
<p align="center">
 <a href="https://github.com/leonardo-fabricio/Sockets_In_Java/blob/main/Sincrona/sokets_Servidor.java">Iniciar Server</a> ->
 <a href="https://github.com/leonardo-fabricio/Sockets_In_Java/blob/main/Sincrona/sockets_Cliente.java">Inicar Cliente</a> ->
 <a>O cliente deve mandar a primeira mensagem</a> ->
 <a>Troca de mensagens sincronas</a> 
</p>

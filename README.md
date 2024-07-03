<h1>Script Python Windows Users-Policies</h1>

<ul>
  <li>
    <p>Este é um script feito em python, para definir políticas de sistema, como impedir personalizações e definição de wallpaper padrão, em sistema operacionai windows 11.</p>
  </li>
</ul>

<h2>Como colocar para funcionar?</h2>
<ul>
  <li>Após baixar o script, na pasta wallpaper irá conter o wallpaper que você deseja definir como padrão, portanto, a sua imagem deve ficar lá.</li>
  <br>
  <li>No arquivo <b>policies_win11.py</b>, você deverá alterar o diretório da sua imagem, por exemplo, na função 'main', na linha 79, haverá a seguinte string padrão: <b>f"wallpaper\\backmcpf.png"</b>, onde o backmcpf.png, deverá ser substituido pelo o nome de sua imagem junto à sua extensão.</li>
  <br>
  <li>Ainda no mesmo arquivo .py, na linha 5, haverá uma lista vázia, onde você deverá inserir as senhas dos usuários que irão receber as políticas. Porém, note que a ordem das senhas, irá definir também a ordem dos nomes dos usuários.</li>
</ul>

<h2>Como utilizar?</h2>
<ul>
  <li>Após feitas todas configurações, o arquivo a ser executado será o <b>policies_win11.py</b>, que para o correto funcionamento, deverá ser executado como administrador, por exemplo, executando o cmd como administrador e dando o seguinte comando: <code>python "C:\diretório\policies_win11.py"</code>, o script irá funcionar corretamente, aparecendo um input, pedindo os nomes dos usuários que teram as políticas aplicadas. <strong>Note que a ordem dos nomes, deverá ser igual a ordem das senhas definidas anteriormente.</strong></li>
</ul>

<h2>Atenção!</h2>
<ul>
  <li>Este script não foi testado em outros sistemas operacionais além do windows 11.</li>
  <li>É recomendado que seja feito um <strong>backup</strong> do regedit do sistema, para casos de erros.</li>
</ul>

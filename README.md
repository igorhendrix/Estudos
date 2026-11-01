<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
</head>
<body>

  <h1> 📚 Study Journey</h1>

  <p>Repositório dedicado ao registro prático da minha evolução em programação, partindo dos fundamentos da linguagem até a manipulação de dados, automação de fluxos e processos de ETL.</p>

  <hr>

  <h2>📌 Visão Geral do Repositório</h2>

  <p>O objetivo deste espaço é documentar conceitos teóricos, exercícios práticos e scripts reutilizáveis para o dia a dia de análise, automação e integração de sistemas.</p>

  <pre><code>├── Python/       # Sintaxe básica, estruturas de dados e POO
├── Bancos de dados e ETL/ # Pandas, tratamento de arquivos e ETL  </code></pre>

  <hr>

  <h2>🗺️ Roadmap de Estudos</h2>

  <h3>1. Fundamentos da Linguagem</h3>
  <p>Tópicos essenciais de lógica, estruturação de código e paradigmas em Python:</p>

  <ul class="task-list">
    <li><input type="checkbox" checked disabled> <span><strong>Variáveis e Tipos de Dados Primitivos</strong> (<code>int</code>, <code>float</code>, <code>str</code>, <code>bool</code>)</span></li>
    <li><input type="checkbox" checked disabled> <span><strong>Estruturas de Dados Básicas</strong> (Listas, Tuplas, Dicionários, Conjuntos)</span></li>
    <li><input type="checkbox" checked disabled> <span><strong>Controle de Fluxo e Condicionais</strong> (<code>if</code>, <code>elif</code>, <code>else</code>)</span></li>
    <li><input type="checkbox" checked disabled> <span><strong>Laços de Repetição</strong> (<code>for</code>, <code>while</code>, compreensão de listas)</span></li>
    <li><input type="checkbox" checked disabled> <span><strong>Funções e Escopo</strong> (Parâmetros, retornos, <code>*args</code>, <code>**kwargs</code>, funções lambda)</span></li>
    <li>
      <div>
        <input type="checkbox" checked disabled> <strong>Programação Orientada a Objetos (POO)</strong>:
        <ul class="task-list">
          <li><input type="checkbox" checked disabled> <span>Classes e Objetos</span></li>
          <li><input type="checkbox" checked disabled> <span>Atributos e Métodos</span></li>
          <li><input type="checkbox" checked disabled> <span>Métodos Especiais (<code>__init__</code>, <code>__str__</code>, etc.)</span></li>
          <li><input type="checkbox" disabled> <span>Herança e Polimorfismo</span></li>
          <li><input type="checkbox" disabled> <span>Encapsulamento</span></li>
        </ul>
      </div>
    </li>
    <li><input type="checkbox" checked disabled> <span><strong>Gerenciamento de Pacotes e Módulos</strong> (<code>pip</code>, <code>import</code>, ambientes virtuais)</span></li>
    <li><input type="checkbox" disabled> <span><strong>Tratamento de Exceções</strong> (<code>try</code>, <code>except</code>, <code>finally</code>, <code>raise</code>)</span></li>
    <li><input type="checkbox" disabled> <span><strong>Manipulação Básica de Arquivos</strong> (<code>open</code>, <code>with</code>, leitura/escrita)</span></li>
  </ul>

  <hr>

  <h3>2. Manipulação de Dados, ETL &amp; Automação <em>(Em Progresso)</em></h3>
  <p>Conteúdo focado na integração de fontes heterogêneas, limpeza e pipelines de dados:</p>

  <ul class="task-list">
    <li>
      <div>
        <input type="checkbox" disabled> <strong>Ambiente e Versionamento</strong>:
        <ul class="task-list">
          <li><input type="checkbox" disabled> <span>Organização do Ambiente de Desenvolvimento (<code>venv</code>, dependências)</span></li>
          <li><input type="checkbox" disabled> <span>Comandos Básicos de Git e GitHub (commit, push, branches, pull)</span></li>
        </ul>
      </div>
    </li>
    <li>
      <div>
        <input type="checkbox" disabled> <strong>Conceitos de ETL</strong>:
        <ul class="task-list">
          <li><input type="checkbox" disabled> <span>Introdução teórica e prática a fluxos de Extração, Transformação e Carga</span></li>
          <li><input type="checkbox" disabled> <span>Automação de fluxos de trabalho recorrentes</span></li>
        </ul>
      </div>
    </li>
    <li>
      <div>
        <input type="checkbox" disabled> <strong>Manipulação e Engenharia de Arquivos</strong>:
        <ul class="task-list">
          <li><input type="checkbox" disabled> <span>Leitura e escrita de arquivos Excel (<code>.xlsx</code>, <code>.xls</code>)</span></li>
          <li><input type="checkbox" disabled> <span>Processamento de arquivos delimitados (CSV, TXT, TSV)</span></li>
          <li><input type="checkbox" disabled> <span>Junções, limpeza e normalização de dados vindos de fontes distintas</span></li>
        </ul>
      </div>
    </li>
    <li>
      <div>
        <input type="checkbox" disabled> <strong>Módulo Pandas</strong>:
        <ul class="task-list">
          <li><input type="checkbox" disabled> <span>Estruturas <code>Series</code> e <code>DataFrame</code></span></li>
          <li><input type="checkbox" disabled> <span>Filtragem, agrupamento (<code>groupby</code>) e agregação</span></li>
          <li><input type="checkbox" disabled> <span>Operações de junção (<code>merge</code>, <code>join</code>, <code>concat</code>)</span></li>
        </ul>
      </div>
    </li>
    <li>
      <div>
        <input type="checkbox" disabled> <strong>Bancos de Dados &amp; SQL</strong>:
        <ul class="task-list">
          <li><input type="checkbox" disabled> <span>Conexão Python com SGBDs (SQLite, PostgreSQL, MySQL ou SQL Server)</span></li>
          <li><input type="checkbox" disabled> <span>Execução de scripts e manipulação de dados via SQL direto no código</span></li>
          <li><input type="checkbox" disabled> <span>Carga automatizada de DataFrames para tabelas de banco</span></li>
        </ul>
      </div>
    </li>
    <li>
      <div>
        <input type="checkbox" disabled> <strong>Coleta &amp; Extração de Dados Web</strong>:
        <ul class="task-list">
          <li><input type="checkbox" disabled> <span>Automação de navegação e extração com <strong>Selenium</strong></span></li>
          <li><input type="checkbox" disabled> <span>Download automatizado de relatórios e interação com formulários</span></li>
        </ul>
      </div>
    </li>
    <li><input type="checkbox" disabled> <span><strong>Repositório de Scripts Práticos</strong>: Biblioteca pessoal de scripts e utilitários reutilizáveis</span></li>
    <li><input type="checkbox" disabled> <span><strong>Módulos Bônus &amp; Atualizações Contínuas</strong></span></li>
  </ul>

  <hr>

  <h2>🛠️ Tecnologias e Bibliotecas</h2>
  <ul>
    <li><strong>Core:</strong> Python 3.x</li>
    <li><strong>Controle de Versão:</strong> Git / GitHub</li>
    <li><strong>Dados &amp; Análise:</strong> Pandas, OpenPyXL</li>
    <li><strong>Bancos de Dados:</strong> SQLite, SQLAlchemy</li>
    <li><strong>Automação Web:</strong> Selenium WebDriver</li>
  </ul>

  <hr>
</body>
</html>

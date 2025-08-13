# 🧛‍♂️ Tradutor Ollama: Vampiro a Máscara 🦇

Um tradutor de texto CLI especializado no universo de *Vampiro: A Máscara*, utilizando a API do Ollama com saídas estruturadas e um glossário dinâmico para garantir traduções consistentes e fiéis à terminologia do cenário.

## ✨ Funcionalidades

-   **Tradução Especializada:** Focado na terminologia e no tom de *Vampiro: A Máscara*.
-   **Glossário Dinâmico:** Identifica termos do glossário no texto de entrada e os injeta no prompt do modelo para traduções precisas.
-   **Fuzzy Matching:** Utiliza correspondência aproximada (`thefuzz`) para encontrar termos do glossário, mesmo com pequenas variações.
-   **Saídas Estruturadas:** Configurado para receber traduções em formato JSON do Ollama, garantindo fácil parseamento.
-   **Uso via CLI:** Traduza textos diretamente do terminal, passando o texto como argumento.
-   **Integração Desktop (Linux):** Atalho `.desktop` para facilitar o uso em ambientes gráficos.

## 🚀 Como Usar

### Pré-requisitos

-   **Python 3.10+**
-   **uv:** Um gerenciador de pacotes Python rápido (alternativa ao `pip`).
    ```bash
    pip install uv
    ```
-   **Ollama:** Servidor Ollama rodando localmente com um modelo compatível (ex: `llama2`, `gemma`).
    ```bash
    ollama run llama2 # ou ollama run gemma
    ```

### Instalação

1.  Clone este repositório:
    ```bash
    git clone https://github.com/seu-usuario/tradutor-ollama.git # Substitua pelo seu repositório
    cd tradutor-ollama
    ```
2.  Instale as dependências com `uv`:
    ```bash
    uv sync
    ```

### Execução

Para traduzir um texto, execute o script `main.py` via `uv run`, passando o texto entre aspas:

```bash
uv run main.py "The Kindred must uphold the Masquerade or risk the wrath of the Camarilla."
```

Exemplo com termo com apóstrofo:

```bash
uv run main.py "Don't forget the Masquerade, young Fledgling!"
```

### Gerenciamento do Glossário

O glossário está localizado em `glossario.json`. Ele é um arquivo JSON onde as chaves são os termos em inglês e os valores são suas traduções oficiais em português.

Exemplo de `glossario.json`:

```json
{
    "Abandon": "Abandonado (vampiro sem lar ou domínio)",
    "Masquerade": "Máscara (regra de manter a existência dos vampiros em segredo)",
    "Fledgling": "Recém-criado (vampiro recém-abraçado)"
}
```

Você pode editar este arquivo para adicionar ou modificar termos conforme a necessidade do seu projeto.

### Prompt do Sistema

O prompt do sistema que guia o comportamento do modelo Ollama está em `system_prompt.txt`. Este arquivo define a persona do tradutor, o contexto, o tom, a metodologia e o formato de saída esperado.

## 🖥️ Integração Desktop (Linux)

Para criar um atalho no seu ambiente de desktop Linux:

1.  Torne o arquivo `.desktop` executável:
    ```bash
    chmod +x tradutor-ollama.desktop
    ```
2.  Instale-o no menu de aplicativos do sistema:
    ```bash
    xdg-desktop-menu install tradutor-ollama.desktop
    ```
    Após isso, você deverá encontrar "Tradutor Ollama" no seu menu de aplicativos.

Para usar o atalho com um texto:
-   Você pode arrastar e soltar um arquivo de texto sobre o ícone do "Tradutor Ollama" (se o seu ambiente de desktop suportar).
-   Ou, em alguns gerenciadores de arquivos, usar a opção "Abrir com..." e selecionar "Tradutor Ollama".

**Nota:** Clicar diretamente no ícone sem fornecer um argumento pode abrir e fechar uma janela de terminal rapidamente, pois o script espera um texto para traduzir.

## 🤝 Contribuição

Sinta-se à vontade para contribuir com melhorias, adicionar mais termos ao glossário ou refatorar o código.

## 📄 Licença

Este projeto está licenciado sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.

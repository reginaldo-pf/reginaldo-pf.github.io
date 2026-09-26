document.addEventListener('DOMContentLoaded', () => {
    // Seletores de Elementos
    const displayMain = document.getElementById('display-main');
    const displayHistory = document.getElementById('display-history');
    const statusMode = document.getElementById('status-mode');
    const statusError = document.getElementById('status-error');
    const toggleScientificBtn = document.getElementById('toggle-scientific-btn');
    const scientificPanel = document.getElementById('scientific-panel');
    const btnClear = document.getElementById('btn-clear');
    const btnBackspace = document.getElementById('btn-backspace');
    const btnEquals = document.getElementById('btn-equals');
    const btnClearHistory = document.getElementById('btn-clear-history');
    const historyList = document.getElementById('history-list');

    // Estado da Calculadora
    let currentExpression = '0';
    let isResultDisplayed = false;
    let isScientificActive = false;

    // Helper para obter o Cookie de CSRF do Django
    function getCSRFToken() {
        let cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            const cookies = document.cookie.split(';');
            for (let i = 0; i < cookies.length; i++) {
                const cookie = cookies[i].trim();
                if (cookie.substring(0, 10) === 'csrftoken=') {
                    cookieValue = decodeURIComponent(cookie.substring(10));
                    break;
                }
            }
        }
        return cookieValue;
    }

    // Inicialização
    updateDisplay();
    loadHistory();

    // Toggle do Painel Científico
    toggleScientificBtn.addEventListener('click', () => {
        isScientificActive = !isScientificActive;
        toggleScientificBtn.classList.toggle('active', isScientificActive);
        scientificPanel.classList.toggle('active', isScientificActive);
        statusMode.textContent = isScientificActive ? 'Científica' : 'Padrão';
    });

    // Eventos dos botões com dados de valor ou operação
    document.querySelectorAll('.btn-num, .btn-sci, .btn-operator, .btn-action').forEach(btn => {
        btn.addEventListener('click', () => {
            const val = btn.getAttribute('data-val');
            const op = btn.getAttribute('data-op');

            clearError();

            if (val !== null) {
                handleNumberInput(val);
            } else if (op !== null) {
                handleOperatorInput(op);
            }
        });
    });

    // Limpar Display (AC)
    btnClear.addEventListener('click', () => {
        currentExpression = '0';
        displayHistory.textContent = '';
        isResultDisplayed = false;
        clearError();
        updateDisplay();
    });

    // Apagar Último Caractere (Backspace)
    btnBackspace.addEventListener('click', () => {
        clearError();
        if (isResultDisplayed) {
            currentExpression = '0';
            isResultDisplayed = false;
        } else {
            if (currentExpression.length <= 1) {
                currentExpression = '0';
            } else {
                // Se apagar uma função científica por completo (ex: "sin("), ajuda o usuário
                const functions = ['sqrt(', 'log10(', 'exp(', 'sin(', 'cos(', 'tan(', 'log('];
                let deletedFunction = false;
                for (let func of functions) {
                    if (currentExpression.endsWith(func)) {
                        currentExpression = currentExpression.slice(0, -func.length);
                        deletedFunction = true;
                        break;
                    }
                }
                if (!deletedFunction) {
                    currentExpression = currentExpression.slice(0, -1);
                }
                
                if (currentExpression === '') {
                    currentExpression = '0';
                }
            }
        }
        updateDisplay();
    });

    // Calcular Resultado (=)
    btnEquals.addEventListener('click', executeCalculation);

    // Limpar Histórico do Banco de Dados
    btnClearHistory.addEventListener('click', clearHistoryOnServer);

    // Entrada de Números
    function handleNumberInput(val) {
        if (currentExpression === '0' || isResultDisplayed) {
            currentExpression = val;
            isResultDisplayed = false;
        } else {
            currentExpression += val;
        }
        updateDisplay();
    }

    // Entrada de Operadores
    function handleOperatorInput(op) {
        // Se um resultado acabou de ser exibido, podemos continuar a conta em cima dele
        if (isResultDisplayed) {
            isResultDisplayed = false;
        }
        
        if (currentExpression === '0' && (op === '-' || op === '(' || op === 'sin(' || op === 'cos(' || op === 'tan(' || op === 'log(' || op === 'log10(' || op === 'sqrt(' || op === 'exp(')) {
            currentExpression = op;
        } else if (currentExpression === '0' && op !== ')') {
            currentExpression = '0' + op;
        } else {
            currentExpression += op;
        }
        updateDisplay();
    }

    // Atualiza o Display principal com ajuste dinâmico de tamanho de fonte
    function updateDisplay() {
        displayMain.textContent = currentExpression;
        
        // Ajustar tamanho de fonte para expressões muito longas
        const length = currentExpression.length;
        if (length > 25) {
            displayMain.style.fontSize = '1.3rem';
        } else if (length > 15) {
            displayMain.style.fontSize = '1.7rem';
        } else {
            displayMain.style.fontSize = '2.2rem';
        }
    }

    // Exibe mensagens de erro no rodapé do display
    function showError(msg) {
        statusError.textContent = msg;
        statusError.style.opacity = '1';
    }

    // Limpa mensagens de erro
    function clearError() {
        statusError.textContent = '';
        statusError.style.opacity = '0';
    }

    // AJAX: Executa Cálculo na API REST
    async function executeCalculation() {
        if (!currentExpression || currentExpression === '0') return;

        clearError();
        const csrfToken = getCSRFToken();

        try {
            const response = await fetch('/api/calculate/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': csrfToken
                },
                body: JSON.stringify({ expression: currentExpression })
            });

            const data = await response.json();

            if (response.ok && data.success) {
                displayHistory.textContent = currentExpression + ' =';
                currentExpression = data.result;
                isResultDisplayed = true;
                updateDisplay();
                loadHistory(); // Atualizar painel de histórico lateral
            } else {
                showError(data.error || 'Erro ao calcular.');
            }
        } catch (err) {
            showError('Erro de conexão com o servidor.');
            console.error(err);
        }
    }

    // AJAX: Carrega Histórico da API REST
    async function loadHistory() {
        try {
            const response = await fetch('/api/history/');
            const data = await response.json();

            historyList.innerHTML = '';

            if (data.length === 0) {
                historyList.innerHTML = `
                    <li class="history-empty">
                        <i data-lucide="inbox"></i>
                        <p>Nenhum cálculo recente</p>
                    </li>
                `;
                lucide.createIcons();
                return;
            }

            data.forEach(item => {
                const li = document.createElement('li');
                li.className = 'history-item';
                li.innerHTML = `
                    <div class="history-expr">${item.expression}</div>
                    <div class="history-res">${item.result}</div>
                    <span class="history-time">${item.timestamp}</span>
                `;
                
                // Clicar no histórico carrega a expressão de volta
                li.addEventListener('click', () => {
                    clearError();
                    currentExpression = item.expression;
                    displayHistory.textContent = '';
                    isResultDisplayed = false;
                    updateDisplay();
                });

                historyList.appendChild(li);
            });
        } catch (err) {
            console.error('Erro ao carregar histórico:', err);
        }
    }

    // AJAX: Limpa Histórico no Servidor
    async function clearHistoryOnServer() {
        const csrfToken = getCSRFToken();
        try {
            const response = await fetch('/api/history/clear/', {
                method: 'DELETE',
                headers: {
                    'X-CSRFToken': csrfToken
                }
            });

            const data = await response.json();
            if (response.ok && data.success) {
                loadHistory();
            } else {
                showError('Erro ao limpar histórico.');
            }
        } catch (err) {
            showError('Erro de conexão com o servidor.');
            console.error(err);
        }
    }

    // Suporte Completo a Teclado
    document.addEventListener('keydown', (e) => {
        const key = e.key;

        // Impedir comportamentos indesejados para teclas usadas
        if (key === '/' || key === 'Enter' || key === 'Backspace' || key === 'Escape') {
            e.preventDefault();
        }

        clearError();

        // Números e pontos
        if (/[0-9.]/.test(key)) {
            handleNumberInput(key);
        }
        // Operadores e Parênteses
        else if (key === '+') {
            handleOperatorInput('+');
        } else if (key === '-') {
            handleOperatorInput('-');
        } else if (key === '*') {
            handleOperatorInput('×');
        } else if (key === '/') {
            handleOperatorInput('÷');
        } else if (key === '%') {
            handleOperatorInput('%');
        } else if (key === '^') {
            handleOperatorInput('^');
        } else if (key === '(') {
            handleOperatorInput('(');
        } else if (key === ')') {
            handleOperatorInput(')');
        }
        // Ações
        else if (key === 'Backspace') {
            btnBackspace.click();
        } else if (key === 'Escape') {
            btnClear.click();
        } else if (key === 'Enter') {
            btnEquals.click();
        }
    });
});

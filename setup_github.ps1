# Script para configurar Git e enviar para GitHub

# Cores para output
$info = "Green"
$warning = "Yellow"

Write-Host "🚀 Configurando GitHub para o Dashboard" -ForegroundColor $info
Write-Host "======================================" -ForegroundColor $info
Write-Host ""

# Verificar se Git está instalado
try {
    $gitVersion = git --version
    Write-Host "✓ Git encontrado: $gitVersion" -ForegroundColor $info
} catch {
    Write-Host "✗ Git não está instalado. Instale em: https://git-scm.com/" -ForegroundColor Red
    exit
}

# Inicializar repositório Git
Write-Host "Inicializando repositório Git..." -ForegroundColor $info
git init
git config user.email "seu-email@example.com"
git config user.name "Seu Nome"

# Adicionar arquivos
Write-Host "Adicionando arquivos..." -ForegroundColor $info
git add .

# Primeiro commit
Write-Host "Criando primeiro commit..." -ForegroundColor $info
git commit -m "Dashboard Streamlit de Análise de Filmes - Inicial"

# Instruções para criar branch main e conectar ao GitHub
Write-Host ""
Write-Host "======================================" -ForegroundColor $warning
Write-Host "⚠️  PRÓXIMOS PASSOS NECESSÁRIOS:" -ForegroundColor $warning
Write-Host "======================================" -ForegroundColor $warning
Write-Host ""
Write-Host "1️⃣  Crie um novo repositório no GitHub:" -ForegroundColor $info
Write-Host "   - Acesse: https://github.com/new" -ForegroundColor $info
Write-Host "   - Nome: dashboard-filmes-streamlit" -ForegroundColor $info
Write-Host "   - Descrição: Dashboard interativo de análise de filmes" -ForegroundColor $info
Write-Host "   - Deixe outras opções padrão e clique em 'Create repository'" -ForegroundColor $info
Write-Host ""

Write-Host "2️⃣  Após criar o repositório, copie o URL e execute:" -ForegroundColor $info
Write-Host '   git branch -M main' -ForegroundColor $warning
Write-Host '   git remote add origin https://github.com/SEU_USUARIO/dashboard-filmes-streamlit.git' -ForegroundColor $warning
Write-Host '   git push -u origin main' -ForegroundColor $warning
Write-Host ""

Write-Host "3️⃣  Deploy no Streamlit Cloud:" -ForegroundColor $info
Write-Host "   - Acesse: https://streamlit.io/cloud" -ForegroundColor $info
Write-Host "   - Clique em 'New app'" -ForegroundColor $info
Write-Host "   - Selecione seu repositório GitHub" -ForegroundColor $info
Write-Host "   - Selecione 'dashboard.py' como main file" -ForegroundColor $info
Write-Host "   - Clique em 'Deploy'" -ForegroundColor $info
Write-Host ""

Write-Host "✓ Setup local concluído!" -ForegroundColor $info
Write-Host "📊 Status do Git:" -ForegroundColor $info
git status

## **Passos para Iniciar o Ambiente Virtual**

### **1. Criar o Ambiente Virtual**

#### Linux/macOS:
Execute o comando abaixo para criar o ambiente virtual:
```bash
python -m venv web-vuln
```

#### Windows:
Execute o comando abaixo para criar o ambiente virtual:
```bash
python -m venv web-vuln
```

---

### **2. Ativar o Ambiente Virtual**

#### Linux/macOS:
Use o comando abaixo para ativar o ambiente virtual:
```bash
source web-vuln/bin/activate
```

#### Windows:
1. Verifique a política de execução do PowerShell:
   ```powershell
   Get-ExecutionPolicy
   ```
   Se a saída for `Restricted`, você precisará alterar a política de execução:

   ```powershell
   Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
   ```

2. Ative o ambiente virtual:
   ```powershell
   web-vuln\Scripts\activate
   ```

---

### **3. Desativar o Ambiente Virtual**
Após terminar de usar o ambiente virtual, você pode desativá-lo com:
```bash
deactivate
```

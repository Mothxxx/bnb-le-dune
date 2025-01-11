## Distribuzione su Heroku

1. Installare Heroku CLI: Se non l'hai già fatto, installa la Heroku CLI per poter distribuire l'app direttamente dal terminale.
Accedi a Heroku: Una volta installato Heroku CLI, accedi al tuo account Heroku:

```bash
heroku login
```
2. Crea un file Procfile: In Heroku, per eseguire l'app, devi creare un file chiamato Procfile nella directory principale del progetto. 
Aggiungi il seguente contenuto al Procfile:

```bash
web: python app.py
```

3. Crea il progetto Heroku: Crea un'app su Heroku con il comando:
```bash
heroku create bnb-le-dune
```

4. Distribuisci il codice su Heroku: Ora fai il push del codice su Heroku:
```bash
git push heroku main
```
```bash
git push heroku main
```
```bash
git add Procfile requirements.txt
git commit -m "Added Procfile and updated requirements"
```
```bash
git push heroku main
```
```bash
heroku ps:scale web=1
```

Collega Heroku direttamente a GitHub
Se vuoi che Heroku si occupi di sincronizzarsi automaticamente con GitHub, puoi configurare il deploy continuo:
Vai alla dashboard di Heroku.
Seleziona l'app (bnb-le-dune).
Vai su Deploy.
Nella sezione Deployment method, scegli GitHub.
Autorizza Heroku a collegarsi al tuo account GitHub.
Cerca il repository Mothxxx/BnB e collegalo.
Attiva Enable Automatic Deploys per sincronizzare automaticamente il codice ogni volta che esegui un push su GitHub.

Passo 3: Gestisci i DNS
Accanto al dominio le-dune.com, clicca su Manage.
Nella sezione Nameservers, seleziona Custom DNS.
Passo 4: Configura il CNAME per Heroku
Dopo aver selezionato Custom DNS, sotto la sezione Host Records, aggiungi un nuovo record CNAME:
Host: www
Type: CNAME
Value: il DNS target fornito da Heroku (lo troverai nella sezione "Domains and certificates" della dashboard di Heroku dopo aver aggiunto il dominio).
Se il tuo dominio principale (senza "www") deve essere reindirizzato a www.le-dune.com, aggiungi anche un record URL Redirect:
Host: @
Value: http://www.le-dune.com
Type: URL Redirect
Passo 5: Salva le modifiche
Salva i cambiamenti DNS.
La propagazione dei DNS potrebbe richiedere fino a 24 ore, anche se spesso avviene più velocemente.
3. Aggiungi il dominio personalizzato su Heroku
Una volta configurato il dominio su Namecheap, devi aggiungerlo su Heroku:
Accedi alla Dashboard di Heroku.
Seleziona l'app che hai distribuito (ad esempio bnb-le-dune).
Vai alla sezione Settings.
Scorri verso il basso fino a Domains and Certificates e clicca su Add domain.
Inserisci il dominio www.le-dune.com.
Dopo aver aggiunto il dominio, Heroku ti fornirà un DNS Target. Assicurati che sia inserito correttamente nelle impostazioni DNS su Namecheap.
4. Verifica il dominio
Dopo che i DNS sono stati propagati, visita il tuo dominio www.le-dune.com nel browser. Se tutto è configurato correttamente, dovresti vedere la tua app Flask in esecuzione su Heroku.
Consigli su altri provider di dominio
Se Namecheap non ti sembra ideale, ci sono altri provider molto validi che offrono domini a buon prezzo:
GoDaddy: Fornisce domini con una buona assistenza clienti.
Google Domains: Offre una configurazione semplificata e buona integrazione con altri servizi Google.
Bluehost: Ottimo anche per hosting e domini, con una buona gestione dei DNS.
1. SSL Gratuito tramite Heroku
Heroku offre un certificato SSL gratuito per i domini che vengono configurati correttamente, tramite Let’s Encrypt. Questo è sufficiente per la maggior parte dei siti web. Ecco come configurarlo:
Passo 1: Aggiungi il dominio personalizzato su Heroku
Se non lo hai già fatto, aggiungi il dominio residence-le-dune.com alla tua app Heroku seguendo questi passaggi:
Vai alla Dashboard di Heroku.
Seleziona la tua app (ad esempio bnb-le-dune).
Vai su Settings > Domains and Certificates.
Clicca su Add domain e inserisci residence-le-dune.com.
Passo 2: Verifica la configurazione del DNS
Dopo aver aggiunto il dominio, Heroku ti fornirà un DNS target. Assicurati di configurarlo correttamente nel pannello DNS di Namecheap o del tuo provider di dominio.
Passo 3: Attiva SSL (Let’s Encrypt)
Heroku gestirà automaticamente il certificato SSL gratuito tramite Let’s Encrypt per il tuo dominio residence-le-dune.com. Puoi verificare che l'SSL sia attivo seguendo questi passaggi:
Nella dashboard di Heroku, vai su Settings della tua app.
Scorri fino alla sezione Domains and Certificates.
Se vedrai un'icona di un lucchetto verde accanto al tuo dominio, significa che il certificato SSL è attivo e il tuo sito è sicuro.
Nota: La propagazione dei DNS può richiedere alcune ore (fino a 24 ore in alcuni casi). Dopo che la propagazione è completata, il tuo dominio sarà protetto con SSL automaticamente.

3. Redirect automatico da HTTP a HTTPS
Una volta che l'SSL è attivo, dovrai configurare il tuo sito per forzare il traffico a HTTPS.
Passo 1: Modifica il codice dell'app Flask per forzare HTTPS
Puoi farlo aggiungendo una riga di codice al tuo file app.py in Flask:
from flask import Flask, redirect, request

app = Flask(__name__)

@app.before_request
def before_request():
    if not request.is_secure:
        return redirect(request.url.replace("http://", "https://"))

# Il resto del codice della tua app
Questa modifica garantirà che ogni richiesta HTTP venga reindirizzata automaticamente a HTTPS.
Passo 2: Verifica il sito
Una volta configurato l'SSL e forzato il reindirizzamento a HTTPS, visita il tuo sito (ad esempio https://residence-le-dune.com) per verificare che il certificato SSL sia attivo e che la connessione sia sicura (cerca il lucchetto verde nel browser).



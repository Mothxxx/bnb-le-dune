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


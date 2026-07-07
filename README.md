# ALPHA AI — Bot Telegram de publication automatique

Ce bot publie automatiquement des messages (et images) sur ton canal ou
groupe Telegram, à des dates et heures programmées.

## Fonctionnalités
- Planning de posts défini dans `posts.json`
- Support texte + image
- Vérification automatique toutes les 60 secondes
- Fonctionne 24/7 une fois déployé sur un serveur

---

## Étape 1 — Créer le bot sur Telegram

1. Ouvre Telegram et cherche **@BotFather**
2. Envoie la commande `/newbot`
3. Choisis un nom d'affichage, puis un username finissant par `bot`
   (ex: `alpha_ai_bot`)
4. BotFather te donne un **token** du type :
   `123456789:ABC-DEF1234ghIkl-zyx57W2v1u123ew11`
   → garde-le, c'est ton `TELEGRAM_BOT_TOKEN`

## Étape 2 — Récupérer l'ID de ton canal/groupe

- **Canal public** : utilise directement `@nomducanal` comme `TELEGRAM_CHAT_ID`
- **Canal privé ou groupe** :
  1. Ajoute ton bot comme **administrateur** du canal/groupe
  2. Envoie un message test dans le canal
  3. Va sur `https://api.telegram.org/bot<TON_TOKEN>/getUpdates` dans ton
     navigateur (remplace `<TON_TOKEN>`)
  4. Cherche `"chat":{"id": -1001234567890, ...}` → c'est ton `TELEGRAM_CHAT_ID`

## Étape 3 — Configurer le projet

1. Copie `.env.example` en `.env`
2. Remplis `TELEGRAM_BOT_TOKEN` et `TELEGRAM_CHAT_ID`
3. Édite `posts.json` avec tes propres publications :

```json
{
  "id": "post-003",
  "text": "Ton message ici",
  "image": "photo1.jpg",
  "datetime": "2026-07-10T14:30:00",
  "sent": false
}
```

- Si tu utilises une image, place le fichier dans un dossier `media/`
  (à créer à côté de `bot.py`) et indique juste son nom dans `"image"`.
- Laisse `"image": null` pour un post texte seul.
- Le bot passe automatiquement `"sent"` à `true` une fois le post publié.

## Étape 4 — Tester en local (optionnel)

```bash
pip install -r requirements.txt
python bot.py
```

Le bot tourne tant que ton terminal reste ouvert. Pour un fonctionnement
24/7, passe à l'étape 5.

## Étape 5 — Déployer sur Railway (recommandé, gratuit pour démarrer)

1. Crée un compte sur [railway.app](https://railway.app) (connexion via GitHub)
2. Mets ton dossier de projet sur un repo GitHub (privé de préférence)
3. Sur Railway : **New Project → Deploy from GitHub repo**
4. Sélectionne ton repo
5. Dans l'onglet **Variables**, ajoute :
   - `TELEGRAM_BOT_TOKEN`
   - `TELEGRAM_CHAT_ID`
6. Railway détecte automatiquement `requirements.txt` et lance `python bot.py`
   - Si besoin, précise la commande de démarrage dans **Settings → Deploy**
7. Le bot tourne maintenant 24/7 sans que ton PC soit allumé

### Mettre à jour le planning de posts une fois déployé
Le plus simple : modifie `posts.json` sur GitHub (ou dans ton repo local puis
`git push`) — Railway redéploie automatiquement à chaque changement.

---

## Alternatives d'hébergement
| Plateforme | Avantage | Inconvénient |
|---|---|---|
| **Railway** | Simple, gratuit pour démarrer | Crédit limité au-delà d'un certain usage |
| **Render** | Gratuit avec limites | Peut "s'endormir" si mal configuré |
| **VPS (Hetzner, OVH...)** | Contrôle total, pas cher | Demande plus de configuration technique |
| **PC personnel** | Gratuit | Doit rester allumé en permanence |

## Sécurité
- Ne commit jamais ton fichier `.env` sur GitHub (ajoute-le à `.gitignore`)
- Ne partage jamais ton `TELEGRAM_BOT_TOKEN`

## Prochaines évolutions possibles
- Génération automatique de texte via IA avant publication
- Publication multi-canaux
- Interface web pour gérer le planning sans toucher au JSON
- Statistiques de publication (vues, clics)

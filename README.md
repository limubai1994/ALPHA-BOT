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
[
  {
    "id": "post-001",
    "text": "🚀 CRYPTO — Le Bitcoin reste l'actif de référence du marché crypto. Mais la vraie question n'est pas \"quand acheter\", c'est \"combien de temps peux-tu tenir sans paniquer\" ? La patience bat souvent le timing parfait.",
    "image": null,
    "datetime": "2026-07-09T08:00:00",
    "sent": false
  },
  {
    "id": "post-002",
    "text": "📈 MARKETING — Une audience de 1000 personnes vraiment engagées vaut plus que 100 000 followers passifs. Concentre-toi sur la valeur que tu apportes, pas sur le chiffre affiché.",
    "image": null,
    "datetime": "2026-07-09T14:00:00",
    "sent": false
  },
  {
    "id": "post-003",
    "text": "🔥 MOTIVATION — Personne ne se souvient du jour où tu as commencé. Tout le monde se souvient du jour où tu as réussi. Continue.",
    "image": null,
    "datetime": "2026-07-09T20:00:00",
    "sent": false
  },
  {
    "id": "post-004",
    "text": "🏋️ SPORT — La discipline bat la motivation à tous les coups. La motivation va et vient, la discipline te fait avancer même les jours où tu n'as pas envie.",
    "image": null,
    "datetime": "2026-07-10T08:00:00",
    "sent": false
  },
  {
    "id": "post-005",
    "text": "✨ LIFESTYLE — Ton environnement façonne tes habitudes plus que ta volonté. Change ton décor, change tes fréquentations, et tes résultats suivront.",
    "image": null,
    "datetime": "2026-07-10T14:00:00",
    "sent": false
  },
  {
    "id": "post-006",
    "text": "💎 LUXE — Le vrai luxe aujourd'hui, ce n'est plus la montre ou la voiture. C'est le temps libre et le contrôle total de son emploi du temps.",
    "image": "luxe1.jpg",
    "datetime": "2026-07-10T20:00:00",
    "sent": false
  },
  {
    "id": "post-007",
    "text": "💼 BUSINESS — Un business qui ne résout aucun problème réel ne survit jamais longtemps. Avant de vendre, demande-toi : est-ce que je résous une vraie douleur ?",
    "image": null,
    "datetime": "2026-07-11T08:00:00",
    "sent": false
  },
  {
    "id": "post-008",
    "text": "🤖 IA — L'intelligence artificielle ne remplace pas les gens qui savent l'utiliser. Elle remplace ceux qui refusent de l'apprendre.",
    "image": null,
    "datetime": "2026-07-11T14:00:00",
    "sent": false
  },
  {
    "id": "post-009",
    "text": "🚀 CRYPTO — La diversification n'est pas juste une stratégie, c'est une protection contre ton propre ego. Ne mets jamais tous tes fonds sur une seule conviction.",
    "image": null,
    "datetime": "2026-07-11T20:00:00",
    "sent": false
  },
  {
    "id": "post-010",
    "text": "📈 MARKETING — Les gens n'achètent pas des produits, ils achètent des transformations. Vends le résultat, pas juste les caractéristiques.",
    "image": null,
    "datetime": "2026-07-12T08:00:00",
    "sent": false
  },
  {
    "id": "post-011",
    "text": "🔥 MOTIVATION — Tu n'as pas besoin d'être prêt à 100%. Tu as juste besoin de commencer à 1%. Le reste se construit en avançant.",
    "image": null,
    "datetime": "2026-07-12T14:00:00",
    "sent": false
  },
  {
    "id": "post-012",
    "text": "🏋️ SPORT — Ton corps s'adapte à ce que tu lui imposes régulièrement. Un effort ponctuel ne change rien, la régularité change tout.",
    "image": null,
    "datetime": "2026-07-12T20:00:00",
    "sent": false
  },
  {
    "id": "post-013",
    "text": "✨ LIFESTYLE — Dormir 7-8h n'est pas une perte de temps, c'est l'investissement le plus rentable de ta journée. Un cerveau reposé prend de meilleures décisions.",
    "image": null,
    "datetime": "2026-07-13T08:00:00",
    "sent": false
  },
  {
    "id": "post-014",
    "text": "💎 LUXE — Posséder beaucoup de choses n'est pas un signe de succès. Pouvoir dire non sans se justifier, ça, c'en est un.",
    "image": "luxe2.jpg",
    "datetime": "2026-07-13T14:00:00",
    "sent": false
  },
  {
    "id": "post-015",
    "text": "💼 BUSINESS — Le meilleur moment pour lancer ton projet était il y a un an. Le deuxième meilleur moment, c'est aujourd'hui.",
    "image": null,
    "datetime": "2026-07-13T20:00:00",
    "sent": false
  },
  {
    "id": "post-016",
    "text": "🤖 IA — Savoir poser les bonnes questions à une IA devient une compétence aussi précieuse que savoir coder il y a 10 ans.",
    "image": null,
    "datetime": "2026-07-14T08:00:00",
    "sent": false
  },
  {
    "id": "post-017",
    "text": "🚀 CRYPTO — Le marché récompense la patience et punit l'impulsivité. Ceux qui gagnent sur le long terme sont rarement ceux qui font le plus de trades.",
    "image": null,
    "datetime": "2026-07-14T14:00:00",
    "sent": false
  },
  {
    "id": "post-018",
    "text": "📈 MARKETING — La cohérence bat la perfection. Mieux vaut publier tous les jours un contenu correct que publier une fois par mois un contenu parfait.",
    "image": null,
    "datetime": "2026-07-14T20:00:00",
    "sent": false
  },
  {
    "id": "post-019",
    "text": "🔥 MOTIVATION — Ceux qui réussissent ne sont pas ceux qui n'ont jamais douté. Ce sont ceux qui ont continué malgré le doute.",
    "image": null,
    "datetime": "2026-07-15T08:00:00",
    "sent": false
  },
  {
    "id": "post-020",
    "text": "🏋️ SPORT — Tu ne trouveras jamais le temps parfait pour t'entraîner. Tu dois le créer, chaque jour, même 20 minutes.",
    "image": null,
    "datetime": "2026-07-15T14:00:00",
    "sent": false
  },
  {
    "id": "post-021",
    "text": "✨ LIFESTYLE — Le succès silencieux est souvent plus solide que le succès affiché. Construis en privé, montre les résultats.",
    "image": "lifestyle1.jpg",
    "datetime": "2026-07-15T20:00:00",
    "sent": false
  }
]

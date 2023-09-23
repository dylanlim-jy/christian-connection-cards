# Christian Connection Cards
This is a variant of the popular card game '[We're Not Really Strangers](https://www.werenotreallystrangers.com/)'.

This game is built using [Django](https://www.djangoproject.com/), [django-tailwind](https://django-tailwind.readthedocs.io/en/latest/installation.html), and [DaisyUI](https://daisyui.com/). The questions are loaded from a JSON static file.

You can find the Render site [here](https://christian-connection-cards.onrender.com/).

### TODO
- Add suggest view with a simple form and read up on [email services](https://docs.djangoproject.com/en/4.2/topics/email/)
- Add dark mode toggle on sidebar menu
- Persist dark mode state

### Roadmap
- Add keyboard shortcuts to index questions
- Migrate questions to database
- Add superuser and users
- Create models for ratings and register on admin
- Create async rooms where people can join with a private hash link and write to each member of the room
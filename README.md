# Christian Connection Cards
This is a variant of the popular card game '[We're Not Really Strangers](https://www.werenotreallystrangers.com/)'.

This game is built using [Django](https://www.djangoproject.com/), [django-tailwind](https://django-tailwind.readthedocs.io/en/latest/installation.html), and [DaisyUI](https://daisyui.com/). The questions are loaded from a JSON static file.

You can find the Render site [here](https://christian-connection-cards.onrender.com/).

### TODO
- Review questions
- Add suggest view with a simple form and read up on email services
- Dynamically render the max number of questions the slider allows
- Add dark mode toggle on sidebar menu
- Persist dark mode state
- Add ending view (extra link that's conditionally shown) that shows the final note activity

### Roadmap
- Add keyboard shortcuts to index questions
- Add functionality to swipe through questions on mobile
- Migrate questions to database
- Add superuser and users
- Create models for ratings and register on admin
- Create async rooms where people can join with a private hash link and write to each member of the room
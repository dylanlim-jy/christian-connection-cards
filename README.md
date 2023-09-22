# Christian Connection Cards
This is a variant of the popular card game '[We're Not Really Strangers](https://www.werenotreallystrangers.com/)'.

This game is built using [Django](https://www.djangoproject.com/), [django-tailwind](https://django-tailwind.readthedocs.io/en/latest/installation.html), and [DaisyUI](https://daisyui.com/). The questions are loaded from a JSON static file.


Setting up Tailwind for Development:
```
python manage.py collectstatic --no-input
python manage.py tailwind start
```

Setting up Tailwind for Production:
```
python manage.py tailwind build
```
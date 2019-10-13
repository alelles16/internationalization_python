# Internationalization python

This project is an example about how to translate your python scripts using `gettext` - python library.

You can read more about `gettext` and how install and prepare your environment in your machine.

📚📚📚

[Internacionalización de programas Python](https://freakspot.net/internacionalizaci%C3%B3n-de-programas-python/) 

[How To Translate Python Applications With The GNU Gettext Module](https://medium.com/i18n-and-l10n-resources-for-developers/how-to-translate-python-applications-with-the-gnu-gettext-module-5c1c085041bd)


## Generate `.POT` file

We need to generate a `.pot` file. This file is a catalog of unprocessed messages, these messages are those translatable strings that we have marked in our program, in this case with `_` that we put before the string that we want to translate.

You can use this command to generate `.pot` file.

```bash
pygettext -d base -p locale main.py
```

🚨The previous command is not working for me. I need to use `pygettext.py` because my OS has some problems with that. If you have problems too, you can use the next command:

```bash
python pygettext.py -d base -o locale/base.pot main.py
```

## License
[MIT](https://choosealicense.com/licenses/mit/)

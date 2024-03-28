- Selenium Tutorial - Checking Chrome Version

Before installing the Selenium package (`pip install selenium`), it is important to check the version of the web browser you are using. Selenium supports various popular web browsers including Chrome, Firefox, and others. Here is a simplified tutorial specifically for checking the Chrome version:

1. Click on the sidebar menu (three dots at the top right corner) in Chrome.
2. Select "說明" (Help) from the menu.
3. Click on "關於Google" (About Google) from the dropdown.
4. A new tab will open, displaying information about your Chrome browser, including the version number.

Once you know your Chrome version, you can visit the following link to find the appropriate version of ChromeDriver that matches your Chrome browser:

[Chrome for Testing](https://googlechromelabs.github.io/chrome-for-testing/)

At this link, you will find a list of available Chrome versions along with their corresponding ChromeDriver versions. Make sure to choose the ChromeDriver version that matches your Chrome browser version for optimal compatibility.

--------

- Streamlit Lecture 4 Warning -

I have noticed that some of the packages used in the Streamlit lecture are outdated. However, the author intentionally used the older versions to demonstrate specific methods without encountering any errors. Here are some suggestions to ensure smooth execution:

1. If you are using the latest version of Python, such as Python 3.11, it is recommended to downgrade to Python 3.9 or 3.8. This is because the Gensim package may not be compatible with the newer versions of Python.

To install Gensim version 3.8.2, you can use the following command in your command prompt or terminal:

```shell
pip install gensim==3.8.2
```

This will install Gensim version 3.8.2 specifically.

2. It is important to note that the commands `streamlit.beta_expander` and `streamlit.beta_columns` mentioned in the lecture are no longer supported. The updated commands are `streamlit.expander` and `streamlit.columns` respectively. Please make sure to use the correct commands in your code.

3. The package `spacy` has also been updated. Instead of using `spacy.load('en')`, you should now use `spacy.load('en_core_web_sm')`. Before using this command, ensure that you have already installed the package by running the following command:

```shell
python -m spacy download en_core_web_sm
```

This command will download the English language model to your local machine.

4. Lastly, for other packages, you can either use the latest version with `pip install`, or if you prefer using conda, you can use `conda install` to install and manage the packages.


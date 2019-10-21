# A Trivial Geospatial Example for Binder

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/wenzeslaus/trivial-geospatial-example-for-binder/master?urlpath=lab)

This is a trivial example showing usage of Binder for geospatial computations.

## Obtaining a Binder badge (link)

Go to https://mybinder.org/ website. Enter your repo GitHub page URL. Copy the Markdown text for the "binder badge". Text is an image which is link for creating a new computational environment on Binder. The text will look like this:

```
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/your-gh-username/your-repo-name/master)
```

Add the following text to the end of the repo URL to start Binder in the JupyterLab mode instead of the default Jupyter Notebook mode:

```
?urlpath=lab
```

 The modified text will look like this:

```
[![Binder](https://mybinder.org/badge_logo.svg)](.../your-repo-name/master?urlpath=lab)
```

Add this to your README file. When you click on the badge, Binder will create for you a new computational environment based on your repository.

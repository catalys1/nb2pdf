# Work for BYU CS 611 - Fall 2019

## Converting notebooks to PDFs

This assumes you are using Ubuntu or similar, python 3.6+, and that you have the basic packages installed already (i.e., jupyter).

### Dependencies

Make sure the dependencies are installed:
```
sudo apt install pandoc, texlive-xetex
pip install nbconvert
```

### Update the notebook metadata

Inside the notebook, open the `edit` menu and click on `Edit Notebook Metadata`. You should see an editor with some json inside, something like this:
```
{
  "kernelspec": {
    "name": "python3",
    "display_name": "Python 3",
    "language": "python"
  },
  "language_info": {
    "name": "python",
    "version": "3.7.1",
    "mimetype": "text/x-python",
    "codemirror_mode": {
      "name": "ipython",
      "version": 3
    },
    "pygments_lexer": "ipython3",
    "nbconvert_exporter": "python",
    "file_extension": ".py"
  },
}
```
Add two items to the json: a field for the author and one for the title. The result should look like:
```
{
  "authors": [
    "Your Name Here"
  ],
  "title": "Title you want to appear at top of PDF",
  "kernelspec": {
    "name": "python3",
    "display_name": "Python 3",
    "language": "python"
  },
  "language_info": {
    "name": "python",
    "version": "3.7.1",
    "mimetype": "text/x-python",
    "codemirror_mode": {
      "name": "ipython",
      "version": 3
    },
    "pygments_lexer": "ipython3",
    "nbconvert_exporter": "python",
    "file_extension": ".py"
  }
}
```
Save the changes and then save the notebook.

### Generate the PDF

The file `topdf.sh` will create the PDF from the notebook. It first converts the notebook to latex, and then runs `addauthor.py`, which tweaks a few things in the latex to make it look better (and actually print an author name, since just adding it to the metadata apparently isn't enough). It then converts the latex to a pdf using `pdflatex`. The resulting file will have the same name as the notebook, but with a `.pdf` extension.
```
# run ./topdf.sh with the name of the notebook
# and the name of the author (you still need to
# specify something in the "authors" field in the notebook)
./topdf.sh myfile.ipynb "My Name"
```

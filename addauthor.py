if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('file')
    parser.add_argument('author')
    args = parser.parse_args()

    s = open(args.file).read()

    # Adding an "authors" field to the notebook metadata causes the empty
    # \authors{} tag to show up in the latex, but doens't add the authors
    # names for whatever reason
    s = s.replace(r'\author{}', f'\\author{{{args.author}}}\n\n\\date{{}}')
    # change \*section{...} tags to \*section*{tags} (removes section
    # numbers, since they tend not to be grounded properly)
    s = s.replace(r'section{', r'section*{')

    open(args.file, 'w').write(s)


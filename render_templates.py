from staticjinja import make_site


OUTPATH = "site"


if __name__ == "__main__":
    site = make_site(outpath=OUTPATH)
    site.render()
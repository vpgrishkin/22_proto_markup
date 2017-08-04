from staticjinja import make_site


OUTPATH = "site"

def index_context(template):
    return {'page': 'index'}

if __name__ == "__main__":
    site = make_site(outpath=OUTPATH,
                     contexts=[('index.html', index_context)])
    site.render()
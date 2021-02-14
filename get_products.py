#!/usr/bin/python3
#!/utf/8in/get_products
#!/ali/elainous

from    bs4         import  BeautifulSoup
from    requests    import  get

def avito():
    # https://www.avito.ma/?/??/???/????--%C3%A0_vendre
    # ?    : lang (ar,fr)
    # ??   : ville (agadir,tanger,...) ,(maroc)
    # ???  : categorie (tablets,pc,...) (avito_categorie.txt) sep('_')
    # ???? : nom de produit  sep('_')

    url     = 'https://www.avito.ma/fr/{}/{}/{}--à_vendre'
    ville   = input('ville/maroc : ')
    categ   = input('categorie/avito_categorie.txt : ')
    produit = input('nom de produit : ').replace(' ','_').lower()

    req = get(url.format(ville,categ,produit))
    bs  = BeautifulSoup(req.text,'html5lib')
    req.close()
    produits = []
    for i in bs.findAll('script'):
        if  'application/ld+json' in i.get_attribute_list('type'):
            produits += [str(i.get_text())]
    del req,bs
    for produit in produits:
        print('-'*35)
        for key,value in eval(produit).items():
            if  key[0] in '@u':
                continue
            if  key is 'offers':
                print('url   : {}\nprix  : {} {}'.format(value['url'],value['price'],value['priceCurrency']))
            elif key is 'image':
                print(*value,sep='\n')
            else:
                print(value)

if  __name__ == '__main__':
    avito()

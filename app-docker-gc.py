import docker
import datetime
import dateutil.parser

client = docker.from_env()
date_30_min_ago = datetime.datetime.today() - datetime.timedelta(minutes=30)

###########-----get list of all repos and formating-----#############

repo_list1 = []
repo_list2 = []
for image in client.images.list():   
    repo_list1.append(image.tags)
str = ''.join(str(x) for x in repo_list1)
newstr = str.replace("[", "").replace("]", "").split("'")
sep = ':'
for elem in (list(dict.fromkeys(newstr))):
    repo_list2.append(elem.split(sep, 1)[0])
repos = list(set(repo_list2))

###########-----go trought each repo, check -----#############
for repo in repos[1:]:
    repo_f = []
    for image in client.images.list(filters = { "reference" : repo}): # get all images for repo
        repo_f.append(image.tags)
    print(repo_f)
    for tag in repo_f[3:]:   #leave first 3 images, start from 4
        for image in client.images.list(filters = { "reference" : tag}):
            creation_date = dateutil.parser.parse(image.attrs['Created'])   # get image creation date
            print (id)
            print (creation_date)
            print(date_30_min_ago)
            if creation_date.replace(tzinfo=None) < date_30_min_ago.replace(tzinfo=None):  # compare image creation date with your date value
                print ("The insertion date is older than 30 minutes")
                x = ''.join(image.tags)
                print(x)
                client.images.remove(x)  # remove image
            else:
                print ("Your image is new")
       


# docker-gc
 
 task: 
 
 solution:
 wrote simp[le python script which do next:
 - get all repos via DockerAPI
 - for each repo get all images
 - get image creation date --> compare --> delete if image old
 - kep first three images
 
used "client.images.remove()" insted of ""client.images.prune() as looks filters and labes working strange for this method in DockerSDK for Python and no well docs for that, even in google) Also looks there is no way to pass image name for prune method.   
 
 Docs used:
 https://docker-py.readthedocs.io/en/stable/images.html
 https://docs.docker.com/engine/reference/commandline/images/#examples
 https://docs.docker.com/engine/reference/commandline/image_rm/
 https://docs.docker.com/engine/api/v1.41/#operation/ImageSearch
 

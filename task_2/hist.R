df = read.csv("./Housing.csv" , sep=",")
#Création de l'histogrammepour la variable bedrooms
hist(df$bedrooms,breaks=10,col="blue",main="Distribution des chambres",
     xlab="bedrooms")
df = read.csv("L2_IFRI/Projet_Python&R/Housing.csv" , sep=",")

#Structure des données dans le dataset
dim(df)
summary(df)
is.na(df)
#Création de l'histogrammepour la variable bedrooms
hist(df$bedrooms,breaks=10,col="blue",main="Distribution des chambres",
     xlab="bedrooms")
#Création du nuage de points pour les variables price et superficie
plot(df$area,df$price,col="green",main = "Nuage de points entre la 
     superficie et le prix",xlab="area",ylab="price")


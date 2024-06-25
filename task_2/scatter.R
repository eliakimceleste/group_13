df = read.csv("task_2/Housing.csv" , sep=",")
#Création du nuage de points pour les variables price et superficie
plot(df$area,df$price,col="green",main = "Nuage de points entre la 
     superficie et le prix",xlab="area",ylab="price")

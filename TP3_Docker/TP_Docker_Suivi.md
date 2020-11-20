11h30 : Je n'ai pas encore réussi l'installation de Docker, je me bats actuellement pour installer ubuntu sur ma vm, j'ai du recommencer l'install 4 ou 5 fois.<br>
J'ai tout de même pu pas mal me documenter sur Docker et les différentes commandes ainsi que leur utilisation. (Voir DockerCheatSheet)<br>
<br>
QUICKSTART DOCKER :<br>
<br>
- Différence entre images et containers<br>
<br>
--->Une IMAGE Docker est un fichier immuable, qui constitue une capture instantanée d’un container et de sa config. Lorsque qu'on lance une image avec la commande run, cela produit un container ayant la config exacte de l'image. Cela permet de partager un container. <br>
Sur le Dockerhub par exemple, on peut récupérer des images crées par des utilisateurs, afin de récupérer des environnements spécifiques.<br>
--->Un container est une "brique", dans laquelle on peut déployer un environnement, ou bien un 'bloc' d'une app. Un container est constitué d'une image Docker, un environnement d’exécution et un ensemble d’instructions standard.<br>
<br><br>
- A quoi sert un Dockerfile ?<br>
<br>
--->Un Dockerfile est un fichier texte décrivant les différentes étapes permettant de partir d'une base pour aller vers une application fonctionnelle. Docker lit les instructions que l'on inscrit dans le Dockerfile pour créer automatiquement l'image requise.
<br><br>
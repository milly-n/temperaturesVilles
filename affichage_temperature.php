<?php

//sous Wamp
$bdd = new PDO('mysql:host=localhost; dbname=bdd_temperaturevilles', 'root', '');
$bdd->query('SET lc_time_names = "fr_FR"');
$les_villes = htmlspecialchars($_POST['ville']);

$reponse = $bdd->prepare('SELECT temperature, ville, DATE_FORMAT(last_update, "Le %d %M %Y à %H h %i") as last_update FROM temperaturevilles WHERE ville = ?');
$reponse->execute(array($les_villes));


while ($donnee = $reponse->fetch())
    {
	echo $donnee['last_update']. " à " . ucwords($les_villes). " il fait actuellement ".$donnee['temperature']. "°";
	echo '<br>';
		
	}
	

?>
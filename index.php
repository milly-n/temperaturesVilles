<form method='post' action='affichage_temperature.php'>
<fieldset>
<label for='ville'>Selectionnez une ville: </label>
	<select name='ville' id='ville' required>
	
    <?php
    $dbh = new PDO('mysql:host=localhost;dbname=bdd_temperaturevilles', 'root', '');
    $reponse = $dbh->query('SELECT * FROM temperaturevilles');
        while($donnee = $reponse->fetch())
		{?>
	
		<option value="<?php echo $donnee['ville']; ?>">
						<?php echo ucwords($donnee['ville']); ?>
						</option>
						<?php } ?>
	
	</select>
<input type='submit' name='Valider'>
</fieldset>
</form>



	


<?php
$id = $_GET['id'];
$connexion = new PDO("mysql:host=localhost;dbname=football","root","");
$sql = "DELETE FROM joueurs WHERE id_joueur = ?";
$stmt = $connexion->prepare($sql);
$stmt->execute([$id]);
header('Location: listeJoueur.php?success=1');
exit();
?>

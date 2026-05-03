<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.8/dist/css/bootstrap.min.css" rel="stylesheet">
    <title>Ajouter joueur</title>
</head>
<body>
    <div class="container">
    <form method="post">
        <h4 class="text-center my-3">Ajouter un joueur</h4>
        <hr>

        <label class="form-label">Nom du joueur :</label>
        <input type="text" class="form-control" name="nom">

        <label class="form-label">Prénom du joueur :</label>
        <input type="text" class="form-control" name="prenom">

        <label class="form-label">Âge du joueur :</label>
        <input type="number" class="form-control" name="age" min="18" max="50">

        <input type="submit" value="Ajouter" name="ajouter" class="btn btn-primary my-3">
        <a href="listeJoueur.php" class="btn btn-danger">Précédent</a>
    </form>
</div>

<?php
try {
    $connexion = new PDO("mysql:host=localhost;dbname=football","root","");
    $connexion->setAttribute(PDO::ATTR_ERRMODE,PDO::ERRMODE_EXCEPTION);
} catch(PDOException $e) {
    die("Erreur de connexion : " . $e->getMessage());
}

if(isset($_POST['ajouter'])) {

    $nom = trim($_POST['nom']);
    $prenom = trim($_POST['prenom']);
    $age = trim($_POST['age']);

    if (!empty($nom) && !empty($prenom) && !empty($age)) {

        $sql = "INSERT INTO joueurs (id_joueur,nom_joueur,prenom_joueur,age_joueur) VALUES (null,?,?,?)";
        $stmt = $connexion->prepare($sql);
        $stmt->execute([$nom,$prenom,$age]);

        echo '<div id="successAlert" class="alert alert-success">
                Le joueur est bien ajouté !
              </div>';

    } else {

        echo '<div id="warningAlert" class="alert alert-warning">
                Nom, prénom et âge sont obligatoires !
              </div>';
    }
}
?>

<script>
setTimeout(function() {

    let success = document.getElementById('successAlert');
    let warning = document.getElementById('warningAlert');

    if(success){
        success.style.transition = "0.5s";
        success.style.opacity = "0";
        setTimeout(() => success.remove(), 500);
    }

    if(warning){
        warning.style.transition = "0.5s";
        warning.style.opacity = "0";
        setTimeout(() => warning.remove(), 500);
    }

}, 900);
</script>
</body>
</html>
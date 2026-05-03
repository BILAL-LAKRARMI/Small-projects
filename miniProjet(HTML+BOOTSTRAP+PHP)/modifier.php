<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.8/dist/css/bootstrap.min.css" rel="stylesheet">
    <title>Document</title>
</head>
<body>
    <?php
    $id_joueur = $_GET['id'];
    $connexion = new PDO("mysql:host=localhost;dbname=football","root","");
    $sql = "SELECT * FROM joueurs WHERE id_joueur = ?";
    $stmt = $connexion->prepare($sql);
    $stmt->execute([$id_joueur]);
    $joueur = $stmt->fetch(PDO::FETCH_ASSOC);
    ?>
    <div class="container">
    <form method="post">
        <h4 class="text-center my-2">Modification d'informations du Joueur</h4>

        <input type="hidden" class="form-control" name="id_joueur" value="<?= $joueur['id_joueur']?>">

        <label class="form-label">Nom du joueur :</label>
        <input type="text" class="form-control" name="nouveau_nom" value="<?= $joueur['nom_joueur']?>">

        <label class="form-label">Prénom du joueur :</label>
        <input type="text" class="form-control" name="nouveau_prenom" value="<?= $joueur['prenom_joueur']?>">

        <label class="form-label">Âge du joueur :</label>
        <input type="number" class="form-control" name="nouveau_age" value="<?= $joueur['age_joueur']?>">

        <input type="submit" value="Modifier" name="modifier" class="btn btn-primary my-3">
        <a href="listeJoueur.php" class="btn btn-danger">Précédent</a>
    </form>
</div>
<?php
    if(isset($_POST['modifier'])) {
        $id = $_POST['id_joueur'];
        $nouveauNom = $_POST['nouveau_nom'];
        $nouveauPrenom = $_POST['nouveau_prenom'];
        $nouveauAge = $_POST['nouveau_age'];

        $sql1 = "UPDATE joueurs SET nom_joueur = ?, prenom_joueur = ?, age_joueur = ? WHERE id_joueur = ?";
        $stmt1 = $connexion->prepare($sql1);
        $stmt1->execute([$nouveauNom,$nouveauPrenom,$nouveauAge,$id]);
        ?>
        <div class="alert alert-success" role="alert">
            Modification réussie !
        </div>
        <?php
    }
    ?>
</body>
</html>
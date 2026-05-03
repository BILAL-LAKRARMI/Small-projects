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
    $connexion = new PDO("mysql:host=localhost;dbname=football","root","");
    $sql = "SELECT * FROM joueurs";
    $stmt = $connexion->query($sql);
    $stmt->execute();
    $joueurs = $stmt->fetchAll(PDO::FETCH_ASSOC);
    ?>
    <h4 class="text-center my-3">La liste des joueurs</h4>
    <hr>
    <a href="ajouterJoueur.php" class="btn btn-primary my-3 mx-3">Ajouter de joueur</a>
    <table class="table mx-3">
  <thead>
    <tr>
      <th scope="col">#id</th>
      <th scope="col">Nom du Joueur</th>
      <th scope="col">Prénom du Joueur</th>
      <th scope="col">Age de Joueur</th>
      <th scope="col">Opérations</th>
    </tr>
  </thead>
  <tbody>
    <?php 
    foreach($joueurs as $joueur) {?>
        <tr>
            <th scope="row"><?php echo $joueur['id_joueur']; ?></th>
            <th><?php echo $joueur['nom_joueur']; ?></th>
            <td><?php  echo $joueur['prenom_joueur']; ?></td>
            <td><?php echo $joueur['age_joueur']; ?></td>
            <td>
                <a href="modifier.php?id=<?= $joueur['id_joueur']?>" class="btn btn-primary">Modifier</a>
                <a href="supprimer.php?id=<?= $joueur['id_joueur']?>" class="btn btn-danger" onclick="return confirm('Voulez vous vraiment supprimer le joueur <?php echo $joueur['nom_joueur']; ?> ?')">Supprimer</a>
            </td>
            </tr>
    <?php 
    }
    ?>
    <script>
    setTimeout(function() {
        let alert = document.getElementById('successAlert');
        if(alert){
            alert.classList.remove('show');
            alert.classList.add('fade');
            alert.style.opacity = "0";

            setTimeout(() => alert.remove(), 500); 
        }
    }, 900); 
</script>
  </tbody>
</table>
<?php if(isset($_GET['success'])) { ?>
    <div id="successAlert" class="alert alert-success">
        Joueur supprimé avec succès !
    </div>
<?php }?>
</body>
</html>
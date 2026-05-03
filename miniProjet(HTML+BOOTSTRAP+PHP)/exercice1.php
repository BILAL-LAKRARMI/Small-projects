<?php
class Joueur {
    PRIVATE $nom;
    PRIVATE $prenom;
    PRIVATE $age;

    public function __construct($nom,$prenom,$age) {
        $this->nom = $nom;
        $this->prenom = $prenom;
        $this->age = $age;
    }
    public function statu() {
        if($this->age >= 18) {
            echo "le joueur " . $this->prenom . " est sénior";
        }else {
             echo "le joueur " . $this->prenom . " est junior";
        }
    }
}

$joueur1 = new Joueur("HAKIMI","ACHRAF",22);
$joueur1->statu();
?>
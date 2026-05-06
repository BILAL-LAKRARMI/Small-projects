let livres = [
        {"isbn":"01234","titre":"Langage C","image":"langagec.jpg","prix":150},
        {"isbn":"56789","titre":"Programmation Javascript","image":"javascript.jpg","prix":250},
        {"isbn":"11778","titre":"Laravel","image":"laravel.jpg","prix":200}
    ];

    function charger() {
        let select = document.getElementById("select");

        for(let i = 0 ; i < livres.length ; i++) {
            let option = document.createElement("option");

            option.text = livres[i].titre;
            option.value = livres[i].isbn;
            select.appendChild(option);
        }

    }
    function afficher() {
        let i = document.getElementById("select").selectedIndex;

        // document.getElementById("titre").textContent = livres[i].titre;
        document.getElementById("image").src = livres[i].image;
        document.getElementById("prix").innerHTML = "<h6> -> le prix de livre " + livres[i].titre + "  :  " + livres[i].prix +" dhs</h6>";
        document.getElementById("panier").innerHTML = "<h4> votre commande (panier) : " + panier.length + "</h4>";

    }
    let panier = [];
    let totale = 0;
    function ajouter() {

        let i = document.getElementById("select").selectedIndex;

        panier.push(livres[i]);
        totale += livres[i].prix;

        update();
        showMessage("Livre est bien ajouté dans panier");
    }

    function retirer() {
        let i = document.getElementById("select").selectedIndex;
        for(let j = 0 ; j < panier.length ; j++) {
            if(panier[j].isbn == livres[i].isbn) {
                totale -= panier[j].prix;
                panier.splice(j,1);
                break;
            }

        }
        update();
        showMessage1("Livre est bien retiré dans panier");
    }
    charger();
    afficher();
    function update() {

        document.getElementById("panier").innerHTML = "<h4> votre commande (panier) : " + panier.length + "</h4>";
        document.getElementById("prixTotale").innerHTML ="<h4>Totale Finale : " + totale + " dhs</h4>";

    }
    function showMessage(text) {
        document.getElementById("message").innerHTML = 
            '<div class = "alert alert-success">' + text + '</div>'
        
        setTimeout(function() {
            document.getElementById("message").innerHTML = "";
        },1900);
    }

    function showMessage1 (text){
        document.getElementById("message").innerHTML = 
        '<div class = "alert alert-danger">' + text + '</div>'

        setTimeout(function() {
            document.getElementById("message").innerHTML = "";
        },1900);
    }
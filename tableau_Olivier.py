script du tableau des menus de la cantine:
<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8">
        <link rel="stylesheet" href="style.css" />      
    </head>   
       
        
<body>
<h1>Menus de la cantine</h1>
<table border = 1>
            <thead>
                 <tr>
                    <th>Jour</th>
                    <th>Entrée</th>
                    <th>Plat</th>
                    <th>Dessert</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                  <?php
                    $menu = array(
                    "Lundi" => array('Entree' => "Macédoine", 'Plat' => "Cari de porc", 'Dessert' => "Fromage et mandarine"),
                    "Mardi" => array('Entree' => "Salade", 'Plat' => "Rôtie de dindonneau", 'Dessert' => "Fromage gouda"),
                    "Mercredi" => array('Entree' => "Salade de tomate", 'Plat' => "Rôtie de poulet", 'Dessert' => "Fromage chédard"),
                    "Jeudi" => array('Entree' => "Salade de laitue", 'Plat' => "Sauté de poulet", 'Dessert' => "Yaourt"),
                    "Vendredi" => array('Entree' => "Salade de pomme de terre", 'Plat' => "Poisson pané", 'Dessert' => "Fromage vache qui rit et orange"));
                    
                    //$menu['Plat']='Poulet';?>
                </tr>

                <tr><?php    
                      Foreach($menu as $cle1 => $valeur1){
                        echo "<tr>";
                        echo "<td>";
                        echo " ".$cle1."<br/><br>";
                        echo "</td>";

                        Foreach($valeur1 as $cle2 => $valeur2){
                          echo "<td>";
                          echo " ".$valeur2."<br/><br>";
                          echo "</td>";
                        }
                      echo "</tr>";
                      }?>
                </tr>
            </tbody>
</table>
<form action = "modifier.php" method="get">
                      <input type = "hidden" name = "id" value ="1234">
                      <input type = "submit" value = "Modifier">
</form>
<form action = "supprimer.php" method="get">
                      <input type = "hidden" name = "id" value ="974">
                      <input type = "submit" value = "Supprimer">
</form>
</body>
</html>



Script modifier.php:
<?php
    //$connect=mysqli_connect("localhost","root","") or die("Erreur de connexion à la BDD");
    //mysqli_select_db($connect, "annuaire") or die("Erreur de connexion a la table");
?>

<form action="" method="post">
<p>
<input type="hidden" name="id">
Ajouter un menu :
</p>
<p>
<label>Jour :</label>
<input type="texte" name="Jour" size="15">
</p>
<p>
<label>Entrée :</label>
<input type="texte" name="Entrée" size="15">
</p>
<p>
<label>Plat :</label>
<input type="texte" name="Plat" size="15">
</p>
<p>
<label>Dessert :</label>
<input type="texte" name="Dessert" size="15">
</p>
<p>
<input type="submit" name="save" value="Ajouter">
</p>
</form>

Le css:
table{
    margin: auto;
}

th, tr, td,h1 {
    text-align:center;
    }
th {
    background: rgba(255, 102, 0, 0.87);
    color: white;
}
tr:nth-child(even) {
    background: rgba(240, 166, 7, 0.959);
}

tr:nth-child(odd) {
    background: rgba(247, 150, 4, 0.562);
}

form {
    display: block;
    width: 12em; /* largeur des boutons */
    height: 2.8em; /* longueur des boutons */
    background-color: #fff; /* couleur des boutons */
    color: #000; /* Couleur de la police dans les boutons */
    text-align: center; /* Centre le texte dans les boutons */
    font-weight: bold; /* Met l'écriture en gras */
    
    position: relative;
    bottom: 3.7em; /* Position bouton */
    left: 46em; 
    display: inline-block;
    margin: 0 2em;
    margin-top: 4%;
    margin-right: auto;
    margin-left: auto;
}

form#myform label { display:inline-block; width:100px; }
form#myform input { display:inline-block; }
form#myform input[type=submit] { color:#fff; background-color:green; }

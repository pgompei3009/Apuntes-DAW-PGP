<?php

try {
    $pdo = new PDO(
        'mysql:host=db;port=3306;dbname=juegos;charset=utf8',
        'usuario',
        'pass',
        [
            PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION,
            PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC,
        ]
    );
} catch (PDOException $e) {
    die('Error de conexión a la base de datos: ' . $e->getMessage());
}

$stmt = $pdo->query("SELECT titulo, portada, id FROM videojuego");
$videojuegos = $stmt->fetchAll();
?>
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="styles.css">
    <title>Document</title>
</head>
<body>
    <div class="container">
        <h1>Videojuegos Disponibles</h1>
        <div class="juegos">
        <?php foreach ($videojuegos as $juego): ?>
            <div class="card juego" style="width:18rem;">
                <img src=<?= 'img/'.$juego['portada']; ?> class="card-img-top">
                <div class="card-body">
                    <h2 class="card-title"><?= $juego['titulo']; ?></h2>
                    <a href="juego.php?id=<?= $juego['id'] ?>" class="btn btn-primary">Ver juego</a>
                </div>
            </div>
        <?php endforeach; ?>
        </div>
    </div>
</body>
</html>
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

$id = $_GET['id'] ?? null;

if (!$id) {
    die('Juego no especificado.');
}

$stmt = $pdo->prepare("SELECT * FROM videojuego WHERE id = ?");
$stmt->execute([$id]);
$juego = $stmt->fetch();

if (!$juego) {
    die('Juego no encontrado.');
}
?>
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title><?= $juego['titulo'] ?></title>
    <link rel="stylesheet" href="juego.css">
</head>
<body>
    <div class="container">
        <h1><?= $juego['titulo'] ?></h1>
        <p><strong>Fecha de salida:</strong> <?= $juego['fecha_salida'] ?></p>
        <img src="<?= 'img/' . $juego['portada'] ?>" alt="<?= $juego['titulo'] ?>">
        <br>
        <a href="index.php">← Volver</a>
    </div>
</body>
</html>
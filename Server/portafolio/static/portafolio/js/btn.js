window.onscroll = function() {
    if (document.body.scrollTop > 390 || document.documentElement.scrollTop > 390) {
      document.getElementById("btn-subir").style.display = "block";
    } else {
      document.getElementById("btn-subir").style.display = "none";
    }
  };
  
  // Cuando el usuario haga clic en el botón, se desplazará hacia arriba
  document.getElementById("btn-subir").addEventListener("click", function() {
    document.body.scrollTop = 0; // Para Safari
    document.documentElement.scrollTop = 0; // Para Chrome, Firefox, IE y Opera
  });
  
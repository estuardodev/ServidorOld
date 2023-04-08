const id = window.location.pathname.split('/').pop();
const apiBaseUrl = "http://estuardodev.com/api/"; // Nueva URL base de la API

fetch(`${apiBaseUrl}articulo/${id}`)
  .then(response => response.json())
  .then(data => {
    if (data.message === 'success') {
      const article = data.article[0];
      if (article['visits'] == 100) {
        document.title = `Eres especial, eres la visita 100 del articulo - ${article.titulo}`;
      } else if (article['visits'] == 1000) {
        document.title = `Eres especial, eres la visita 1000 del articulo - ${article.titulo}`;
      }
    } else {
      console.error('Error al obtener la información del artículo');
    }
  })
  .catch(error => {
    console.error(`Error de red: ${error}`);
  });
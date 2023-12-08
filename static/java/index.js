const urlParams = new URLSearchParams(window.location.search);
        const nombre = urlParams.get('usuario');
    
        // Actualiza el contenido de la página
                if (nombre) {
            document.getElementById('nombreUsuario').textContent = nombre;
            var nuevoHipervinculo = document.createElement('a');
            nuevoHipervinculo.href = 'noticia.html';
            nuevoHipervinculo.textContent = 'Tu noticia';
            document.querySelector('nav').appendChild(nuevoHipervinculo);
            document.getElementById('login').style.display = 'none'; // Oculta el enlace de inicio de sesión
            const hipervinculos = document.querySelectorAll('a');
            hipervinculos.forEach(function (hipervinculo) {
              const href = hipervinculo.getAttribute('href');
              if (href) {
                // Agrega el parámetro usuario al hipervínculo
                const separador = href.includes('?') ? '&' : '?';
                hipervinculo.href = `${href}${separador}usuario=${nombre}`;
              }
            });
        }
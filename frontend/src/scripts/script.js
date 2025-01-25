document.getElementById('buscar-btn').addEventListener('click', async () => {
    // Obtener los valores de las fechas
    const fechaInicio = document.getElementById('fecha-inicio').value;
    const fechaFin = document.getElementById('fecha-fin').value;
  
    // Validar que las fechas no estén vacías
    if (!fechaInicio || !fechaFin) {
      alert('Por favor selecciona ambas fechas.');
      return;
    }
  
    try {
      // Construir la URL con los parámetros de consulta
      const url = `https://backend-service.onrender.com/api/totales/?fecha_inicio=${fechaInicio}&fecha_fin=${fechaFin}`;
      console.log(`Consultando API: ${url}`); // Solo para depuración
  
      // Realizar la solicitud al backend
      const response = await fetch(url);
  
      // Verificar si la respuesta es exitosa
      if (!response.ok) {
        throw new Error('Error al obtener los datos del backend.');
      }
  
      // Procesar la respuesta en formato JSON
      const data = await response.json();
  
      // Seleccionar el cuerpo de la tabla para mostrar los resultados
      const tbody = document.querySelector('#resultados tbody');
      tbody.innerHTML = ''; // Limpiar cualquier resultado anterior
  
      if (data.length === 0) {
        // Si no hay datos, mostrar un mensaje
        const row = tbody.insertRow();
        const cell = row.insertCell();
        cell.colSpan = 2;
        cell.textContent = 'No hay datos para las fechas seleccionadas.';
      } else {
        // Agregar las filas a la tabla con los datos recibidos
        data.forEach(item => {
          const row = tbody.insertRow();
          row.insertCell().textContent = item.nombre || 'Desconocido'; // Clave correcta para el nombre del departamento
          row.insertCell().textContent = `$${item.total.toFixed(2)}`; // Total con dos decimales
        });
      }
    } catch (error) {
      console.error(error); // Mostrar el error en la consola para depuración
      alert('Hubo un error al obtener los datos. Verifica la consola para más detalles.');
    }
    data.forEach(item => {
      console.log('Departamento:', item.departamento__nombre, 'Total:', item.total); // Depuración
      const row = tbody.insertRow();
      row.insertCell().textContent = item.departamento__nombre || 'Desconocido'; 
      row.insertCell().textContent = `$${parseFloat(item.total).toFixed(2)}`;
    });
    
  });
  
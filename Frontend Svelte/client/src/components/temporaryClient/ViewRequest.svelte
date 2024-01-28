<script>
  import Header from '../Header.svelte';
  import Footer from '../Footer.svelte';
    import { empty } from 'svelte/internal';

  const token = sessionStorage.getItem("jwtToken");

let roles = getTokenByRol(token);
let rut = getTokenByRut(token);
console.log(roles);
console.log(rut);

function getTokenByRol(token) {
  if (!token) {
    return null;
  }

  const decodedToken = decodeToken(token);

  if (!decodedToken || !decodedToken.roles) {
    return null;
  }
  return decodedToken.roles;
}
function getTokenByRut(token) {
  if (!token) {
    return null;
  }

  const decodedToken = decodeToken(token);

  if (!decodedToken || !decodedToken.roles) {
    return null;
  }
  return decodedToken.sub.replace(/[.-]/g, "");
}

function decodeToken(token) {
  if (!token) {
    return null;
  }
  const base64Url = token.split(".")[1];
  const base64 = base64Url.replace(/-/g, "+").replace(/_/g, "/");
  const jsonPayload = decodeURIComponent(
    atob(base64)
      .split("")
      .map(function (c) {
        return "%" + ("00" + c.charCodeAt(0).toString(16)).slice(-2);
      })
      .join("")
  );

  return JSON.parse(jsonPayload);
}


  let enrollment = [];
  let data = [];
  let rowCount = 0;
  let showButton = false;
  let api = false;
  // console.log(rutLogIn)

  function formateRUT(numero) {
 
  numero = String(numero)
  if (numero.length === 8) {
    const parte1 = numero.slice(0, 1);
    const parte2 = numero.slice(1, 4);
    const parte3 = numero.slice(4, 7);
    const digitoVerificador = numero.slice(7);

    const rutFormateado = `${parte1}.${parte2}.${parte3}-${digitoVerificador}`;
    return rutFormateado;
  } else {
    const parte1 = numero.slice(0, 2);
    const parte2 = numero.slice(2, 5);
    const parte3 = numero.slice(5, 8);
    const digitoVerificador = numero.slice(8);

    const rutFormateado = `${parte1}.${parte2}.${parte3}-${digitoVerificador}`;
    return rutFormateado;
  }
}

  let rut1 = formateRUT(rut)
  console.log(rut1)
  
  async function fetchEnrollments() {
    try {
      const response = await fetch(`${import.meta.env.VITE_BASE_API_URL}/enrollment-user/${rut1}`, {
        method: 'GET',
      });

      if (response.ok) {
        enrollment = await response.json();
        data = enrollment.enrollments;
        rowCount = data.length;
        if (rowCount === 8) {
          showButton = true;
        }
        console.log(data);
        updatePagination();
        api = true;
      } else {
        console.error('Error al cargar datos de profesores desde la API');
      }
    } catch (err) {
      console.error("Error al realizar la solicitud a la API:", err);
    }
  }
  fetchEnrollments();

  let currentPage = 1;
  const itemsPerPage = 5;
  let totalPages = 0;

  function updatePagination() {
    const totalItems = data.length;
    const totalPages = Math.ceil(totalItems / itemsPerPage);
    if (currentPage > totalPages) {
      currentPage = totalPages;
    }
  }

  function showPage(page) {
    currentPage = page;
    console.log({ currentPage });
  }

  function nextPage() {
    totalPages = Math.ceil(data.length / itemsPerPage);
    if (currentPage < totalPages) {
      currentPage++;
    }
  }

  function previousPage() {
    if (currentPage > 1) {
      currentPage--;
      console.log({ currentPage });
    }
  }

</script>

<body>
  <Header />
  <main>
    <div class="div-main">
      <p class="title-info">Mís matrículas</p>
      {#if !api || data.length === 0}
        <h2
          class="title-info"
          style="color: black; font-size: 20px; font-weight: 300"
        >
          No hay matrículas registradas.
        </h2>
      {:else}
        <div class="text-center table-responsive">
          <table class="table table-striped border table-bordered align-middle">
            <thead class="align-middle">
              <tr>
                <th class="col-2">Número</th>
                <th class="col-2">Fecha de solicitud</th>
                <th class="col-2">Nombre alumno</th>
                <th class="col-2">Curso</th>
                <th class="col-2">Estado</th>
              </tr>
            </thead>
            <tbody>
              {#each data.slice((currentPage - 1) * itemsPerPage, currentPage * itemsPerPage) as item, index (index + 1)}
                <tr>
                  <td>{index+1}</td>
                  <td>{item.date}</td>
                  <td>{item.student_name}</td>
                  <td>{item.year_parallel}</td>
                  <td> {#if item.status === 2}
                    Pendiente
                  {:else if item.status === 1}
                    Aceptada
                    {:else if item.status === 0}
                    Rechazada
                  {/if}
                  </td>
                </tr>
              {/each}
            </tbody>
          </table>
        </div>

        <div class="pagination-container">
          <nav aria-label="Page navigation example">
            <ul class="pagination justify-content-center">
              <li class="page-item">
                <a
                  class="page-link"
                  href="#"
                  aria-label="Previous"
                  on:click={previousPage}
                >
                  <span aria-hidden="true">&laquo;</span>
                </a>
              </li>
              {#each Array.from({ length: totalPages }, (_, i) => i + 1) as page}
                <li class="page-item">
                  <a class="page-link" href="#" on:click={() => showPage(page)}
                    >{page}</a
                  >
                </li>
              {/each}
              <li class="page-item">
                <a
                  class="page-link"
                  href="#"
                  aria-label="Next"
                  on:click={nextPage}
                >
                  <span aria-hidden="true">&raquo;</span>
                </a>
              </li>
            </ul>
          </nav>
        </div>
      {/if}
    </div>
  </main>
  <Footer />
</body>

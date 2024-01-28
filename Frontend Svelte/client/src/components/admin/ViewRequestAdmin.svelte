<script>
  import Header from "../Header.svelte";
  import Footer from "../Footer.svelte";

  let enrollment = [];
  let data = [];
  let rowCount = 0;
  let showButton = false;
  let api = false;

  async function fetchEnrollments() {
    try {
      const response = await fetch(
        `${import.meta.env.VITE_BASE_API_URL}/enrollment`,
        {
          method: "GET",
        }
      );

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
        console.error("Error al cargar datos de profesores desde la API");
      }
    } catch (err) {
      console.error("Error al realizar la solicitud a la API:", err);
    }
  }
  fetchEnrollments();

  let currentPage = 1;
  showPage(1);
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

  let isOpen = false;
  let isOpen1 = false;
  let isOpen2 = false;
  let isOpen3 = false;
  let selectedEnrollment = null;
  let idEdit;
  let statusEdit;

  function modalAccept(id) {
    selectedEnrollment = data.find((enrollment) => enrollment.id === id);
    idEdit = id;
    statusEdit = 1;
    console.log(selectedEnrollment);
    isOpen = !isOpen;
    console.log(idEdit);
  console.log(statusEdit);
  }

  function modalDecline(id) {
    selectedEnrollment = data.find((enrollment) => enrollment.id === id);
    idEdit = id;
    statusEdit = 0;
    console.log(selectedEnrollment);
    isOpen1 = !isOpen1;
    console.log(idEdit);
  console.log(statusEdit);
  }

  async function editEnrollment(enrollment_id, status) {
    const edit = { enrollment_id, status };
    console.log(edit)
    const response = await fetch(`${import.meta.env.VITE_BASE_API_URL}/enrollment`,
      {
        method: "PATCH",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(edit),
      }
    );
    if (response.ok) {
      const responseData = await response.json();
      const dataEdit = responseData.enrollment
      console.log("dataEdit",dataEdit)
      console.log(responseData.message)
      if (status === 1) {
        isOpen = !isOpen;
        isOpen2 = !isOpen2;
        setTimeout(() => {
          isOpen2 = !isOpen2;
        }, 1500);
        window.location.reload();
      }

      if (status === 0) {
        isOpen1 = !isOpen1;
        isOpen3 = !isOpen3;
        setTimeout(() => {
          isOpen3 = !isOpen3;
        }, 1500);
        window.location.reload();
      }
    } else {
      throw new Error("Error al editar el recurso");
    }
  }
</script>

<body>
  <Header />
  <main>
    <div class="div-main">
      <p class="title-info">Listado de solicitudes de matriculas</p>
      {#if !api || data.length === 0}
        <h2
          class="title-info"
          style="color: black; font-size: 20px; font-weight: 300"
        >
          No hay solicitudes pendientes.
        </h2>
      {:else}
        <div class="text-center table-responsive">
          <table class="table table-striped border table-bordered align-middle">
            <thead class="align-middle">
              <tr>
                <th class="col-2">Número</th>
                <th class="col-2">Fecha de solicitud</th>
                <th class="col-2">Nombre apoderado</th>
                <th class="col-2">Nombre alumno</th>
                <th class="col-2">Curso</th>
                <th class="col-2">Acciones</th>
              </tr>
            </thead>
            <tbody>
              {#each data.slice((currentPage - 1) * itemsPerPage, currentPage * itemsPerPage) as item}
                <tr>
                  <td>{item.id}</td>
                  <td>{item.date}</td>
                  <td>{item.user_name}</td>
                  <td>{item.student_name}</td>
                  <td>{item.year_parallel}</td>
                  <td>
                    <div
                      class="button-container display-flex justify-content-center align-items-center;"
                    >
                      <button
                        on:click={() => modalAccept(item.id)}
                        type="button"
                        class="button-icon col bi bi-check-lg"
                        style=" background-color: #09ff00; margin-right: 10px"
                        data-toggle="tooltip"
                        data-placement="bottom"
                        title="Aceptar"
                      />
                      <button
                        on:click={() => modalDecline(item.id)}
                        type="button"
                        class="button-icon col bi bi-x-lg"
                        style=" background-color: red;"
                        data-toggle="tooltip"
                        data-placement="bottom"
                        title="Rechazar"
                      />
                    </div>
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
    {#if isOpen}
      <div class="modal-overlay">
        <div class="modal-software w-50">
          <div style="text-align:right">
            <button class="close-button" on:click={modalAccept}>&times;</button>
          </div>
          <div class="container-modal">
            <h2>¿Estas seguro que deseas aceptar la solicitud?</h2>
            <div class="modal-button">
              <button
                class="button-confirm"
                on:click={() => editEnrollment(idEdit, statusEdit)}
                >Confirmar</button
              >
              <button
                class="button-confirm button-cancel"
                on:click={modalAccept}>Cancelar</button
              >
            </div>
          </div>
        </div>
      </div>
    {/if}

    {#if isOpen1}
      <div class="modal-overlay">
        <div class="modal-software w-50">
          <div style="text-align:right">
            <button class="close-button" on:click={modalDecline}>&times;</button
            >
          </div>
          <div class="container-modal">
            <h2>¿Estas seguro que deseas rechazar la solicitud?</h2>
            <div class="modal-button">
              <button
                class="button-confirm"
                on:click={() => editEnrollment(idEdit, statusEdit)}
                >Confirmar</button
              >
              <button
                class="button-confirm button-cancel"
                on:click={modalDecline}>Cancelar</button
              >
            </div>
          </div>
        </div>
      </div>
    {/if}
    {#if isOpen2}
                <div class="modal-overlay">
                    <div class="modal-software w-50">
                        <h5>Solicitud aceptada.</h5>
                    </div>
                </div>
            {/if}
            {#if isOpen3}
            <div class="modal-overlay">
                <div class="modal-software w-50">
                    <h5>Solicitud rechazada.</h5>
                </div>
            </div>
        {/if}       
  </main>
  <Footer />
</body>

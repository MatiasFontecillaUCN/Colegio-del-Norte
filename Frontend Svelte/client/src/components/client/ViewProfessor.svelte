<script>
  import Header from '../Header.svelte';
  import Footer from '../Footer.svelte';

  let isOpen = false;
  let isOpen1 = false;
  let professorName = '';
  let professorEmail = '';
  let professors = [];
  let api = false;
  let affair = '';
  let affairError = true;
  let message = '';
  let messageError = true;
  let rowCount = 0;
  let showButton = false;

  async function fetchProfessors() {
    try {
      const response = await fetch(`${import.meta.env.VITE_BASE_API_URL}/professors`, {
        method: 'GET',
      });

      if (response.ok) {
        professors = await response.json();
        rowCount = professors.length;
        if (rowCount === 8) {
          showButton = true;
        }
        console.log(professors);
        updatePagination();
        api = true;
      } else {
        console.error('Error al cargar datos de profesores desde la API');
      }
    } catch (err) {
      console.error("Error al realizar la solicitud a la API:", err);
    }
  }
  fetchProfessors();

  function handleChangeAffair(e) {
    if (e.key === ' ') {
      e.preventDefault();
    }
    affair = e.target.value;
    if (affair.length > 0) {
      affairError = false;
    } else {
      affairError = true;
    }
  }

  function handleChangeMessage(e) {
    if (e.key === ' ') {
      e.preventDefault();
    }
    message = e.target.value;
    if (message.length > 0) {
      messageError = false;
    } else {
      messageError = true;
    }
  }

  let professor = null;
  function modal(event) {
    isOpen = !isOpen;
    if (event.target) {
      const rowIndex = event.target.closest('tr')?.rowIndex;
      if (rowIndex !== undefined && rowIndex >= 0) {
        professor = professors[rowIndex - 1];
        professorName = `${professor.name} ${professor.lastname}`;
        professorEmail = `${professor.email}`;
        console.log(`Mensaje para el profesor: ${professorName}`);
      }
    }
  }

  function showModal() {
    messageError = true;
    affairError = true;
    isOpen = !isOpen;
    isOpen1 = !isOpen1;
    setTimeout(() => {
      isOpen1 = !isOpen1;
    }, 1500);
  }

  let currentPage = 1;
  showPage(1);
  const itemsPerPage = 5;
  let totalPages = 0;

  function updatePagination() {
    const totalItems = professors.length;
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
    totalPages = Math.ceil(professors.length / itemsPerPage);
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
      <p class="title-info">Ver profesores</p>
      {#if !api || professors.length === 0}
        <h2
          class="title-info"
          style="color: black; font-size: 20px; font-weight: 300"
        >
          No hay Profesores registrados.
        </h2>
      {:else}
        <div class="text-center table-responsive">
          <table class="table table-striped border table-bordered align-middle">
            <thead class="align-middle">
              <tr>
                <th class="col-2">Nombre</th>
                <th class="col-2">Rut</th>
                <th class="col-2">Teléfono</th>
                <th class="col-2">Correo</th>
                <th class="col-2">Asignatura</th>
                <th class="col-2">Acciones</th>
              </tr>
            </thead>
            <tbody>
              {#each professors.slice((currentPage - 1) * itemsPerPage, currentPage * itemsPerPage) as item}
                <tr>
                  <td>{item.name} {item.lastname}</td>
                  <td>{item.rut}</td>
                  <td>+{item.phone_number}</td>
                  <td data-fullvalue={item.email}>{item.email}</td>
                  <td>{item.subject}</td>
                  <td
                    ><button
                      class="button-options button-edit"
                      style="margin:auto; border-radius: 20px"
                      on:click={modal}>Mensaje</button
                    ></td
                  >
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
            <button class="close-button" on:click={modal}>&times;</button>
          </div>
          <div class="container-modal">
            <form>
              <h3>Mensaje para {professorName}</h3>
              <h5>{professorEmail}</h5>
              <h5 style="text-align: start;">Asunto</h5>

              <input
                type="text"
                class="form-control input-edit"
                on:input={handleChangeAffair}
              />
              {#if affairError}
                <p style="color: red; margin:5px 0 0; text-align: start">
                  Debe colocar un asunto.
                </p>
              {/if}

              <h5 style="text-align: start; margin-top: 10px">Mensaje</h5>
              <textarea
                class="form-control input-edit"
                on:input={handleChangeMessage}
              />
              {#if messageError}
                <p style="color: red; margin:5px 0 0; text-align: start">
                  Debe colocar un mensaje.
                </p>
              {/if}
            </form>
            <div class="modal-button">
              <button
                class="button-confirm"
                on:click={showModal}
                disabled={affairError || messageError}>Enviar</button
              >
              <button class="button-confirm button-cancel" on:click={modal}
                >Cancelar</button
              >
            </div>
          </div>
        </div>
      </div>
    {/if}

    {#if isOpen1}
      <div class="modal-overlay">
        <div class="modal-software w-50">
          <h5>El mensaje a {professorName} fue enviado con éxito.</h5>
        </div>
      </div>
    {/if}
  </main>
  <Footer />
</body>

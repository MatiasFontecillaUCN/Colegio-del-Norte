<script>
    import Header from '../Header.svelte';
    import Footer from '../Footer.svelte';
</script>
<body>
    <Header/>
    <main>
        <div class='div-main'>
            <p class="title-info">Mis alumnos</p>
            <p class="title-info text-start">1. Gonzalo Díaz</p>
            <div class="row text-center">
                <div class="col-md-4 col-sm-12">
                    <table class="table table-striped border table-bordered">
                        <thead class="">
                          <tr>
                            <th class="w-75">Asignatura</th>
                            <th scope="col">Nota</th>
                          </tr>
                        </thead>
                        <tbody>
                          <tr>
                            <td>Matemática</td>
                            <td>7,0</td>
                          </tr>
                          <tr>
                            <td>Lenguaje</td>
                            <td>6,8</td>
                          </tr>
                          <tr>
                            <td>Inglés</td>
                            <td>6,7</td>
                          </tr>
                        </tbody>
                    </table>
                </div>
                <div class="col-md-4 col-sm-12">
                    <table class="table table-bordered">
                        <tbody>
                          <tr>
                            <td class="w-75"><strong>Promedio general</strong></td>
                            <td>7,0</td>
                          </tr>
                        </tbody>
                    </table>
                </div>
                <div class="col-md-4 col-sm-12">
                    <table class="table table-bordered">
                        <tbody>
                          <tr>
                            <td class="w-75"><strong>Asistencia</strong></td>
                            <td>98%</td>
                          </tr>
                        </tbody>
                    </table>
                </div>

            </div>
        </div>
    </main>
    <Footer/>
</body>

/*!
* Start Bootstrap - New Age v6.0.6 (https://startbootstrap.com/theme/new-age)
* Copyright 2013-2022 Start Bootstrap
* Licensed under MIT (https://github.com/StartBootstrap/startbootstrap-new-age/blob/master/LICENSE)
*/
//
// Scripts
// 
const API_URL = "https://www.dolarsi.com/api/api.php?type=valoresprincipales";
var aCompras = document.getElementsByClassName('compravalor');
var aVentas = document.getElementsByClassName('ventavalor');
var aAgencias = document.getElementsByClassName('agenciavalor');


window.addEventListener('DOMContentLoaded', event => {

    // Activate Bootstrap scrollspy on the main nav element
    const mainNav = document.body.querySelector('#mainNav');
    if (mainNav) {
        new bootstrap.ScrollSpy(document.body, {
            target: '#mainNav',
            offset: 74,
        });
    };

    // Collapse responsive navbar when toggler is visible
    const navbarToggler = document.body.querySelector('.navbar-toggler');
    const responsiveNavItems = [].slice.call(
        document.querySelectorAll('#navbarResponsive .nav-link')
    );
    responsiveNavItems.map(function (responsiveNavItem) {
        responsiveNavItem.addEventListener('click', () => {
            if (window.getComputedStyle(navbarToggler).display !== 'none') {
                navbarToggler.click();
            }
        });
    });

});
window.onload = actualizarCotizaciones();

function actualizarCotizaciones() {
    let aDataCompras = [], aDataVentas = [], aDataAgencias = [];
    for (let i = 0; i < aVentas.length; i++) {
        aVentas[i].innerHTML = "Cargando...";
        aAgencias[i].innerHTML = "Cargando...";
        aCompras[i].innerHTML = "Cargando...";
    }
  fetch(API_URL)
    .then((response) => response.json())
    .then((data) => {
        for (const item of data) {
            if (item.casa.nombre.includes('Dolar') && !item.casa.compra.includes('No Cotiza')) {
                aDataCompras.push(item.casa.compra);
                aDataVentas.push(item.casa.venta);
                aDataAgencias.push(item.casa.agencia);
            }
        }
        for (let i = 0; i < aVentas.length; i++) {
            aVentas[i].innerHTML = '$' + aDataVentas[i];
            aAgencias[i].innerHTML = 'Agencia ' + aDataAgencias[i];
            aCompras[i].innerHTML = '$' + aDataCompras[i];
        }
})}
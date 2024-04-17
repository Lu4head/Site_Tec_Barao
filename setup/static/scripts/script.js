document.addEventListener("DOMContentLoaded", function() {
    const addToCartButtons = document.querySelectorAll(".add-to-cart");
    const cartIcon = document.querySelector(".cart-icon");
    const cartCount = document.querySelector(".cart-count");
  
    let totalItemsInCart = 0;
  
    addToCartButtons.forEach(button => {
      button.addEventListener("click", function() {
        totalItemsInCart++;
        updateCartCount(totalItemsInCart);
      });
    });
  
    function updateCartCount(count) {
      cartCount.textContent = count;
    }
});
// Seleciona o carrossel e define a quantidade de deslocamento horizontal
const carousel = document.querySelector('.carousel');
const scrollAmount = 300; // Valor de deslocamento em pixels

// Função para rolar para a esquerda
function scrollLeft() {
  carousel.scrollBy(-scrollAmount, 0);
}

// Função para rolar para a direita
function scrollRight() {
  carousel.scrollBy(scrollAmount, 0);
}

// Adiciona eventos de clique aos botões de rolagem
document.querySelector('.scroll-left').addEventListener('click', scrollLeft);
document.querySelector('.scroll-right').addEventListener('click', scrollRight);
